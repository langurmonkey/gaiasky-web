+++
title = "Gaia Sky 3.5.5"
date = "2023-09-29T09:10:00"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 Gaia Sky 3.5.5 available now!

<!--more-->


## Features
- add new user interface mode to replace the old controls window. The old UI is still available via a checkbox in the preferences. 
- add new 'play camera path' action, bound to `alt`+`c` by default. 
- controls window pane key bindings (time, camera, bookmarks, etc.) updated to not use the `Alt-L` key.
- add better star close-up shader.
- add new 'Scene settings' section in preferences window with an option to render stars as spheres.
- revamp shader include directive to accept different extensions and file references in angle brackets. 
- move shader libraries to `shader/lib`.
- retire Gaia FOV camera modes.
- adjust default atmosphere exposure value.
- disable fading scrollbars everywhere.
- prepared PBR shaders to accept iridescence, transmission and thickness values (still inactive).
- tune normal strength in tessellation shaders to map to elevation multiplier.

## Bug Fixes
- enable full shader file names in raymarching shaders.
- typo, 'user interface resetted' -> 'user interface reset'.
- restore height sampling functionality to prevent clipping through tessellated terrain.
- remove cinematic camera slow-down when close to the surface of a planet.
- scale tessellation quality using the body size to prevent severe slow-downs in smaller bodies.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.5.5.3b4d54b77/).