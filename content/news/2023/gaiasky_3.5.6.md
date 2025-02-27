+++
title = "Gaia Sky 3.5.6"
date = "2023-10-20T10:04:00"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 Gaia Sky 3.5.6 available now!

<!--more-->


## Features
- add film grain filter (disabled by default).
- set a maximum age for `.part` download files of 6 hours.
- improve recursive grid with travelling pulses and a noise mask.
- add 'animate' setting to recursive grid preferences to toggle animation on and off.
- add checkbox to control recursive grid animation.
- add initial notice about Gaia Sky contacting the server to get the dataset updates list.
- improve shader compilation error handling.
- enable elevation (height) representation without tessellation in a new 'regular' mode. This is the new default mode, as tessellation is a bit to taxing on old and integrated GPUs.
- discontinue parallax mapping elevation type; the new vertex displacement type supersedes it.
- add full support for point lights, and use them for stars.
- true depth-tested close-by stars, also working with light glow enabled.

## Bug Fixes
- prevent creation of background blur object, as camera motion blur was disabled a few versions ago.
- use predicted position for tracking objects.
- 'reload defaults' button in visual settings component actually sets the default value to the elevation multiplier slider.
- new star shader in intel GPUs.
- mouse coordinates collision with objects when back buffer scale != 1.

## Code Refactoring
- move GLSL snippet shader chunks to own directory `assets/shader/snippet`.
- rename shaders from 'normal' to 'pbr'.

## Build System
- set `-source` to 16 in gradle build script to enable pattern matching in instanceof.

## Style
- code style now formats Javadoc comments.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.5.6.8bb71564a/).