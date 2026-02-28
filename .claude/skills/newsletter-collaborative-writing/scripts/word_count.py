#!/usr/bin/env python3
"""
Word Count Analysis for Newsletter
Counts words in different sections for reading time estimation
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

    # Split by category markers (any H2 header with emoji)
    categories = re.split(r'(?=## (?:🤖|🕸️|💻|🏢|🧠))', content)

    # Count words in analysis sections only ("Cosa succede questa settimana?")
    analysis_words = 0
    main_content_words = 0

    for category in categories:
        # Find analysis section
        analysis_match = re.search(r'### Cosa succede questa settimana\?(.*?)(?=###|$)', category, re.DOTALL)
        if analysis_match:
            analysis_text = analysis_match.group(1)
            analysis_words += count_words(analysis_text)

        # Find takeaways and action items
        takeaway_match = re.search(r'### I Takeaways per gli AI Engineers(.*?)(?=### Cosa succede|### I link|$)', category, re.DOTALL)
        if takeaway_match:
            main_content_words += count_words(takeaway_match.group(1))

    # Main content = analysis + takeaways + action items (excluding link sections)
    main_content_words = analysis_words + main_content_words

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
