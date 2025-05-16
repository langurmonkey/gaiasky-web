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
- Add on-demand loading of JSON datasets to particle groups, which enables having thousands of extrasolar systems to explore.
- Add script to translate a NASA exoplanet archive VOTable to the Gaia Sky JSON format.
- Replace CPU-based procedural generation with GPU-based implementation, which is orders of magnitude faster.
- Improve layout of procedural generation window.
- Improve cloud color and atmospheric fog density randomizers.
- Use normal map when elevation type is 'None' in procedural generation.
- Add initial amplitude to noise parametrization in procedural generation.
- Surface generation presets (Earth-like, gas giant, rocky planet, etc.), and hide noise parameters in collapsible pane.
- Add procedurally generated texture resolution to configuration and preferences window.
- Add procedural generation button to camera info interface.
- Move 'save textures' of procedural generation to a parallel thread.
- Divide procedural generation in 4 consecutive frames. Add emission generation as an extra (optional) channel.
- Add 'systems' component type, to contain all extrasolar planetary systems.
- Automatic DPI scaling to support multi-DPI configurations.
- Add new graphical presets (low, medium, high) to settings dialog. These presets are sets of settings that are applied all at once.
- Change antialiasing settings from only type to type and quality in the configuration file.
- Add tooltip with hotkeys to cinematic camera checkbox.
- Improve camera velocity display units in camera info pane.
- New splash image based on NASA exoplanets.
- Enable multiple lights (and also point lights) for cloud shader. This is necessary for the NASA exoplanets.
- Add 'refreshRate' to orbit objects to control how often they are updated (if needed), add button to camera info interface to refresh the orbit of the selected object.

## Bug Fixes
- Relativistic shaders define their own helper functions.
- Broken anchor in readme file.
- Error computing next focus and closest body positions.
- Restore elevation-aware planet traversal.
- Artifacts in atmosphere shader when SSR is active.
- Adjust maximum reach of point lights.
- Improve single star selection code, especially when close to stars.
- Regression where orientation lock stopped working altogether.
- Adjust frequency and lacunarity randomizers so that more strucutre is always present.
- Crash during initialization when model is set to randomize.
- Tooltip background width incorrectly computed.
- Remove call to pack() in constructor.

## Performance Improvements
- Enable fast-math usage by default, and remove old, unused trigo scaffolding classes.
- Improve performance of recursive grid shader, which was very slow due to the background fill (with interpolation), and the animation. Animation is now removed.

## Build System
- Upgrade bundled JRE to 21, minimum language version to 17.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.6.3.929b0f7a6/).