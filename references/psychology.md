# The psychology layer — how people perceive, decide, and remember

Beneath the journey and the lenses sits the reason any of it works: the human mind has a fixed "blueprint" for how
it perceives, decides, and remembers, and good experience design works *with* that grain instead of against it.
This is the difference between UI and **experience** — UI is what's on the screen; experience is what happens in
the user's head and how it *feels over time*. A screen can be immaculate and still produce a bad experience if it
fights how people actually think.

Use this layer two ways: in **evaluation**, at each journey step ask *which mental system is the user in, what is
the design asking of their attention / memory / decision-making, and does the emotional arc land?* In **building**,
design *for* System 1, reduce cognitive load, sequence choices, and deliberately engineer the peak and the ending.

The named "laws" here are the foundation (the *why*); `heuristics.md` is their screen-level application (the
*what to check*). Some names appear in both, in different roles.

## A. The engine of decisions — System 1 vs System 2 (Kahneman)
The single most useful idea in UX psychology. The mind runs two modes:
- **System 1** — fast, automatic, intuitive, emotional, effortless. It handles the large majority of decisions
  (Kahneman's estimate is ~95%), below awareness, by pattern and association.
- **System 2** — slow, deliberate, analytical, effortful — and *lazy*. It only engages when it must, and tires
  quickly.

Design implications (these drive almost everything else):
- **Design for System 1.** Most use is glance-and-react, not read-and-reason. Make the right action obvious by
  pattern, position, and default so the user never has to *think* — the whole premise of "Don't Make Me Think."
  Most "confusing UI" is a spot where the design forced System 2 where the user expected to coast.
- **Reserve — and force — System 2 deliberately.** For consequential, irreversible, or costly actions (delete,
  pay, send), intentionally *slow the user down*: friction, confirmation, a summary to read. Speed is a virtue
  everywhere except the cliff edge.
- **Context beats information.** Because decisions rarely reach System 2, telling users things ("please remember
  to…", more copy, a warning) rarely changes behavior. Changing the *context* — the default, the ordering, the
  friction, the prompt's timing — does. When a behavior isn't happening, redesign the path, don't add a sentence.
- System 1's shortcuts are systematic, so they produce predictable **biases** you can design around (next).

## B. The biases System 1 runs on (Kahneman & Tversky)
Each is a lever — and an ethical responsibility (§H):
- **Cognitive load.** Working memory is tiny; every demand to hold, recall, or compute spends a scarce budget.
  Reduce extraneous load ruthlessly — chunk, default, show don't ask, carry context forward. (Dual-process is
  *why* load matters: load is System 2 effort, and System 2 is the bottleneck.)
- **Anchoring.** The first number/option seen frames every judgment after it (the middle pricing tier, the
  "was $99" strike-through). Choose anchors honestly and deliberately.
- **Loss aversion (prospect theory).** Losses loom roughly twice as large as equivalent gains. People work
  harder to avoid losing progress than to gain something new — which is exactly why a half-finished profile or a
  cart "about to expire" pulls so hard (and why that pull must be used honestly, §H). Frame value around what's
  protected, not only what's gained.
- **Framing.** The same fact stated as 90% success vs 10% failure changes the choice. Frame truthfully but with
  awareness that the frame is never neutral.
- **Default effect.** People overwhelmingly accept the default. A good default is the highest-leverage humane
  design decision you can make; a self-serving default is a deceptive pattern.
- **Sunk cost & escalation.** Invested effort makes people continue what they would never start fresh. The
  honest use: surface real progress and let it genuinely carry over (a saved draft, a resumable setup). The
  abuse: "you'll lose everything you've built" framing to block cancellation or deletion — that's exploiting
  the bias, not serving the user (§H).
- **Endowment & the IKEA effect.** People value what they own, and overvalue what they helped build. Early
  personalization and customization create real attachment (the profile *they* filled in, the view *they*
  configured) — and this is also why users resist redesigns that silently discard their configurations: those
  saved views are *theirs*. Migrate, don't delete.
- **Present bias (temporal discounting).** Value now outweighs value later, steeply. Show value before asking
  for commitment (the funnel rule in `journey-evaluation.md` §5 is this bias, applied); and make future costs —
  renewal, price-after-trial, the payment that comes due — as vivid as present benefits. Burying the future
  cost exploits the bias and is a finding.

## C. Managing choice — load, options, complexity
- **Hick's Law.** More options (and more complex ones) → slower, harder decisions. Reduce choices, or stage them
  (progressive disclosure); break a long set into 3–4 at a time.
- **Miller's Law.** Working memory holds only ~7±2 chunks — really "chunk and reduce." Group and segment;
  never make the user hold many loose items across steps.
- **Tesler's Law (conservation of complexity).** Every system has irreducible complexity; the only question is
  *who absorbs it*. Push it into the product (smart defaults, inference, good structure), not onto the user.
- **Choice architecture / nudges (Thaler).** The arrangement of options is never neutral, so arrange it to make
  the choice that serves the user the easy one — ethically (§H).

## D. The glance — perception & attention (Gestalt + attention effects)
How the eye groups and notices before any reading happens:
- **Gestalt grouping** — *proximity* (near = related), *similarity* (alike = related), *common region* (shared
  boundary/background = a group), *uniform connectedness* (linked elements = related), *Prägnanz* (the mind reads
  the simplest interpretation). These *are* visual hierarchy: group by meaning and the structure becomes legible
  without labels.
- **Von Restorff (isolation) effect.** The one item that differs is the one that's noticed and remembered → make
  the single primary action visually distinct; don't dilute it with five equal "primary" buttons.
- **Selective attention / banner blindness.** People filter out what looks like ads or chrome — so important
  things that *look* like decoration get skipped.
- **Serial position effect.** First and last items are best remembered → put the most important nav/list items at
  the ends.

## E. Social dynamics — influence & trust (Cialdini)
Decisions are made in a social context, and *other people* are the strongest System-1 shortcut of all. These
levers dominate conversion and trust surfaces (landing pages, pricing, signup, checkout) — and they are the
most-abused territory in UX, so every one carries the §H test: it must be **true**. A fabricated instance of
any of these is an automatic finding, and several are now outright unlawful (fake reviews, fake urgency).
- **Social proof.** Under uncertainty, people copy others — ratings, testimonials, usage numbers ("1,200 riders
  earn with us"). Strongest when the others are *similar* to the user (riders in their city, companies their
  size — not "users worldwide"). Real, attributable, consented proof only; cherry-picked or invented proof is
  a deceptive pattern.
- **Scarcity & urgency.** Limits on supply or time raise perceived value and prompt action — honest when the
  limit is real (actual stock, a real deadline) and stated plainly. Evergreen countdowns and fake "only 2 left"
  are the canonical deceptive pattern.
- **Authority.** Credentials, expertise, and recognizable affiliations transfer trust. Borrowed authority must
  be verifiable — a real certification links to its source; an invented badge is fabricated proof.
- **Reciprocity.** Give genuine value first (a useful free tool, real content) and people feel a pull to give
  back (attention, signup). Honest when the gift is actually useful before any ask; hollow "free" bait that
  exists only to extract the ask is manipulation.
- **Commitment & consistency.** Small first steps create identity pull toward larger consistent ones — the
  foot-in-the-door, and why micro-commitments in onboarding work. Escalate genuinely valuable engagement;
  don't ratchet people into what they'd refuse if asked outright up front.
In evaluation: on any conversion or trust surface, check which of these levers are present and whether each is
*true* — that's the whole audit of this layer.

## F. Memory & feeling over time — the experience layer
This is what "experience, not UI" most directly means: an experience is lived as a sequence and remembered as a
shape, not as the average of its pixels.
- **Peak-end rule (Kahneman).** People judge an experience by its most intense moment (the *peak*) and its
  *ending* — not the average. So the emotional high point and especially the **final step of a journey** carry
  disproportionate weight: design the success state, the confirmation, the "you did it" moment with care, and
  fix a janky ending before a mediocre middle. A flow that ends well is remembered well.
- **Zeigarnik effect.** Unfinished tasks create cognitive tension and stay in memory ("open loops"). Progress
  indicators, "65% complete," step-of-N, save-and-resume, and a started-but-unfinished state all harness this to
  help users finish what they began. (Ethics in §H — this is the most easily abused principle here.)
- **Goal-gradient effect.** Motivation rises the closer the goal feels → show progress, accelerate cues near the
  end, and consider *endowed progress* (start the user partway, e.g. "2 of 5 done" at signup) so the goal already
  feels within reach.
- **Flow (Csikszentmihalyi).** Engagement lives where challenge matches skill — too hard breeds anxiety, too easy
  breeds boredom. Scale difficulty and support to the user's level across the journey.

## G. Expectations, speed & action
- **Jakob's Law.** Users spend most of their time on *other* products, so they expect yours to work like those.
  Honor conventions; novelty in plumbing (nav, forms, checkout) costs relearning. (Mental models: people act on
  what they *expect* to happen, so match the expectation or set it.)
- **Postel's Law.** Be liberal in what you accept — forgive input variation (spaces in card numbers, any date
  format) and normalize it yourself.
