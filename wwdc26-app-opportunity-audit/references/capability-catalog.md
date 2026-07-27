# WWDC 2026 Capability Catalog

Use this catalog as a dated research launchpad. It reflects official material available on 2026-07-27. Re-open the sources during every audit because OS releases, program eligibility, provider support, and beta status can change.

## Source order

Prefer evidence in this order:

1. Apple framework documentation and availability annotations
2. Apple platform release notes
3. WWDC 2026 session pages and transcripts
4. Apple security, privacy, support, program, and App Review documentation
5. official third-party provider documentation for external model claims

Marketing pages and keynote demos can identify an experience, but they do not prove a third-party API exists.

## Apple Intelligence overview

- WWDC26 Apple Intelligence guide
  https://developer.apple.com/wwdc26/guides/apple-intelligence/
- WWDC26 iOS guide
  https://developer.apple.com/wwdc26/guides/ios/
- WWDC26 video index
  https://developer.apple.com/videos/wwdc2026/

The Apple Intelligence guide is the best current routing page. As of the catalog date it describes:

- model-agnostic `LanguageModel` conformance in the Foundation Models framework
- Apple on-device models, third-party providers, multimodal prompting, Dynamic Profiles, and evaluations
- an Apple Foundation Model on Private Cloud Compute subject to program and download eligibility
- App Intents as the developer integration surface for Siri AI

Verify the detailed documentation and legal terms before treating these summaries as implementation commitments.

As of 2026-07-27, iOS 27, iPadOS 27, macOS 27, watchOS 27, visionOS 27, Xcode 27, Siri AI, and most WWDC26 additions are prerelease. The skill must separate shipped OS 26 framework baselines from OS 27 beta enhancements.

Current Siri AI baseline to recheck:

- developer beta on iOS, iPadOS, macOS, and visionOS 27
- watchOS support promised for a later beta seed
- initial user beta in English
- initial iPhone, iPad, and Apple Watch restriction in the EU, with different Mac and Vision Pro availability
- unavailable new Apple Intelligence and Siri AI features in China
- Apple Intelligence-capable hardware, settings, account, and model readiness remain required

## Foundation Models and AI quality

- What’s new in the Foundation Models framework
  https://developer.apple.com/videos/play/wwdc2026/241/
- Build agentic app experiences with the Foundation Models framework
  Find from the Apple Intelligence guide or WWDC26 video index.
- Build with the new Apple Foundation Model on Private Cloud Compute
  Find from the Apple Intelligence guide or WWDC26 video index.
- Bring an LLM provider to the Foundation Models framework
  https://developer.apple.com/videos/play/wwdc2026/339/
- Meet the Evaluations framework
  Find from the Apple Intelligence guide or WWDC26 video index.
- Create robust evaluations for agentic apps
  Find from the Apple Intelligence guide or WWDC26 video index.
- Debug and profile agentic app experiences with Instruments
  Find from the Apple Intelligence guide or WWDC26 video index.
- Secure your app: mitigate risks to agentic features
  Find from the WWDC26 video index.
- Meet Core AI / integrate on-device AI models using Core AI
  Find from the WWDC26 video index.
- Foundation Models documentation
  https://developer.apple.com/documentation/foundationmodels/
- Private Cloud Compute developer program
  https://developer.apple.com/private-cloud-compute/
- Private Cloud Compute entitlement
  https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.private-cloud-compute

Audit questions:

- Does the use case fit a small on-device model, Apple PCC model, third-party cloud model, custom Core AI model, or hybrid router?
- Is the model available on the user’s device, language, and region?
- Does the feature need fresh external knowledge, long context, media generation, tools, or deterministic structured output?
- Are tool calls authorized per action and protected from prompt injection?
- Are evaluations versioned and representative of unsupported or low-confidence states?

Current constraints that require re-verification:

- The shipped on-device system model has a shared 4,096-token budget across instructions, prompts, transcript, and output; it works offline without a request quota.
- Do not use it as a source of current facts or for arithmetic, code generation, or complex logical reasoning.
- Guided generation constrains schema shape, not truth or deterministic field values. Validate every field.
- Rerun prompt and evaluation suites after OS or model updates.
- OS 27 adds beta multimodal, provider, profile, evaluation, and model-routing surfaces.
- Apple PCC is not a general endpoint. Its current developer path uses a 32K context, requires network access, has per-user daily quotas, and is Preview.
- Current PCC eligibility requires App Store Small Business Program membership, fewer than two million aggregate first-time downloads across the developer’s apps, the granted `com.apple.developer.private-cloud-compute` entitlement, and supported App Store, TestFlight, or ad hoc distribution. Verify Apple Intelligence reach too.
- If PCC eligibility is lost, the current program describes a six-month migration period. Do not rank PCC above P2 until enrollment, aggregate downloads, and entitlement are proven for the audited developer.
- A Foundation Models provider adapter does not give the app access to a user’s provider subscription or Apple’s private Siri context.
- A named provider package requires its own official repository/release, supported-platform, authentication, and provider-documentation proof. “Will soon publish” in a WWDC session is Unverified.

