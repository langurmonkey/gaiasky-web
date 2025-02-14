#!/bin/bash

for file in content/news/2025/*.md; do
    # Get the first commit date from Git
    first_commit_date=$(git log --reverse --format="%ad" --date=iso -- "$file" | head -n 1)

    if [[ -n "$first_commit_date" ]]; then
        # Convert date format to match TOML style (YYYY-MM-DDTHH:MM:SSZ)
        first_commit_date=$(date -d "$first_commit_date" --utc +'%Y-%m-%dT%H:%M:%SZ')

        # Update the existing 'date' field in place
        sed -i -E "s/^date = \".*\"/date = \"$first_commit_date\"/" "$file"
    fi
done
