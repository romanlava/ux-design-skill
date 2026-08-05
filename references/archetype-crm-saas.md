# Archetype — CRM / marketing SaaS / operator-facing apps

For multi-user, data-heavy, integration-rich products: CRMs, admin panels, internal tools, marketing SaaS,
operator dashboards. These are the surfaces that show up again and again in this kind of app and accumulate the
most UX debt. Run after the universal lenses; check the sections that apply to the product in front of you.
Each item is a thing to verify in an audit or design deliberately when building.

## 1. Data tables & grids
The single most-reused component here, and where most consistency debt lives.
- [ ] Sort state is visible and persists across navigation/refresh; default sort is sensible.
- [ ] Column headers indicate sortability; multi-sort behavior (if any) is discoverable.
- [ ] Sticky header (and often sticky first column) on long/wide tables — but ensure a keyboard-focused row
      isn't hidden behind the sticky header (WCAG 2.2 SC 2.4.11); scroll focused content into clear view.
- [ ] **Empty vs. filtered-empty are distinct messages** — "No contacts yet" vs. "No contacts match these filters."
- [ ] Loading shows a skeleton in the table shape, not a spinner over a blank rectangle; no layout shift on load.
- [ ] Row selection semantics are clear: what a checkbox selects, what persists across pages, how to clear.
- [ ] Pagination vs. infinite scroll is appropriate to the task; total count shown; page size adjustable for power users.
- [ ] Row actions are discoverable (not all buried in a single unlabeled "⋯") and destructive ones are guarded.
- [ ] Long values truncate gracefully with full value on hover/expand; numbers right-aligned and formatted.
- [ ] Column visibility / ordering / density is adjustable and remembered for data-dense tools.
- [ ] **Data-ink is maximized** (Tufte): units and currencies consolidated into column headers, not repeated in
      every row; whitespace and alignment do the grouping before borders and fills do; decoration never competes
      with the numbers. (Judgment, not law — e.g. row striping genuinely helps very wide tables.)

