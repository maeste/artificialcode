# Buffer GraphQL API Reference

Notes on Buffer's GraphQL API specifically for this skill. These are lessons learned from real usage.

## Endpoint

```
https://api.buffer.com/graphql
```

Not `graph.buffer.com`. That hostname returns:
```json
{"errors":[{"message":"Please use api.buffer.com","extensions":{"code":"UNAUTHENTICATED"}}]}
```

## Authentication

Use a Bearer token:
```
Authorization: Bearer <API_KEY>
```

Get the key at https://publish.buffer.com/settings/api.

## User-Agent header is mandatory

Without a `User-Agent` header, requests are blocked by Cloudflare with HTTP 403 and body `error code: 1010`.

The scripts set `User-Agent: buffer-social-scheduler/1.0`. Python's default `urllib` user agent is rejected.

## Free plan limits

- Maximum 3 channels connected
- Maximum 10 scheduled posts per channel

The scheduler checks these limits in dry-run and errors out if exceeded.

## Introspection

Useful queries for debugging schema issues:

```graphql
# List query fields
{ __schema { queryType { fields { name args { name } } } } }

# Inspect an input type
{ __type(name: "CreatePostInput") { inputFields { name type { name kind ofType { name } } } } }
```

## Fetch channels

```graphql
{
  account {
    id
    organizations {
      id
      name
      channels {
        id
        name
        service
      }
    }
  }
}
```

Service values observed: `twitter`, `linkedin`, `facebook`, `instagram`, `mastodon`, `threads`, `bluesky`, `youtube`, `pinterest`.

## Create a post

```graphql
mutation CreatePost($input: CreatePostInput!) {
  createPost(input: $input) {
    ... on PostActionSuccess { post { id dueAt } }
    ... on MutationError { message }
  }
}
```

With variables:
```json
{
  "input": {
    "text": "Post body here",
    "channelId": "<channel id>",
    "schedulingType": "automatic",
    "mode": "customScheduled",
    "dueAt": "2026-04-13T08:00:00.000Z",
    "assets": {
      "images": [{"url": "https://..."}]
    }
  }
}
```

### Required fields

- `text`
- `channelId`
- `schedulingType`: `automatic` or `manual`
- `mode`: `addToQueue` (next slot) or `customScheduled` (requires `dueAt`)

### Optional fields

- `dueAt`: ISO-8601 datetime with milliseconds precision (`YYYY-MM-DDTHH:MM:SS.000Z`)
- `assets.images[].url`: public URL of an image
- `assets.videos[].url`: public URL of a video
- `assets.documents[].url`: public URL of a PDF
- `assets.link`: link preview object

### Media

Media must be a **public HTTPS URL**. Buffer fetches it to upload to the target network. No direct upload via API.

Valid hosts observed:
- `raw.githubusercontent.com/...`
- `cdn.buffer.com/...`
- Any public static host

## Delete a post

```graphql
mutation {
  deletePost(input: { id: "<post id>" }) {
    __typename
  }
}
```

Selection must include `__typename` (or another field). GraphQL validation error otherwise.

Response type on success: `DeletePostSuccess`.

## Duplicate detection

Buffer rejects posts that are "too similar" to recently created posts:

```json
{
  "data": {
    "createPost": {
      "message": "Invalid post: Whoops, it looks like you've posted that one recently. Unfortunately, we're not able to post the same thing again so soon!"
    }
  }
}
```

Observed triggers:
- **Identical or near-identical text** across the same channel queue
- **Cooldown** after multiple failed creation attempts on the same channel (several minutes)
- **First-line similarity**: the opening line has more weight than the body

Mitigation:
- Vary the first line between posts on the same channel
- Wait a few minutes between retries when a post is rejected
- Rewrite more than just one or two words

## LinkedIn page mentions

The `@[Page Name]` syntax **does not work via the API**. Posts containing it are created as plain text. Page tagging must be done by editing the post in the Buffer web UI or in the published post on LinkedIn.

Recommendation: document this in campaign markdown so the user edits manually after scheduling.

## Twitter/X character limit

Default tier: 280 characters including URL (URLs are counted as 23 characters regardless of length).

X Premium: up to 25,000 characters, but most clients still truncate in feeds. For campaign posts, stay within 280 unless you have a strong reason.

## Rate limits

Not documented publicly. Observed: no issues with 14 posts created in under a minute, but repeated failures on the same channel trigger a cooldown.

## Error codes

| Code | Meaning | Fix |
|------|---------|-----|
| 403 + code 1010 | Cloudflare block (missing User-Agent) | Add User-Agent header |
| `GRAPHQL_VALIDATION_FAILED` | Schema mismatch | Check mutation with introspection |
| `UNAUTHENTICATED` | Wrong endpoint or invalid key | Use `api.buffer.com`, verify key |
| "Invalid post: ... recently" | Duplicate detection | Reword substantially, wait, retry |
