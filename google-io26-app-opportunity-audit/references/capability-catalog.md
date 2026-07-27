# Google I/O 2026 Capability Catalog

Use this as a dated discovery map. It reflects official material available on 2026-07-27. Re-open the sources during every audit because AndroidX maturity, device support, private previews, Firebase products, models, policy, and quotas change.

## Source order

Prefer:

1. Android, AndroidX, Firebase, Google AI, and Google Play API documentation
2. official release notes and dependency status
3. Google I/O sessions and official Android or Google developer blogs
4. official device and product documentation for reach constraints
5. official external-provider documentation

A keynote or Pixel/Gemini demo does not establish a third-party API.

## Current AI routing pages

- Find the right AI/ML solution for your app
  https://developer.android.com/ai/overview
- Top AI on Android updates from Google I/O 2026
  https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26
- Android Developers AI section
  https://developer.android.com/ai

The current solution guide separates three paths:

- on-device inference such as ML Kit GenAI over Gemini Nano or custom LiteRT models
- cloud inference such as Firebase AI Logic and Gemini models
- exposing app functionality to system intelligence through AppFunctions

Do not collapse these paths into one “Gemini integration.”

As of 2026-07-27, Android 17/API 37 is final, while many I/O 2026 intelligence additions are not. Record platform maturity and library/service maturity separately.

## AppFunctions and Android MCP

- AppFunctions overview
  https://developer.android.com/ai/appfunctions

As of the catalog date:

- AppFunctions is a platform API plus Jetpack library for exposing app tools, services, and data to an on-device registry.
- Google describes AppFunctions as the mobile equivalent of MCP tools and as enabling an app to behave like an on-device MCP server.
- The API is experimental preview.
- Gemini integration is a separate private preview or trusted-tester path.
- The documented integration starts on Android 16+, but exact callers, permissions, schema support, and production access must be rechecked.

Recheck every status, supported Android version, schema restriction, permission, caller, and testing requirement. Never recommend “ship Gemini control now” solely because the AppFunctions API can be prototyped.

Implementing AppFunctions does not expose the app to ChatGPT, Claude, or arbitrary MCP clients. Those integrations require a separately reachable remote MCP or API service, independent authentication or OAuth, tool authorization, retention analysis, and operating cost.

Audit:

- actions and data safe enough to expose
- idempotency and confirmation
- authentication and user-presence requirements
- least-privilege data return
- background execution and timeout behavior
- prompt-injection and confused-deputy risks
- test-agent coverage
- fallback to ordinary in-app UI, intents, or app links

## Gemini Nano and on-device inference

- Gemini Nano
  https://developer.android.com/ai/gemini-nano
- Build intelligent Android apps: on-device inference
  https://developer.android.com/blog/posts/build-intelligent-android-apps-on-device-inference
- AI/ML solutions overview
  https://developer.android.com/ai/overview

Current ML Kit GenAI families to verify include:

- Prompt
- summarization
- proofreading
- rewriting
- image description
- speech recognition

Google I/O 2026 material also discusses Gemini Nano 4 preview, structured output, and prefix caching. Confirm the actual artifact version and maturity rather than treating “upcoming” as shipped.

Check:

- compatible device and AICore availability
- model download and storage
- token and media limits
- supported languages and regions
- battery, thermal, latency, and concurrency
- output safety and terms
- offline behavior before and after model availability
- fallback for unsupported devices

At the catalog date the ML Kit GenAI surfaces are beta and device-limited. Inference is allowed only while the app is the top foreground application; a foreground service does not qualify and can receive `BACKGROUND_USE_BLOCKED`. Reject scheduled, notification-triggered, widget-only, unattended, and background-critical Nano designs.

Require:

