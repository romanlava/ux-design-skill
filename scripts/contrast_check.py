#!/usr/bin/env python3
"""
WCAG contrast checker.

Computes the WCAG 2.x contrast ratio between foreground and background colors
and reports pass/fail against AA and AAA thresholds for normal text, large text,
and UI components / graphical objects.

Usage:
    python3 contrast_check.py "#1a1a1a" "#ffffff"
    python3 contrast_check.py "111" "fff" "#6b7280,#ffffff" "rgb(107,114,128),#fff"

Accepts one or more color pairs. A pair is either two separate args
(foreground background) or a single "fg,bg" arg. Hex (#abc, #aabbcc, with or
without #) and rgb()/rgba() are accepted.

Thresholds (WCAG 2.1/2.2):
    Normal text  : AA 4.5:1   AAA 7:1
    Large text   : AA 3:1     AAA 4.5:1   (>=24px, or >=18.66px/14pt bold)
    UI / graphics: 3:1        (SC 1.4.11 — components, focus indicators, icons)

Exit code is 0 if every pair passes at least AA-normal, else 1 — handy in scripts.
Bad input (an odd number of colors, or a color that can't be parsed) exits 2.
"""

import re
import sys

USAGE = (
    'usage: contrast_check.py "#fg" "#bg" ["#fg2,#bg2" ...]  '
    "— colors come in foreground/background pairs; hex or rgb() accepted"
)


def parse_color(s):
    """Return (r, g, b) as ints 0-255 from hex or rgb() string."""
    s = s.strip()
    m = re.match(r"rgba?\(\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)", s, re.I)
    if m:
        return tuple(int(round(float(m.group(i)))) for i in (1, 2, 3))
    h = s.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6 or not re.fullmatch(r"[0-9a-fA-F]{6}", h):
        raise ValueError(f"cannot parse color: {s!r}")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))


def _linearize(channel_8bit):
    c = channel_8bit / 255.0
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def relative_luminance(rgb):
    r, g, b = (_linearize(v) for v in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(fg, bg):
    l1 = relative_luminance(fg)
    l2 = relative_luminance(bg)
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def verdicts(ratio):
    return {
        "normal AA (4.5)": ratio >= 4.5,
        "normal AAA (7)": ratio >= 7.0,
        "large AA (3)": ratio >= 3.0,
        "large AAA (4.5)": ratio >= 4.5,
        "UI/graphics (3)": ratio >= 3.0,
    }


_COLOR_TOKEN = re.compile(r"rgba?\([^)]*\)|#?[0-9a-fA-F]{3,8}", re.I)


def _pairs_from_args(args):
    """Yield (fg_str, bg_str) from a flexible arg list.

    Colors may arrive as separate arguments or comma-joined into one ("#fg,#bg"),
    in any mix of hex and rgb()/rgba() notation — the commas inside an rgb() stay
    with their color.
    """
    flat = []
    for a in args:
        tokens = _COLOR_TOKEN.findall(a)
        # Whatever is left once the recognized colors are removed is junk; surface
        # it instead of silently dropping part of the argument.
        leftover = _COLOR_TOKEN.sub("", a).replace(",", "").strip()
        if not tokens or leftover:
            raise ValueError(f"cannot parse color: {a!r}")
        flat.extend(tokens)
    if len(flat) % 2 != 0:
        raise ValueError(
            f"expected an even number of colors (foreground/background pairs), got {len(flat)}"
        )
    for i in range(0, len(flat), 2):
        yield flat[i], flat[i + 1]


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 0
    # Parse everything up front so a bad argument fails before any output is printed.
    try:
        pairs = [
            (fg_s, bg_s, parse_color(fg_s), parse_color(bg_s))
            for fg_s, bg_s in _pairs_from_args(argv[1:])
        ]
    except ValueError as e:
        print(f"contrast_check.py: error: {e}", file=sys.stderr)
        print(USAGE, file=sys.stderr)
        return 2
    all_ok = True
    for fg_s, bg_s, fg, bg in pairs:
        ratio = contrast_ratio(fg, bg)
        v = verdicts(ratio)
        print(f"\n{fg_s}  on  {bg_s}   ratio = {ratio:.2f}:1")
        for label, ok in v.items():
            print(f"  {'PASS' if ok else 'FAIL'}  {label}")
        if not v["normal AA (4.5)"]:
            all_ok = False
    print()
    return 0 if all_ok else 1


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except BrokenPipeError:
        sys.exit(0)
