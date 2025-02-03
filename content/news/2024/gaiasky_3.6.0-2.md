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
- annotate camera files with frame rate so that playback can adjust it automatically. 

## Bug Fixes
- camcorder play and record button inconsistent states.
- state handling in the camcorder.
- `sleep(seconds)` call also respects the camcorder FPS setting during recording.
- rename some API calls, deprecate old versions.
- add companion calls for camera orientation and position transitions.
- orbit coordinate not working when time is before the orbit start.
