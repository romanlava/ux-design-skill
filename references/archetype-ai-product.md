# Archetype — AI / LLM-powered product interfaces

For products where the core interaction is with a generative model: chat assistants, copilots, agentic tools,
generation features embedded in a larger app. These have failure modes no other archetype has — nondeterministic
output, latency measured in seconds, confident wrongness, and cost that scales with use. Run after the universal
lenses. The guiding principle: **the interface must keep the user in control of a system that is fast, fallible,
and opaque.**

## 1. Latency & streaming
Model responses are slow by UI standards (seconds, not milliseconds), so perceived performance is central.
- [ ] Output **streams** token-by-token rather than appearing after a long blank wait; the user sees progress immediately.
- [ ] A visible thinking/working state covers the gap before the first token; for agentic runs, show the steps
      or tools being used, not just a spinner.
- [ ] The user can **stop generation** mid-stream and keep the partial output.
- [ ] Long autonomous runs report progress, are interruptible, and let the user leave and return.

## 2. Control over a nondeterministic system
The model won't always get it right; the UI's job is to make iteration cheap and the user feel in command.
- [ ] **Regenerate** is available, ideally with a way to steer the retry ("shorter", "more formal").
- [ ] The user can **edit their last input and re-run** without retyping everything.
- [ ] Output is **editable** by the user, not a take-it-or-leave-it block.
- [ ] Conversation/history is preserved, navigable, and the user can branch or go back without losing work.
- [ ] Destructive or external actions an agent takes are **confirmed or reversible** — never silently executed
      on the user's behalf (especially anything that sends, buys, deletes, or messages someone).

## 3. Uncertainty & trust
Confident wrongness is the signature AI failure; the interface must not launder it into apparent authority.
- [ ] The product is **honest that output may be wrong**; it doesn't present generated content with unearned
      certainty (see the aesthetic-usability effect — a polished answer feels more correct than it is).
- [ ] Where factual, claims are **grounded with citations/sources** the user can check, and the UI makes
      verification easy.
- [ ] **Confidence or uncertainty is surfaced** where it matters (e.g. "I'm not sure, verify this") rather than
      hidden behind a fluent tone.
- [ ] Refusals and safety limits are explained in plain language, not a curt "I can't help with that," with a
      constructive path where one exists.
- [ ] Hallucination-prone surfaces (numbers, quotes, names, code that must run) get extra verification
      affordances or guardrails.

## 4. Input affordances
The blank prompt box is the hardest empty state in software.
- [ ] First-run shows **what the thing can do** with concrete example prompts or starter actions — not a blank box.
- [ ] Suggested follow-ups, templates, or autocomplete lower the "what do I even type" cost.
- [ ] Constraints are visible (attachment types/sizes, context limits) before the user hits them.
- [ ] The user can attach/reference the right context (files, selection, data) clearly.

## 5. Feedback & improvement loop
- [ ] Lightweight feedback (thumbs, flag, "regenerate worse/better") is present and frictionless.
- [ ] Reporting a bad or harmful output is easy and the user knows it was received.
- [ ] If feedback shapes future behavior or training, that's disclosed honestly.

## 6. Cost, limits & transparency
AI features cost money per use, and limits surprise users who don't see them coming.
- [ ] Usage against any quota/credits is visible **before** the user hits the wall; approaching it warns ahead.
- [ ] Rate-limit / overload states are graceful and tell the user when to retry — not a raw error.
- [ ] Where the user pays per use, the cost of an action is knowable before they commit to it.

## 7. Data, privacy & safety
- [ ] It's clear whether inputs are stored, used for training, or shared — with a real opt-out where promised.
- [ ] Sensitive-data handling is honest; the UI doesn't encourage pasting secrets it will then log.
- [ ] Memory/personalization (what the system remembers about the user) is visible, correctable, and deletable.

## 8. Failure & edge states
- [ ] Model timeout, overload, content-filter block, empty response, and tool-call failure each have a designed,
      plain-language state with a next step — not a stack trace or a frozen UI.
- [ ] Partial agentic failure (3 of 5 steps done) is reported precisely, with retry of just the failed part.
- [ ] Network drop mid-stream recovers gracefully without losing the conversation.

---

*Universal-scope pack for AI-native interfaces; hybridize with the CRM-SaaS pack for AI features embedded in an
operator tool, or the content-SEO pack for AI content pipelines.*
