# Universal flows — auth, forms, onboarding

Three flows recur in nearly every app regardless of archetype, and each is a reliable source of UX damage. Treat
this as the pack that almost always applies: check the flows that are present (evaluation) or design them
deliberately (build), then move on to the archetype pack for the product-specific surfaces. As with the
archetype packs, items are prompts for judgment — turn each hit into a finding or a design decision, not a
ticked box.

## 1. Authentication & account access
The first thing every user touches and a flow teams routinely under-design.
- [ ] **Sign-up** asks for the minimum, states password rules *before* submission (not as a post-failure
      surprise), and offers show-password. Email verification, if required, is explained and resendable.
- [ ] **Sign-in** errors are helpful without leaking which field was wrong in a way that aids attackers
      ("email or password is incorrect"); lockout/rate-limit gives feedback, not silence.
- [ ] **Password reset** is a complete loop: request → email → set new → signed in, with no dead ends; expired
      reset links explain and offer a new one.
- [ ] **Session expiry** never silently discards work — warn before timeout, preserve in-progress input, and
      return the user to where they were after re-auth (not to a generic home).
- [ ] **SSO / OAuth** explains the scope requested and returns cleanly; a failed/declined flow has a path back.
      (Per platform rules, the user performs the actual credential/authorization step.)
- [ ] **2FA**, if present, has recovery codes and a recovery path; losing the second factor isn't a lockout cliff.
- [ ] **Accessible authentication** — don't require a cognitive-function test with no alternative: allow paste
      and password managers in every field (never block paste on password or OTP inputs), and don't force the
      user to memorize, transcribe, or solve a puzzle to log in (WCAG 2.2 SC 3.3.8). Email/SMS links or
      passkeys/WebAuthn are compliant alternatives.
- [ ] **Logout** is findable, and "remember me" vs. shared-device expectations are clear.
- [ ] Across all of the above: errors preserve entered data, and the primary action is unmistakable.

## 2. Forms & data entry (the universal treatment)
Forms are the workhorse of almost every interface and where good intentions quietly fail. The build defaults are
in `build-playbook.md` §5; this is the evaluation/quality view — the surfaces and failure modes to check.
- [ ] **Labels** are visible and persistent (above the field), not placeholder-as-label that vanishes on focus.
- [ ] **Required vs. optional** is unambiguous; mark the rarer of the two consistently.
- [ ] **Validation timing**: validate on blur and at submit, not only at submit; don't error a field the user
      hasn't reached yet.
- [ ] **Errors** are specific, adjacent to the field, programmatically associated (`aria-describedby`), and not
      signaled by color alone; they say how to fix, not just "invalid."
- [ ] **Input is never lost** — on validation error, on back navigation, on accidental reload, on session blip.
- [ ] **Forgiving formats** — accept spaces/dashes in card and phone numbers and normalize server-side; don't
      reject "+1 (555) 123-4567."
- [ ] **Right input type** for the data: pickers for constrained sets, native date/number controls, correct
      mobile keyboard (`inputmode`), autocomplete attributes.
- [ ] **Multi-step** forms show progress, allow back without data loss, and ideally autosave; long forms save drafts.
- [ ] **Submit** has one clear primary action naming the outcome, disables-with-reason rather than failing
      silently, guards against double-submit, and shows progress when slow.
- [ ] **No redundant entry** — don't ask for information the user already provided earlier in the same process;
      auto-populate it or offer it as a selectable default (WCAG 2.2 SC 3.3.7). Re-typing the shipping address as
      the billing address is the classic offender.
- [ ] **Success and failure** states are explicit; on failure the user knows what to do next and keeps their input.

## 3. Onboarding & first-run
The empty, brand-new account — where users decide whether the product is worth their time.
- [ ] First-run orients to the **core job and first value**, not an exhaustive feature tour; get the user to one
      real outcome fast.
- [ ] **Empty states act as onboarding** — they teach what goes here and offer the first action, rather than
      showing a void or a discouraging zero.
- [ ] Setup/checklists track **real progress**, are dismissible and **resumable**, and don't block the product
      behind a wall of configuration before any value is shown.
- [ ] **Sample/demo data or templates** lower the empty-account cliff where appropriate.
- [ ] Guidance is **contextual and progressive** (revealed where and when needed), not a front-loaded modal the
      user dismisses and forgets.
- [ ] Permissions and integrations are requested **in context, with the reason**, at the moment they're needed —
      not all up front.
- [ ] The user can **skip and explore**; nothing critical is reachable *only* through a one-time wizard.

---

*Universal across archetypes. After this, load the matching `archetype-*.md` for product-specific surfaces.*
