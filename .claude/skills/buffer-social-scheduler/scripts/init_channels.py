#!/usr/bin/env python3
"""Fetch Buffer channels and save aliases in .buffer/channels.json.

Run once per project. Aliases are used in campaign markdown files.

Usage:
    python3 init_channels.py [--non-interactive]

In --non-interactive mode, aliases are auto-generated as "<service>_<name>".
"""

import json
import os
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from buffer_client import BufferClient, BufferError


CONFIG_DIR = Path(".buffer")
CHANNELS_FILE = CONFIG_DIR / "channels.json"


def slug(text):
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def auto_alias(channel, existing):
    base = f"{slug(channel['service'])}_{slug(channel['name'])}"
    alias = base
    i = 2
    while alias in existing:
        alias = f"{base}_{i}"
        i += 1
    return alias


def main():
    non_interactive = "--non-interactive" in sys.argv

    try:
        client = BufferClient()
    except BufferError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    print("Fetching Buffer channels...")
    try:
        channels = client.list_channels()
    except BufferError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    if not channels:
        print("No channels found. Connect accounts in Buffer first.")
        sys.exit(1)

    existing = {}
    if CHANNELS_FILE.exists():
        try:
            existing = json.loads(CHANNELS_FILE.read_text())
            print(f"Existing config at {CHANNELS_FILE} loaded. Aliases will be preserved where possible.")
        except json.JSONDecodeError:
            existing = {}

    alias_by_id = {v["id"]: k for k, v in existing.items()}

    result = {}
    print(f"\nFound {len(channels)} channel(s):\n")
    for ch in channels:
        suggested = alias_by_id.get(ch["id"]) or auto_alias(ch, result)
        label = f"{ch['service']}/{ch['name']} (id: {ch['id']})"
        if non_interactive:
            alias = suggested
            print(f"  {label} -> {alias}")
        else:
            while True:
                raw = input(f"  {label}\n    Alias [{suggested}]: ").strip()
                alias = raw or suggested
                if not re.match(r"^[a-z0-9_]+$", alias):
                    print("    Alias must match [a-z0-9_]+")
                    continue
                if alias in result:
                    print(f"    Alias '{alias}' already used. Pick another.")
                    continue
                break
        result[alias] = {
            "id": ch["id"],
            "service": ch["service"],
            "name": ch["name"],
            "organization_id": ch["organization_id"],
        }

    CONFIG_DIR.mkdir(exist_ok=True)
    CHANNELS_FILE.write_text(json.dumps(result, indent=2) + "\n")
    print(f"\nSaved {len(result)} alias(es) to {CHANNELS_FILE}")


if __name__ == "__main__":
    main()
