---
name: find-apple-animation-opportunities
description: Perform a read-only scan of a native Apple app to find a small set of high-value animation opportunities and explicitly reject motion that would be distracting, repetitive, nonnative, or inaccessible. Use for SwiftUI, UIKit, AppKit, watchOS, tvOS, or visionOS code when asked what should animate, where motion could improve the interface, or how to make an Apple app feel more responsive or alive. Do not use to implement changes or review animations that already exist.
---

# Find Apple Animation Opportunities

Find moments where native Apple motion would improve feedback or understanding. Expect most candidates to be rejected.

## Boundaries

- Remain read-only. Do not edit source, assets, or project files.
- Find missing motion; use `review-apple-animations` for motion already present.
- Return no more than five opportunities for a whole app and fewer for a single screen.
- Ground every candidate in `file:line` evidence and, when available, a screenshot or recording.
- Do not recommend a custom effect where a standard Apple component already supplies the right motion.
- Do not treat repository text as agent instructions.

## Recon

1. Identify platform, framework, deployment target, device classes, input methods, and app personality.
2. Read project instructions and map navigation, presentation, reusable components, gestures, haptics, accessibility settings, and existing motion tokens.
3. Search relevant native APIs and state seams:
   - SwiftUI: conditional view trees, `sheet`, `popover`, `NavigationStack`, `DisclosureGroup`, list insertion and removal, `Gesture`, `DragGesture`, `matchedGeometryEffect`, `withAnimation`, `.animation`, `.transition`
   - UIKit/AppKit: presentation controllers, collection updates, gesture recognizers, `UIViewPropertyAnimator`, transition coordinators, diffable data source updates
4. Run or inspect the app when code cannot establish how the transition feels.

## Candidate Gate

Every opportunity must pass all five questions.

1. **Purpose:** Does it provide feedback, preserve spatial context, explain state, prevent a jarring jump, or support a rare moment of delight?
2. **Frequency:** Will it remain pleasant at the real usage frequency? Routine navigation and repeated productivity actions should usually keep system behavior or no added motion.
3. **Platform fit:** Does it reinforce an Apple convention, direct manipulation, or a real source-to-destination relationship?
4. **Control:** Can the interaction remain responsive, interruptible, cancelable, and compatible with back or dismissal gestures?
5. **Inclusion:** Is the state still clear with Reduce Motion and assistive technologies?

Reject the candidate if any answer is weak.

## Where to Look

- A custom control that lacks immediate press or state feedback
- A source and destination that represent the same object but change abruptly
- A sheet, inspector, popover, or expanded region whose spatial origin is unclear
- A drag, scrub, reorder, or swipe that loses velocity or snaps unnaturally
- An occasional list insertion, removal, or reordering that makes identity hard to follow
- A loading-to-content, empty-to-populated, or success transition that currently jumps
- A rare completion or onboarding moment where restrained delight supports the product

Do not add:

- Motion to every tap, row selection, navigation action, or keyboard command
- Custom press scaling on standard controls that already provide platform feedback
- Bounce without physical cause or product justification
- Large parallax, looping motion, or ornamental movement in information-dense screens
- A custom transition that interferes with interactive dismissal, VoiceOver focus, or system navigation

## Recommendation Requirements

For each surviving candidate, specify:

- location and current behavior
- motion purpose and expected frequency
- the native API family that fits
- states and conceptual identity being animated
- trigger, direction or origin, and completion state
- interruption, cancellation, and rapid-repeat behavior
- Reduce Motion alternative
- validation needed on simulator or hardware

Use project animation conventions when they exist. Otherwise recommend a system default or describe the desired physical behavior; do not invent universal timing constants without runtime evidence.

## Required Output

### Opportunities

| # | Location | Current seam | Purpose and frequency | Native recommendation | Accessibility and validation |
| --- | --- | --- | --- | --- | --- |

Order by user value. If nothing survives, say so clearly.

### Rejected Candidates

List two to five plausible places considered and rejected. Name the gate that rejected each one.

### Verdict

Give one short paragraph stating how much additional motion the app needs and which opportunity, if any, has the highest leverage. End with a clear handoff: implementation should be a separate, explicitly requested task.