- `checkStatus()` or the task-specific `checkFeatureStatus()` before use
- handling for AVAILABLE, DOWNLOADABLE, DOWNLOADING, UNAVAILABLE, BUSY, and battery quota states where exposed
- exact device, language, task, token, and media limits
- awareness that supported devices can use different Nano base models and outputs
- fallback for unavailable or busy states
- current unlocked-bootloader restrictions where documented

## Cloud and hybrid AI

Start from:

- Firebase AI Logic documentation
  https://firebase.google.com/docs/ai-logic
- Gemini Developer API documentation
  https://ai.google.dev/gemini-api/docs
- Android AI/ML solutions overview
  https://developer.android.com/ai/overview

Verify:

- supported models and modalities
- client SDK versus server SDK trust boundary
- App Check, authentication, quotas, billing, abuse controls, and rate limits
- data use, retention, regions, and safety settings
- hybrid routing and offline fallback
- structured output, function or tool calling, streaming, retrieval, evaluation, and observability

Use LiteRT or LiteRT-LM for app-owned models only when model quality, delivery size, hardware reach, updates, and safety are credible.

A Firebase AI Logic candidate cannot be P0 without enforced production App Check using Play Integrity, per-user quotas, remotely controllable model selection, and explicit abuse and spend handling. Debug-provider-only enforcement is pre-production.

## Android 17 and adaptive native experience

- Google I/O 2026 adaptive ecosystem overview
  https://android-developers.googleblog.com/2026/05/android-adaptive-development-ecosystem.html
- Compose-first direction
  https://android-developers.googleblog.com/2026/05/android-ui-development-is-compose-first.html
- Android I/O 2026 highlights
  https://android-developers.googleblog.com/2026/05/17-things-android-developers-google-io.html
- Android 17
  https://developer.android.com/about/versions/17
- Android 17 migration
  https://developer.android.com/about/versions/17/migration
- Material 3 in Compose
  https://developer.android.com/develop/ui/compose/designsystems/material3
- Navigation 3
  https://developer.android.com/guide/navigation/navigation-3
- Shared transitions
  https://developer.android.com/develop/ui/compose/animation/shared-elements
- Compose graphics
  https://developer.android.com/develop/ui/compose/graphics/draw/overview
- AGSL and runtime shaders in Compose
  https://developer.android.com/develop/ui/compose/graphics/draw/brush

Verify the current status of:

- Android 17 adaptive behavior
- Compose, Material, Navigation 3, Styles, Grid, Flexbox, and other AndroidX artifacts
- phone, foldable, tablet, resizable desktop-window, keyboard, trackpad, stylus, and focus support
- Googlebook or other newly announced form factors

Use current Kotlin and Compose for new native UI. Treat Views as interoperability or migration. AGSL, motion, and expressive styling are implementation tools, not standalone product value.

Prefer Compose for net-new UI when the existing architecture supports it. Views remain supported; do not recommend a wholesale rewrite without a concrete adaptive, accessibility, maintainability, or delivery benefit.

Navigation 3 has a stable 1.0 line, but every exact dependency must still be verified. Android 17 removes more large-screen opt-outs for API 37 targets, making resize, keyboard, pointer, state restoration, and adaptive-window testing mandatory groundwork rather than optional polish.

## Devices and ecosystem

Use current official platform guides for:

- Wear OS, Tiles, complications, Health Services, Health Connect, notifications, and voice or glanceable tasks
- earbuds, Bluetooth, audio routing, media sessions, speech recognition, and hands-free use
- Android Auto and Automotive OS
- Android TV
- Android XR
- foldables, tablets, desktop windows, ChromeOS, and Googlebook
- cross-device SDKs and nearby or companion-device capabilities
- widgets and Glance

Differentiate a public Android API from Gemini, Pixel, Nest, or first-party accessory behavior. Require a clear phone fallback when proposing wearable, XR, or accessory experiences.

Current cautions to recheck:

