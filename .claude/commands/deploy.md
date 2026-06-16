---
description: Build and deploy the Astronautisté site to gh-pages (astronautiste.cz)
argument-hint: "[--ci | --direct]  (default: --ci)"
allowed-tools: Bash, Read
---

# /deploy — publish the Astronautisté site

Deploy the Zola site to the `gh-pages` branch served at **astronautiste.cz**.
Repo-specific. The user invoking this command IS the deploy authorization (doctrine:
deploys are user-only).

## Pre-flight (always)
1. Working tree must be clean (`git status --short` empty). If not, stop and suggest
   `/commit` — never deploy uncommitted state.
2. Build must be green:
   ```bash
   bash scripts/build.sh        # Tailwind → vendor JS → zola build → zola check
   ```
   If the build or `zola check` reports broken **internal** links, stop. Never publish a
   failing build.

## Mode: `--ci` (DEFAULT, blessed path)
The site deploys via GitHub Actions on push to `master`
(`.github/workflows/deploy.yml` → build · check · Playwright smoke · `peaceiris/actions-gh-pages`,
`force_orphan`, `cname: astronautiste.cz`). `master` and `gh-pages` are deliberately separate.

1. Confirm with the user which source they want on `master` (merge the current feature
   branch, or they push it themselves for PR review). Do not merge to `master` without
   explicit confirmation.
2. After merge/push to `master`, report the Actions run URL (`gh run watch` / `gh run list`)
   and that gh-pages will update when it goes green.

## Mode: `--direct` (manual, immediate)
Publish the locally built `public/` straight to `gh-pages`, mirroring the CI output.
Use when CI is unavailable or an immediate push is needed.

1. Build for production base_url:
   ```bash
   BASE_URL="https://astronautiste.cz" bash scripts/build.sh
   ```
2. Ensure deploy artifacts in `public/`: `echo "astronautiste.cz" > public/CNAME` and
   `touch public/.nojekyll` (CI's peaceiris injects these; replicate them).
3. Publish via a throwaway worktree so the working branch is untouched:
   ```bash
   git worktree add -B gh-pages-deploy /tmp/astro-ghp origin/gh-pages
   rm -rf /tmp/astro-ghp/* /tmp/astro-ghp/.nojekyll
   cp -a public/. /tmp/astro-ghp/
   git -C /tmp/astro-ghp add -A
   CLAUDE_COMMIT_SKILL=1 git -C /tmp/astro-ghp commit -q -m "deploy: publish site $(git rev-parse --short HEAD)

   Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
   git -C /tmp/astro-ghp push origin gh-pages-deploy:gh-pages
   git worktree remove --force /tmp/astro-ghp
   ```
   (The commit needs the sentinel prefix — the block-git-commit hook applies in worktrees too.)
4. Never `--force` onto `gh-pages` except the controlled push above; never delete history
   beyond what `force_orphan` parity requires.

## After deploy
Report the deployed commit, target branch, and the live URL. Verify reachability only if
asked (it can take a minute for Pages to refresh).
