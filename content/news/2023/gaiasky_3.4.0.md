+++
title = "Gaia Sky 3.4.0"
date = "2023-02-14T08:35:00"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 Gaia Sky 3.4.0 available now!

<!--more-->


## Features

- Sparse virtual texture support. This unlocks new virtual texture (VT) datasets, where extremely large textures are split in tiles and loaded and streamed to the GPU on-demand.
- Add filter box to dataset lists in the dataset manager.
- Add 'clear' button to text fields to clear the contents at once.
- Add initial support for the JPEG-XL (.jxl) image format.
- Enable updating pre-loaded objects via JSON, add SVT (sparse virtual textures) component and loading mechanisms.

## Build System

- Upgrade build script to install4j 10.0.4.

## Documentation

- Flag Gaia Sky VR as alpha software.

## Bug Fixes

- VR controller paths in VR context. Fixes [#702](https://codeberg.org/gaiasky/gaiasky/issues/702).
- Build task including certs and other unneeded stuff.
- Error computing mean position in particle set when there are no particles.
- Escape config file backup path in Windows.
- Implement bilinear interpolation on SVT, make interpolation generic regardless of data structure used.
- Skip only GB instead of GBA in RGB buffer readout in automatic tone mapping effect.

## Refactoring

- Move light glow code to own render pass class.
- Move shadow map code to own render pass class.
- Move source version to settings.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.4.0.33ecc89f4/).