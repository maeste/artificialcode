#!/usr/bin/env python3
"""
Word Count Analysis for Newsletter (Deep-Dive Format)
Counts words in different sections for reading time estimation.
Supports both Italian and English newsletter formats.

Document structure expected:
  [Title + Introduction + Agenda]
  ---
  [Deep-dive article]
  ---
  [Curated links with POV]
"""

import sys
import re


def count_words(text):
    """Count words in text, ignoring markdown link URLs but keeping link text."""
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    return len(text.split())


def analyze_newsletter(file_path):
    """Analyze deep-dive format newsletter and return word counts by section."""

    with open(file_path, 'r') as f:
        content = f.read()

    total_words = count_words(content)

    # Split by horizontal rules (--- on its own line, with optional whitespace)
    parts = re.split(r'\n\s*---\s*\n', content)

    deep_dive_words = 0
    links_words = 0

    if len(parts) >= 3:
        # Standard structure: [intro+agenda] --- [deep-dive] --- [links]
        deep_dive_words = count_words(parts[1])
        links_text = '\n---\n'.join(parts[2:])
        links_words = count_words(links_text)
    elif len(parts) == 2:
        # Fallback: try to detect links section by header
        links_headers = [
            r'##\s+I link che mi hanno colpito',
            r'##\s+Links that caught my',
        ]
        combined = parts[1]
        split_pos = None
        for header in links_headers:
            match = re.search(header, combined)
            if match:
                split_pos = match.start()
                break

        if split_pos is not None:
            deep_dive_words = count_words(combined[:split_pos])
            links_words = count_words(combined[split_pos:])
        else:
            deep_dive_words = count_words(combined)

    return {
        'deep_dive': deep_dive_words,
        'links': links_words,
        'deep_dive_plus_links': deep_dive_words + links_words,
        'total': total_words,
    }


def calculate_reading_time(words, speed=200):
    """Calculate reading time in minutes at given words-per-minute speed."""
    return max(1, round(words / speed))


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 word_count.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    counts = analyze_newsletter(file_path)

    print(f"DEEP_DIVE_WORDS={counts['deep_dive']}")
    print(f"LINKS_WORDS={counts['links']}")
    print(f"DEEP_DIVE_PLUS_LINKS_WORDS={counts['deep_dive_plus_links']}")
    print(f"TOTAL_WORDS={counts['total']}")

    deep_dive_time = calculate_reading_time(counts['deep_dive'])
    deep_dive_links_time = calculate_reading_time(counts['deep_dive_plus_links'])
    total_time = calculate_reading_time(counts['total'])

    print(f"DEEP_DIVE_TIME={deep_dive_time}")
    print(f"DEEP_DIVE_LINKS_TIME={deep_dive_links_time}")
    print(f"TOTAL_TIME={total_time}")


if __name__ == '__main__':
    main()