- Wear OS 7 and new Wear intelligence surfaces have different maturity from established Tiles, complications, Health Services, and media sessions.
- Gemini on headphones is a system/user feature, not a general third-party command API.
- Fast Pair companion integration is for qualifying hardware partners and certification programs.
- Cross Device SDK Developer Preview must never be P0 or a production recommendation. It is limited to phone/tablet and two-device interactions. Use it only for P1/P2 prototyping; evaluate Android 17 Handoff, Cast, media sessions, account sync, or Companion Device Manager for production.
- Treat Googlebook Magic Pointer, prompt-created custom widgets, Quick Access to phone files, and seamless phone-app access as system/product behavior unless a current public API proves the proposed integration. Durable app work is adaptive layouts, multi-instance, keyboard/pointer, drag and drop, files/print, and ordinary widgets.
- Android XR audio-glasses and display-glasses augmented experiences are prototype/emulator-only until official distribution guidance changes and cannot be P0. Headset and wired-XR-glasses proposals must separately verify the mobile versus dedicated XR track and manifest features.
- Health Services supplies real-time Wear OS sensors and exercise metrics; Health Connect is the shared health and fitness data store with its own permissions. Do not treat them as interchangeable.
- For watch faces, verify the current Watch Face Format requirement. For Wear apps with native libraries, verify the 64-bit requirement taking effect 2026-09-15.

## Play, privacy, and distribution

Verify:

- Target API requirements
  https://developer.android.com/google/play/requirements/target-sdk
- Android developer verification
  https://developer.android.com/developer-verification
- Data Safety
  https://support.google.com/googleplay/android-developer/answer/10787469
- Generative AI policy
  https://support.google.com/googleplay/android-developer/answer/13985936

Audit target deadlines, package registration, signing ownership, SDK data flows, privacy policy, Data Safety, retention and deletion, child safety, moderation, and report or flag flows. Purely on-device processing and cloud transmission have different disclosure implications. Any cloud AI path needs explicit abuse, quota, spend, credential, and user-visible failure controls.

## External providers, subscriptions, and MCP

Verify current official provider documentation for:

- API authentication and model availability
- consumer plan versus developer API billing
- delegated OAuth or user-account access
- key handling, retention, regions, rate limits, and safety terms
- MCP client/server support and transport security

Start with:

- OpenAI API and help center
  https://platform.openai.com/docs/
  https://help.openai.com/
- Anthropic API and support
  https://docs.anthropic.com/
  https://support.anthropic.com/
- Gemini API documentation
  https://ai.google.dev/gemini-api/docs
- Model Context Protocol specification
  https://modelcontextprotocol.io/
- OpenAI API key safety
  https://help.openai.com/en/articles/5112595-best-practices-for-api
- ChatGPT subscription versus API
  https://help.openai.com/en/articles/8156019-how-can-i-move-my-chatgpt-subscription-to-the-api
- Anthropic subscription versus API
  https://support.anthropic.com/en/articles/9876003-i-subscribe-to-a-paid-claude-ai-plan-why-do-i-have-to-pay-separately-for-api-usage-on-console
- Anthropic API key safety
  https://support.anthropic.com/en/articles/9767949-api-key-best-practices-keeping-your-keys-safe-and-secure
- Gemini API billing
  https://ai.google.dev/gemini-api/docs/billing

Default unless current documentation proves otherwise:

- consumer chat subscriptions are not developer API credentials or budgets
- long-lived provider secrets do not belong in the APK
- MCP is a protocol and tool boundary, not a model or an automatic paid-account bridge
- AppFunctions’ Android MCP role does not make an arbitrary remote MCP server available to Gemini

## Required truth-record format

```text
Capability:
Proposed app use:
Public surface:
API/dependency status:
Gemini/system integration status, if separate:
Maturity:
Access:
Reach:
Minimum API/SDK/library:
Device/language/country/account constraints:
Permission/policy/quota:
Processing boundary:
Source title:
Source URL:
Source date or last updated:
Checked on:
Unknowns:
```
