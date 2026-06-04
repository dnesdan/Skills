---
name: reddit-promo-writing
description: Draft Reddit promo posts and comments for indie apps in a source-aware, non-spammy style. Use when asked to create, revise, localize, or adapt Reddit marketing copy, launch posts, feedback requests, subreddit-specific posts, or comment replies for an app.
---

# Reddit Promo Writing

Use this skill for Reddit-facing promo copy for apps. The output should feel like an indie developer asking for useful attention, not a polished ad.

## Default Voice

- Voice: direct, practical, humble, specific.
- Avoid hype, fake virality, corporate launch language, and generic AI-marketing phrasing.
- Lead with the concrete user problem, the app's constraint, or the thing the developer built differently.
- Mention being the developer when relevant.
- Czech or English depending on subreddit and user request.
- Prefer one strong post over many broad variants unless the user asks for variants.

## Posting Context

Ask for or infer these when the user wants ready-to-post subreddit copy:

- Reddit account/login to post from, formatted as a username such as `u/example_dev`.
- Target subreddit names, formatted as `r/example`.
- Whether the account is the developer's official/personal account, a company account, or another disclosed role.
- Whether links should be included in the post body, first comment, or omitted.

Example context format:

```text
Reddit login: u/example_dev
Target subreddits: r/iosapps, r/SideProject, r/AppleWatch, r/czech
Disclosure: I am the developer.
Link policy: Put the App Store link in the first comment only if subreddit rules allow it.
```

Treat these as examples of shape only. Do not assume these exact subreddits, login, or disclosure unless the user provides them.

## Inputs To Gather

Use local evidence first:

- app repo README, metadata, App Store / Play metadata files
- screenshots or `app_store_assets` context
- release notes / recent git changes when the post is about an update
- subreddit rules and tone when a target subreddit is named
- previous Reddit profile/style notes if available in the current workspace or session history
- user-provided Reddit login, target subreddits, and disclosure preference

If subreddit rules or current posts are needed, browse only when the user asked for subreddit-specific posting or up-to-date fit.

## Workflow

1. Identify the app, audience, subreddit, and post objective:
   - launch
   - feedback request
   - update announcement
   - problem/solution story
   - comment reply
2. Extract truthful product claims from source files.
3. Confirm posting context when needed:
   - target subreddit(s)
   - Reddit login/account identity
   - disclosure wording
   - link placement
4. Pick a Reddit shape:
   - `Feedback request`: "I built X because Y; what would you change?"
   - `Build story`: short context, hard tradeoff, result, ask
   - `Useful resource`: explain the problem and include the app as the implementation
   - `Update`: what changed, why it matters, what feedback is needed
5. Draft:
   - title options, usually 3-5
   - one main post
   - optional first comment with link/disclosure if useful
   - short note about subreddit fit/risk

## Style Rules

- Be specific about the app's actual behavior.
- Keep the first paragraph short.
- Use plain language, not App Store keyword copy.
- Include a real ask: feedback, edge cases, critique, testers, or experience reports.
- Avoid dark patterns:
  - no fake user persona
  - no pretending not to be the developer
  - no astroturfing
  - no mass-posting plan
- For Czech apps, natural Czech is preferred over literal English marketing translations.

## Output Template

```markdown
**Subreddit Fit**
...

**Posting Context**
- Account: `u/...`
- Target: `r/...`
- Disclosure: ...

**Titles**
1. ...
2. ...
3. ...

**Post**
...

**Optional First Comment**
...

**Risk / Edit Notes**
...
```

Skip sections that are not useful for a tiny request.

## Guardrails

- If a subreddit forbids promotion, propose a feedback-first or discussion-first rewrite, or recommend not posting.
- Do not fabricate metrics, ratings, downloads, testimonials, or user stories.
- Do not include store links unless the user wants a ready-to-post version or the subreddit allows it.
- Keep variants meaningfully different: angle, audience, or ask must change.
