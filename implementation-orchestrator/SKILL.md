---
name: implementation-orchestrator
description: "Plan and execute an approved feature, redesign, or release remediation with dependency-aware work packets, validation gates, and parallel worker agents. Use when a plan has already been chosen and the work should be coordinated safely across multiple files or modules."
---

# Implementation Orchestrator

Turn an approved plan into safe execution. Unlike advisory swarms, this skill may analyze, delegate implementation, integrate results, and validate the final outcome. Use read-only planning first, then execute only after a dependency-aware plan exists.

## Modes

Choose the mode from the user's request:

- `plan-only`: build the execution plan and work packets, but do not start implementation
- `execute`: build the plan and run worker agents
- `execute-and-validate`: build the plan, run worker agents, and complete the required validation gates

If the user does not specify, default to:

- `plan-only` when the user asks to break work down or orchestrate a plan
- `execute` when the user asks to implement
- `execute-and-validate` when the user asks to implement and verify

## Step 1: Build the Execution Packet

Collect the smallest useful execution packet:

1. Chosen plan or approved direction
2. Success criteria and done definition
3. Target paths, modules, or feature area
4. Behavior or interfaces that must remain unchanged
5. Constraints such as deadlines, rollout requirements, compatibility, or migration rules
6. Required checks and validation expectations
7. Explicit non-goals and out-of-scope areas

If several materially different plans are still in play, stop after planning and ask the user to choose, or explicitly state which default recommendation you are using.

Before planning, read the closest local instructions and relevant docs for the touched area, such as:

- `AGENTS.md`
- architecture docs
- rollout or migration docs
- test and release workflow docs

## Step 2: Run Four Read-Only Planning Lanes in Parallel

Launch four planning sub-agents when the scope is large enough that decomposition benefits from multiple lenses. For a tiny and tightly coupled change, it is acceptable to plan locally instead.

For every planning sub-agent:

- give the same execution packet
- state that the sub-agent is read-only during planning
- do not let the sub-agent edit files, run `apply_patch`, stage changes, commit, or perform any other state-mutating action
- ask for concise decomposition guidance only
- ask for: packet candidates, dependencies, key risks, required checks, integration notes, and confidence
- tell the sub-agent to avoid proposing overlapping file ownership unless the overlap is unavoidable and explicitly justified

Use these four planning lanes.

### Sub-Agent 1: Architecture and Boundary Lane

Clarify the technical shape of the work.

Check for:

1. Touched subsystems and interface seams
2. Invariants that must be preserved
3. Coupling risks and migration edges
4. The smallest maintainable architecture change that fits the approved plan

This sub-agent is read-only. It must not edit files, apply patches, or make any other workspace changes.

Recommended sub-agent role: `explorer` for broad codebase mapping, or `reviewer` when the scope is already tightly known

### Sub-Agent 2: Ownership and Packetization Lane

Split the work into safe execution units.

Check for:

1. Non-overlapping file ownership
2. Natural packet boundaries
3. Dependency order and parallel execution waves
4. Likely merge-conflict zones or ownership collisions

This sub-agent is read-only. It must not edit files, apply patches, or make any other workspace changes.

Recommended sub-agent role: `explorer`

### Sub-Agent 3: Validation and Rollout Lane

Protect correctness and ship safety.

Check for:

1. Packet-level checks
2. Cross-packet integration checks
3. Rollout, flag, telemetry, and rollback requirements
4. The smallest validation sequence that still gives real confidence

This sub-agent is read-only. It must not edit files, apply patches, or make any other workspace changes.

Recommended sub-agent role: `reviewer`

### Sub-Agent 4: Risk and Integration Lane

Look for execution traps before implementation starts.

Check for:

1. Ordering, shared state, or concurrency risks
2. Data, migration, or compatibility fallout
3. Adjacent flows that must change together
4. Main-thread integration risks and fallback needs

This sub-agent is read-only. It must not edit files, apply patches, or make any other workspace changes.

Recommended sub-agent role: `reviewer`

## Step 3: Build One Dependency-Aware Execution Plan

The main agent owns synthesis. Merge the planning outputs into one work graph before any worker starts.

Every work packet must include:

1. Packet ID and objective
2. Owned files
3. Dependencies
4. Invariants to preserve
5. Out-of-scope boundaries
6. Required checks
7. Integration notes
8. Done criteria

Follow these rules:

- one owner per file per execution wave
- no parallel edits on overlapping file sets
- keep packets narrow, testable, and measurable
- stop and re-plan when packet boundaries remain unstable

If the user asked for `plan-only`, stop here and report the plan.

## Step 4: Execute with Worker Agents

Spawn one worker per independent packet in the current execution wave. The number of workers is dynamic and does not need to be four.

For every worker:

- assign explicit file or module ownership
- state that the worker is not alone in the codebase and must ignore unrelated edits by others
- tell the worker not to touch files outside ownership unless the main agent explicitly reassigns scope
- require the worker to implement only the packet objective
- require the worker to run the packet's required checks and report exact results
- require the worker to return changed files and integration notes

Do not start worker execution before the dependency-aware plan is complete.

## Step 5: Integrate and Validate

The main agent integrates worker output and owns final validation.

Run validation in this order:

1. Packet-level checks
2. Cross-packet integration checks
3. Broader safety checks when the scope is wide enough to justify them

Do not claim completion if any required check fails. Stop and re-plan if integration repeatedly exposes bad packet boundaries.

## Step 6: Report and Close

Close with a concise execution summary:

1. Completed packets
2. Blocked or deferred packets
3. Validation run and exact outcomes
4. Residual risks
5. Recommended next step

This skill may edit files through worker execution and main-thread integration, but it should not stage, commit, or push unless the user explicitly asked for those actions.
