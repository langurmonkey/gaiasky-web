# This script crawls the repository listing and generates a page for
# each old Gaia Sky release in $GSW/content/downloads/releases. It also
# generates a listing with all releases.

import os
import re
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from pathlib import Path
from git import Repo

script_path = os.path.dirname(os.path.realpath(__file__))
# Base URL for Gaia Sky releases
BASE_URL = "https://gaia.ari.uni-heidelberg.de/gaiasky/releases/"
OUTPUT_DIR = f"{script_path}/../content/downloads/releases"  # Adjust to Hugo content directory

# Regex pattern to match version numbers: major.minor.rev[-patch].build
VERSION_PATTERN = re.compile(r"\d+\.\d+\.\d+(?:-\d+)?\.[0-9a-f]{7,}")

def parse_date(date_str):
    """Convert release date string to Hugo-compatible format (YYYY-MM-DDTHH:MM:SS)."""
    try:
        date_str = " ".join(date_str.split())  # Normalize multiple spaces
        return datetime.strptime(date_str, "%d-%b-%Y %H:%M").strftime("%Y-%m-%dT%H:%M:%S")
    except ValueError:
        return "Unknown"

def split_version(version):
    """Split the version into (version, build) components."""
    match = re.match(r"(\d+\.\d+\.\d+(?:-\d+)?)(\.[0-9a-f]{7,})$", version)
    if match:
        return match.group(1), match.group(2)[1:]  # Remove the leading dot from the build
    return version, None  # Return None if no build hash is found

def get_tag_info(repo_path, tag_name):
    repo = Repo(repo_path)
    tag = repo.tags[tag_name]
    commit = tag.commit
    return {
        "date": commit.committed_datetime,
        "message": commit.message.strip()
    }


def fetch_releases():
    """Fetch the list of releases from the Gaia Sky releases page."""
    response = requests.get(BASE_URL)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    releases = []
    
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and VERSION_PATTERN.fullmatch(href.strip('/')):
            version_build = href.strip('/')
            version, build = split_version(version_build)

            date_text = link.next_sibling.string.strip() if link.next_sibling and link.next_sibling.string else ""
            date_match = re.match(r"(\d{2}-[A-Za-z]{3}-\d{4}\s+\d{1,2}:\d{2})", date_text)
            release_date = parse_date(date_match.group(1)) if date_match else "Unknown"
            
            # Get Git tag info
            try:
                gsdir = os.environ['GS']
                if gsdir:
                    tag = get_tag_info(gsdir, version)
                    date = tag['date']
                    date_fmt = date.strftime("%Y-%m-%dT%H:%M:%S") 
                    release_date = date_fmt
            except Exception as e:
                # Ignore
                print(f"Exception getting tag {version}: {e}")

            
            releases.append((version, build, release_date))
    
    return sorted(releases, key=lambda x: x[2], reverse=True)  # Sort by date descending


