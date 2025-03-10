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

- sparse virtual texture support. This unlocks new virtual texture (VT) datasets, where extremely large textures are split in tiles and loaded and streamed to the GPU on-demand.
- add filter box to dataset lists in the dataset manager.
- add 'clear' button to text fields to clear the contents at once.
- add initial support for the JPEG-XL (.jxl) image format.
- enable updating pre-loaded objects via JSON, add SVT (sparse virtual textures) component and loading mechanisms.

## Build System

- upgrade build script to install4j 10.0.4.

## Documentation

- flag Gaia Sky VR as alpha software.

## Bug Fixes

- VR controller paths in VR context. Fixes [#702](https://codeberg.org/gaiasky/gaiasky/issues/702).
- build task including certs and other unneeded stuff.
- error computing mean position in particle set when there are no particles.
- escape config file backup path in Windows.
- implement bilinear interpolation on SVT, make interpolation generic regardless of data structure used.
- skip only GB instead of GBA in RGB buffer readout in automatic tone mapping effect.

## Refactoring

- move light glow code to own render pass class.
- move shadow map code to own render pass class.
- move source version to settings.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.4.0.33ecc89f4/).