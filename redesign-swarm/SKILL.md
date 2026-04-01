---
name: redesign-swarm
description: "Parallel read-only multi-agent redesign planning for evaluating an existing surface and proposing 2-4 redesign directions with tradeoffs and one recommended path. Use when the user wants to improve the UX, information architecture, or visual direction before implementation starts."
---

# Redesign Swarm

Evaluate an existing product surface with four read-only redesign lanes in parallel, then have the main agent synthesize a small set of redesign directions and recommend one. This skill is advisory only: it does not edit files or produce implementation code.

## Step 1: Build the Redesign Packet

Collect the smallest useful redesign packet:

1. The target surface, flow, or screen
2. Current pain points or reasons a redesign is being considered
3. Target users and primary tasks
4. Screenshots, recordings, mockups, or relevant file paths when available
5. Product, brand, platform, and design system constraints
6. Success criteria for the redesign
7. Explicit non-goals or things that must stay recognizable

If the request is underspecified, infer a minimal redesign brief and say what is still unknown.

Before launching sub-agents, read the closest project instructions and relevant docs for the touched area, such as:

- `AGENTS.md`
- product notes or support feedback summaries
- design system or brand guidance
- architecture notes for the target surface

## Step 2: Bound the Redesign Brief

Write a short redesign brief for the swarm:

1. What feels broken or weak today
2. What should remain stable
3. What kind of improvement matters most
4. Which evidence is user-backed versus inferred
5. What a successful redesign recommendation must answer

Use read-only evidence gathering where useful:

- reviewing screenshots, mocks, flows, and current UI code
- reading product notes, bug reports, and support feedback
- checking relevant navigation, state, and styling code paths

Do not edit files or implement the redesign as part of this skill.

## Step 3: Launch Four Read-Only Redesign Lanes in Parallel

Launch four sub-agents when the redesign is strategic enough that parallel thinking helps. For a tiny polish request, it is acceptable to plan locally instead.

For every sub-agent:

- give the same redesign packet and redesign brief
- state that the sub-agent is read-only
- do not let the sub-agent edit files, run `apply_patch`, stage changes, commit, or perform any other state-mutating action
- ask for concise redesign output only
- ask for: diagnosis, design principles, recommended direction, biggest risks, missing information, and confidence
- tell the sub-agent to avoid vague aesthetic commentary without user or product impact
- tell the sub-agent to send findings back to the main agent only

Use these four redesign lanes.

### Sub-Agent 1: Friction and User Journey Lane

Clarify where the current experience creates friction.

Check for:

1. Confusing entry points or unclear next actions
2. Friction in the main user journey
3. Failure, empty, or edge states that weaken confidence
4. Whether the redesign should simplify, reorder, or remove steps

This sub-agent is read-only. It must not edit files, apply patches, or make any other workspace changes.

Recommended sub-agent role: `reviewer`

### Sub-Agent 2: Information Architecture and Interaction Lane

Reshape structure and interaction logic.

Check for:

1. Screen hierarchy, grouping, and emphasis
2. Navigation model and control placement
3. Whether users can predict outcomes and recover from mistakes
4. Opportunities to simplify the interaction model without hiding critical power

This sub-agent is read-only. It must not edit files, apply patches, or make any other workspace changes.

Recommended sub-agent role: `reviewer`

### Sub-Agent 3: Visual System and Affordance Lane

Improve the visual direction and clarity of the interface.

Check for:

1. Visual hierarchy and emphasis
2. Affordance, feedback, and state clarity
3. Consistency with the app's broader visual system
4. Whether the redesign should be subtle, strong, or system-level

This sub-agent is read-only. It must not edit files, apply patches, or make any other workspace changes.

Recommended sub-agent role: `reviewer`

### Sub-Agent 4: Implementation and Rollout Lane

Shape a redesign that can actually ship.

Check for:

1. The safest slicing of redesign work
2. Risks around migration, hidden coupling, or visual regressions
3. Whether the redesign needs instrumentation, rollout steps, or user education
4. The cost of a minimal refresh versus a deeper rethink

This sub-agent is read-only. It must not edit files, apply patches, or make any other workspace changes.

Recommended sub-agent role: `reviewer`

Report only redesign output that materially improves clarity, usability, or product fit. It is better to return two strong redesign directions than a large pile of generic feedback.

## Step 4: Synthesize 2-4 Redesign Directions

The main agent owns synthesis. Treat sub-agent output as redesign input, not final output.

Merge the lane outputs and build 2-4 credible redesign directions. Avoid fake variety. If only one or two directions are real options, say so directly.

Normalize each direction into this shape:

1. Direction label
2. Core design idea
3. Main flow or layout changes
4. Visual language tendencies
5. What improves most
6. What remains stable
7. Cost, risk, and implementation pressure
8. Confidence: high, medium, or low

When useful, aim for a set like:

- minimal refresh
- targeted redesign
- deeper rethink

## Step 5: Recommend One Direction

Present the result in this order:

1. Recommended direction
2. Other credible directions
3. Why the recommendation wins
4. Quick wins that can ship first
5. Decisions or assumptions to confirm before implementation

If the evidence is too weak for a serious redesign recommendation, say so directly and lead with the missing context instead of inventing certainty.

Do not implement the redesign as part of this skill. The output is a read-only redesign recommendation with multiple directions and one clear preferred path.
