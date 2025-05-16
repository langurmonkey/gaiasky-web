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

- Docs project no longer a submodule.
- Move namespace from 'gitlab.com/langurmonkey' to 'gitlab.com/gaiasky'.

## Features

- Save configuration when closing dataset manager window.
- Use view angle instead of view angle apparent for `goToObject()` API call.

## Bug Fixes

- Break link in dataset manager if too long.
- Filters crash with instanced star renderers.
- Frame sequence number synchronized, value updated when opening preferences.
- Highlight 'all visible' setting in quad-based star renderers.
- Hotkey tooltip backgrounds.
- Increase number of vertices of minimap shape renderer, fixes crash in heliosphere minimap.
- Jump in Pluto's orbit due to deviation between full periods.
- Modal windows made not collapsible by default.
- Moon orbits are recomputed more often.
- Translate strings of filters, shapes, datasets and minimap. Fixes [#403](https://gitlab.com/gaiasky/gaiasky/issues/403).
- Typo in Jupiter English translation file, add meshes to data descriptor file.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.2.1.41e4b0a5b/).