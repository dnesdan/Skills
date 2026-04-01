---
name: release-readiness-swarm
description: "Parallel read-only multi-agent release assessment for deciding whether an app, feature, or build is ready to ship. Use when the user wants one clear verdict, prioritized blockers, missing evidence, and the fastest path to higher release confidence without editing source files."
---

# Release Readiness Swarm

Assess ship readiness with four read-only release lanes in parallel, then have the main agent synthesize one release verdict and a prioritized path forward. This skill is diagnosis-first: it does not edit source files or implement fixes.

## Step 1: Build the Release Packet

Collect the smallest useful release packet:

1. What is intended to ship
2. Target platform, environment, and release channel
3. Current branch, build, tag, or scope under consideration
4. Available evidence such as tests, CI, crash reports, screenshots, bug lists, performance notes, signing status, or store metadata
5. Known risks, caveats, or launch requirements
6. Explicit release gates or deadlines

Prefer this source order:

1. Direct user description
2. Explicit artifacts such as logs, screenshots, tests, CI output, release docs, or build notes
3. Closest repo docs and workflow instructions
4. Current diff, branch state, or recent repo history
5. The smallest safe validation commands that improve confidence quickly

If the release request is underspecified, infer a minimal release question and say what is still unknown.

Before launching sub-agents, read the closest project instructions and relevant docs for the touched area, such as:

- `AGENTS.md`
- release checklists
- packaging or deployment docs
- store, privacy, signing, or rollout docs

## Step 2: Bound the Readiness Brief

Write a short readiness brief for the swarm:

1. What is expected to ship
2. What is already proven
3. What remains risky or unproven
4. Which release gates matter most
5. What would count as a blocker versus a caveat

Use read-only evidence gathering where useful:

- `rg`, `git diff`, `git log`, `git show`
- reading CI logs, crash traces, bug lists, or packaging config
- running the smallest safe compile, test, or verification commands that materially improve confidence
- checking screenshots, simulator output, or release artifacts when available

Do not edit source files or apply release fixes as part of this skill.

## Step 3: Launch Four Read-Only Release Lanes in Parallel

Launch four sub-agents when the release question is broad enough that parallel assessment helps. For a tiny patch release with very tight scope, it is acceptable to assess locally instead.

For every sub-agent:

- give the same release packet and readiness brief
- state that the sub-agent is read-only
- do not let the sub-agent edit files, run `apply_patch`, stage changes, commit, or perform any other state-mutating action
- ask for concise release assessment only
- ask for: blockers, caveats, supporting evidence, missing evidence, fastest proof step, and confidence
- tell the sub-agent to avoid generic quality commentary without release impact
- tell the sub-agent to send findings back to the main agent only

Use these four release lanes.

### Sub-Agent 1: User-Facing Quality Lane

Assess what end users are most likely to feel.

Check for:

1. Breaks in critical flows
2. User-visible rough edges that are unacceptable for ship
3. Edge cases around onboarding, permissions, or error states
4. Regressions that would undermine confidence immediately after release

This sub-agent is read-only. It must not edit files, apply patches, or make any other workspace changes.

Recommended sub-agent role: `reviewer`

### Sub-Agent 2: Engineering Quality and Reliability Lane

Assess correctness, resilience, and runtime risk.

Check for:

1. Missing or weak tests for the release scope
2. Crash, hang, memory, performance, or persistence risks
3. Ordering, race, migration, or contract issues
4. Reliability gaps that make the release fragile under real usage

This sub-agent is read-only. It must not edit files, apply patches, or make any other workspace changes.

Recommended sub-agent role: `reviewer`

### Sub-Agent 3: Release Operations and Compliance Lane

Assess the mechanics of actually shipping.

Check for:

1. Build, versioning, signing, config, or environment mismatches
2. Feature flag, entitlement, permission, or privacy issues
3. Store, packaging, or submission readiness gaps
4. Release process risks that could block or invalidate the launch

This sub-agent is read-only. It must not edit files, apply patches, or make any other workspace changes.

Recommended sub-agent role: `reviewer`

### Sub-Agent 4: Observability and Support Lane

Assess whether the team can see and control what happens after ship.

Check for:

1. Missing logs, metrics, alerts, or dashboards
2. Weak rollout, rollback, or kill-switch planning
3. Poor support readiness for known issues
4. Gaps that would make post-release diagnosis or mitigation too slow

This sub-agent is read-only. It must not edit files, apply patches, or make any other workspace changes.

Recommended sub-agent role: `reviewer`

Report only evidence-backed issues that materially affect ship confidence. It is better to return a small set of real blockers than a long list of generic worries.

## Step 4: Synthesize One Release Verdict

The main agent owns synthesis. Treat sub-agent output as release input, not final output.

Merge the lane outputs and filter aggressively:

- combine duplicates
- discard weak speculation
- separate blockers from caveats
- keep missing evidence explicit when it changes the verdict

Use one of these verdicts:

- `ready`
- `ready with caveats`
- `not ready`
- `insufficient evidence`

Normalize the surviving issues into this shape:

1. Area
2. Severity: blocker, caveat, or watch item
3. Why it matters
4. Supporting evidence
5. Fastest proof or fix step
6. Confidence: high, medium, or low

## Step 5: Output a Clear Ship Recommendation

Present the result in this order:

1. Release verdict
2. Blockers to fix now
3. Things to verify now
4. Things to watch after release
5. Explicit missing evidence, if any

If the release is not ready, lead with the shortest path to changing that verdict. If the evidence is too weak for a serious verdict, say so directly instead of pretending the app is ready.

Do not implement fixes as part of this skill. The output is a read-only release assessment with one clear verdict and a prioritized path forward.
