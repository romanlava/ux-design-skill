# Build playbook — designing usability in from the start

When building an interface, the experience is decided before the pixels. This file expands the build workflow in
SKILL.md. The throughline: **a screen isn't designed until its empty and error states are.** Aesthetics come
after the experience is sound — through a visual-design companion skill where one is available, and by your own
hand where none is.

**Contents**
1. Sequence (do it in this order)
2. Job & flow first
3. Design every state
4. Information architecture
5. Forms & input
6. Dangerous & destructive actions
7. Accessibility from the structure
8. Write the words
9. The visual layer (hand off, or execute it yourself)
10. Worked example (the build quality bar, filled in)

---

## 1. Sequence
Decide in this order; each step constrains the next:
**job & users → critical flows → screens & their states → IA & navigation → forms & actions → copy → accessibility
pass → visual execution.**
Skipping ahead to visuals is the most common failure: you get a beautiful happy-path screen with no empty state,
no error handling, and a flow that dead-ends.

## 2. Job & flow first
Write it in one line before drawing: *[user] wants to [job] so they can [outcome].* Then list the happy-path
flow as concrete steps. If you can't write the steps, you don't understand the task well enough to design it.
Name the 2–3 things that must be effortless; everything else is secondary.

## 3. Design every state
For each screen, define all six states up front (see lens 11 in `heuristics.md`):
- **Empty** — orient and offer the first action; teach, don't show a void. Separate true-empty from filtered-empty.
- **Loading** — skeleton matching the eventual layout; no layout shift; feedback < ~1s.
- **Partial** — some loaded / some failed; some bulk items done / some not — reported precisely.
- **Error** — plain language, locates the problem, preserves input, offers the fix.
- **Success** — confirmed; the user knows it worked and what's next.
- **Edge / too-much** — long strings, huge numbers, thousands of rows, zero permissions, expired session,
  offline. Decide the behavior now, not in a bug report later.
Make this a literal checklist per screen. An interface designed only for the success state will fail in
production on day one.

## 4. Information architecture
- Group and label by the user's mental model and vocabulary, not the data model.
- Every screen has one obvious primary action; secondary actions are visibly subordinate.
- No dead ends — every screen offers a clear next step or way back.
- Navigation labels match destination titles; current location is always marked.
- Depth over breadth only when it matches how users think; prefer flat, scannable structures for frequent tasks.

## 5. Forms & input
Forms are where good intentions go to die. (Authentication, forms, and onboarding are the universal flows that
recur in almost every app — `references/universal-flows.md` covers all three as both build and audit surfaces;
design them deliberately.) Defaults that move the needle:
- **Fewest fields possible**; ask only for what's needed now; defer the rest.
- **Smart defaults** and remembered values; pre-fill what you can infer.
- **Inline validation** on blur, not only on submit; validate format forgivingly (accept "+1 (555) 123-4567"
  and normalize it yourself).
- **Never lose input** — preserve on error, on back, on accidental navigation.
- **Clear labels above fields** (not placeholder-as-label, which vanishes on focus).
- **Match input type to data** — pickers for constrained sets, native date/number inputs, correct mobile keyboards.
- **One primary submit**, clearly labeled with the outcome verb; disable-with-reason rather than silent failure.
- **Guard double-submit**; show progress on slow submits.

## 6. Dangerous & destructive actions
- Prefer **reversibility over confirmation**: an "Undo" toast beats an "Are you sure?" dialog for the common case,
  because confirmation fatigue trains users to click through.
- Reserve confirmation dialogs for the truly irreversible, and make them describe the consequence specifically
  ("Delete 1,204 contacts permanently? This can't be undone.") with the safe action as default.
- Separate destructive controls spatially from common ones; never place "Delete" adjacent to "Save."
- For bulk/irreversible operations, show exactly what will be affected and require deliberate confirmation
  (type-to-confirm for the catastrophic).

## 7. Accessibility from the structure
Build it in; retrofitting is expensive and worse. As you create each component:
- Use semantic elements (`button`, `a`, `label`, headings, landmarks) — they bring keyboard and screen-reader
  behavior for free.
- Ensure keyboard operability and a visible focus state for everything interactive; manage focus on modal
  open/close and route changes.
- Meet contrast (4.5:1 text, 3:1 large/UI) and target size (≥24px, 44px comfortable) as you choose tokens and
  spacing — not in a later "a11y pass."
- Associate labels and error messages with inputs programmatically; never signal state by color alone.
- Respect `prefers-reduced-motion`. Support text resize to 200% (SC 1.4.4) and reflow at 320px / 400% zoom (SC 1.4.10).

