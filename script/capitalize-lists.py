#!/usr/bin/env python3

import os
import sys
import re

def process_file(file_path):
    with open(file_path, 'r') as f:
        content = f.readlines()

    updated_lines = []
    for line in content:
        match = re.match(r"^(\s*-\s+)(.*)", line)
        if match:
            prefix, item = match.groups()
            # Capitalize the first letter and preserve the rest
            item = item[0].upper() + item[1:] if item else item
            # Remove trailing whitespace and ensure period at end
            item = item.rstrip()
            if not item.endswith("."):
                item += "."
            updated_lines.append(f"{prefix}{item}\n")
        else:
            updated_lines.append(line)

    with open(file_path, 'w') as f:
        f.writelines(updated_lines)

    print(f"Processed: {file_path}")


def main(content_dir):
    for root, _, files in os.walk(content_dir):
        for file in files:
            if file.endswith(".md"):
                process_file(os.path.join(root, file))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <content_dir>")
        sys.exit(1)
    main(sys.argv[1])
