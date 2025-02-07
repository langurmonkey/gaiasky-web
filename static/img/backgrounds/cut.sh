#!/bin/bash

# Cut top and bottom 20% of every image in directory.


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

# Loop through all images in the directory
for file in "$DIR"/*.{jpg,jpeg,png,avif}; do
  # Check if there are no image files (to avoid errors)
  [ -e "$file" ] || continue

  # Get the base name of the file
  base_name=$(basename "$file")

  # Define the output file path
  output_file="$DIR/cropped_$base_name"

  # Calculate the crop dimensions
  height=$(identify -format "%h" "$file")
  top_crop=$((height * 20 / 100))
  bottom_crop=$((height * 80 / 100))

  # Crop the image
  magick "$file" -crop ${width}x${bottom_crop}+0+$top_crop +repage "$output_file"

  echo "Processed $file to $output_file"
done
