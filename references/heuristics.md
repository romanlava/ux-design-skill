# Universal evaluation lenses — operational detail

The twelve lenses from SKILL.md, expanded into what to actually look for: the signals, the thresholds, and the
failure patterns that recur across every kind of interface. Read this before any serious audit, and keep it in
mind when building. Each lens lists *what good looks like* and *common failures* so you can pattern-match fast.

**Contents**
1. Visibility of state
2. Match to the real world
3. User control & freedom
4. Consistency & standards
5. Error prevention
6. Recognition over recall
7. Flexibility & efficiency
8. Aesthetic & minimalist focus
9. Error recovery
10. Help in context
11. All states designed
12. Accessible & inclusive
— plus five cross-cutting concerns: perceived performance, trust & credibility, content & microcopy,
localization & internationalization, and resilience & adverse conditions.

---

## 1. Visibility of state
**Good:** The user always knows where they are, what mode they're in, what the system is doing, and what just
happened. Current location is marked in nav. Actions produce immediate acknowledgment. Long operations show
progress. Selections, filters, and unsaved changes are visible. And feedback lands at the user's **focal
point** (spatial locality — Fitts + Gestalt proximity): confirmation and errors appear where the interaction
happened, and controls sit next to the thing they act on — Save/Apply beside the edited field or row, not only
at the far end of the page.
**Failures:** Clicking a button with no visible response (so the user clicks again). Async save with no
confirmation. Active nav item not highlighted. A filtered table that looks identical to an unfiltered one.
"Saving…" that never resolves to "Saved." Mode changes (edit vs. view) with no visual difference. A global
toast as the only signal for a local field error. A page-bottom global "Save" as the only commit for a single
inline edit, forcing the eye and cursor to hunt for the system's reaction elsewhere on the screen.

## 2. Match to the real world
**Good:** Labels, icons, and ordering follow the user's mental model and vocabulary. Dates, numbers, and units
are formatted the way the audience expects. Information appears in a natural, logical order.
**Failures:** Database/engineering jargon leaking into the UI ("null", "entity", "param"). Icons whose meaning
isn't obvious and isn't labeled. Ordering by `created_at` when the user thinks alphabetically. Ambiguous dates
(03/04 — which is the month?). Mystery-meat navigation.

## 3. User control & freedom
**Good:** Clearly marked exits everywhere. Undo for most actions; redo where it makes sense. Cancel that
actually cancels (and discards cleanly). Back behaves logically and preserves state. The user is never trapped
in a flow with no way out but completion.
**Failures:** Modal with no close affordance. Multi-step flow you can't back out of without losing everything.
Back button reloads and wipes form data. No undo after a destructive action. "Are you sure?" as the only safety
net (see lens 5) instead of reversibility.

## 4. Consistency & standards
**Good:** The same concept uses the same word, color, and component everywhere. Primary actions sit in
predictable places. Platform conventions are honored (iOS back gestures, web underlined links, standard form
controls). Internal consistency: spacing, button styles, and terminology don't drift between screens.
*(This is **Jakob's Law**: users spend most of their time on other products, so they expect yours to work the
way those do. Deviating from convention costs the user re-learning — only do it when the payoff clearly exceeds
that cost.)*
**Failures:** "Delete" here, "Remove" there, "Trash" elsewhere for the same action. Primary button on the left
in one dialog, right in another. Custom controls that look clickable but aren't (or vice versa). Three different
date pickers in one app. Reinventing a scrollbar or dropdown badly.

**When a design system exists, it is the arbiter of internal consistency — audit against it.** Flag ad-hoc
values where a token exists (one-off hex colors, arbitrary spacing/type sizes), duplicated one-off components
where a primitive exists (a hand-rolled spinner beside the system's), and semantic misuse (the `danger` color
used for mere emphasis). Drift compounds: every exception weakens the system's promise that same-look =
same-behavior, and each is a small finding even when the screen "looks fine." In build mode the rule is
*extend, don't fork* — a needed new variant belongs in the system, not inline; check both light and dark themes
if the system defines them, since drift often hides in the theme nobody develops in.

## 5. Error prevention
**Good:** The design makes costly mistakes hard *before* they happen. Sensible defaults. Constraints that block
invalid input (disabled states with a reason, input masks, range limits). Confirmation only for the genuinely
destructive, and ideally reversibility instead. Forgiving formats. Guardrails on bulk and irreversible actions.
*(The manufacturing name for this is **poka-yoke** — Shingo's mistake-proofing: constrain the system so the
invalid state cannot be entered at all. Where the system already knows a value is invalid, a picker, mask, or
inline check beats letting the user submit and fail.)*
**Failures:** A "Delete account" button one pixel from "Save." Free-text where a picker belongs. No guard on a
destructive bulk action. Defaults that cause harm if left unchanged. Confirmation dialogs so frequent users
click through them blind ("Are you sure?" fatigue).

