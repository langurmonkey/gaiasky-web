# This script reads the public data descriptor JSON file of Gaia Sky
# and generates a page with all the datasets for this website.

import json
import gzip
import requests
import io
import os.path
from pathlib import Path
from millify import millify

# Generates a datasets.md file from the online dataset descriptor file.

# Function to convert bytes to a human-readable format
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

# Get attribute by trying multiple names, with a default fallback
def get_attr(dataset: dict, names: list[str], default=None):
    for name in names:
        if name in dataset:
            return dataset[name]
    return default

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

# Base URL for repository
base_url = 'https://gaia.ari.uni-heidelberg.de/gaiasky/repository/'

# Step 1: Enrich each dataset with its per-dataset dataset.json (more up-to-date metadata)
for key, dataset in list(latest_datasets.items()):
    ds_url = os.path.dirname(update_link(dataset.get('file', ''), base_url))
    try:
        ds_json_url = ds_url + "/dataset.json"
        ds_response = requests.get(ds_json_url, timeout=5)
        if ds_response.status_code == 200:
            ds_json = ds_response.json()
            # Merge: dataset.json values take precedence, original dataset fills gaps
            dataset = {**dataset, **ds_json}
            latest_datasets[key] = dataset
    except Exception:
        pass

# Step 2: Cross-populate replaces/replacedBy so relationships are complete both ways
for key, dataset in list(latest_datasets.items()):
    replaces = get_attr(dataset, ['replaces'], [])
    replaced_by = get_attr(dataset, ['replacedBy', 'replacedby'], [])

    # For each dataset this one replaces, ensure this dataset appears in its replacedBy
    for rpl_key in replaces:
        if rpl_key in latest_datasets:
            rpl_dataset = latest_datasets[rpl_key]
            rpl_replaced_by = get_attr(rpl_dataset, ['replacedBy', 'replacedby'], [])
            if key not in rpl_replaced_by:
                rpl_replaced_by.append(key)
                rpl_dataset['replacedBy'] = rpl_replaced_by
                latest_datasets[rpl_key] = rpl_dataset

    # For each dataset that replaces this one, ensure this dataset appears in its replaces
    for rpl_key in replaced_by:
        if rpl_key in latest_datasets:
            rpl_dataset = latest_datasets[rpl_key]
            rpl_replaces = get_attr(rpl_dataset, ['replaces'], [])
            if key not in rpl_replaces:
                rpl_replaces.append(key)
                rpl_dataset['replaces'] = rpl_replaces
                latest_datasets[rpl_key] = rpl_dataset

# Now: group by type, preserving type order as seen in the original files
datasets_by_type = OrderedDict()
already_grouped = set()
for dataset in files:
    key = dataset.get('key')
    version = dataset.get('version')
    dstype = dataset.get('type', 'N/A')

    # Only consider the latest version
    if key is None or version is None:
        continue
    if key not in latest_datasets:
        continue
    if key in already_grouped:
        continue
    already_grouped.add(key)

    # Use the enriched dataset from latest_datasets
    enriched_dataset = latest_datasets[key]
    dstype = enriched_dataset.get('type', dstype)

    if dstype not in datasets_by_type:
        datasets_by_type[dstype] = []
    datasets_by_type[dstype].append(enriched_dataset)

# Sort datasets within each type: first non-replaced (alphabetically), then replaced (alphabetically)
for dstype in datasets_by_type:
    datasets_by_type[dstype].sort(key=lambda d: (
        1 if get_attr(d, ['replacedBy', 'replacedby'], []) else 0,
        d.get('name', '').lower()
    ))

# Generate Markdown
markdown_content = []
webdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

for dstype, datasets in datasets_by_type.items():
    type_n = type_name(dstype)
    markdown_content.append(f"<h2 id='{dstype}'>{type_n}</h2>\n")

    for dataset in datasets:
        ds_url = os.path.dirname(update_link(dataset.get('file', ''), base_url))
        file = ds_url + "/index.html"
        name = dataset.get('name', 'N/A')
        key = dataset.get('key', 'N/A')  # Use 'name' as key
        description = dataset.get('description', 'N/A')
        dstype = dataset.get('type', 'N/A')
        version = dataset.get('version', 'N/A')
        mingsversion = get_attr(dataset, ['mingsversion', 'minGsVersion'], 'N/A')
        minversion_str = decode_version(mingsversion)
        credits = dataset.get('credits', None)
        creator = dataset.get('creator', 'N/A')
        size_bytes = get_attr(dataset, ['size', 'sizeBytes'], 0)
        nobjects = get_attr(dataset, ['nobjects', 'nObjects'], 'N/A')
        nobjects_pretty = pretty_number(nobjects)
        replaces = get_attr(dataset, ['replaces'], [])
        replaced_by = get_attr(dataset, ['replacedBy', 'replacedby'], [])
        link = update_link(dataset.get('link', ''), base_url)
        links = [update_link(s, base_url) for s in dataset.get('links', [])]
        links = combine(link, links)

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

        # Warning icon if this dataset is replaced by others
        replaced_warning = ""
        if replaced_by:
            replaced_titles = ", ".join(replaced_by)
            replaced_warning = f' <span class="replaced-warning" title="Replaced by: {replaced_titles}">\u26a0\ufe0f</span>'

        markdown_content.append(f"<a href='#{key}'></a>")
        markdown_content.append(f'<details id="{key}">\n')
        markdown_content.append("<summary>\n")
        markdown_content.append(f"<h3>{name}{replaced_warning} <span style='font-size: 0.4em;'><a href='{file}' title='{name} files'>\U0001f517</a></span>\n")
        markdown_content.append(f"<a href='gaiasky://load?dataset={key}' title='Open \"{name}\" in Gaia Sky. Only works with Gaia Sky 3.8.1+ installed from an OS package.' class='gs-url-protocol'><i class='gs-mdi-satellite-uplink'></i> Open in Gaia Sky</a>\n")
        markdown_content.append(f"<br/><i class=\"gs-{dataicon}\" title=\"Type: {dstype}\"></i> <code title=\"Key: {key}\">{key}</code></h3>\n")
        if img:
            imgname = os.path.splitext(img)[0]
            markdown_content.append(f'<img src="/img/datasets/{img}" title="{imgname}"></img>\n')
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

        if replaces:
            markdown_content.append(f"- **Replaces:**\n")
            for rpl in replaces:
                markdown_content.append(f"    - [{rpl}](#{rpl})\n")

        if replaced_by:
            markdown_content.append(f"- **Replaced by:**\n")
            for rpl in replaced_by:
                markdown_content.append(f"    - [{rpl}](#{rpl})\n")
        
        if links:
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
