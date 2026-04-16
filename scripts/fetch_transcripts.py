#!/usr/bin/env python3
"""
fetch_transcripts.py
====================
Fetches YouTube transcripts for all 6 video creators in the AI-Powered SEO
Content Production research project.

Run this locally — YouTube blocks transcript requests from cloud/CI environments.

Requirements:
    pip install youtube-transcript-api yt-dlp

Usage:
    # Fetch all creators
    python scripts/fetch_transcripts.py

    # Fetch a single creator
    python scripts/fetch_transcripts.py --author julian-goldie

    # Fetch with verbose output
    python scripts/fetch_transcripts.py --verbose
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

# ── Configuration ─────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).parent.parent
TRANSCRIPTS_DIR = REPO_ROOT / "research" / "youtube-transcripts"

# Pre-seeded video IDs discovered during initial research (April 2026).
# The script will also auto-discover the 5 most recent videos per channel
# and merge them with this list.
CREATORS = {
    "koray-gubur": {
        "channel": "https://www.youtube.com/@TopicalAuthority",
        "display_name": "Koray Tuğberk GÜBÜR",
        "known_video_ids": [
            ("IRa83T0zlNg", "Topical Authority Deep Dive"),
        ],
    },
    "gael-breton": {
        "channel": "https://www.youtube.com/@gbreton",
        "display_name": "Gael Breton",
        "known_video_ids": [],
    },
    "matt-diggity": {
        "channel": "https://www.youtube.com/@MattDiggity",
        "display_name": "Matt Diggity",
        "known_video_ids": [],
    },
    "nathan-gotch": {
        "channel": "https://www.youtube.com/@NathanGotch",
        "display_name": "Nathan Gotch",
        "known_video_ids": [],
    },
    "julian-goldie": {
        "channel": "https://www.youtube.com/@JulianGoldieSEO",
        "display_name": "Julian Goldie",
        "known_video_ids": [
            ("1kCge93_u8s", "AI SEO SOP Walkthrough"),
            ("jMEhA3vhuuQ", "SEO Automation Pipeline"),
            ("iqWYmm4sQfw", "SEO Tool Integration"),
            ("ak36QQQZ4QE", "AI SEO Full Workflow"),
            ("ymuKyHxOAPA", "AI SEO Strategy Breakdown"),
            ("QHDF4G0NB-0", "Automated Publishing Pipeline"),
        ],
    },
    "income-school": {
        "channel": "https://www.youtube.com/@IncomeSchool",
        "display_name": "Income School (Ricky Kesler)",
        "known_video_ids": [],
    },
}

VIDEOS_PER_CHANNEL = 5  # How many recent videos to auto-discover per channel


# ── Helpers ───────────────────────────────────────────────────────────────────

def log(msg: str, verbose: bool = False, force: bool = False):
    if force or verbose:
        print(msg)


def discover_recent_videos(channel_url: str, n: int = 5) -> list[tuple[str, str, str]]:
    """
    Use yt-dlp to get the N most recent video IDs + titles + upload dates.
    Returns list of (video_id, title, upload_date).
    """
    result = subprocess.run(
        [
            "yt-dlp",
            "--flat-playlist",
            "--playlist-end", str(n),
            "--print", "%(id)s|||%(title)s|||%(upload_date)s",
            f"{channel_url}/videos",
        ],
        capture_output=True,
        text=True,
        timeout=90,
    )
    videos = []
    for line in result.stdout.strip().split("\n"):
        if "|||" in line:
            parts = line.split("|||")
            if len(parts) >= 2:
                vid_id = parts[0].strip()
                title = parts[1].strip()
                date = parts[2].strip() if len(parts) > 2 else "unknown"
                if vid_id:
                    videos.append((vid_id, title, date))
    return videos


def fetch_transcript(video_id: str) -> tuple[str, int] | None:
    """
    Fetch transcript for a YouTube video.
    Returns (full_text, word_count) or None on failure.
    """
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        yta = YouTubeTranscriptApi()
        fetched = yta.fetch(video_id)
        segments = list(fetched)
        full_text = " ".join(
            s.text if hasattr(s, "text") else s["text"] for s in segments
        )
        full_text = re.sub(r"\s+", " ", full_text).strip()
        return full_text, len(full_text.split())
    except ImportError:
        print("ERROR: youtube-transcript-api not installed. Run: pip install youtube-transcript-api")
        sys.exit(1)
    except Exception as e:
        return None, str(e)


def save_transcript(
    author_slug: str,
    video_id: str,
    title: str,
    upload_date: str,
    full_text: str,
    word_count: int,
):
    out_dir = TRANSCRIPTS_DIR / author_slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{video_id}.md"

    # Format upload_date nicely
    try:
        d = datetime.strptime(upload_date, "%Y%m%d")
        date_str = d.strftime("%B %d, %Y")
    except Exception:
        date_str = upload_date

    content = f"""# {title}