def generate_markdown(version, build, release_date):
    """Generate markdown content for a given release version."""
    release = f"{version}.{build}"
    release_url = f"{BASE_URL}{release}/"
    response = requests.get(release_url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    
    download_links = [
        (link.text, release_url, link.get('href'))
        for link in links
        if link.get('href') and link.get('href') not in ('../', 'updates.xml') and not link.get('href').startswith('releasenotes.')
    ]

    links = []
    for dl_tuple in download_links:
        if not dl_tuple[0].endswith(".sig"):
            found = False
            for other in download_links:
                if not found and not dl_tuple[0].endswith(".sig") and dl_tuple[0] != other[0] and dl_tuple[0] + ".sig" == other[0]:
                    links.append((dl_tuple[0], dl_tuple[1], dl_tuple[0], other))
                    found = True
            if not found:
                links.append((dl_tuple[0], dl_tuple[1], dl_tuple[0], None))
            
    short_date = datetime.strptime(release_date, "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d")

    front_matter = f"""+++
title = "Release {version}.{build}"
date = "{release_date}"
type = "page"
hidden = true
showtitle = false
css = ["css/downloads.css", "css/releases.css"]
+++
"""
    
    content = f"{front_matter}\n<div class=\"download-container\">\n"
    content += f"<div id=\"download-title\">\n"
    content += "<i class=\"gs-mdi-tag\"></i>\n"
    content += f"Gaia Sky <span class=\"downloads-version\">{version}</span> \n"
    content += f"<time class=\"downloads-releasedate\" datetime=\"{release_date}\" title=\"Published: {release_date}\"><i class=\"gs-mdi-calendar\"></i> {short_date}</time>\n"
    content += f"<div class=\"downloads-build\">Build {build}</div></div>\n"
    content += f"<div class=\"download-section\">\n"

    pack = 0
    for dl in links:
        file = f"{dl[0]}"
        link = f"{dl[1]}{dl[2]}"

        if file.endswith(".exe"):
            if "x64" in file:
                name = "Windows x86-64"
            else:
                name = "Windows 32-bit"
            ext = ".exe"
            cl = "fa6-brands-windows"
        elif file.endswith(".dmg"):
            name = "macOS"
            ext = ".dmg"
            cl = "fa6-brands-apple"
        elif file.endswith(".tar.gz"):
            name = "TGZ package"
            ext = ".tar.gz"
            cl = "mdi-zip-box"
        elif file.endswith(".appimage"):
            name = "AppImage"
            ext = ".appimage"
            cl = "material-symbols-box"
        elif file.endswith(".deb"):
            name = "DEB package"
            ext = ".deb"
            cl = "mdi-debian"
        elif file.endswith(".rpm"):
            name = "RPM package"
            ext = ".rpm"
            cl = "mdi-fedora"
        elif file.endswith(".sh"):
            name = "UNIX Installer"
            ext = ".sh"
            cl = "token-unix"
        else:
            continue
        
        content += f"<a href=\"{link}\" class=\"download-button\"><i class=\"gs-{cl} icon-button\"></i> {name} <code>{ext}</code><span class=\"download-sub\">{file}</span></a>\n"

        if dl[3]:
            link = f"{dl[3][1]}{dl[3][2]}"
            content += "<span class=\"signature\">\n"
            content += f"<a href=\"{link}\">signature</a>  by  <a href=\"https://keyserver.ubuntu.com/pks/lookup?search=0x448C2B189756743013D5F7C22FD2A59C1D734C1F&fingerprint=on&op=index\">tsagrista</a>\n"
            content += "</span>\n"
        else:
            content += "<span class=\"signature\">no signature</span>\n"

        
    content += "</div>\n</div>\n"

    
    # Fetch release notes if available
    release_notes_url = f"{release_url}releasenotes.md"
    release_notes_response = requests.get(release_notes_url)
    if release_notes_response.status_code == 200:
        lines = release_notes_response.text.splitlines()
        filtered_lines = []
        skip_header = True
        for line in lines:
            if skip_header and re.match(r"^# ", line.strip()):
                continue
            skip_header = False
            filtered_lines.append(line)
        content += f"\n<section class=\"release-notes\">\n\n# Release Notes\n\n" + '\n'.join(filtered_lines)
        content += "\n</section>\n\n"

    footer = """
<p class="center-text" style="padding: 30px;"><a href="/downloads/releases"><i class="gs-mdi-arrow-left-bold-circle"></i> Back to releases</a>
</p>
"""

    content += f"{footer}"
    
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
title = "Old Releases"
type = "releases"
layout = "releases"
hidden = true
css = ["css/releases.css"]
+++

## Old Releases

Below is a listing of all the **past releases** of Gaia Sky. We do not offer support for old releases, but they may still work. Use them at your own risk.

You can also browse **all Gaia Sky** tags in our [repository](https://codeberg.org/gaiasky/gaiasky/tags).

"""
    
    content = f"{front_matter}\n<section class=\"releases-list\">\n"

    for version, build, releasedate in releases:
        short_date = datetime.strptime(releasedate, "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d")
        content += "<div class=\"releaseentry\">\n"
        content += f"<a href=\"./v{version}\" class=\"versionlink\">\n"
        content += "<i class=\"gs-mdi-tag tag\"></i>\n"
        content += "<div class=\"release\">\n"
        content += f"Gaia Sky {version}\n</div>\n"
        content += f"<code class=\"build\">{build}</code>\n"
        content += "<div class=\"releasedate\">\n"
        content += "<i class=\"gs-mdi-calendar calendar\"></i>\n"
        content += f"<time datetime=\"{releasedate}\" title=\"Published: {releasedate}\">{short_date}</time></div>\n"
        content += "</a>\n"
        content += "</div>\n"

    content += "</section>\n"
    
    output_path = Path(OUTPUT_DIR) / "_index.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    

def main():
    releases = fetch_releases()
    
    idx = 0
    for version, build, release_date in releases:
        print(f"Processing {version}.{build}")
        
        markdown_content = generate_markdown(version, build, release_date)
        save_markdown(version, markdown_content)
        idx += 1
    
    generate_index(releases)
    print("Markdown files generated successfully!")

if __name__ == "__main__":
    main()
