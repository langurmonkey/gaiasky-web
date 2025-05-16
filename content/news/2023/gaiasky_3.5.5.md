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
- Add new user interface mode to replace the old controls window. The old UI is still available via a checkbox in the preferences.
- Add new 'play camera path' action, bound to `alt`+`c` by default.
- Controls window pane key bindings (time, camera, bookmarks, etc.) updated to not use the `Alt-L` key.
- Add better star close-up shader.
- Add new 'Scene settings' section in preferences window with an option to render stars as spheres.
- Revamp shader include directive to accept different extensions and file references in angle brackets.
- Move shader libraries to `shader/lib`.
- Retire Gaia FOV camera modes.
- Adjust default atmosphere exposure value.
- Disable fading scrollbars everywhere.
- Prepared PBR shaders to accept iridescence, transmission and thickness values (still inactive).
- Tune normal strength in tessellation shaders to map to elevation multiplier.

## Bug Fixes
- Enable full shader file names in raymarching shaders.
- Typo, 'user interface resetted' -> 'user interface reset'.
- Restore height sampling functionality to prevent clipping through tessellated terrain.
- Remove cinematic camera slow-down when close to the surface of a planet.
- Scale tessellation quality using the body size to prevent severe slow-downs in smaller bodies.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.5.5.3b4d54b77/).