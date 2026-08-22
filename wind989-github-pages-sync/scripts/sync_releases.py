"""Fetch public GitHub Releases for the projects listed in _data/projects.json."""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
PROJECTS_FILE = ROOT / "_data" / "projects.json"
RELEASES_FILE = ROOT / "_data" / "releases.json"


def github_json(url: str):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "wind989-blog-release-sync",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    request = Request(url, headers=headers)
    with urlopen(request, timeout=30) as response:
        return json.load(response)


def clean_summary(markdown: str, limit: int = 220) -> str:
    text = re.sub(r"[`*_>#\[\]()]", "", markdown or "")
    text = " ".join(text.split())
    if len(text) > limit:
        return text[: limit - 1].rstrip() + "…"
    return text


def main() -> None:
    projects = json.loads(PROJECTS_FILE.read_text(encoding="utf-8"))
    items = []

    for project in projects:
        repo = project["repo"]
        url = f"https://api.github.com/repos/{repo}/releases?per_page=5"
        try:
            releases = github_json(url)
        except (HTTPError, URLError) as error:
            print(f"Unable to read {repo}: {error}")
            continue

        for release in releases:
            if release.get("draft") or release.get("prerelease"):
                continue

            published_at = release.get("published_at") or release.get("created_at")
            items.append(
                {
                    "repo": repo,
                    "project": project["name"],
                    "tag": release.get("tag_name", ""),
                    "name": release.get("name") or release.get("tag_name", "未命名版本"),
                    "summary": clean_summary(release.get("body", "")),
                    "published_at": published_at,
                    "url": release.get("html_url", project["url"]),
                }
            )

    items.sort(key=lambda item: item.get("published_at") or "", reverse=True)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "items": items,
    }
    RELEASES_FILE.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Synced {len(items)} public releases from {len(projects)} projects.")


if __name__ == "__main__":
    main()
