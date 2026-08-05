# Journey evaluation — the user's goal is the unit of analysis

This is the primary lens of the whole skill. **A user does not come to admire a screen; they come to get
something done.** Everything else — screens, components, copy, color — is a *step* on the way to resolving that
intent, and is judged by one question: does it move the user closer to their goal, or get in the way? A
beautiful screen that doesn't advance the goal is a failure. And the worst UX damage almost never lives *on* a
screen — it lives *between* screens, in the transitions, dropped context, dead ends, and detours that a
screen-by-screen audit literally cannot see. So evaluate the journey first; zoom into individual screens second,
and only because the journey told you where to look.

## 1. Start from the goal, not the screen
Before anything, name the user's real **job-to-be-done** — the outcome they came for, stated in their terms, not
the system's. The job is "land more interviews," not "use the resume analyzer." The job is "get paid," not
"submit an invoice." Distinguish:
- **User goal** (what they want: a stronger resume that gets callbacks) vs. **system task** (what the UI makes
  them do: upload, wait, read a score, click fixes). Good UX makes the second the shortest possible path to the
  first. Friction is every step that serves the system's model instead of the user's goal.
- A product usually has **2–4 top jobs**. Name them. Each is a journey to evaluate.
If the user hasn't told you the goal, infer it from the product and state your assumption — but never evaluate
without one, because "is this good?" is unanswerable without "good *for getting what done*?"

## 2. Map the journey
For each top job, lay out the realistic end-to-end path the user takes across screens:

> **entry point → step → step → … → goal achieved (success)**

Capture, per step: *what the user is trying to do here, what the system asks of them, what they need in order to
proceed, and how they get to the next step.* Include the **unhappy paths** — error, abandonment, "I'll come back
later," the returning user — because that's where journeys actually break. A rough map is enough; the point is
to make the *sequence and the transitions* visible, not to produce a pretty diagram.

## 3. Walk the journey (cognitive walkthrough)
At **each step**, ask the four questions — this is the core evaluative act:
1. **Will the user know what to do here?** Is the next action toward their goal obvious, or do they have to
   figure out the system?
2. **Will they see how to do it?** Is the control to take that action findable, or buried/ambiguous?
3. **Will they understand what happened?** Does the feedback confirm they moved *closer to the goal* (not just
   "saved")?
4. **Did this step earn its place?** Does it move the user measurably toward the goal, or is it busywork the
   system imposed? If you can't justify a step by the user's goal, that's a finding.

A "no" at any step is usually a bigger problem than any single-screen heuristic violation, because it stalls the
whole journey.

