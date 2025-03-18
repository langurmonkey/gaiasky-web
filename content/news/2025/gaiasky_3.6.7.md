+++
title = "Gaia Sky 3.6.7"
date = "2025-03-18T13:20:00Z"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 We are happy to announce the release of Gaia Sky 3.6.7. This release comes with a few minor features and many important bug fixes, especially related to VR and scripting.

<!--more-->

## Features
- add composition of timed orbit coordinates and timed orbit coordinates to enable changing orbits during an object's lifetime.
- update app colors in metainfo file.
- update metainfo with better screenshots, appropriately sized for Flathub.
- update icons to higher resolution, add macOS and round versions.
- update pointers to project website and docs.
- add script to test frame output.
- add instructions to new website in release script.
- adjust star shader so that sunspots are more prominent. Enable hot reload in star shaders (use `Ctrl`+`Shift`+`Y`).
- remove music classes and events.
- increase default line width of recursive grid.

## Bug Fixes
- star velocity vectors in VR do not work.
- star's proper motions do not work in VR.
- `stopRecordingCameraPath()` does not work.
- default to '.jpg' instead of '.jpeg' as file extension for screenshots and still frames.
- refreshing orbits sometimes crashes the thread.
- constellation names sometimes not showing up with LOD catalogs.
- `FORCE_OBJECT_LABEL_CMD` now accepts an `Entity` type to work with `setForceDisplayLabel(name)` API call.
- adjust recursive grid labels and base model size.
- billboard rendering for single stars in VR mode.
- do not show component types with no style in visibility component or game pad GUI.
- focus orientation lock does not work consistently.
- trajectory scaling.
- missing translation keys for invisible component type.
- resotre motion blur settings crashes the app.
- changelog template contains wrong URL paths.

## Code Refactoring
- clean up skins, remove unused icons.

## Build System
- upgrade to Gradle 8.10.
- remove old downloads-table template, update release script with new instructions regarding release publishing on the new gaiasky.space website.
- include metainfo file in tarball, Flathub now requires this file to come from upstream.
- remove 16 and 32 pixel icons from launchers. Use only 128 pixels for macOS.

## Documentation
- update website pointers in README file.

As always, you can grab it in the [downloads page]({{< ref "downloads" >}}).
