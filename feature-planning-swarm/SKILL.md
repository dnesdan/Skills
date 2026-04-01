---
name: feature-planning-swarm
description: "Parallel read-only multi-agent feature planning that turns a proposed feature into 2-4 concrete implementation plans with tradeoffs, risks, and one recommended path. Use when the user has a feature idea and wants product, UX, architecture, and delivery input before coding."
---

# Feature Planning Swarm

Shape a proposed feature with four read-only planning lanes in parallel, then have the main agent synthesize a small set of implementation plans and recommend one. This skill is advisory only: it does not edit files or start implementation.

## Step 1: Build the Feature Packet

Collect the smallest useful packet:

1. Feature idea in one sentence
2. User problem or opportunity
3. Target users, platforms, and entry points
4. Desired outcome or success signal
5. Constraints such as timeline, compatibility, architecture, compliance, or release timing
6. Relevant evidence such as screenshots, current flows, repo areas, support notes, analytics, or related bugs
7. Explicit non-goals

If the request is underspecified, infer a minimal problem statement and say what is still unknown.

Before launching sub-agents, read the closest project instructions and any relevant docs for the touched area, such as:

- `AGENTS.md`
- product or roadmap docs
- architecture notes for the affected module
- design system or platform guidance if the feature is UI-heavy

## Step 2: Bound the Planning Brief

Write a short planning brief for the swarm:

1. What should improve
2. What should remain stable
3. What counts as MVP
4. Which assumptions are evidence-backed versus speculative
5. What a good recommendation must answer

Use read-only evidence gathering where useful:

- `rg`, `git diff`, `git log`, `git show`
- reading relevant code paths and docs
- inspecting screenshots, mockups, or existing flows
- checking current tests, flags, or config for nearby constraints

Do not edit files or implement the feature as part of this skill.

## Step 3: Launch Four Read-Only Planning Lanes in Parallel

Launch four sub-agents when the feature is large enough or ambiguous enough that parallel shaping helps. For a tiny and obvious change, it is acceptable to plan locally instead.

For every sub-agent:

- give the same feature packet and planning brief
- state that the sub-agent is read-only
- do not let the sub-agent edit files, run `apply_patch`, stage changes, commit, or perform any other state-mutating action
- ask for concise planning output only
- ask for: recommended plan shape, assumptions, biggest risks, missing information, suggested sequencing, and confidence
- tell the sub-agent to avoid generic brainstorming, nits, or speculative ideas without clear user value
- tell the sub-agent to send findings back to the main agent only

Use these four planning lanes.

### Sub-Agent 1: Product and Value Lane

Clarify the user and product case for the feature.

Check for:

1. The real user problem being solved
2. The narrowest credible MVP boundary
3. Risks of scope creep or feature bloat
4. Whether the feature is likely to create adoption friction, confusion, or weak value density

This sub-agent is read-only. It must not edit files, apply patches, or make any other workspace changes.

Recommended sub-agent role: `reviewer`

### Sub-Agent 2: UX and Interaction Lane

Shape the user flow and interaction model.

Check for:

1. Main task flow and entry point clarity
2. Empty, loading, error, and permission states
3. Discoverability, reversibility, and edge cases
4. Whether the experience can be simplified without weakening the outcome

This sub-agent is read-only. It must not edit files, apply patches, or make any other workspace changes.

Recommended sub-agent role: `reviewer`

### Sub-Agent 3: Engineering and Architecture Lane

Trace the likely implementation shape and technical seams.

Check for:

1. Touched subsystems, data contracts, and integration points
2. Risks around shared state, migrations, or compatibility
3. Whether the feature fits existing architecture or needs new boundaries
4. The smallest implementation shape that remains maintainable

This sub-agent is read-only. It must not edit files, apply patches, or make any other workspace changes.

Recommended sub-agent role: `explorer` for broad codebase lookup, or `reviewer` when a deeper reasoning pass is more useful

### Sub-Agent 4: Delivery and Rollout Lane

Shape the implementation sequence and launch safety.

Check for:

1. The safest way to slice the work
2. Testability, observability, and rollback needs
3. Whether the feature needs flags, staged rollout, or telemetry
4. Risks that could make the feature expensive to deliver relative to its value

This sub-agent is read-only. It must not edit files, apply patches, or make any other workspace changes.

Recommended sub-agent role: `reviewer`

Report only planning output that materially improves the odds of building the right thing. It is better to return three credible paths than eight vague feature ideas.

## Step 4: Synthesize 2-4 Implementation Plans

The main agent owns synthesis. Treat sub-agent output as planning input, not final output.

Merge the lane outputs and build 2-4 concrete plans. Avoid fake variety. If only one or two plans are truly credible, say so directly.

Normalize each surviving plan into this shape:

1. Plan label
2. User promise and scope boundary
3. Main UX shape
4. Main architecture shape
5. Suggested implementation sequence
6. Main risks and tradeoffs
7. Validation and rollout notes
8. Confidence: high, medium, or low

When useful, aim for a set like:

- fastest viable plan
- balanced plan
- strategic or extensible plan

## Step 5: Recommend One Path

Present the result in this order:

1. Recommended plan
2. Other credible plans
3. Why the recommendation wins
4. Decisions or assumptions to confirm before implementation
5. Suggested next step

If the evidence is too weak for a real recommendation, say so directly and lead with the missing information instead of pretending the decision is settled.

Do not implement the feature as part of this skill. The output is a read-only planning recommendation with multiple plan options and one clear preferred path.
