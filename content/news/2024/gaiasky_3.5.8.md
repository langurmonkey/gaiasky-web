+++
title = "Gaia Sky 3.5.8"
date = "2024-01-26T11:01:00"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 Gaia Sky 3.5.8 available now!

<!--more-->


## Features
- Add bookmarks section in gamepad GUI. See [#757](https://codeberg.org/gaiasky/gaiasky/issues/757).
- Cloud shadow projections on the surface of planets, for regular textures, cubemaps and SVT clouds.
- Add new `backupSettings()` and `restoreSettings()` API calls to back up and restore the entire settings in Gaia Sky from a script.
- Move 'star glow over objects' check box to Scene settings > Stars section.
- Add used, free, allocated and total memory to memory information window in help dialog.
- Enable eclipse outlines (for umbra and penumbra) by default in configuration file.
- Add application-level shader disk cache that stores binary shaders to disk to speed up application startup. Disabled by default, as most GPU drivers already do this on their own.
- Add binary particle group loader/writer to be able to load particles using an own binary format that loads much faster.
- Support `PARTICLE_EXT` attributes, additionally to the base `PARTICLE` attributes in the new binary format for particle groups.
- Increase number of divisions in shapes around objects from 15 to 35. Do not cull faces. See [#756](https://codeberg.org/gaiasky/gaiasky/issues/756).
- Enable exporting cubemap sides to image files, action bound to `F7` by default. Fixes [#753](https://codeberg.org/gaiasky/gaiasky/issues/753).
- Adjust constants so that the Sun size is accurate.

## Bug Fixes
- Use actual tree map for currently pressed keys in keyboard input controller, so that actions can be retrieved reliably.
- Do not activate surface mode (where the view follows the mouse location) with gamepad input.
- Layout and information in about/help dialog.
- Dataset detection to use dataset key by default instead of name.
- Apply graphics quality after restart. Remove graphics quality update events.
- Graphics quality update is now a 'needs restart' operation, otherwise the system crashes trying to load in new parameters, textures and so on. This is part of [#719](https://codeberg.org/gaiasky/gaiasky/issues/719).
- Increase constellation and boundaries line width to prevent rastering artifacts. This is part of [#719](https://codeberg.org/gaiasky/gaiasky/issues/719).
- Star flickering issues due to quad sizes mended by setting a minimum quad solid angle roughly equal to the pixel size of the back-buffer. Fixes [#719](https://codeberg.org/gaiasky/gaiasky/issues/719).
- Tooltips in number validators using the `MAX_VALUE` or `MIN_VALUE` should use infinity instead. Part of [#756](https://codeberg.org/gaiasky/gaiasky/issues/756).
- Add orientation to shape dialog (camera, equatorial, ecliptic, galactic). Fixes [#756](https://codeberg.org/gaiasky/gaiasky/issues/756).
- Remove all shapes [& around object] actually removes all shapes and not only the first in the list. This is part of [#756](https://codeberg.org/gaiasky/gaiasky/issues/756).
- Default to scientific notation only when abs(num) > 9999. Fixes [#755](https://codeberg.org/gaiasky/gaiasky/issues/755).
- Possible null pointer exceptions in OpenXR driver.
- Enable breaking string sequences at forward and backward slashes, as well as whitespaces. This prevents overflown content in the error dialog in certain cases.
- Run actual octant update code in the main thread.
- Particle sizing and size limits in the loader.

## Performance Improvements
- Remove unnecessary synchronized blocks from index.
- Use parallel sort instead of regular single-threaded sort for particle and star sets.
- Make sure that unseen stars (i.e. computed final color is 0) do not take up fragment shader resources.

## Code Refactoring
- Rename attributes of UCD and UCDParser to comport with the global style.

## Build System
- Upgrade to gradle 8.5.

## Merge Requests
- Merge branch 'star-shading'.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.5.8.77b1dcbf6/).