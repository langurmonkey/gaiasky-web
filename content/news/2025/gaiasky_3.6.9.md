+++
title = "Gaia Sky 3.6.9"
description = "Turkish, motion trails, and more"
date = 2025-07-02
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

**Edit (2025-07-03):** Update post with fixes in patch release **3.6.9-2**.

Exactly one month after Gaia Sky 3.6.8, today we are proud to release **Gaia Sky 3.6.9**. This new version brings some exciting features, like **motion trails** for star and particle groups, a new **Turkish translation**, and a new **API (v2)**, and fixes some bugs. Keep reading for the full list of changes included in this release.

{{< fig src1="img/2025/07/motion-trails.jxl" type1="image/jxl" src2="img/2025/07/motion-trails.avif" type2="image/avif" src="img/2025/07/motion-trails.jpg" class="fig-center fig-post" title="Motion trails in Gaia Sky 3.6.9." width="70%" loading="lazy" >}}
<!--more-->

## New Features & Improvements
- Add motion trail effect, which stretches stars and particles in the velocity direction. Can be toggled off in the settings.
- Add Turkish translation, contributed by Erdem Uygun.
- Migrate go-to-object operation in the camera info pane to use the smooth transitions API, which creates seamless, bumpy-free rides between two camera states.
- Add a new API v2, which re-names and re-organizes the single access port we had in the previous API into several modules grouped by function. It also improves documentation and standardizes function and parameter names when possible.
- Adapt REST server and console to also accept APIv2 calls.
- Add new setting to enable and disable notification messages, and add checkbox to preferences window. Notifications are off by default. Fixes [#847](https://codeberg.org/gaiasky/gaiasky/issues/847).
- Update monospace fonts to include all supported characters, now using Liberation Mono.
- Add missing characters to font files to ready them for the Turkish translation.
- Left and right trigger buttons (LT, RT) in gamepads to control slider values in gamepad GUI.
- Update default lens flare shader.
- Add `generateIndex` attribute to particle sets, so that the index can be omitted for sets that do not need it (which is most of them).

## Bug Fixes
- Fix issues with upper- and lower-case conversions not using the correct locale.
- Star glow effect flickers due to using a different method to render the billboard depending on whether the effect is active or not.
- Big bug fix campaign in scripting. All scripting tests were reviewed and fixed so that they all run fine.
- Add missing `"` character to fonts, fix custom and messages interfaces' computation of position coordinates.
- Dataset highlight API call not working properly.
- Use concurrent set as collections in event manager to avoid concurrent modification exceptions.
- Proper motions produce index out of bounds due to incorrect computation of maximum number of arrows.
- Correct many instances where the wrong locale is used to convert strings to upper and/or lower case. Enable star name localization for the index and labels.
- Properly scale camera mouse scroll and drag operations with the current frame rate.
- Disable OpenAL system.
- Use `RGBA16F` float format for the lens flare ping-pong buffer, otherwise AMD APUs show banding artifacts. Fixes [#846](https://codeberg.org/gaiasky/gaiasky/issues/846).
- Resolve redirects for Wikipedia titles, as the API does not resolve redirects automatically. This leads to 403 errors.
- Make sure `versionFile` task is executed when packing the app by setting the right dependencies.
- Adjust layout and width of about window to avoid UI overflow.

## Performance Improvements
- Use `GL_RGB16F` instead of `GL_RGBA16F` format (omitting the alpha channel) for internal post-processing effects buffers (lens flare, bloom, etc.). This saves some VRAM, especially useful in integrated graphics.
- Set a default value of 0.4 scale for the lens flare effect to minimize fill rate and make the ping-pong pass much faster.

## Code Refactoring
- Harmonize and consolidate star and particle set creation methods under the same class.

## Build System
- Disable OptFlowCam export option for keyframes in Flatpak in order to avoid Python dependencies.
- Upgrade to Gradle 8.14.2, which supports Java 24.
- Update to bundled JRE 24 in packages.

## Documentation
- Add new APIv2 package-level documentation.
