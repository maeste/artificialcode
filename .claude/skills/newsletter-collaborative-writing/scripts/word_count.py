#!/usr/bin/env python3
"""
Word Count Analysis for Newsletter
Counts words in different sections for reading time estimation.
Supports both Italian and English newsletter formats, with or without emoji in headers.
"""

import sys
import re


def count_words(text):
    """Count words in text, ignoring markdown links."""
    # Remove markdown links but keep the text
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    return len(text.split())


def analyze_newsletter(file_path):
    """Analyze newsletter and return word counts for different sections."""

    with open(file_path, 'r') as f:
        content = f.read()

    # Total word count
    total_words = len(content.split())

    # Find all analysis sections (IT: "Cosa succede questa settimana?", EN: "What's happening this week?")
    analysis_pattern = r'###\s+(?:Cosa succede questa settimana\?|What\'s happening this week\?)(.*?)(?=###|## |$)'
    analysis_matches = re.findall(analysis_pattern, content, re.DOTALL)
    analysis_words = sum(count_words(match) for match in analysis_matches)

    # Find all takeaway/action item sections (IT and EN)
    takeaway_pattern = r'###\s+(?:I Takeaways per gli AI Engineers|Takeaways for AI Engineers)(.*?)(?=###|## |$)'
    takeaway_matches = re.findall(takeaway_pattern, content, re.DOTALL)
    takeaway_words = sum(count_words(match) for match in takeaway_matches)

    # Main content = analysis + takeaways + action items (excluding link sections)
    main_content_words = analysis_words + takeaway_words

    return {
        'analysis': analysis_words,
        'main_content': main_content_words,
        'total': total_words
    }


def calculate_reading_time(words, speed=200):
    """Calculate reading time in minutes."""
    return round(words / speed, 1)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 word_count.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    counts = analyze_newsletter(file_path)

    # Print results for parsing
    print(f"ANALYSIS_WORDS={counts['analysis']}")
    print(f"MAIN_CONTENT_WORDS={counts['main_content']}")
    print(f"TOTAL_WORDS={counts['total']}")

    # Calculate reading times
    analysis_normal = calculate_reading_time(counts['analysis'], 200)
    main_normal = calculate_reading_time(counts['main_content'], 200)
    total_normal = calculate_reading_time(counts['total'], 200)

    print(f"ANALYSIS_TIME_NORMAL={analysis_normal}")
    print(f"MAIN_CONTENT_TIME_NORMAL={main_normal}")
    print(f"TOTAL_TIME_NORMAL={total_normal}")


if __name__ == '__main__':
    main()
