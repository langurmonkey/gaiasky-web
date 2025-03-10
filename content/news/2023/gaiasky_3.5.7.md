+++
title = "Gaia Sky 3.5.7"
date = "2023-11-07T09:47:00"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 Gaia Sky 3.5.7 available now!

<!--more-->


## Features
- add surface exploration mode for planets, where the camera moves relative to the position of the pointer when close to a planet or moon.
- add floating-point completion rates to billboard datasets.
- combine SSR with cubemap reflections to fill in parts that reflect to off-screen locations.
- add Debian build files. Add Makefile. Add `createDebian` task to gradle build script.
- updated Bulgarian translation

## Bug Fixes
- crash when enabling 'Others' component type at startup in VR.
- sizing of datasets scroll pane with expand/collapse groups is incorrect in some instances.
- add free space check before downloads, and clean up properly after a failed extraction operation. Fixes [#744](https://codeberg.org/gaiasky/gaiasky/issues/744).
- auto-scroll to target when cycling through UI elements with gamepad left stick. Selection and action with gamepad in dataset manager window.
- zero-length keyframed path crashes the 'normalize times' action. Fixes [#741](https://codeberg.org/gaiasky/gaiasky/issues/741).
- add missing, untranslated strings to I18N files. Fixes [#740](https://codeberg.org/gaiasky/gaiasky/issues/740).
- start and dataset manager buttons do not scale horizontally with content.
- ascending node parameter in rotation component does not apply correctly. Bump source version to 3.5.7, for new data is needed.
- recursive tile lookup in sparse virtual textures module does not work correctly.
- prevent SVT level overflows, and prompt for restart when tile cache size is modified in preferences.
- remove custom amount of vertical scroll in scroll panes. Scrolling should now be much easier.

## Build System
- upgrade to LibGDX 1.12.1 and LWJGL 3.3.3.

## Style
- add missing deprecated tags to deprecated items.

## Merge Requests
- Merge branch 'RacerBG-bg-update'

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.5.7.9d7eedd2e/).