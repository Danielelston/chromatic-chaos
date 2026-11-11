#!/usr/bin/env python3
"""Block players from editing notes with `owner: dm` in frontmatter."""
import json, os, re, sys

data = json.load(sys.stdin)
ti = data.get("tool_input", {})
path = ti.get("file_path", "")
root = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())

def role():
    try:
        return open(os.path.join(root, ".claude", "role")).read().strip().lower()
    except OSError:
        return "player"

def owner_of(text):
    m = re.match(r"\A---\s*\n(.*?)\n---\s*(\n|$)", text, re.S)
    if not m:
        return None
    o = re.search(r"^owner:\s*['\"]?(\w+)", m.group(1), re.M)
    return o.group(1).lower() if o else None

if not path.endswith(".md") or role() == "dm":
    sys.exit(0)

existing = None
try:
    existing = owner_of(open(path, encoding="utf-8").read())
except OSError:
    pass
new = owner_of(ti.get("content", "")) if "content" in ti else None

if existing == "dm" or new == "dm":
    print(
        f"BLOCKED: {os.path.basename(path)} is DM-owned (owner: dm). Players must not edit it. "
        "Use /propose to create or update its companion note instead.",
        file=sys.stderr,
    )
    sys.exit(2)
sys.exit(0)
