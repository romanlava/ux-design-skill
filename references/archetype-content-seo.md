# Archetype — content / SEO / publishing platforms

For content platforms with a public reading surface and (often) an automated, LLM-driven publishing pipeline:
SEO blog services, programmatic content sites, editorial CMSes with generation and scheduled jobs. Run after the
universal lenses. Both the *reader's* experience and the *operator's* workspace matter — they have different
users with different needs.

## 1. Public reading experience
Long-form reading has its own UX, and it's what separates an authoritative site from one that reads like scraped
content.
- [ ] Comfortable line length (~50–75 characters) and line height; body text large enough to read.
- [ ] Table of contents for long articles, with active-section highlighting on scroll.
- [ ] Author block with name, credential, and a real "last updated" date (E-E-A-T signal, and honest).
- [ ] Inline citations/links to sources; FAQ rendered as accessible accordion where present.
- [ ] Breadcrumb reflecting real site structure; clear related-content / next-read.
- [ ] Reading experience holds on mobile: no horizontal scroll, tappable targets, readable code/tables.
- [ ] Images have meaningful alt text and don't cause layout shift; lazy-loaded below the fold.

## 2. SEO & GEO technical hygiene
- [ ] Canonical tags correct and self-referential where expected; no accidental cross-canonicalization.
- [ ] `robots`/meta-robots, XML sitemap, and `404`/`410`/`301` statuses are correct and consistent.
- [ ] Structured data (Article, FAQPage, BreadcrumbList) is present and **matches visible content** (no markup-only claims).
- [ ] Titles/meta descriptions are unique, present, and within length; OG/Twitter cards render.
- [ ] **GEO** (generative-engine optimization): answer-first H2s, high fact density, RAG-friendly paragraph
      structure, `llms.txt` present where used.
- [ ] Core Web Vitals are sane (LCP/CLS/INP); no render-blocking surprises on article pages.
- [ ] Pagination/archive/tag pages don't create thin-content or duplicate-content traps.

## 3. Admin / content-ops workspace
The operator surface — where most operator-UX issues hide.
- [ ] Semantic-core / topic manager is legible: what's planned, in progress, published, held.
- [ ] **Held-for-review workspace**: a readable **diff view**, failed checks shown **with their thresholds** (not
      just "failed"), and a link from each article to the exact generation prompt/version that produced it
      (in whatever prompt registry or LLM-eval tool the pipeline uses).
- [ ] Signals/metrics views (GSC clicks, impressions, positions) are scoped, dated, and timezone-clear.
- [ ] Editing an article preserves formatting and doesn't silently lose content; autosave + version history.
- [ ] Bulk content actions follow the CRM pack rules (selection scope, partial-success, undo).

## 4. Pipeline observability & cost controls
- [ ] Pipeline runs are visible: queued / running / succeeded / failed, with timestamps and per-stage status.
- [ ] **Spend caps and current spend are visible** before a budget is blown; approaching a cap warns ahead.
- [ ] Per-article / per-run cost is attributable; runaway loops are detectable and stoppable.
- [ ] Failed stages show the reason and offer retry; nothing fails silently.

## 5. Destructive-action safety gates
- [ ] Bulk publish / unpublish / delete of articles is gated and previews scope.
- [ ] Regenerate/overwrite warns before discarding human edits; held human edits aren't clobbered by a re-run.
- [ ] Archive vs. delete is a deliberate distinction with a clear URL policy (below).

## 6. Multi-zone / cross-project integration
- [ ] If the public site and admin live in different zones/apps, navigation and auth between them is seamless.
- [ ] Shared components (header/footer) stay consistent across zones; no jarring style/version drift.
- [ ] Cross-subdirectory attribution and analytics survive zone boundaries (see CRM pack §13).
- [ ] Preview/draft URLs are `noindex` and don't leak into production indexing.

## 7. Automated outputs
- [ ] Generated content is clearly reviewable before publish; nothing auto-publishes without the configured gate.
- [ ] Output quality checks (readability, fact density, duplicate detection) are visible and tunable.
- [ ] Scheduled jobs show next-run, last-run, and outcome; misfires are surfaced.

## 8. Editorial governance
- [ ] Brand-voice rules are editable config, not hardcoded.
- [ ] Stop-topics list is editable and actually applied in generation prompts.
- [ ] Approved proprietary statistics list is editable and used verbatim.
- [ ] Reviewer name + credential editable per article; per-article author override possible (E-E-A-T hygiene).
- [ ] Published articles retain edit history / audit log (who/what/when).
- [ ] Archived articles have a clear URL policy (301 to related, or `noindex` + keep).
- [ ] YMYL-topic guard: flagged for human review before publish.
- [ ] Duplicate-content check against existing articles (e.g. pgvector similarity threshold).

---

*Source: generalized from a production E2E checklist for an automated SEO/blog publishing platform. Add or
prune per project.*
