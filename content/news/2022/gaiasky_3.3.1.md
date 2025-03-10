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
- migration to new dataset structure, add data location cleaner utility at startup. 
- support gzipped data descriptor files. 
- re-balance the weights for every axis-mapped action in main gamepad listener, resulting in a much smoother navigation with game controllers and joysticks. 
- add sRGB color space support in preparation for migration to OpenXR. Activate it with the key `graphics::useSRGB` in the configuration file. 
- add support for images in tip generator, include gamepad input images. 
- complete Spanish translation to 100%. 
- add star visual settings to gamepad GUI. 
- increase global font size and UI spacing. 
- generic controller support in all UI windows. 
- add preliminary keyboard support for navigating UI menus and windows. 
- add some extra room between dataset types to improve readability. 
- add star glow factor control and API call to fine tune the amount of light irradiated by stars close to the camera. 
- add screen mode button at the top-right of the welcome GUI. 
- add gamepad support in dataset manager window. 
- remove music component from controls window. 
- activate lazy shader loading for all but the basic shader versions (SSR, motion blur, relativistic mode, gravitational waves). 
- introduce index of refraction for the celestial sphere when orthosphere view is on. Included as a slider in the experimental section of the GUI.

## Bug Fixes
- backup/restore perspective camera state before/after rendering off-screen frames and screenshots to avoid rendering artifacts whenever any of the cubemap-based modes (planetarium, panorama) is on. 
- context menu crashes when no object is hit. Fixes [#694](https://codeberg.org/gaiasky/gaiasky/issues/694).
- add 'gamepads detected' notification text to I18N files. 
- screen resizing sets internal resolution state and is persisted on restart. Adjust automatic UI scaling algorithm. 
- apply 'angle from zenith' in planetarium mode as camera rotation instead of as an effect parameter to enable 5-side optimization when aperture <= 180. 
- reimplement automatic tone mapping algorithm and manager. 
- refocusing on a star set does not always work. 
- camera speed API call not mapping values correctly. 
- add 'compiling shaders' message during loading process. 
- bookmarks to stars not selecting the right objects. 
- affine transformations applied correctly to mesh objects. 

## Build System
- changelog creation script now does not produce a full change log for the whole history of the project anymore. It now gets the tag or tag range as input and the maintainer is supposed to update the   `CHANGELOG.md` file manually. The changes are provided since a few releases ago in the release notes file. 

## Code Refactoring
- move ambient light watcher from main Gaia Sky class to own inner class, remove unused event. 
- guard GLSL libraries with `#ifndef`/`#define` preprocessor statements to prevent double definitions. 
- change screenshots system from poll to reactive. 
- rename controller GUI to gamepad GUI. 
- move content of 'Gaia' tab to 'Data' tab in preferences window. 

## Documentation
- improve contributing guidelines for translations. 

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.3.1.d6f853125/).