- **Paradox of the Active User.** People don't read manuals; they dive in. Design to be self-evident and
  learnable by doing, not by tutorial.
- **Doherty Threshold.** Below ~400ms response, attention and engagement hold; above it, flow breaks. Perceived
  speed (optimistic UI, skeletons) protects the experience.
- **Labor illusion (operational transparency).** People value results more when they can *see* the work being
  done — "Checking 3 sources…" with real steps beats a blank spinner, and sometimes beats an instant answer
  that looks too cheap to trust. Doherty says "be fast"; this says what to show when you can't be: narrate the
  *actual* work (AI thinking/tool states, search progress, import stages). Never fabricate fake work to inflate
  perceived value — that's theater, and it fails the §H test.
- **Fogg Behavior Model (B = MAP).** A behavior happens only when **M**otivation, **A**bility, and a **P**rompt
  converge at the same moment. If users aren't doing something, usually the cheapest fix is raising *ability*
  (removing friction) and fixing the *prompt's timing* — not pumping motivation. Most "they won't do X" problems
  are friction or timing problems.

## H. The ethical line — persuasion vs manipulation
Every principle above is dual-use: the same lever that helps a user finish a task they *want* to finish can trap
them in one that only serves your metrics. This is the line between persuasive design and a deceptive pattern,
and it is not optional — several deceptive patterns are now unlawful (GDPR, FTC, the EU's deceptive-design rules).

The test to apply to any psychological lever (Zeigarnik loop, loss-aversion framing, a default, a nudge):
**"If the user does what this nudges them toward, are they genuinely better off — or am I extracting behavior
against their interest for engagement/revenue?"** If it's the latter, it's manipulation, and it's an automatic
finding in an audit and a hard no in a build. Use this layer to *reduce friction toward the user's own goals*,
never to manufacture goals that serve only the business. Honest progress, honest framing, humane defaults,
real value at the end of the loop.

## I. The evaluator's own biases (turn the lens on yourself)
Every bias above runs in the reviewer and the designer too, and three of them corrupt audits and builds
specifically. The method's discipline (name the audience, walk as the user, falsify findings) exists to
counter them — it's debiasing, not bureaucracy.
- **Curse of knowledge.** Once you know how the system works, you cannot simulate not-knowing it. Jargon reads
  fine, the missing onboarding is invisible, the "obvious" icon is obvious only to you. This is why the
  cognitive walkthrough forces the question "will the user *know* what to do here?" step by step, and why
  expert review complements but never replaces watching a real first-time user.
- **False consensus.** You project your own mental model and preferences onto users — "I'd never tap that,"
  "everyone knows this pattern." You are not the user; the audience framed in step 1 is, and their devices,
  vocabulary, and expertise are the reference, not yours.
- **Confirmation bias in the audit itself.** Once you form a thesis about a product ("this onboarding is the
  problem"), you notice confirming evidence and stop seeing the rest. The "falsify before you promote" rule
  (`audit-method.md` §0) is the standing counter — apply it hardest to the findings you're most sure of.

---

*Sources: Kahneman, "Thinking, Fast and Slow" (System 1/2, peak-end, prospect theory); Tversky & Kahneman
(heuristics & biases); Zeigarnik (open loops); Yablonski, "Laws of UX" (the heuristics/Gestalt/bias framing);
Csikszentmihalyi (flow); Fogg (behavior model); Thaler & Sunstein (choice architecture, endowment); Cialdini,
"Influence" (social dynamics); Buell & Norton (the labor illusion). A calibration note: these effects are
directional design guidance, not lab constants — treat the named numbers (~95%, 7±2, ~400ms) as rules of
thumb, and note that some popular "UX psychology" (ego depletion, strong priming claims) failed replication
and is deliberately excluded here. This layer is the foundation; apply it through the journey method and the
screen lenses.*
