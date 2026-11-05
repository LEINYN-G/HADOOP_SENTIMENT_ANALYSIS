#!/usr/bin/env python3
import sys
import csv
import re

def clean_text(text):
    """
    Applies regex cleaning rules to handle URLs, hashtags, mentions, 
    and extra spaces (Task 2 NLP Requirements).
    """
    # Convert to lowercase
    text = text.lower()
    # Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    # Remove User Mentions (e.g., @nisha)
    text = re.sub(r'@\w+', '', text)
    # Strip punctuation but keep word text character strings
    text = re.sub(r'[^\w\s]', '', text)
    # Clean up redundant spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Read from standard input stream line by line
for line in sys.stdin:
    line = line.strip()
    try:
        row = list(csv.reader([line]))
        if len(row) >= 2:
            # Clean raw social post text field
            raw_text = row[0]
            cleaned_text = clean_text(raw_text)
            
            # Capture the target label evaluation value
            sentiment = row[-1].strip()
            
            # Map structural tokens to keys
            if sentiment in ["-1", "0"]:
                print(f"negative\t1")
            elif sentiment in ["0", "neutral"]:
                print(f"neutral\t1")
            elif sentiment in ["1", "4", "positive"]:
                print(f"positive\t1")
    except Exception:
        continue
