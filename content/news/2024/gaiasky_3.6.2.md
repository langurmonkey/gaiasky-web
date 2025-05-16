+++
title = "Gaia Sky 3.6.2"
date = "2024-06-05T15:27:00"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 Gaia Sky 3.6.2 available now!

<!--more-->


## Features
- Enable ray-marching effects in stereoscopic mode.

## Bug Fixes
- Use a new instance of the preferences dialog each time it is open, so that all preferences are reinitialized correctly.
- Invert-x/-y button in gamepad GUI does not work/update correctly.
- Ray-marching effects in cubemap modes. Probably a source of unforeseen consequences.
- Remove blank frame produced when activating a ray-marching effect for the first time.
- Never skip future closest body position computation.
- Restore light glow effect in cubemap modes (360, planetarium, orthosphere).
- Restore light glow effect in stereoscopic mode.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.6.2.1b1e23dbb/).