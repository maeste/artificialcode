# Media Pipeline (GitHub Auto-Upload)

Buffer requires public HTTPS URLs for images and videos. This skill uses the project's own GitHub repository to serve media via `raw.githubusercontent.com`.

## Flow

```
Local file (social/media/foo.png)
  → check if tracked by git
  → if not: git add
  → if uncommitted: git commit
  → ask user to git push
  → verify URL accessibility
  → use URL in Buffer createPost
```

## URL construction

Given:
- `git remote get-url origin` → `https://github.com/<owner>/<repo>.git` (or SSH form)
- `git rev-parse --abbrev-ref HEAD` → `<branch>`
- Media path relative to repo root: `<path>`

The raw URL is:
```
https://raw.githubusercontent.com/<owner>/<repo>/<branch>/<path>
```

Remote URL parsing handles:
- `https://github.com/owner/repo.git`
- `https://github.com/owner/repo`
- `git@github.com:owner/repo.git`

## Fallback configuration

If `git remote get-url origin` does not match a GitHub URL, the scheduler looks for overrides in `.buffer/config.json`:

```json
{
  "github_owner": "maeste",
  "github_repo": "artificialcode",
  "github_branch": "main"
}
```

If neither is available, the script errors with a clear message asking the user to either add a GitHub remote or create `config.json`.

## Commit grouping

During dry-run, the scheduler collects all media files that need committing and reports them. During `--confirm` mode, if any are still missing, the script:

1. `git add` all of them in a single call
2. Creates one commit with a message like: `Add media for <campaign-name> social campaign`
3. Asks the user to run `git push` and confirm
4. Verifies each URL returns HTTP 200 with `curl -I` before proceeding

The scheduler never pushes automatically. The user must run `git push` themselves.

## Skipping the pipeline

If `media:` in the campaign markdown is already an `https://` URL (e.g. `https://lince.sh/assets/foo.png`), the pipeline is skipped for that file. The scheduler verifies the URL is reachable and uses it as-is.

## Private repositories

This pipeline only works for **public GitHub repositories**. `raw.githubusercontent.com` does not serve private repo content without authentication, and Buffer cannot authenticate to private hosts.

If your repo is private, options:
- Move media to a public repo
- Use a public CDN (upload elsewhere, put the URL in `media:`)
- Use a public gist

The scheduler warns if `gh api repos/{owner}/{repo}` reports the repo as private (best-effort check, uses `gh` CLI if available).

## Security note

Once a file is pushed to a public GitHub repo, it is public forever even if later deleted (git history). Do not push sensitive content through this pipeline.
