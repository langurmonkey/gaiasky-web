+++
title = "Gaia Sky 3.6.0-2"
date = "2024-03-14T08:56:00"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 Gaia Sky 3.6.0-2 available now!

<!--more-->


## Features
- Annotate camera files with frame rate so that playback can adjust it automatically.

## Bug Fixes
- Camcorder play and record button inconsistent states.
- State handling in the camcorder.
- `sleep(seconds)` call also respects the camcorder FPS setting during recording.
- Rename some API calls, deprecate old versions.
- Add companion calls for camera orientation and position transitions.
- Orbit coordinate not working when time is before the orbit start.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.6.0-2.4479175dc/).