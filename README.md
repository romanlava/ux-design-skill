# ux-design — a Claude Code skill

A goal-first, journey-first UX evaluation and design skill for Claude Code. The unit of
analysis is the user's goal and the whole journey to it across screens — not isolated UI
elements. Two modes: **Evaluate** (audit an existing product from a URL, screenshots, or
code) and **Build** (design flows, states, IA, and content before pixels).

## What's inside

```
SKILL.md                          ← entry point: principles, mode router, 12 lenses, workflows
README.md                         ← this file
LICENSE                           ← MIT
.gitignore                        ← ignores .DS_Store and __pycache__
references/
  journey-evaluation.md           ← the primary method: mapping and walking journeys
  audit-method.md                 ← input recipes, severity model, report template
  heuristics.md                   ← the 12 lenses in operational detail
  psychology.md                   ← the psychology layer (Kahneman, biases, ethics)
  universal-flows.md              ← auth, forms, onboarding — the universal three
  build-playbook.md               ← build-mode workflow detail
  archetype-crm-saas.md           ← archetype packs: product-specific surfaces
  archetype-content-seo.md
  archetype-mobile-consumer.md
  archetype-ai-product.md
scripts/
  contrast_check.py               ← WCAG contrast ratio calculator
```

## Install

Clone into your Claude Code user skills directory:

```bash
git clone https://github.com/romanlava/ux-design-skill.git ~/.claude/skills/ux-design
```

The skill auto-activates on UX evaluation and design tasks (or invoke with `/ux-design`).

## The contrast script

`scripts/contrast_check.py` is a WCAG contrast checker — standard library only, so `python3`
(3.8+) is the only requirement. Its path is relative to the skill directory (wherever you
installed it), not to the project you're working in:

```bash
python3 ~/.claude/skills/ux-design/scripts/contrast_check.py "#767676" "#ffffff"
```

Takes one or more foreground/background pairs (hex or `rgb()`). Exits `0` if every pair clears
AA for normal text, `1` if any fails, `2` on bad input.

## Composes with (all optional — nothing below is required)

The skill is self-contained: it needs nothing but this repository. Where these companions
happen to be installed, it uses them; where they aren't, it does the work itself.

- **A visual-design skill** (e.g. `frontend-design`) — owns visual craft (typography,
  color, motion); this skill owns the experience layer. Without one, this skill carries
  the visual execution itself rather than stopping at a handoff.
- **A dataviz skill** — owns chart-level craft (chart form, palettes, marks, axes).
- **A design-rules base** — some projects connect one: rule files carrying stable IDs
  (`UX-ERR-01` and the like), indexed for on-demand loading. When present, this skill
  treats it as the canonical law layer and cites rule IDs in findings; when absent — the
  common case — nothing changes.

## License

MIT — see [LICENSE](LICENSE).