**Video ID:** `{video_id}`
**URL:** https://www.youtube.com/watch?v={video_id}
**Upload Date:** {date_str}
**Word Count:** {word_count:,}
**Fetched:** {datetime.now().strftime("%Y-%m-%d")}

---

## Transcript

{full_text}
"""
    out_path.write_text(content, encoding="utf-8")
    return out_path


# ── Main ──────────────────────────────────────────────────────────────────────

def process_creator(slug: str, config: dict, verbose: bool = False):
    display = config["display_name"]
    channel = config["channel"]
    out_dir = TRANSCRIPTS_DIR / slug

    print(f"\n{'='*60}")
    print(f"  {display}")
    print(f"{'='*60}")

    # 1. Auto-discover recent videos
    print(f"  Discovering {VIDEOS_PER_CHANNEL} recent videos from {channel} ...")
    try:
        discovered = discover_recent_videos(channel, VIDEOS_PER_CHANNEL)
        log(f"  Found {len(discovered)} videos via yt-dlp", verbose, force=True)
    except Exception as e:
        print(f"  WARNING: yt-dlp discovery failed: {e}")
        discovered = []

    # 2. Merge with known video IDs
    all_videos: dict[str, tuple[str, str]] = {}  # id → (title, date)
    for vid_id, title in config["known_video_ids"]:
        all_videos[vid_id] = (title, "unknown")
    for vid_id, title, date in discovered:
        if vid_id not in all_videos:
            all_videos[vid_id] = (title, date)

    print(f"  Total unique videos to process: {len(all_videos)}")

    # 3. Skip already-fetched transcripts
    results = {"success": 0, "skipped": 0, "failed": 0}
    for vid_id, (title, date) in all_videos.items():
        out_path = out_dir / f"{vid_id}.md"
        if out_path.exists():
            print(f"  ⏭  [{vid_id}] Already fetched — skipping")
            results["skipped"] += 1
            continue

        print(f"  ⬇  [{vid_id}] {title[:60]} ...")
        result = fetch_transcript(vid_id)

        if result[0] is None:
            print(f"  ✗  [{vid_id}] FAILED — {result[1]}")
            results["failed"] += 1
            # Write a stub so we know it was attempted
            stub = f"""# {title}

**Video ID:** `{vid_id}`
**URL:** https://www.youtube.com/watch?v={vid_id}
**Status:** Transcript fetch failed
**Error:** {result[1]}
**Attempted:** {datetime.now().strftime("%Y-%m-%d")}

> Re-run `python scripts/fetch_transcripts.py --author {slug}` to retry.
"""
            out_path = out_dir / f"{vid_id}_FAILED.md"
            out_path.write_text(stub, encoding="utf-8")
        else:
            full_text, word_count = result
            saved = save_transcript(slug, vid_id, title, date, full_text, word_count)
            print(f"  ✓  [{vid_id}] {word_count:,} words → {saved.name}")
            results["success"] += 1

        time.sleep(1)  # be polite to YouTube

    print(f"\n  Summary: {results['success']} fetched, {results['skipped']} skipped, {results['failed']} failed")
    return results


def main():
    parser = argparse.ArgumentParser(description="Fetch YouTube transcripts for SEO research project")
    parser.add_argument(
        "--author",
        choices=list(CREATORS.keys()) + ["all"],
        default="all",
        help="Which creator to fetch (default: all)",
    )
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    args = parser.parse_args()

    # Check dependencies
    try:
        import youtube_transcript_api  # noqa
    except ImportError:
        print("ERROR: Missing dependency. Run:\n  pip install youtube-transcript-api yt-dlp")
        sys.exit(1)

    targets = CREATORS if args.author == "all" else {args.author: CREATORS[args.author]}

    total = {"success": 0, "skipped": 0, "failed": 0}
    for slug, config in targets.items():
        r = process_creator(slug, config, verbose=args.verbose)
        for k in total:
            total[k] += r[k]

    print(f"\n{'='*60}")
    print(f"  ALL DONE")
    print(f"  Fetched: {total['success']} | Skipped: {total['skipped']} | Failed: {total['failed']}")
    print(f"  Transcripts saved to: {TRANSCRIPTS_DIR}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
