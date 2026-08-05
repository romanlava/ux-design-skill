# Archetype — mobile-first consumer apps & self-service portals

For products end consumers use on their own phones: native apps, PWAs, and mobile-web self-service portals —
a rider or driver portal, a customer account area, a patient or member portal, a banking-style app. The defining
conditions: the device is a personal phone (often low-end), the network is often bad, the audience is *not*
an operator who lives in the tool — they come back repeatedly for a few concrete jobs (check a balance, pay,
submit a thing, see status), and they may have limited digital literacy or be using a second language. Run after
the universal lenses. The guiding principle: **the phone in a pocket, on a bad network, used with one thumb,
is the real product.**

## 1. Thumb ergonomics & one-handed use
Most use is one-handed, on the move, with the thumb doing all the work.
- [ ] Primary actions and navigation sit in the **thumb zone** (bottom half of the screen); nothing critical
      lives only in the top corners on tall phones.
- [ ] Bottom nav (if present) has 3–5 labeled destinations; the current one is marked; icons are never
      unlabeled.
- [ ] Touch targets meet the floor (≥24×24px; 44×44px comfortable) *and* have breathing room — adjacent
      tappable rows/buttons don't cause fat-finger misfires on real, small screens.
- [ ] Layout respects **safe areas** (notch, home indicator, browser chrome); fixed bottom bars don't hide
      content or sit under the home indicator.
- [ ] The on-screen **keyboard doesn't cover the focused input** or the submit button; the form scrolls the
      active field into view.
- [ ] Sticky headers/footers are lean — chrome must not eat a small viewport.

