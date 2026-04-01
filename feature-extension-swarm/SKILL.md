---
name: feature-extension-swarm
description: "Parallel read-only multi-agent repo scan that proposes the strongest next feature extensions for making an app more competitive. Use when the user wants the current codebase, product surface, and optional market context analyzed to decide what to add next."
---

# Feature Extension Swarm

Scan the current repo and app surface with four read-only discovery lanes in parallel, then have the main agent synthesize the most valuable next feature extensions and recommend one. This skill is advisory only: it does not edit files or start implementation.

## Step 1: Build the Product and Repo Packet

Collect the smallest useful packet:

1. Repo root and target app or module
2. App purpose, target users, and primary platform
3. What the app already does, if known
4. Explicit product goals such as growth, retention, monetization, collaboration, or differentiation
5. Named competitors, aspirational products, or market references, if provided
6. Constraints such as timeline, team size, architecture, business model, or release pressure
7. Supporting artifacts such as docs, screenshots, onboarding flows, issues, roadmap notes, analytics notes, or support feedback

If the request is underspecified, infer a minimal product brief from the repo and say what is still unknown.

Before launching sub-agents, read the closest project instructions and relevant docs, such as:

- `AGENTS.md`
- `README.md`
- product, roadmap, or release notes
- architecture docs
- design system, store metadata, or landing page copy when available

## Step 2: Map the Whole Repo Surface First

Start with a broad, read-only repo scan before deeper analysis. The goal is to understand the whole app shape, not just the currently touched files.

Use breadth-first evidence gathering where useful:

- `rg --files`, `find`, or `git ls-files` to map the repo
- opening top-level app wiring, routing, navigation, feature folders, settings, onboarding, monetization, sync, sharing, and notification areas
- reading README files, docs, changelogs, feature flags, entitlement config, analytics hooks, and release notes
- reviewing screenshots, mockups, or simulator output when available

Prefer representative file reads over opening every file line by line. Build a whole-product map first, then inspect the most important seams more closely.

If competitiveness depends on current market claims or named competitors, verify those claims with current primary sources before making recommendations. If no market context is provided, infer cautiously from the repo and state that the market view is incomplete.

Do not edit files or implement any feature ideas as part of this skill.

## Step 3: Bound the Extension Brief

Write a short discovery brief for the swarm:

1. What product category the app appears to serve
2. What the core user promise seems to be
3. What is already present and likely mature
4. What gaps or weak spots appear most plausible
5. What a strong recommendation must answer

Be explicit about what is observed versus inferred.

## Step 4: Launch Four Read-Only Discovery Lanes in Parallel

Launch four sub-agents when the app is large enough or ambiguous enough that parallel discovery helps. For a tiny app or tightly scoped module, it is acceptable to analyze locally instead.

For every sub-agent:

- give the same product and repo packet plus the extension brief
- state that the sub-agent is read-only
- do not let the sub-agent edit files, run `apply_patch`, stage changes, commit, or perform any other state-mutating action
- ask for concise discovery output only
- ask for: observed strengths, apparent gaps, suggested extensions, why they matter, biggest risks, missing information, and confidence
- tell the sub-agent to avoid generic brainstorming that is not grounded in repo evidence or clear market logic
- tell the sub-agent to send findings back to the main agent only

Use these four discovery lanes.

### Sub-Agent 1: Current Capability and Core Loop Lane

Map what the app already does well and where the core loop appears weak.

Check for:

1. Main user workflows and repeat-use loops
2. Features that look complete versus thin
3. Missing adjacent capabilities that would strengthen the current product promise
4. Signs that the product has depth in one area but obvious holes in the surrounding workflow

This sub-agent is read-only. It must not edit files, apply patches, or make any other workspace changes.

Recommended sub-agent role: `explorer`

### Sub-Agent 2: User Friction and Opportunity Lane

Find the most likely product pain points and extension opportunities.

Check for:

1. Onboarding, activation, retention, or collaboration gaps
2. Places where users likely leave the app to complete the job elsewhere
3. Missing automation, discoverability, or convenience features
4. Opportunities for premium value without turning the app into a kitchen sink

This sub-agent is read-only. It must not edit files, apply patches, or make any other workspace changes.

Recommended sub-agent role: `reviewer`

### Sub-Agent 3: Technical Leverage and Feasibility Lane

Find extensions that fit the current architecture and can be built efficiently.

Check for:

1. Existing data models, services, or UI patterns that can support a nearby feature
2. Platform capabilities or integrations already partly present
3. Architectural seams where an extension would be low-friction versus expensive
4. Risks around shared state, sync, privacy, or migration

This sub-agent is read-only. It must not edit files, apply patches, or make any other workspace changes.

Recommended sub-agent role: `explorer` for broad codebase lookup, or `reviewer` when a deeper reasoning pass is more useful

### Sub-Agent 4: Competitive Positioning Lane

Judge what would make the app feel more competitive and differentiated.

Check for:

1. Table-stakes features that appear missing for the category
2. Extensions that would improve differentiation, not just parity
3. Opportunities to make the product more defensible or more obviously valuable
4. Whether the best next move is a quick win, a strategic bet, or a foundational capability

This sub-agent is read-only. It must not edit files, apply patches, or make any other workspace changes.

Recommended sub-agent role: `reviewer`

Report only extensions that materially improve competitiveness, retention, user value, or strategic product strength. It is better to return five strong candidates than a large list of generic ideas.

## Step 5: Synthesize a Prioritized Feature Extension Set

The main agent owns synthesis. Treat sub-agent output as discovery input, not final output.

Merge the lane outputs and build a prioritized shortlist of the strongest next feature extensions. Avoid fake precision. If the repo evidence is weak, say so directly.

Normalize each surviving extension into this shape:

1. Extension name
2. The user or market gap it addresses
3. Why it fits this app specifically
4. Whether it is table stakes, quick win, growth lever, or differentiator
5. Likely implementation pressure: low, medium, or high
6. Main risks or dependencies
7. Confidence: high, medium, or low

Aim for a set like:

- best next feature
- quick win
- strategic differentiator
- foundational enabler

## Step 6: Recommend What to Build Next

Present the result in this order:

1. Best next feature extension
2. Other high-value extensions
3. Why the top recommendation wins now
4. Assumptions or missing evidence that could change the ranking
5. Suggested next step, such as moving into `feature-planning-swarm`

If the repo evidence is too incomplete for a serious competitiveness recommendation, say so directly and lead with the missing product context instead of inventing certainty.

Do not implement features as part of this skill. The output is a read-only extension recommendation grounded in repo evidence and, when available, current market context.
