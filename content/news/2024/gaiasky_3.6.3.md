+++
title = "Gaia Sky 3.6.3"
date = "2024-07-12T11:10:00"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 Gaia Sky 3.6.3 available now!

<!--more-->


## Features
- add on-demand loading of JSON datasets to particle groups, which enables having thousands of extrasolar systems to explore.
- add script to translate a NASA exoplanet archive VOTable to the Gaia Sky JSON format.
- replace CPU-based procedural generation with GPU-based implementation, which is orders of magnitude faster.
- improve layout of procedural generation window.
- improve cloud color and atmospheric fog density randomizers.
- use normal map when elevation type is 'None' in procedural generation.
- add initial amplitude to noise parametrization in procedural generation.
- surface generation presets (Earth-like, gas giant, rocky planet, etc.), and hide noise parameters in collapsible pane.
- add procedurally generated texture resolution to configuration and preferences window.
- add procedural generation button to camera info interface.
- move 'save textures' of procedural generation to a parallel thread.
- divide procedural generation in 4 consecutive frames. Add emission generation as an extra (optional) channel.
- add 'systems' component type, to contain all extrasolar planetary systems.
- automatic DPI scaling to support multi-DPI configurations.
- add new graphical presets (low, medium, high) to settings dialog. These presets are sets of settings that are applied all at once.
- change antialiasing settings from only type to type and quality in the configuration file.
- add tooltip with hotkeys to cinematic camera checkbox.
- improve camera velocity display units in camera info pane.
- new splash image based on NASA exoplanets.
- enable multiple lights (and also point lights) for cloud shader. This is necessary for the NASA exoplanets.
- add 'refreshRate' to orbit objects to control how often they are updated (if needed), add button to camera info interface to refresh the orbit of the selected object.

## Bug Fixes
- relativistic shaders define their own helper functions.
- broken anchor in readme file.
- error computing next focus and closest body positions.
- restore elevation-aware planet traversal.
- artifacts in atmosphere shader when SSR is active.
- adjust maximum reach of point lights.
- improve single star selection code, especially when close to stars.
- regression where orientation lock stopped working altogether.
- adjust frequency and lacunarity randomizers so that more strucutre is always present.
- crash during initialization when model is set to randomize.
- tooltip background width incorrectly computed.
- remove call to pack() in constructor.

## Performance Improvements
- enable fast-math usage by default, and remove old, unused trigo scaffolding classes.
- improve performance of recursive grid shader, which was very slow due to the background fill (with interpolation), and the animation. Animation is now removed.

## Build System
- upgrade bundled JRE to 21, minimum language version to 17.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.6.3.929b0f7a6/).