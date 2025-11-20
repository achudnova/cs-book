import os
import json
import re

# Configuration
CONTENT_DIR = 'content'
OUTPUT_FILE = 'index.json'

data = {}

print(f"Scanning '{CONTENT_DIR}' for markdown files...")

# Get all subfolders
try:
    topics = [d for d in os.listdir(CONTENT_DIR) if os.path.isdir(os.path.join(CONTENT_DIR, d))]
except FileNotFoundError:
    print(f"Error: Folder '{CONTENT_DIR}' not found. Please create it.")
    topics = []

for topic in topics:
    topic_path = os.path.join(CONTENT_DIR, topic)
    files = []
    
    # Find all .md files in this topic
    for filename in os.listdir(topic_path):
        if filename.endswith(".md"):
            full_path = os.path.join(topic_path, filename)
            
            display_title = filename.replace('.md', '').replace('_', ' ').title()
            
            # Try to read the first line of the file
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    first_line = f.readline().strip()
                    # If line starts with #, strip it and use as title
                    if first_line.startswith('#'):
                        display_title = first_line.lstrip('#').strip()
            except Exception as e:
                print(f"Warning: Could not read {filename}")

            files.append({
                "title": display_title,
                "filename": filename
            })
    
    if files:
        # Sort files alphabetically
        files.sort(key=lambda x: x['title'])
        data[topic] = files
        print(f"  Found {len(files)} files in '{topic}'")

# Save to index.json
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"✅ Done! Created {OUTPUT_FILE}")