## 6. Recognition over recall
**Good:** Options, commands, and previously entered data are visible or easily retrievable. The user recognizes
rather than remembers. Context carries forward across steps. Recently used / suggested items surface.
**Failures:** Asking the user to remember an ID, code, or value from a previous screen. Hiding all actions
behind an unlabeled "⋯" menu. Search with no suggestions or history. A wizard that doesn't show what you entered
two steps ago. Forcing memorization of syntax with no examples.

## 7. Flexibility & efficiency
**Good:** Novices complete tasks via the obvious path; experts get accelerators — keyboard shortcuts, bulk
actions, saved views/filters, templates, sensible re-use of prior input. The interface scales from first use to
thousandth use.
**Failures:** No keyboard support in a tool people live in all day. No bulk action where users routinely act on
many items. Re-entering the same filters every session. No way to save or share a configured view. Power users
forced through novice-paced flows.

## 8. Aesthetic & minimalist focus
**Good:** Every element earns its place. The primary action is unmistakable. Visual hierarchy guides the eye to
what matters. Secondary information is present but subordinate. Whitespace is used deliberately.
**Failures:** Five competing "primary" buttons. Walls of equal-weight text. Decorative noise that fights the
content. Dashboards that show everything and therefore highlight nothing. Hierarchy that doesn't match
importance. (Note: minimal ≠ sparse — a dense expert tool can be minimalist if every pixel is load-bearing.)
*(Beware the **aesthetic-usability effect**: people perceive attractive interfaces as more usable than they
are, which means a polished visual layer can hide real usability problems — and can fool you, the reviewer, too.
When auditing, judge the interaction on its merits regardless of how good it looks.)*

## 9. Error recovery
**Good:** Errors are in plain language, say what went wrong *and where*, and offer the path forward. Validation
points to the specific field. The user's input is preserved. Recovery is one click where possible.
**Failures:** "An error occurred." "Error 500." Red border with no message. A form that clears on error. Error
text far from the field that caused it. Blaming the user ("Invalid input") instead of guiding ("Phone numbers
need 10 digits"). Dead ends with no retry.

## 10. Help in context
**Good:** Guidance appears where and when it's needed — inline hints, examples in placeholders, tooltips on
unfamiliar terms, empty states that teach. Documentation is reachable but rarely necessary. Help mechanisms
(contact link, chat, help) appear in a **consistent location** across pages (WCAG 2.2 SC 3.2.6).
**Failures:** Critical instructions buried in external docs. No examples for a non-obvious input format.
Onboarding that front-loads everything then disappears. Tooltips on the obvious and silence on the obscure.
Help that moves around or appears on some pages but not others.

## 11. All states designed
This is where modern interfaces fail most. For **every** screen and component, verify each state exists and is
handled deliberately:
- **Empty** — first use / no data yet. Should orient and offer the first action, not show a blank void or a sad
  zero. Distinguish *empty* (no data ever) from *filtered-empty* (your filter matched nothing) — they need
  different messages.
- **Loading** — skeletons or progress, not a frozen screen or layout shift. Feedback within ~1s; progress
  indication past ~1s; for long jobs, let the user leave and get notified.
- **Partial** — some data loaded, some failing; some bulk items succeeded, some didn't. Report partial success
  precisely ("17 of 20 imported; 3 failed — download report").
- **Error** — see lens 9.
- **Success** — confirmed clearly; the user knows it worked and what's next.
- **Too much / edge** — very long names, huge numbers, 10,000 rows, zero permissions, expired session,
  offline. The layout holds and the behavior is sane.
**Failures:** A table that's a blank rectangle before data arrives. An empty state that looks like a bug. A
bulk action that reports "Done" when 3 of 20 silently failed. Text that overflows or truncates without a title
attribute. No offline/expired-session handling.

## 12. Accessible & inclusive
Operationalize WCAG — these are largely *principle violations*, not taste:
- **Contrast** — body text ≥ 4.5:1; large text (≥24px or ≥18.66px/14pt bold) and UI components/graphics ≥ 3:1.
  Measure, don't eyeball: run `python3 <skill-dir>/scripts/contrast_check.py "#fg" "#bg"` (bundled with this
  skill — `<skill-dir>` is the directory containing SKILL.md, not your working directory) for the exact
  ratio and AA/AAA verdicts, or use any contrast tool.
- **Keyboard** — every interactive element reachable and operable by keyboard, in a logical order; visible focus
  indicator; no keyboard traps; skip-to-content link on dense pages.
- **Focus not obscured** — when an element receives focus it must not be hidden behind sticky headers, footers,
  or other overlapping content (WCAG 2.2 SC 2.4.11). *This is the catch on sticky headers/toolbars: pin them, but
  make sure the keyboard-focused row or field still scrolls into clear view.*
- **Semantics & labels** — real `<button>`/`<a>`/`<label>`/headings, not `<div onclick>`. Every input has a
  programmatic label. Images have meaningful `alt` (or empty alt if decorative). Landmarks/regions present.
