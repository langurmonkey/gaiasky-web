+++
title = "Gaia Sky 3.5.7-2"
date = "2023-11-21T12:33:00"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 Gaia Sky 3.5.7-2 available now!

<!--more-->


## Features
- display stars with missing radial velocity information as 'N/A' instead of 0. This requires a re-generation of the catalogs.
- add oblateness to sphere parameters.
- artificially increase the number of labels setting in star groups of compact octrees (fewer than 3 nodes).
- enable `numLabels` attribute for star set objects in order to control the number of labels rendered for a given star set.
- add script to generate gitstats from repository.

## Bug Fixes
- restore octree drawing functionality.
- always initialize star group sorting data (not only if 'numLabels' = 0), otherwise the system may crash, for it is used elsewhere for other purposes.
- check active list in star set exists before using.
- free XR events after using them.
- make sure that a mesh exists before disposing.
- rename `scene::star::group::numLabel` configuration property to `scene::star::group::numLabels`.

## Build System
- update gradle wrapper script files and jar.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.5.7-2.987bbd941/).