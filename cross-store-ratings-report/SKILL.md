---
name: cross-store-ratings-report
description: Produce a private cross-store ratings and reviews report for Dan's app portfolio using App Store Connect via asc and the Google Play developer client via gplay or gpc. Use when asked to map, audit, compare, monitor, or summarize ratings/reviews across iOS and Android apps. Do not use public store scraping or public lookup endpoints as a substitute for developer data.
---

# Cross-Store Ratings Report

Use this skill for portfolio-wide App Store + Google Play ratings and reviews snapshots for Dan's apps. This is a private developer-data workflow, not a public-store research workflow.

## Hard Requirements

- Use `asc` for App Store Connect.
- Use the local Google Play developer client: prefer `gplay`; use `gpc` only when that is the configured client in the current environment.
- Do not use public App Store search, public Google Play pages, third-party scrapers, or public lookup endpoints to fill missing ratings.
- If a developer client is unauthenticated or missing app configuration, report that as a data gap with the exact missing local config or credential path if the tool exposes it.
- Keep credentials, tokens, service-account JSON contents, and private review IDs out of the final answer.

## Inputs

Default assumptions for Dan:

- Scope: all apps in the configured developer accounts unless explicit bundle/package IDs are given.
- Stores: both App Store Connect and Google Play.
- Window: current aggregate rating state plus reviews from the last 30 days.
- Output language: match the user's language; Czech is fine when the request is Czech.

## App Store Connect

1. Confirm `asc` is available:
   - `asc --help`
2. List app records from ASC:
   - `asc apps list --output json`
3. For each relevant app, collect:
   - ASC app ID
   - app name
   - bundle ID
   - platform
   - current customer ratings and review counts when exposed by the current `asc` command set
   - recent customer reviews and dates when requested
4. Discover exact current subcommands from `asc --help` or `asc <group> --help`; `asc` changes over time, so prefer command discovery over remembered syntax.

## Google Play

1. Confirm the available developer client:
   - `command -v gplay`
   - `command -v gpc`
2. Prefer `gplay` if it is installed and configured. Use `gpc` when `gplay` is unavailable or the existing environment clearly uses `gpc`.
3. Verify auth/config with cheap read-only commands before querying all apps:
   - `gplay --help` / `gpc --help`
   - app list/status command for configured apps
4. Collect for each relevant package:
   - package name
   - app title
   - current rating and rating count if exposed by the developer API/client
   - review count in the selected window
   - notable recent review themes when review text was fetched
5. If no apps are configured in the client, derive package candidates from repo metadata only to know what to ask the client for explicitly. Do not treat repo metadata as review data.

## Identity Matching

Normalize by identifiers, not title alone:

- iOS: ASC app ID + bundle ID
- Android: package name
- Cross-store pairing: matching product family names in repo metadata, shared app names, or explicit user mapping

When uncertain, keep iOS and Android rows separate rather than guessing.

## Output

Start with a compact table:

| App | iOS bundle | ASC app ID | iOS rating | iOS ratings | iOS reviews | Android package | Play rating | Play ratings | Play reviews | Notes |

Then include:

- `Notable themes`: only from developer-fetched review text.
- `Data gaps`: missing auth, unpublished apps, missing app config, client/API limitations, or apps not present in one store.
- `Next actions`: concrete fixes such as restoring a Google Play service-account key, adding configured apps to the client, or replying to specific reviews when requested.

## Guardrails

- Read-only by default.
- Do not reply to reviews unless explicitly asked.
- Do not overstate missing data as zero. Use `missing`, `not exposed`, or `not configured`.
- Separate aggregate ratings from individual review counts.
- Reuse narrower skills for follow-up work:
  - `gplay-review-management` for Google Play replies.
  - `asc-aso-audit` / `aso-audit` for listing optimization.