- **Target size** — interactive targets ≥ 24×24px (WCAG 2.2 SC 2.5.8); 44×44px is comfortable, especially on
  touch. *(This is **Fitts's Law** in practice: acquisition time grows as targets shrink and recede — small,
  crowded, or far-flung controls are slow and error-prone, so size and space the important ones generously.)*
- **Touch & pointer** — no **hover-only** affordances (there is no hover on touch — anything revealed on hover
  must also be reachable by tap/focus); any action driven by a **drag/gesture** has a single-pointer alternative
  such as a button (WCAG 2.2 SC 2.5.7 — relevant to reorder, kanban, sliders, swipe-to-delete); place primary
  actions within comfortable thumb reach on mobile.
- **Accessible authentication** — don't gate login behind a cognitive-function test (memorizing/transcribing
  codes, solving puzzles) with no alternative; allow paste and password managers (WCAG 2.2 SC 3.3.8). Detail in
  `universal-flows.md`.
- **Motion & media** — respect `prefers-reduced-motion`; no content that flashes >3×/sec; captions/transcripts
  for media; nothing conveyed by color alone.
- **Forms & errors** — errors associated with fields programmatically (`aria-describedby`), announced to assistive
  tech, not signaled by color alone.
- **Zoom & reflow** — text resizable to 200% without loss of content or function (WCAG SC 1.4.4), and content
  reflows at 320px width / 400% zoom with no horizontal scrolling (WCAG SC 1.4.10).
**Failures:** Light-gray placeholder text as the only label. `div` buttons. Icon-only controls with no
accessible name. Focus that disappears on tab or hides under a sticky header. Actions only reachable by hover or
drag. Color-only state (red = error with no text/icon). Carousels that auto-advance with no pause.

**A note on automated checks:** the contrast script and code review catch the *machine-detectable* share of
accessibility issues (roughly a third in practice). Meaningful alt text, logical focus order, sensible heading
structure, and whether a control's accessible name actually describes it still require human judgment — never
report "accessible" on the strength of automated checks alone.

---

## Cross-cutting concerns

These are every bit as important as the twelve lenses — they're listed separately because they don't live on a
single screen-level check; they thread through *all* twelve. Perceived performance shapes visibility, feedback,
and flow; trust shapes error handling, forms, and content; content design *is* most of what the user reads. Weigh
them accordingly.


**Perceived performance.** Speed is felt, not measured. Acknowledge input instantly (<100ms feels instant,
<1s keeps flow, >1s needs a spinner, >10s needs progress + the ability to leave — Nielsen's response-time
limits; the **Doherty threshold**, ~400ms, is where interaction stops feeling like waiting). Use optimistic UI
where safe, skeletons over spinners for content, and prefetch likely next steps. A fast-feeling slow app beats a
slow-feeling fast one.

**Trust & credibility.** Especially before asking for money, data, or commitment: clear identity, honest copy,
no **deceptive patterns** (the term the field now prefers over "dark patterns": no pre-checked opt-ins, fake
urgency, hidden costs, roach-motel cancellation), visible privacy and security signals where relevant, graceful
handling of the user's data. Deceptive patterns are an automatic finding — flag them as such, and note that
several are now outright unlawful (GDPR consent rules, FTC guidance, the EU's deceptive-design provisions), so
they're a liability, not just bad manners.

**Content & microcopy.** Words are interface. Button labels are verbs that name the outcome ("Create invoice",
not "Submit"). Empty states teach. Error messages guide. Tone matches the audience and the moment (calm in
errors, never cute in failure). Avoid jargon, hedging, and walls of text. Real copy reveals UX problems that
lorem ipsum hides — when building, write the actual words.

**Localization & internationalization.** If the product ships in more than one language, the layout and logic
must survive translation — and most don't. Check: **text expansion** (German and Russian run 30–40% longer than
English; fixed-width buttons and single-line labels break — design for flex and wrapping); **RTL** (Arabic/Hebrew
mirror layout, icons, and progress direction); **locale formatting** of dates, numbers, currency, and units (and
timezone — never show a bare timestamp without its zone); **translation completeness** (no untranslated strings
or raw keys leaking through; sensible fallback); **no concatenated sentences** built from fragments (they
mistranslate and break grammar); correct encoding and **locale-aware sorting and input** (names, addresses,
phone formats vary). For a single-locale product this is a non-issue — scope it to reality.

**Resilience & adverse conditions.** Most interfaces are designed on a fast laptop on office wifi and then used
on a three-year-old Android phone on 3G in a basement. Check the gap: **payload weight** (does the page ship
megabytes of JS/images that stall on a slow connection?); **offline and flaky connectivity** (does an action
queue and retry, or just fail and lose the user's input? is there any offline tolerance where the task warrants
it?); **graceful degradation** (does core function survive when a script fails to load, or does the whole screen
white-screen?); **optimistic UI with rollback** (show the action as done, but reconcile and tell the user if it
didn't); **low-end device performance** (does scrolling a long list or a heavy animation jank?). This matters
disproportionately for products with users on cheap devices and weak networks — judge against the real device
and connection your audience has, not the one you built on.
