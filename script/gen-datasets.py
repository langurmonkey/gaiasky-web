import json
import gzip
import requests
import io
import os.path

# Function to convert bytes to MB
def bytes_to_mb(size_in_bytes):
    return size_in_bytes / (1024 * 1024)

# Replace the "@mirror-url@" placeholder in the link
def update_link(link, base_url):
    return link.replace('@mirror-url@', base_url)

# Decode an integer into the version string
def decode_version(s: str) -> str:
    try:
        n = int(s)  # Try converting to an integer
        patch = n % 100  # Last two digits
        revision = (n // 100) % 100  # Next two digits
        minor = (n // 10_000) % 100  # Next two digits
        major = n // 1_000_000  # Remaining digits
        return f"{major}.{minor}.{revision}-{patch}"
    except ValueError:
        return "N/A"

# Types to icons
icons = {
    "data-pack" : "fa-solid fa-database",
    "texture-pack" : "fa-regular fa-image",
    "virtualtex-pack" : "fa-solid fa-panorama",
    "catalog-lod" : "fa-solid fa-chart-diagram",
    "catalog-gaia" : "fa-solid fa-sun",
    "catalog-star" : "fa-solid fa-sun",
    "catalog-gal" : "fa-solid fa-box-open",
    "catalog-cluster" : "fa-solid fa-globe",
    "catalog-sso" : "fa-solid fa-meteor",
    "catalog-other" : "fa-solid fa-cube",
    "system" : "fa-solid fa-earth-europe",
    "mesh" : "fa-solid fa-hexagon-nodes",
    "spacecraft" : "fa-solid fa-satellite",
    "volume" : "fa-solid fa-cloud",
}
def icon(type):
    return icons.get(type, "fa-regular fa-cube")

# Load JSON from a gzipped URL
json_gz_url = "https://gaia.ari.uni-heidelberg.de/gaiasky/repository/gaiasky-data-03060501.json.gz"


response = requests.get(json_gz_url)
response.raise_for_status()  # Ensure the request was successful

# Decompress the gzipped content correctly
with gzip.GzipFile(fileobj=io.BytesIO(response.content), mode='rb') as decompressed:
    data = json.load(decompressed)  # Load JSON directly from decompressed data

# Group datasets by their unique key and keep the latest version
latest_datasets = {}

# Process the 'files' list in the dictionary
files = data.get('files', [])

for dataset in files:
    key = dataset.get('key', None)
    version = dataset.get('version', None)
    
    if key is not None and version is not None:
        # Keep the latest version for each key
        if key not in latest_datasets or int(version) > int(latest_datasets[key]['version']):
            latest_datasets[key] = dataset

# Generate Markdown
base_url = 'https://gaia.ari.uni-heidelberg.de/gaiasky/repository/'
markdown_content = []

for dataset in latest_datasets.values():
    name = dataset.get('name', 'N/A')
    key = dataset.get('key', 'N/A')  # Use 'name' as key
    description = dataset.get('description', 'N/A')
    dstype = dataset.get('type', 'N/A')
    version = dataset.get('version', 'N/A')
    mingsversion = dataset.get('mingsversion', 'N/A')

    minversion_str = decode_version(mingsversion)
    size_bytes = dataset.get('size', 0)
    num_objects = dataset.get('num_objects', 'N/A')
    link = update_link(dataset.get('link', ''), base_url)
    file = os.path.dirname(update_link(dataset.get('file', ''), base_url))

    fa_icon = icon(dstype)

    # Format size in MB
    size_mb = bytes_to_mb(size_bytes)

    markdown_content.append(f"<details>\n")
    markdown_content.append(f"<summary>\n")
    markdown_content.append(f"<h3>{name}<br/><i class='{fa_icon}' title='Type: {dstype}'></i> <code title='Key: {key}'>{key}</code></h3>\n")
    markdown_content.append(f"</summary>\n")
    markdown_content.append(f"<article>\n")
    markdown_content.append(f"{description}\n\n")
    markdown_content.append(f"- **Type:** `{dstype}`\n")
    markdown_content.append(f"- **Dataset version:** {version}\n")
    markdown_content.append(f"- **Minimum Gaia Sky version:** {minversion_str}\n")
    markdown_content.append(f"- **Size:** {size_mb:.2f} MB\n")
    markdown_content.append(f"- **Number of objects:** {num_objects}\n")
    markdown_content.append(f"- [More info]({link})\n")
    markdown_content.append(f"- **Dataset files:** {link}\n")
    markdown_content.append(f"</article>\n")
    markdown_content.append(f"</details>\n")
    markdown_content.append("\n")

# Write Markdown to a file
with open('datasets.md', 'w') as f:
    f.write("""
+++
title = "Datasets"
type = "page"
css = ["css/datasets.css"]
+++

# Gaia Sky Datasets

This page lists the last version for each dataset in Gaia Sky. You can download each dataset directly from within Gaia Sky using the dataset manager (**recommended!**), or by following the 'Dataset files' link in each dataset.
 In order to install any of the packages manually, just download it and extract the contents it in your data folder (defaults to `$HOME/.local/share/gaiasky/data/` in Linux, and `$HOME/.gaiasky/data` in Windows and macOS).

Click on the dataset title to reveal more information. 
<br/><br/>
""")
    f.writelines(markdown_content)

print("Markdown file 'datasets.md' has been generated.")
