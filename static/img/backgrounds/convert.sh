#!/bin/bash
# Converts all jpg files in the given directory to avif.

# Check if a directory is provided as an argument
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

# Directory containing the input files
DIR="$1"

# Check if the provided argument is a valid directory
if [ ! -d "$DIR" ]; then
  echo "Error: $DIR is not a valid directory."
  exit 1
fi

# Loop through all JPG files in the directory
for file in "$DIR"/*.jpg; do
  # Check if there are no JPG files (to avoid errors)
  [ -e "$file" ] || continue

  # Get the base name of the file without extension
  base_name=$(basename "$file" .jpg)

  # Define the output AVIF file path
  output_file="$DIR/$base_name.avif"

  # Convert JPG to AVIF
  avifenc -q 80 "$file" "$output_file"

  echo "Converted $file to $output_file"
done
