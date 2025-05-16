+++
title = "Gaia Sky 3.3.1"
date = "2022-12-18T09:12:00"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 Gaia Sky 3.3.1 available now!

<!--more-->


## Features
- Migration to new dataset structure, add data location cleaner utility at startup.
- Support gzipped data descriptor files.
- Re-balance the weights for every axis-mapped action in main gamepad listener, resulting in a much smoother navigation with game controllers and joysticks.
- Add sRGB color space support in preparation for migration to OpenXR. Activate it with the key `graphics::useSRGB` in the configuration file.
- Add support for images in tip generator, include gamepad input images.
- Complete Spanish translation to 100%.
- Add star visual settings to gamepad GUI.
- Increase global font size and UI spacing.
- Generic controller support in all UI windows.
- Add preliminary keyboard support for navigating UI menus and windows.
- Add some extra room between dataset types to improve readability.
- Add star glow factor control and API call to fine tune the amount of light irradiated by stars close to the camera.
- Add screen mode button at the top-right of the welcome GUI.
- Add gamepad support in dataset manager window.
- Remove music component from controls window.
- Activate lazy shader loading for all but the basic shader versions (SSR, motion blur, relativistic mode, gravitational waves).
- Introduce index of refraction for the celestial sphere when orthosphere view is on. Included as a slider in the experimental section of the GUI.

## Bug Fixes
- Backup/restore perspective camera state before/after rendering off-screen frames and screenshots to avoid rendering artifacts whenever any of the cubemap-based modes (planetarium, panorama) is on.
- Context menu crashes when no object is hit. Fixes [#694](https://codeberg.org/gaiasky/gaiasky/issues/694).
- Add 'gamepads detected' notification text to I18N files.
- Screen resizing sets internal resolution state and is persisted on restart. Adjust automatic UI scaling algorithm.
- Apply 'angle from zenith' in planetarium mode as camera rotation instead of as an effect parameter to enable 5-side optimization when aperture <= 180.
- Reimplement automatic tone mapping algorithm and manager.
- Refocusing on a star set does not always work.
- Camera speed API call not mapping values correctly.
- Add 'compiling shaders' message during loading process.
- Bookmarks to stars not selecting the right objects.
- Affine transformations applied correctly to mesh objects.

## Build System
- Changelog creation script now does not produce a full change log for the whole history of the project anymore. It now gets the tag or tag range as input and the maintainer is supposed to update the   `CHANGELOG.md` file manually. The changes are provided since a few releases ago in the release notes file.

## Code Refactoring
- Move ambient light watcher from main Gaia Sky class to own inner class, remove unused event.
- Guard GLSL libraries with `#ifndef`/`#define` preprocessor statements to prevent double definitions.
- Change screenshots system from poll to reactive.
- Rename controller GUI to gamepad GUI.
- Move content of 'Gaia' tab to 'Data' tab in preferences window.

## Documentation
- Improve contributing guidelines for translations.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.3.1.d6f853125/).