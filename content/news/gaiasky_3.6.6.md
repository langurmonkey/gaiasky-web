+++
title = "Gaia Sky 3.6.6"
date = "2025-01-24"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

Today we publish the version 3.6.6 of Gaia Sky. This is a small update focused on fixing some bugs and improving performance. Also, it comes with proper handling of depth for volumes!


<!--more-->

## Features
- move volumes earlier in the rendering pipeline, because they now write to the depth buffer.
- check for dataset incompatibilities and ask user to confirm action when selecting incompatible datasets.
- add window size and resolution of external view in settings, when the external view is active.

## Bug Fixes
- attitude indicator not scaling with units-per-pixel value in spacecraft UI.
- incorrect initialization of label threshold in volumes in VR mode.
- entering panorama mode resets back-buffer scale. The issue was that the dynamic resolution reset routine was always applied, and not only when the dynamic resolution setting was on.

## Performance Improvements
- replace arbitrary precision `add()` call with double-precision one to compute spherical coordinates of objects. Double-precision is more than sufficient for that purpose.

## Build System
- update install4j template to version 11.

## Documentation
- improve javadoc comments in settings class.

As always, you can grab it [right here](/downloads) ([link to repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases/3.6.6.caf73d2de)).
