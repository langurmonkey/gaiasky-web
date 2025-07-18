# This script reads the public data descriptor JSON file of Gaia Sky
# and generates a page with all the datasets for this website.

import json
import gzip
import requests
import io
import os.path
import math
from pathlib import Path
from millify import millify

# Generates a datasets.md file from the online dataset descriptor file.

# Function to convert bytes to a huma-readable format
def sizeof_fmt(num, suffix="B"):
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"

# Replace the "@mirror-url@" placeholder in the link
def update_link(link, base_url):
    return link.replace('@mirror-url@', base_url)

# Use millify library to make number pretty
def pretty_number(n):
    try:
        n = int(n)
        return millify(n, precision=2)
    except ValueError:
        return "N/A"

# Decode an integer into the version string
def decode_version(s: str) -> str:
    try:
        n = int(s)  # Try converting to an integer
        if n > 999999:
            patch = n % 100  # Last two digits
            revision = (n // 100) % 100  # Next two digits
            minor = (n // 10_000) % 100  # Next two digits
            major = n // 1_000_000  # Remaining digits
            return f"{major}.{minor}.{revision}-{patch}" if patch > 1 else f"{major}.{minor}.{revision}" 
        else:
            revision = n % 100  # Next two digits
            minor = (n // 100) % 100  # Next two digits
            major = n // 10_000  # Remaining digits
            return f"{major}.{minor}.{revision}" 
    except ValueError:
        return "N/A"

def combine(s: str, lst: list[str] | None) -> list[str]:
    if lst is None:
        lst = []
    if s and s not in lst:
        lst.append(s)
    return lst

# Types to icons and names
types = {
    "data-pack" : ("Data packs", "mdi-database-outline"),
    "texture-pack" : ("Texture packs", "material-symbols-texture"),
    "virtualtex-pack" : ("Virtual textures", "mdi-grid"),
    "catalog-lod" : ("Level-of-detail catalogs", "la-cubes"),
    "catalog-gaia" : ("Gaia star catalogs", "tabler-stars-filled"),
    "catalog-star" : ("Star catalogs", "game-icons-stars-stack"),
    "catalog-gal" : ("Galaxy catalogs", "streamline-galaxy-2-solid"),
    "catalog-cluster" : ("Cluster catalogs", "ph-graph"),
    "catalog-sso" : ("Asteroids and SSO", "game-icons-asteroid"),
    "catalog-other" : ("Other catalogs", "mdi-cube"),
    "system" : ("Exoplanets and extrasolar systems", "mdi-orbit"),
    "mesh" : ("3D iso-density meshes", "game-icons-mesh-network"),
    "spacecraft" : ("Missions, spacecraft and satellites", "solar-satellite-bold"),
    "volume" : ("Volumetric objects and effects", "material-symbols-cloud"),
}
def type_icon(type):
    return types.get(type, ("Generic", "fa-regular fa-cube"))[1]

def type_name(type):
    return types.get(type, ("Generic", "fa-regular fa-cube"))[0]

# Load JSON from a gzipped URL
json_gz_url = "https://gaia.ari.uni-heidelberg.de/gaiasky/repository/gaiasky-data/gaiasky-data_v017.min.json.gz"


response = requests.get(json_gz_url)
response.raise_for_status()  # Ensure the request was successful

# Decompress the gzipped content correctly
with gzip.GzipFile(fileobj=io.BytesIO(response.content), mode='rb') as decompressed:
    data = json.load(decompressed)  # Load JSON directly from decompressed data

# Process the 'files' list in the dictionary
files = data.get('files', [])

from collections import OrderedDict

# First: determine latest version per key
latest_datasets = {}
for dataset in files:
    key = dataset.get('key')
    version = dataset.get('version')
    if key is not None and version is not None:
        if key not in latest_datasets or int(version) > int(latest_datasets[key]['version']):
            latest_datasets[key] = dataset

# Now: group by type, preserving type order as seen in the original files
datasets_by_type = OrderedDict()
for dataset in files:
    key = dataset.get('key')
    version = dataset.get('version')
    dstype = dataset.get('type', 'N/A')

    # Only consider the latest version
    if key is None or version is None:
        continue
    if latest_datasets.get(key) != dataset:
        continue

    if dstype not in datasets_by_type:
        datasets_by_type[dstype] = []
    datasets_by_type[dstype].append(dataset)

# Generate Markdown
base_url = 'https://gaia.ari.uni-heidelberg.de/gaiasky/repository/'
markdown_content = []
webdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

for dstype, datasets in datasets_by_type.items():
    type_n = type_name(dstype)
    markdown_content.append(f"<h2 id='{dstype}'>{type_n}</h2>\n")

    for dataset in datasets:
        name = dataset.get('name', 'N/A')
        key = dataset.get('key', 'N/A')  # Use 'name' as key
        description = dataset.get('description', 'N/A')
        dstype = dataset.get('type', 'N/A')
        version = dataset.get('version', 'N/A')
        mingsversion = dataset.get('mingsversion', 'N/A')
        minversion_str = decode_version(mingsversion)
        credits = dataset.get('credits', None)
        creator = dataset.get('creator', 'N/A')
        size_bytes = dataset.get('size', 0)
        nobjects = dataset.get('nobjects', 'N/A')
        nobjects_pretty = pretty_number(nobjects)
        link = update_link(dataset.get('link', ''), base_url)
        links = [update_link(s, base_url) for s in dataset.get('links', [])]
        links = combine(link, links)
        file = os.path.dirname(update_link(dataset.get('file', ''), base_url))

        dataicon = type_icon(dstype)

        # Format byte size
        size_pretty = sizeof_fmt(int(size_bytes))
        # Image
        imgkey = Path(os.path.join(webdir, 'static/img/datasets/', f"{key}.jpg"))
        imgtype = Path(os.path.join(webdir, 'static/img/datasets/', f"{dstype}.jpg"))
        if imgkey.is_file():
            img = f"{key}.jpg"
        elif imgtype.is_file():
            img = f"{dstype}.jpg"
        else:
            img = None

        markdown_content.append(f"<a href='#{key}'></a>")
        markdown_content.append(f"<details id=\"{key}\">\n")
        markdown_content.append(f"<summary>\n")
        markdown_content.append(f"<h3>{name} <span style='font-size: 0.4em;'><a href='{file}' title='{name} files'>🔗</a></span><br/><i class=\"gs-{dataicon}\" title=\"Type: {dstype}\"></i> <code title=\"Key: {key}\">{key}</code></h3>\n")
        if img:
            imgname = os.path.splitext(img)[0]
            markdown_content.append(f"<img src=\"/img/datasets/{img}\" title=\"{imgname}\"></img>\n")
        markdown_content.append(f"</summary>\n")
        markdown_content.append(f"<article>\n")
        markdown_content.append(f"<div class='article-content'>\n")
        markdown_content.append(f"<div class='description'>{description}</div>\n\n")
        markdown_content.append(f"- **Type:** `{dstype}`\n")
        markdown_content.append(f"- **Dataset version:** v{version}\n")
        markdown_content.append(f"- **Minimum Gaia Sky version:** {minversion_str}\n")
        markdown_content.append(f"- **Size:** {size_pretty} <span class='unimportant'>({size_bytes})</span>\n")
        markdown_content.append(f"- **Number of objects:** {nobjects_pretty} <span class='unimportant'>({nobjects})</span>\n")
        if creator:
            markdown_content.append(f"- **Creator:** {creator}\n")
        if credits:
            markdown_content.append(f"- **Credits:**\n")
            for credit in credits:
                markdown_content.append(f"   - {credit}\n")
        
        markdown_content.append(f"- **Sources/links:**\n")
        for link in links:
            markdown_content.append(f"   - [{link}]({link})\n")
        markdown_content.append(f"- **Files:**\n")
        markdown_content.append(f"     - [{file}]({file})\n")
        markdown_content.append(f"</div>\n")
        markdown_content.append(f"</article>\n")
        markdown_content.append(f"</details>\n")
        markdown_content.append("\n")

# Write Markdown to a file
with open('datasets.md', 'w') as f:
    f.write("""
+++
title = "Datasets and catalogs"
description = "Explore the selection of scientific datasets offered with Gaia Sky"
type = "page"
css = ["css/datasets.css"]
+++

This page lists the last version for each dataset in Gaia Sky. You can download each dataset directly from within Gaia Sky using the dataset manager (**recommended!**), or by following the 'Dataset files' link in each dataset.
 In order to install any of the packages manually, just download it and extract the contents it in your data folder (defaults to `$HOME/.local/share/gaiasky/data/` in Linux, and `$HOME/.gaiasky/data` in Windows and macOS).

Click on the dataset title to reveal more information. 
<br/><br/>
""")
    f.writelines(markdown_content)

print("Markdown file 'datasets.md' has been generated.")