## Siri, App Intents, Shortcuts, and Spotlight

- Build intelligent Siri experiences with App Schemas
  https://developer.apple.com/videos/play/wwdc2026/240/
- Explore advanced App Intents features for Siri and Apple Intelligence
  https://developer.apple.com/videos/play/wwdc2026/343/
- Discover new capabilities in the App Intents framework
  https://developer.apple.com/videos/play/wwdc2026/345/
- Validate your App Intents adoption with AppIntentsTesting
  Find from the WWDC26 video index.
- What’s new in Shortcuts
  Find from the WWDC26 video index.
- LLM search using Core Spotlight
  Find from the WWDC26 video index.

Current concepts to verify:

- App Entities and App Schemas model app content for Siri and Apple Intelligence.
- `IndexedEntity`, semantic indexing, structured search, in-app search, onscreen awareness, content transfer, snippets, confirmations, and interaction donation are separate integration decisions.
- Voice-only devices require useful nonvisual responses.
- A consumer Siri capability or phrase does not itself create a public developer hook. “Write with Siri” must be mapped to a documented API or labeled System-only.
- “Write with Siri” is system behavior: standard text controls can adopt it automatically, while custom text engines use documented Writing Tools integration. It is not a callable Siri completion API.

## Images and visual intelligence

- Create high-quality images using Image Playground
  https://developer.apple.com/videos/play/wwdc2026/375/
- Best practices for integrating visual intelligence in your app
  https://developer.apple.com/videos/play/wwdc2026/297/
- Visual Intelligence documentation
  https://developer.apple.com/documentation/visualintelligence
- What’s new in image understanding
  Find from the WWDC26 video index.
- Bring expression to your app with Genmoji
  Follow the related resource from the Image Playground session or current documentation.

Current constraints to verify:

- Image Playground availability depends on Apple Intelligence-capable hardware, supported language and region, and the user enabling image generation.
- Use the documented availability environment or API rather than device-name assumptions.
- Image Playground can return generated image files or adaptive image glyphs depending on style and callback.
- Generated media needs a meaningful product use, storage policy, moderation strategy, accessibility description, and a non-generation fallback.
- The new OS 27 Image Playground experience is user-visible, availability- and quota-dependent, and may expose a user-configured external provider without revealing its credentials or subscription to the app.
- For the new OS 27 model, plan the system sheet or view controller and explicit user interaction. `ImageCreator` is deprecated for this path; reject hidden, unattended, bulk, or server-style generation.
- The system manages Image Playground quota and iCloud+ upsell. Do not build a competing app quota UI for this system experience.
- Persist a returned temporary image before the generation session ends. Preserve `NSAdaptiveImageGlyph` rather than flattening Genmoji to Unicode or a plain string.

For OS 27 Visual Intelligence, verify:

- the system supplies `SemanticContentDescriptor` through the documented App Intents query flow; it is not a general camera or cross-app screen feed
- only one `IntentValueQuery` accepting that descriptor is allowed per app; use `@UnionValue` for multiple entity types
- results are fast and bounded, with schema-based “More results”
- iPad and Mac expansion remains tied to the OS 27 beta baseline

## Device and ecosystem research

Route through the WWDC26 platform guides and current framework docs for:

- watchOS 27, App Intents, widgets, complications, workouts, HealthKit, notifications, and voice-first interactions
- AirPods and audio capabilities, Bluetooth accessories, Now Playing, speech recognition, live communication, and hands-free use
- macOS 27, shared SwiftUI code, App Intents, Spotlight, iCloud or CloudKit, Handoff, Universal Clipboard, Continuity Camera, local networking, and MLX
- iPadOS 27 adaptive layout, PencilKit, drag and drop, multitasking, and external input
- CarPlay, visionOS 27, tvOS, and accessory APIs when product-relevant
- WeatherKit availability, attribution, privacy, rate limits, and product fit

Do not assume Apple’s own AirPods, Siri, Continuity, or device-control experiences are third-party APIs.

Useful anchors:

- watchOS 27 guide
  https://developer.apple.com/wwdc26/guides/watchos/
- macOS 27 guide
  https://developer.apple.com/wwdc26/guides/macos/
- WeatherKit
  https://developer.apple.com/weatherkit/
- WeatherKit attribution
  https://developer.apple.com/documentation/weatherkit/weatherattribution
- Handoff
  https://developer.apple.com/documentation/foundation/implementing-handoff-in-your-app
- AirPods headphone motion
  https://developer.apple.com/documentation/coremotion/getting-motion-activity-data-from-headphones

