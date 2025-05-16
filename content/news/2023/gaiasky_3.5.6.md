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
- Add film grain filter (disabled by default).
- Set a maximum age for `.part` download files of 6 hours.
- Improve recursive grid with travelling pulses and a noise mask.
- Add 'animate' setting to recursive grid preferences to toggle animation on and off.
- Add checkbox to control recursive grid animation.
- Add initial notice about Gaia Sky contacting the server to get the dataset updates list.
- Improve shader compilation error handling.
- Enable elevation (height) representation without tessellation in a new 'regular' mode. This is the new default mode, as tessellation is a bit to taxing on old and integrated GPUs.
- Discontinue parallax mapping elevation type; the new vertex displacement type supersedes it.
- Add full support for point lights, and use them for stars.
- True depth-tested close-by stars, also working with light glow enabled.

## Bug Fixes
- Prevent creation of background blur object, as camera motion blur was disabled a few versions ago.
- Use predicted position for tracking objects.
- 'reload defaults' button in visual settings component actually sets the default value to the elevation multiplier slider.
- New star shader in intel GPUs.
- Mouse coordinates collision with objects when back buffer scale != 1.

## Code Refactoring
- Move GLSL snippet shader chunks to own directory `assets/shader/snippet`.
- Rename shaders from 'normal' to 'pbr'.

## Build System
- Set `-source` to 16 in gradle build script to enable pattern matching in instanceof.

## Style
- Code style now formats Javadoc comments.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.5.6.8bb71564a/).