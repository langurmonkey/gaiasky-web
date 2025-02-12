import json
import requests

# Function to convert bytes to MB
def bytes_to_mb(size_in_bytes):
    return size_in_bytes / (1024 * 1024)

# Replace the "@mirror-url@" placeholder in the link
def update_link(link, base_url):
    return link.replace('@mirror-url@', base_url)

# Load JSON from URL (you can also load it from a file)
json_file_path = '/home/tsagrista/Projects/gaiasky-data/gaiasky-data.json'
with open(json_file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Group datasets by their unique key and keep the latest version
latest_datasets = {}

# Process the 'files' list in the dictionary
files = data.get('files', [])

for dataset in files:
    key = dataset.get('name', None)
    version = dataset.get('version', None)
    
    if key and version:
        # Keep the latest version for each key
        if key not in latest_datasets or version > latest_datasets[key]['version']:
            latest_datasets[key] = dataset

# Generate Markdown
base_url = 'https://gaia.ari.uni-heidelberg.de/gaiasky/repository/'
markdown_content = []

for dataset in latest_datasets.values():
    name = dataset.get('name', 'N/A')
    key = dataset.get('key', 'N/A')  # Use 'name' as key
    description = dataset.get('description', 'N/A')
    type_ = dataset.get('type', 'N/A')
    version = dataset.get('version', 'N/A')
    mingsversion = dataset.get('mingsversion', 'N/A')
    size_bytes = dataset.get('size', 0)
    num_objects = dataset.get('num_objects', 'N/A')
    link = update_link(dataset.get('link', ''), base_url)

    # Format size in MB
    size_mb = bytes_to_mb(size_bytes)

    markdown_content.append(f"### {name} (`{key}`)\n")
    markdown_content.append(f"- **Description:** {description}\n")
    markdown_content.append(f"- **Type:** {type_}\n")
    markdown_content.append(f"- **Dataset version:** {version}\n")
    markdown_content.append(f"- **Minimum Gaia Sky version:** {mingsversion}\n")
    markdown_content.append(f"- **Size:** {size_mb:.2f} MB\n")
    markdown_content.append(f"- **Number of objects:** {num_objects}\n")
    markdown_content.append(f"- **Link:** [{link}]({link})\n")
    markdown_content.append("\n")

# Write Markdown to a file
with open('datasets.md', 'w') as f:
    f.write("""
+++
title = "Datasets"
type = "page"
+++

""")
    f.writelines(markdown_content)

print("Markdown file 'datasets.md' has been generated.")
