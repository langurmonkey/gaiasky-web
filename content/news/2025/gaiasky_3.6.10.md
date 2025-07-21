+++
title = "Gaia Sky 3.6.10"
description = "Lots of minor improvements and bug fixes"
date = 2025-07-21
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

Just before the summer holidays, we are happy to announce the release of **Gaia Sky 3.6.10**. This is a release that improves on 3.6.9 by bringing a handful of minor improvements and quality-of-life updates, and a lot of bug fixes. Additionally, it enables new versions of the [base data](/resources/datasets#default-data) and the [high resolution textures](/reosurces/datasets#hi-res-textures) packs, and a new [virtual texture dataset based on Sentinel-2 data](/resources/datasets/#vt-earth-diffuse-sentinel).

Here is a screenshot with that Sentinel-2 dataset, which goes down to a resolution of 10 meters/pixel:

{{< fig src1="img/2025/07/svt-sentinel-barcelona.jxl" type1="image/jxl" src2="img/2025/07/svt-sentinel-barcelona.avif" type2="image/avif" src="img/2025/07/svt-sentinel-barcelona.jpg" class="fig-center fig-post" title="The Sentinel-2 virtual texture in Gaia Sky." width="70%" loading="lazy" >}}

You can get this dataset in Gaia Sky 3.6.10. The dataset key is `vt-earth-diffuse-sentinel`. See a  video in BlueSky [showcasing the virtual texture sentinel dataset](https://bsky.app/profile/did:plc:lyzlck7lyaeo5g5xcu3raydh/post/3ltowaie5z22l).

<!--more-->

## Features
- Localize Wikipedia API queries for object information.
- Add file-level cache to TLE subsystem. TLE files are also cached per-group to avoid unnecessary sequential calls to fetch the same file. By default, the TTL for TLE files is 1 hour.
- Directory structure of virtual texture tiles now accepts more formats (`levelx`, `levelxx`, `x`, `xx`).
- Set default virtual texture cache size to 10. Add information tooltip to cache size in preferences window.
- Add markers for towns and landmarks. Night lights go out with ambient light in PBR shader.
- Country perimeter lines disappear when the camera gets close to the surface of the Planet.
- Add new attributes to dataset definition format: `links` (now accepts multiple sources as links), `creator` (the creator or curator of the dataset), `credits` (specific attribute for credits instead of adding them to the description; multiple strings accepted).
- Add translation of object names to French.

## Bug Fixes
- Typo in default shader class (`u_emissionCubemap` -> `u_emissiveCubemap`) prevented emissive/night cubemaps from working.
- Add `nightCubemap` as alias to `emissiveCubemap` in material component.
- Add `specularValue` and `specularValues` as aliases to `specular` in material component, with floating point number parameters.
- Properly filter directories when building the SVT quadtree structure to avoid incorrect 'Wrong directory name format' warnings.
- Deactivating atmospheres causes night texture to apply uniformly to all planet as if it were a regular emissive texture.
- Procedural generation window does not fit in the window with the new UI theme. Fix layout by introducing scroll panes and resizing elements.
- Layout issue in right pane of dataset manager window prevented it from using scroll, causing the window to be too large in some cases.
- Layout issue and tooltip text in datasets component.
- Move `genVersionFile` task to the top of the dependency list (before `compileJava`) so that we always have the correct file available.
- Mend wording in new data pack notification window.
- Typo: Korou -> Kourou; Remove titles in object names I18n files.

