+++
title = "Gaia Sky 3.2.1"
date = "2022-11-11T10:16:00"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 Gaia Sky 3.2.1 available now!

<!--more-->


## Build System

- docs project no longer a submodule.
- move namespace from 'gitlab.com/langurmonkey' to 'gitlab.com/gaiasky'.

## Features

- save configuration when closing dataset manager window.
- use view angle instead of view angle apparent for `goToObject()` API call.

## Bug Fixes

- break link in dataset manager if too long.
- filters crash with instanced star renderers.
- frame sequence number synchronized, value updated when opening preferences.
- highlight 'all visible' setting in quad-based star renderers.
- hotkey tooltip backgrounds.
- increase number of vertices of minimap shape renderer, fixes crash in heliosphere minimap.
- jump in Pluto's orbit due to deviation between full periods.
- modal windows made not collapsible by default.
- moon orbits are recomputed more often.
- translate strings of filters, shapes, datasets and minimap. Fixes [#403](https://gitlab.com/gaiasky/gaiasky/issues/403).
- typo in Jupiter English translation file, add meshes to data descriptor file.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.2.1.41e4b0a5b/).