**Then walk the arc, not just the steps.** A journey is *remembered* as a shape, not an average (the psychology
layer, `psychology.md` §F). So evaluate the whole sequence emotionally:
- **The end and the peak (peak-end rule).** People judge the experience by its most intense moment and its last
  moment. Find the journey's emotional peak and its ending — does the final step deliver a real "you did it"
  (clear success, confirmation, what's next), or does it fizzle, dump the user back to a list, or end on a janky
  step? A weak ending taints an otherwise good journey; fix it before any mid-journey nit.
- **Momentum (Zeigarnik & goal-gradient).** Does the journey sustain the pull to finish — visible progress,
  step-of-N, saved state so a return is easy, a goal that feels near? Or does it let the user stall with no sense
  of progress or reason to continue? (Honestly — see the ethical test; momentum must serve the user's goal, not
  just retention.)
- **Cognitive load across the path.** Does effort spike at the wrong moment (a hard decision or heavy form before
  the user has seen value)? Front-load value, defer effort.

## 4. The cross-screen failure catalog (what single-screen audits miss)
These live in the seams between screens. Hunt them explicitly:
- **Dead ends** — a screen with no clear path forward toward the goal; the user completes a step and is stranded.
- **State / context loss across navigation** — filters reset, entered data lost, selection forgotten, scroll
  position gone when moving between steps or hitting back. The user is punished for navigating.
- **Redundant steps & re-entry** — asking again for what was already provided earlier in the journey (re-typing,
  re-selecting, re-uploading). Every repeat is friction and a small insult.
- **Broken handoffs** — the transition between two screens loses momentum, changes vocabulary ("contact" here,
  "lead" there for the same thing), or dumps the user somewhere unexpected instead of the obvious next step.
- **Cross-screen inconsistency** — the same concept rendered with a different label, pattern, or component on
  different screens (e.g. titles truncated on one screen, shown in full on another); the user re-learns each
  screen instead of transferring knowledge. (This is Jakob's Law applied *within* one product.)
- **Orphaned / trap states** — you can reach a state with no way back into the flow, or get stuck mid-journey
  with no exit but completion.
- **Unclear next step** — a screen that's fine in isolation but doesn't tell the user where to go next toward the
  goal; the journey loses its thread.
- **The goal-completion gap** — the system lets the user do many things but never actually closes the loop on
  the original intent. They can analyze, score, and tweak forever, but were they ever taken to *applied with a
  strong resume*? If the journey has no clear "you achieved what you came for," that's the most important finding
  on the page.

## 5. Funnel & drop-off thinking
Even without analytics, predict where users fall out, and treat those steps as high-priority:
- Friction spikes (a long form, a forced decision, a confusing screen) early in the journey, before the user has
  seen enough value to push through.
- **Commitment asked too early** — signup, payment, or heavy input demanded before the product has shown what
  it's worth. The classic leak.
- Steps with unclear value ("why am I being asked this?") or unclear progress ("how much further?").
Name the one or two steps most likely to lose users, and say why.

## 6. The intent-vs-implementation gap (the senior question)
Hold this over the whole journey: **did the user accomplish what they came to do, or did the system make them do
what it wanted?** Steps that exist because of the database schema, the org chart, or an engineering convenience —
rather than the user's goal — are the signature of system-centered design. The reframe in every finding: not
"this screen is awkward" but "this step doesn't serve the goal, and here's the shorter path that would."

## 7. When you only have one screen
You're still evaluating a journey — you've just been handed one step of it. Situate it: name the goal it serves,
ask what comes immediately before and after, and judge whether this step advances the goal and hands off cleanly.
Flag the adjacent steps you can't see ("can't assess whether the result screen closes the loop — need that
view"). Never treat a single screen as the whole world; that's how you miss the journey-level problem entirely.

## 8. Worked example (a journey walk)
Job: *a job-seeker wants to land more interviews.* Mapped across a resume-optimization product (the running
example of this skill):

> **entry (sign up / log in) → upload resume → see analysis & score → apply fixes → compare against target roles
> → (close the loop?) apply to jobs with a strong, targeted resume.**

Walking it surfaces journey-level findings a screen audit wouldn't:
- *Handoff, resumes → analysis:* after uploading, does the user land on the analysis automatically, or are they
  dropped back in the library to hunt for it? A broken handoff here stalls step one.
- *State across fixes:* if applying a fix re-runs analysis, is the user's place and context preserved, or do
  they lose where they were? (Cross-screen state loss.)
- *Vocabulary consistency:* "score" on the resumes screen vs. "match %" on job comparisons — related but
  different numbers; does the product make the relationship clear, or must the user reconcile them alone?
- *The goal-completion gap (the big one):* the journey ends at "compare / see breakdown." Nothing observed takes
  the user to *applied*. The product optimizes the resume beautifully but may never close the loop on the actual
  job (land interviews) — so the strongest improvement might not be any screen, but adding the missing final
  step (export the tailored resume, track applications, "you're ready — here's what's next").

That last finding is worth more than every per-screen nit combined, and it is only visible from the journey.

**The fix (reasoning the gate produces).** Once the gap is named, the fix follows the same goal-first chain into
build mode — and the move that makes it "the real deal" is naming the missing *concept*, not a screen:
- *The missing concept is "ready."* The product has no notion of *done* — every surface points inward to a higher
  score. To deliver "land more interviews" it needs a state called **ready** and a motion that points **outward**
  (toward applying). Readiness is **per role, not per resume** (you're ready for *this* role), so the terminal step
  lives on the job-comparison, the most goal-proximate surface that already exists.
- *New arc:* compare → close role gaps → **"You're ready for this role"** → export the tailored resume → apply →
  **mark as applied** → (later) **mark outcome: interview / offer** — that last beat is "land more interviews" made
  literal, and the feedback loop the product lacks.
- *Psychology, applied to the ending:* peak-end rule says the *ending* is remembered disproportionately, and
  the product's current ending is an anti-climax (a list of more locked fixes). An earned "you're ready, here's your
  resume, go get it" rewrites the remembered experience of the whole product. Goal-gradient: a visible "ready"
  finish line pulls users through the fixes they were stalling on.
- *Ethics:* the tailored resume is the artifact the user *made* — let them export it even on the free tier (charge
  for the analysis/fixes, not for holding their own output hostage). An endless improvement loop that never lets
  the user finish is the manipulative side of Zeigarnik; a real "done" is the honest side.
- *Scope to stage:* MVP = the "ready" success state + export + "mark as applied" (small build, huge arc gain). V2 =
  the outcome tracker and per-role exports. Build the ending first; don't over-spec.

This is the gate in action: steps 1–2 (goal → journey break) found the missing concept; step 3 (psychology) shaped
the ending; step 4 (honesty) set the export/paywall line — and only then did screen-level design follow.

---

*This is the primary method. The screen-level lenses (`heuristics.md`) and archetype packs are the zoom-in you
apply to the steps the journey flagged — not the starting point.*
