import os
import re
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from pathlib import Path

# Base URL for Gaia Sky releases
BASE_URL = "https://gaia.ari.uni-heidelberg.de/gaiasky/releases/"
OUTPUT_DIR = "content/downloads/releases"  # Adjust to Hugo content directory

# Regex pattern to match version numbers: major.minor.rev[-patch].build
VERSION_PATTERN = re.compile(r"\d+\.\d+\.\d+\.[0-9a-f]{7,}")

def parse_date(date_str):
    """Convert release date string to Hugo-compatible format (YYYY-MM-DDTHH:MM:SS)."""
    try:
        date_str = " ".join(date_str.split())  # Normalize multiple spaces
        return datetime.strptime(date_str, "%d-%b-%Y %H:%M").strftime("%Y-%m-%dT%H:%M:%S")
    except ValueError:
        return "Unknown"

def fetch_releases():
    """Fetch the list of releases from the Gaia Sky releases page."""
    response = requests.get(BASE_URL)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    releases = []
    
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and VERSION_PATTERN.fullmatch(href.strip('/')):
            version = href.strip('/')
            date_text = link.next_sibling.string.strip() if link.next_sibling and link.next_sibling.string else ""
            date_match = re.match(r"(\d{2}-[A-Za-z]{3}-\d{4}\s+\d{1,2}:\d{2})", date_text)
            release_date = parse_date(date_match.group(1)) if date_match else "Unknown"
            releases.append((version, release_date))
    
    return sorted(releases, key=lambda x: x[1], reverse=True)  # Sort by date descending

def generate_markdown(version, release_date):
    """Generate markdown content for a given release version."""
    release_url = f"{BASE_URL}{version}/"
    response = requests.get(release_url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    
    download_links = [f"[{link.text}]({release_url}{link.get('href')})" for link in links if link.get('href') and link.get('href') != '../']
    
    front_matter = f"""+++
title = "Gaia Sky {version}"
date = "{release_date}"
type = "page"
+++
"""
    
    content = f"{front_matter}\n## Download Links\n\n" + '\n'.join(f"- {dl}" for dl in download_links)
    
    return content

def save_markdown(version, content):
    """Save the markdown file for a release."""
    output_path = Path(OUTPUT_DIR) / f"v{version}.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

def generate_index(releases):
    """Generate the index page listing all releases."""
    front_matter = f"""+++
title = "Gaia Sky Releases"
type = "releases"
+++
"""
    
    content = f"{front_matter}\n## Available Releases\n\n" + '\n'.join(f"- [{version}](./{version}/)" for version in releases)
    
    output_path = Path(OUTPUT_DIR) / "_index.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    releases = fetch_releases()
    
    for release, release_date in releases:
        markdown_content = generate_markdown(release, release_date)
        save_markdown(release, markdown_content)
    
    generate_index(releases)
    print("Markdown files generated successfully!")

if __name__ == "__main__":
    main()
