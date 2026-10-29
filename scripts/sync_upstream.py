#!/usr/bin/env python3
"""
Upstream Sync Script for MorpheApp Repositories.
Queries all 21 official MorpheApp repositories on GitHub,
compares them against the tracked upstream-manifest.json,
and generates updates in docs/upstream-changelog.md.
"""

import json
import os
import sys
import subprocess
from datetime import datetime

REPOSITORIES = [
    "morphe-patches",
    "morphe-desktop",
    "morphe-manager",
    "morphe-patches-library",
    "morphe-patcher",
    "morphe-documentation",
    "morphe-website",
    "morphe-patches-gradle-plugin",
    "morphe-patches-template",
    "changelog",
    "MicroG-RE",
    "ARSCLib",
    "smali",
    "PotHelper",
    "morphe-library",
    "jadb",
    "multidexlib2",
    "ejs",
    "nowinandroid",
    "Apktool",
    ".github",
]

MANIFEST_FILE = "upstream-manifest.json"
CHANGELOG_FILE = "docs/upstream-changelog.md"


def get_repo_data(repo_name):
    """Fetch latest release or latest commit via GitHub CLI / API."""
    token = os.environ.get("GITHUB_TOKEN")
    auth_header = [f"-H", f"Authorization: token {token}"] if token else []
    
    # Try fetching latest release
    try:
        cmd = ["gh", "api", f"repos/MorpheApp/{repo_name}/releases/latest"]
        res = subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
        rel = json.loads(res.decode("utf-8"))
        return {
            "type": "release",
            "tag": rel.get("tag_name", ""),
            "published_at": rel.get("published_at", ""),
            "name": rel.get("name", ""),
            "html_url": rel.get("html_url", "")
        }
    except Exception:
        # Fall back to latest commit on default branch
        try:
            cmd = ["gh", "api", f"repos/MorpheApp/{repo_name}/commits?per_page=1"]
            res = subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
            commits = json.loads(res.decode("utf-8"))
            if commits:
                latest = commits[0]
                return {
                    "type": "commit",
                    "sha": latest.get("sha", "")[:7],
                    "message": latest.get("commit", {}).get("message", "").split("\n")[0],
                    "date": latest.get("commit", {}).get("committer", {}).get("date", ""),
                    "html_url": latest.get("html_url", "")
                }
        except Exception as e:
            return {"type": "error", "message": str(e)}

    return {"type": "unknown"}


def main():
    old_manifest = {}
    if os.path.exists(MANIFEST_FILE):
        try:
            with open(MANIFEST_FILE, "r") as f:
                old_manifest = json.load(f)
        except Exception:
            old_manifest = {}

    new_manifest = {}
    changes = []

    print(f"Checking {len(REPOSITORIES)} MorpheApp upstream repositories...")
    for repo in REPOSITORIES:
        data = get_repo_data(repo)
        new_manifest[repo] = data
        old_data = old_manifest.get(repo)

        if not old_data:
            changes.append(f"- **{repo}**: Initial baseline tracked (`{data.get('tag') or data.get('sha')}`)")
        elif data.get("type") == "release" and data.get("tag") != old_data.get("tag"):
            changes.append(f"- **{repo}**: New Release [{data.get('tag')}]({data.get('html_url')}) (was `{old_data.get('tag')}`)")
        elif data.get("type") == "commit" and data.get("sha") != old_data.get("sha"):
            changes.append(f"- **{repo}**: New Commit [{data.get('sha')}]({data.get('html_url')}) - {data.get('message')}")

    # Save updated manifest
    with open(MANIFEST_FILE, "w") as f:
        json.dump(new_manifest, f, indent=2)

    has_updates = len(changes) > 0
    print(f"Upstream scan complete. Updates detected: {has_updates}")

    if has_updates:
        now_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        log_entry = f"\n### Upstream Sync Check — {now_str}\n" + "\n".join(changes) + "\n"
        
        if not os.path.exists(CHANGELOG_FILE):
            with open(CHANGELOG_FILE, "w") as f:
                f.write("# Upstream Morphe Ecosystem Changelog\n\nAutomated tracker monitoring all 21 MorpheApp upstream repositories.\n")
        
        with open(CHANGELOG_FILE, "a") as f:
            f.write(log_entry)

    # Set GITHUB_OUTPUT if running inside GitHub Actions
    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a") as f:
            f.write(f"has_updates={'true' if has_updates else 'false'}\n")


if __name__ == "__main__":
    main()