There is no general AirPods SDK or supported hook into Siri’s AirPods conversation. Credible public surfaces are narrower: normal audio and media sessions, routing, microphone capture with permission, supported spatial-audio and head-motion APIs, and app actions exposed through documented system frameworks. Require physical-device validation.

WeatherKit requires its capability, Apple Weather attribution, quota-aware behavior, and correct handling of stale or unavailable data. Preserve severe-weather alert content and source links rather than asking an LLM to rewrite authoritative alerts. Sign REST requests on a trusted server; do not ship the WeatherKit private key in the app.

Current WeatherKit details to recheck include the `com.apple.developer.weatherkit` entitlement, 500,000 included monthly calls, paid tiers above the allowance, Apple Weather mark and legal attribution link, and the issuing agency plus Apple detail link for severe alerts.

For Continuity, verify shared Team ID, universal links or associated domains where required, restorable `NSUserActivity`, and a separate durable sync strategy. Handoff transfers activity, not durable data. Prefer current Network framework paths for new nearby networking rather than deprecated Multipeer Connectivity, and audit local-network or Bonjour declarations.

## Design and graphics

- What’s new in SwiftUI
  https://developer.apple.com/videos/play/wwdc2026/269/
- Apple Human Interface Guidelines
  https://developer.apple.com/design/human-interface-guidelines/
- SwiftUI documentation updates
  https://developer.apple.com/documentation/updates/swiftui
- Compose advanced graphics effects with SwiftUI
  https://developer.apple.com/videos/play/wwdc2026/322/

Use current SwiftUI, semantic Liquid Glass, adaptive layout, native navigation, accessibility, reduced motion/transparency, and energy-aware effects. Treat Metal and shaders as targeted implementation tools, never as evidence that a feature has product value.

## External providers, subscriptions, and MCP

For any external provider, verify current official documentation for:

- API availability and model names
- consumer subscription versus developer API billing
- whether OAuth or delegated access exists for third-party apps
- data retention, training, region, rate limits, and safety terms
- client-side key restrictions and recommended secret handling
- MCP client/server support and transport security

Start with:

- OpenAI API and billing documentation
  https://platform.openai.com/docs/
  https://help.openai.com/
- Anthropic API and billing documentation
  https://docs.anthropic.com/
  https://support.anthropic.com/
- Model Context Protocol specification
  https://modelcontextprotocol.io/

Default conclusion unless current provider documentation proves otherwise:

- a consumer chat subscription is not an API credential or API budget
- provider secrets must not ship in the app bundle
- MCP is an interoperability protocol, not a model and not an automatic bridge to a user’s paid chat account
- Foundation Models provider conformance does not waive provider authentication, billing, privacy, or policy requirements

No Apple-provided general MCP framework or Siri MCP API was identified at the catalog date. Apple Foundation Models `Tool` is not MCP. An app can implement an MCP boundary itself or through a provider/backend, but must supply authentication, authorization, approvals for side effects, auditability, and prompt-injection defenses.

Apple’s first-party ChatGPT extension may use a connected free or paid ChatGPT account inside Apple-controlled Siri, Writing Tools, or Visual Intelligence experiences. It does not expose credentials, history, quota, or subscription benefits to the third-party app and is not a reusable app API.

Direct sources:

- Apple Intelligence and ChatGPT setup
  https://help.openai.com/en/articles/10269382-setting-up-chatgpt-with-apple-intelligence
- ChatGPT subscription versus API
  https://help.openai.com/en/articles/8156019-how-can-i-move-my-chatgpt-subscription-to-the-api
- Anthropic subscription versus API
  https://support.anthropic.com/en/articles/9876003-i-subscribe-to-a-paid-claude-ai-plan-why-do-i-have-to-pay-separately-for-api-usage-on-console
- Anthropic API key safety
  https://support.anthropic.com/en/articles/9767949-api-key-best-practices-keeping-your-keys-safe-and-secure

## App Store, privacy, and payments

Verify:

- App Review Guidelines
  https://developer.apple.com/app-store/review/guidelines/
- App privacy details
  https://developer.apple.com/app-store/app-privacy-details/
- Privacy manifests
  https://developer.apple.com/documentation/bundleresources/privacy-manifest-files
- StoreKit
  https://developer.apple.com/documentation/storekit/

AI data sent off-device must be represented accurately in consent, privacy policy, privacy labels, manifests, logging, deletion, and third-party disclosures. Generated or community content can add moderation, reporting, blocking, safety, IP, and age-rating duties. A user bringing a provider account does not automatically bypass StoreKit rules for the app’s own paid digital functionality.

## Required truth-record format

Record each researched claim as:

```text
Capability:
Proposed app use:
Public surface:
Maturity:
Access:
Reach:
Minimum OS/SDK:
Device/language/region/account constraints:
Entitlement/program/quota:
Processing boundary:
Source title:
Source URL:
Source date or last updated:
Checked on:
Unknowns:
```