## 8. Write the words
Use real microcopy from the start — it surfaces problems lorem ipsum hides:
- **Buttons** name the outcome ("Create invoice", "Send reset link"), not "Submit/OK."
- **Empty states** teach and point to the first action.
- **Errors** guide ("That email's already registered — sign in?"), never blame.
- **Tone** fits the audience and the moment; calm and helpful in failure.
Draft the labels, headings, button verbs, empty-state lines, and error messages as part of the design — not a
content task for "later."

## 9. The visual layer (hand off, or execute it yourself)
Once the experience is sound — flows, all states, IA, forms, copy, accessibility — the visual execution comes
last. If a visual-design companion skill is available (`frontend-design` is the usual one), apply it here: bring
it the structure and content you've defined and let it bring the bold aesthetic point of view (typography, color,
motion, composition). The division of labor: this skill guarantees the result *works*; the visual skill makes it
*distinctive*. Run them together and you get an interface that is both usable and memorable — which is the whole
point.

**If no such skill is available, the work does not stop here.** Do the visual execution yourself on top of the
structure you decided — a deliberate type scale, a coherent palette that meets the contrast numbers, consistent
spacing, restrained motion — and say plainly that the visual layer is yours rather than a specialist's. A spec
handed to nobody is not a deliverable.

**Then verify the built journey.** A spec isn't done when the code compiles. Walk the implemented product the
way evaluation mode would: run it, walk each designed journey end-to-end at desktop and mobile widths, trigger
the empty / loading / error states you specified (don't take their existence on faith), tab through with the
keyboard, and confirm the real copy made it in. Every gap between the spec and the build is a finding to fix
now — the build isn't complete until the journey you designed is the journey that ships.

---

## 10. Worked example (the build quality bar, filled in)
What a build-mode deliverable looks like: a spec that decides the experience completely, so implementation is
mechanical. Task: *"Design the contacts page for a new CRM, for reps who'll live in it daily."* (Compact — a
real spec covers every screen this way.)

> **Job:** a sales rep wants to find a contact and act on it (call, log, assign) fast — findability and speed are
> everything; they'll use this hundreds of times a day.
> **Happy-path flow:** land → scan/filter to the contact → open or act inline.
>
> **States (the contacts list):**
> - *Empty (new account):* not a blank table — a short line "No contacts yet" + a primary "Import contacts" and
>   secondary "Add one manually," because the first job is getting data in.
> - *Filtered-empty:* "No contacts match these filters" + "Clear filters" — distinct from true-empty, so the rep
>   isn't confused into thinking their data vanished.
> - *Loading:* a table-shaped skeleton (header + ~10 rows), no layout shift when data arrives.
> - *Populated:* sticky header; default sort by most-recently-active; row shows name, company, last-contacted,
>   and owner; primary row action visible (not all hidden in "⋯"); checkbox for bulk select.
> - *Error:* "Couldn't load contacts" inline in the table area + "Retry," not a full-page error.
> - *Edge:* 10k+ rows → paginated with total count and adjustable page size; long names truncate with full value
>   on hover; zero-permission rep sees a read-only view with actions disabled-with-reason.
>
> **IA & primary action:** the page's primary action is "Add contact," top-right, consistent across the app.
> Filters are chips above the table, URL-persisted so a view is shareable and survives refresh.
>
> **Key form (add contact):** name + one more field required, everything else optional and deferred; inline
> validation on blur; email accepts any case and trims whitespace; input preserved on error; submit reads
> "Add contact," guards double-submit.
>
> **Copy:** real strings written above (no lorem); button verbs name outcomes; empty state teaches.
>
> **Accessibility:** semantic table markup; row actions have accessible names (not icon-only); keyboard-navigable
> with focus that isn't hidden by the sticky header (SC 2.4.11); contrast on the muted "last-contacted" text
> verified ≥ 4.5:1 with the bundled `contrast_check.py`; any drag-to-assign has a menu alternative (SC 2.5.7).
>
> **Visual layer:** the above goes to a visual-design companion skill if one is available (type scale, color,
> density, motion), or gets executed here if not — either way the experience is already decided, so visual work
> can't accidentally break a flow or drop a state.

Notice the shape: it resolves the lens collisions explicitly (daily action → fast row actions over confirmation
dialogs), designs *all* states before any visuals, writes real copy, and bakes accessibility into the structure.
That is the bar — not a screenshot description, but decisions complete enough to build from.