## 2. Platform conventions & gestures
Consumers carry expectations from every other app on their phone (Jakob's Law at its strongest).
- [ ] The **system back** (Android back, iOS edge-swipe, browser back) behaves correctly everywhere — it goes
      back one step, never exits the app from deep in a flow, never loses entered data, and never traps the
      user in a modal.
- [ ] Gestures (swipe actions, pull-to-refresh, drag) are **discoverable and have a visible non-gesture
      alternative** (a button or menu — WCAG 2.2 SC 2.5.7); nothing important is gesture-only.
- [ ] Native inputs are used where they're better: correct mobile keyboards (`inputmode`), native
      date/select pickers, `autocomplete` attributes — no desktop-style widgets that fight the phone.
- [ ] Web-view / PWA specifics: no hover-dependent affordances, tap highlights sane, no accidental
      double-tap zoom on controls, text readable without pinch-zoom (and zoom is not disabled).

## 3. Consumer authentication (phone-first, OTP, persistent sessions)
Consumer auth is usually phone-number + OTP, on a personal device, and it fails differently than email/password.
- [ ] Phone entry is **forgiving** (accepts spaces, dashes, leading zero, with/without country code) and
      normalized server-side; the expected format is shown, not enforced by rejection.
- [ ] **OTP entry** supports paste and autofill (`autocomplete="one-time-code"`), never blocks paste, shows a
      **resend** with a visible countdown, and states where the code went ("Sent by SMS to +63 ••• 4567").
- [ ] OTP failure modes are designed: wrong code (clear message, attempts remaining), expired code (offer a new
      one), SMS never arrives (resend + an alternate channel or a human escape hatch), wrong number entered
      (an obvious way back to correct it).
- [ ] **Sessions are long-lived on a personal device** — don't make a returning user re-authenticate for every
      visit to check a balance; if a step is sensitive, re-verify at that step, not at the front door.
- [ ] Biometric/passkey unlock offered where available; logout still findable for shared-phone situations.
- [ ] Account recovery works for this audience's reality: changed phone numbers happen — there is a path that
      isn't "email us" for someone who may not use email.

## 4. Money & status surfaces (the trust core)
Most consumer portals exist to answer two questions: *how much do I owe / earn* and *what's my status*. Get
these wrong and nothing else matters.
- [ ] The headline number (balance, amount due, earnings) answers the user's question at a glance, with its
      **as-of time and what it includes** — no ambiguous figures the user must reverse-engineer.
- [ ] Every charge/line-item is **explainable on tap**: what it is, the period it covers, how it was computed.
      Surprise or unexplained amounts are the #1 trust killer.
- [ ] Payment flows show method, exact amount, and consequence before commit; **pending** states are explicit
      ("payment received, processing — reflected within X") so the user isn't left fearing the money vanished.
- [ ] Receipts/confirmation exist and are retrievable later, not just a one-time toast.
- [ ] History is legible to a non-accountant: running balance, plain-language labels, dates in the user's
      format and timezone.
- [ ] Disputes/"this looks wrong" has a path — a human contact or a support flow, reachable from the charge
      itself, not buried.
- [ ] Fees, penalties, and deadline consequences are stated **before** they hit, not discovered after.

## 5. Notifications, SMS & deep links (journey steps that live off-screen)
For consumer products, the journey often *starts* in an SMS or push notification — audit those as first-class
steps, not as an afterthought.
- [ ] Each message answers: what happened, what (if anything) I must do, by when — in the audience's language
      and reading level; sender identity is clear.
- [ ] **Deep links land in context** (the specific bill, the specific task), survive the login step (auth then
      *return to the target*, not to home), and expired/invalid links explain and reroute rather than 404.
- [ ] Message and in-app state agree — an SMS about a due payment matches what the portal shows when they
      arrive; nothing is claimed in a message that the product can't show.
- [ ] Frequency is humane: reminders escalate sensibly rather than spamming; transactional vs. promotional is
      separated; opt-in for the promotional is asked in context, with the reason.
- [ ] Push permission (native/PWA) is **primed in context** — asked at the moment it obviously helps, with the
      benefit stated — never as an ambush on first launch.

## 6. Device & network reality
Design on a flagship, die on a budget Android. Judge against the audience's actual devices and data plans.
- [ ] **Payload is lean**: the critical screens load acceptably on 3G/spotty 4G; images sized for mobile; no
      megabytes of JS to show a balance.
- [ ] Flaky-network behavior is designed: submissions **queue or retry without losing input**; a failed action
      says so and preserves everything; no infinite spinners with no timeout or retry.
- [ ] Some **offline tolerance** where the job warrants it (viewing already-loaded status/history) and honest
      "you're offline" messaging otherwise.
- [ ] Performance holds on low-end hardware: long lists don't jank, animations are cheap, the app works on
      the older OS/browser versions this audience actually has.
- [ ] Data-cost respect: no auto-playing video, heavy media is opt-in or lazy, uploads state size.

## 7. Plain language, literacy & localization
The audience may have limited digital vocabulary, low literacy, or be reading a second language.
- [ ] Words are **plain and concrete** — no system jargon ("session expired", "invalid payload"), no
      finance-speak where a simple word works; reading level suits the audience.
- [ ] Icons are always labeled; nothing important is icon-only or color-only.
- [ ] **Typing is minimized**: pickers, defaults, remembered values, tap choices over free text — every typed
      field is friction and an error source on a phone keyboard.
- [ ] Input is forgiving (Postel's Law hard mode): case, spaces, formats normalized silently; errors guide in
      plain words ("That code has 6 digits — check the SMS") and never blame.
- [ ] Local language/tone is right for the audience (including mixed registers where that's how people actually
      speak); translations complete — no raw keys or half-English screens; text expansion doesn't break layout.
- [ ] There is always a **human escape hatch** — a call/chat/contact path for the user who is stuck, findable
      from anywhere, especially from error and payment screens.

## 8. App lifecycle (native & PWA)
States unique to installed apps that web-thinking forgets.
- [ ] OS **permissions** (camera, location, notifications) are requested in context with the reason; the
      **denied** state is designed (explain what won't work + how to re-enable), not a dead feature.
- [ ] Forced-update / outdated-version states explain and link to the store; the app degrades gracefully rather
      than breaking silently on old versions.
- [ ] PWA install prompt (if used) is offered after value is shown, not on first paint; the installed
      experience (splash, icon, standalone chrome) is intentional.
- [ ] Camera/photo capture flows (documents, meter readings, damage photos) preview before submit, allow
      retake, state size/format limits up front, and survive the app being backgrounded mid-upload.
- [ ] Returning to a backgrounded app resumes where the user left off; it doesn't restart the flow or log
      them out mid-task.

## 9. First-run & the returning user
A portal's real usage shape: one first-run, then hundreds of short return visits for 2–3 jobs.
- [ ] First-run gets to the user's first real answer fast (their status, their balance) — minimal setup, no
      feature tour standing between them and the thing they came to see.
- [ ] The **return visit is the optimized path**: the 2–3 recurring jobs are one tap from landing; the user
      never re-navigates or re-enters what the product already knows.
- [ ] Status changes since last visit are surfaced ("your payment was received") rather than left for the
      user to hunt.
- [ ] The empty first-run state and the rich returning state are both designed — not one screen trying to
      serve both badly.

---

*Hybridize as needed: a consumer portal with billing leans on §4 here plus the forms flow in
`universal-flows.md`; an operator-facing companion app pairs this pack with `archetype-crm-saas.md`. E-commerce
checkout remains universal-flows + journey-method territory, per SKILL.md.*