## 2. Search, filters & saved views
- [ ] Search has scope clarity (what's being searched), suggestions/history, and a clear empty result.
- [ ] Filter state is **URL-shareable** and survives refresh and back.
- [ ] Date-range filters offer presets (Today, Last 7/30 days, MTD) and are **timezone-aware** — state the zone.
- [ ] Applied filters are visible as removable chips; "clear all" is one click.
- [ ] **Saved views** distinguish personal from team/shared; renaming, default-view, and sharing are clear.
- [ ] Filter combinations that yield nothing explain why and offer to broaden.

## 3. Bulk operations
- [ ] Selection across pagination is explicit: **"select all on page" vs. "select all N matching"** are different and labeled.
- [ ] The action confirms the count and scope before running ("Archive 1,204 contacts?").
- [ ] **Partial-success reporting** for async bulk: "17 of 20 done; 3 failed — download report / retry failed."
- [ ] Progress is shown for long bulk jobs; the user can navigate away and be notified on completion.
- [ ] Destructive bulk actions are reversible or gated (type-to-confirm for the catastrophic).
- [ ] Any drag-based interaction (reorder rows, drag-to-kanban, drag-to-assign) has a non-drag alternative —
      a menu action or buttons (WCAG 2.2 SC 2.5.7); drag-only is inaccessible to many users.

## 4. Data import & export
- [ ] Import offers **column mapping** with a preview of parsed rows before committing.
- [ ] **Duplicate handling is a user choice** (skip / update / create) — not a silent default.
- [ ] A **dry-run / validation pass** flags errors before any data is written.
- [ ] On failure, a **downloadable error report** names the rows and reasons; successful rows aren't lost.
- [ ] Export states format, scope (filtered vs. all), and row count; large exports run async with notification.
- [ ] Timezone and encoding are explicit for CSVs; date/number formats match locale.

## 5. Access control (RBAC)
- [ ] Roles and permissions are legible to an admin without docs; what each role can do is discoverable.
- [ ] The UI **hides or disables-with-reason** actions the current user can't perform — no buttons that error on click.
- [ ] Insufficient-permission states explain who to ask, not just "Access denied."
- [ ] Invite / role-change / deactivate flows are clear; the last-admin and self-lockout cases are guarded.
- [ ] (Note: changing sharing/permissions on the user's behalf is a guarded action — surface it, let the user execute.)

## 6. Integrations & connectors
- [ ] Connection status is unambiguous: connected / disconnected / error / expired, each with the next action.
- [ ] OAuth/connect flows explain scope and return cleanly; reconnect is obvious when a token expires.
- [ ] Sync state is visible (last synced, in progress, failed) with a way to force or retry.
- [ ] Failures are actionable ("reconnect Google Ads — token expired") not silent or cryptic.
- [ ] Disconnecting explains the consequence (what stops working / what data is removed).

## 7. Reporting & dashboards
- [ ] Every metric states its **definition, date range, and timezone**; "revenue" means one thing consistently.
- [ ] Loading, empty (no data in range), and error states exist per widget — not one spinner for the whole page.
- [ ] Comparisons (vs. prior period) and units are labeled; no unlabeled axes or mystery numbers.
- [ ] Drill-down from a chart to the underlying rows is possible where users will want it.
- [ ] Export / share / schedule is available; the rendered state matches the exported state.
- [ ] Stale data is flagged ("as of 3h ago") rather than presented as live.

## 8. Async operations & audit logs
- [ ] Long jobs (generation, sync, export, batch) are visible in a jobs/activity area with status and timestamps.
- [ ] The user can leave and return; completion/failure is communicated (toast, badge, email).
- [ ] Failed jobs show the reason and offer retry; they don't vanish.
- [ ] An audit log records who did what, when (especially for destructive and permission changes) and is searchable.

## 9. API keys & webhooks
- [ ] Keys are shown once on creation with a clear copy affordance and a warning they won't be shown again.
- [ ] Keys can be named, scoped, rotated, and revoked; last-used is visible.
- [ ] Webhook config shows delivery status, recent attempts, and a way to test/replay.
- [ ] Secrets are masked in the UI and never placed in URLs or logs.

## 10. Billing & quotas
- [ ] Current plan, usage vs. limit, and renewal date are visible before the user hits a wall.
- [ ] Approaching a quota warns ahead of time; hitting it explains the limit and the upgrade path — never a dead end.
- [ ] Plan changes preview the effect (proration, what's gained/lost) before committing.
- [ ] (Entering payment details and completing purchase are user-driven, guarded actions — surface them, don't auto-fill.)

## 11. Operator onboarding
- [ ] First-run orients to the **core job**, not a feature tour; gets the operator to first value fast.
- [ ] Setup checklists track real progress and are dismissible/resumable.
- [ ] Sample/demo data or templates lower the empty-account cliff.
- [ ] Help is contextual (inline, on the surface where it's needed), not only a separate docs site.

## 12. B2B trust
- [ ] Security/compliance signals are present where they matter (SOC2, data residency, SSO) without clutter.
- [ ] Data handling is honest and clear; export-your-data and account-deletion paths exist and are findable.
- [ ] No deceptive patterns in cancellation/downgrade — the path out is as clear as the path in.
- [ ] Status/incident communication exists for an always-on tool.

## 13. Measurement & tracking integrity
Often invisible to users but central to a marketing/SaaS product working as a business — and a frequent source
of silent failure. Audit the instrumentation as part of the UX:
- [ ] Key events fire correctly and once — no duplicate PageView/conversion events (e.g. Pixel + GTM double-fire).
- [ ] Server-side and client-side events **deduplicate** properly (shared event IDs for CAPI/Pixel).
- [ ] Consent state is respected before tags fire (Consent Mode v2 / region-appropriate gating); no tracking pre-consent.
- [ ] Event parameters are consistent and populated (currency, value, IDs) — not empty or mismatched across surfaces.
- [ ] Cross-domain / cross-subdirectory attribution is preserved where the product spans domains.
- [ ] Server vs. GA4 event counts are sane relative to each other; large unexplained discrepancies are flagged.
- [ ] Custom dimensions / source tags needed for attribution are actually set on the relevant events.

---

*Source: generalized from a production E2E checklist for a CRM / marketing SaaS, extended. Add or prune items
per client; this is a living pack.*
