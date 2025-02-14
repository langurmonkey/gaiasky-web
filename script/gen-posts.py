import re
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# This script generates a Hugo post for each Gaia Sky release
# in the releases directory listing of the repository.

def fetch_page(url):
    """Fetch the HTML content of a page."""
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_listing_page(url):
    """Extract valid version links and their dates from the listing page."""
    html = fetch_page(url)
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    
    pre_tag = soup.find("pre")
    if pre_tag:
        lines = pre_tag.get_text().split("\n")
        for line in lines:
            match = re.search(r'(\S+/)\s+(\d{2}-\w{3}-\d{4}\s+\d{1,2}:\d{2})', line)
            if match:
                link = match.group(1)
                version = '.'.join(link.split('.')[:3])
                date_string = match.group(2)
                date_parse = datetime.strptime(date_string, "%d-%b-%Y %H:%M")
                date = date_parse.strftime("%Y-%m-%dT%H:%M:%S")
                links.append((url + '/' + link, version, date))
            else:
                print(f"Line skipped: {line}")
    
    return links

def process_version_link(version_url, version, date):
    """Download the releasenotes.md file and create a formatted markdown file."""
    html = fetch_page(version_url)
    soup = BeautifulSoup(html, 'html.parser')
    
    for link in soup.find_all('a', href=True):
        if link.text == 'releasenotes.md':
            release_url = version_url + link['href']
            response = requests.get(release_url)
            response.raise_for_status()
            
            content = response.text.split('\n', 1)[-1]  # Remove the first header
            metadata = f"""+++
title = "Gaia Sky {version}"
date = "{date}"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 Gaia Sky {version} available now!

<!--more-->
"""
            
            filename = f"gaiasky_{version}.md"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(metadata + '\n' + content)
                f.write(f"\nYou can get this release in [our repository]({version_url}).")

            
            print(f"Generated: {filename}")
            return

def main(base_url):
    version_links = parse_listing_page(base_url)
    for version_url, version, date in version_links:
        process_version_link(version_url, version, date)

if __name__ == "__main__":
    base_url = "https://gaia.ari.uni-heidelberg.de/gaiasky/releases/"
    main(base_url)
