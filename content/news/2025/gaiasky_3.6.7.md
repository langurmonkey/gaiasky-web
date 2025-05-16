+++
title = "Gaia Sky 3.6.7"
description = "Bugfixes and minor features"
date = "2025-03-18T13:20:00Z"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 We are happy to announce the release of Gaia Sky 3.6.7. This release comes with a few minor features and many important bug fixes, especially related to VR and scripting.

<!--more-->

## Features
- Add composition of timed orbit coordinates and timed orbit coordinates to enable changing orbits during an object's lifetime.
- Update app colors in metainfo file.
- Update metainfo with better screenshots, appropriately sized for Flathub.
- Update icons to higher resolution, add macOS and round versions.
- Update pointers to project website and docs.
- Add script to test frame output.
- Add instructions to new website in release script.
- Adjust star shader so that sunspots are more prominent. Enable hot reload in star shaders (use `Ctrl`+`Shift`+`Y`).
- Remove music classes and events.
- Increase default line width of recursive grid.

## Bug Fixes
- Star velocity vectors in VR do not work.
- Star's proper motions do not work in VR.
- `stopRecordingCameraPath()` does not work.
- Default to '.jpg' instead of '.jpeg' as file extension for screenshots and still frames.
- Refreshing orbits sometimes crashes the thread.
- Constellation names sometimes not showing up with LOD catalogs.
- `FORCE_OBJECT_LABEL_CMD` now accepts an `Entity` type to work with `setForceDisplayLabel(name)` API call.
- Adjust recursive grid labels and base model size.
- Billboard rendering for single stars in VR mode.
- Do not show component types with no style in visibility component or game pad GUI.
- Focus orientation lock does not work consistently.
- Trajectory scaling.
- Missing translation keys for invisible component type.
- Restore motion blur settings crashes the app.
- Changelog template contains wrong URL paths.

## Code Refactoring
- Clean up skins, remove unused icons.

## Build System
- Upgrade to Gradle 8.10.
- Remove old downloads-table template, update release script with new instructions regarding release publishing on the new gaiasky.space website.
- Include metainfo file in tarball, Flathub now requires this file to come from upstream.
- Remove 16 and 32 pixel icons from launchers. Use only 128 pixels for macOS.

## Documentation
- Update website pointers in README file.

As always, you can grab it in the [downloads page]({{< ref "downloads" >}}).
