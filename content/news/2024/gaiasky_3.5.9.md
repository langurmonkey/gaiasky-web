+++
title = "Gaia Sky 3.5.9"
date = "2024-02-19T15:08:00"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 Gaia Sky 3.5.9 available now!

<!--more-->


## Features
- add support for arbitrary affine transformations to datasets, and add controls to create and edit them in the datasets pane.
- separate filters from dataset preferences into their own button/window in datasets pane.
- improve layout of the filters window by moving the 'add' button to the top and adding a scroll pane in the content.
- improve default window skin by adding some padding and a better sprite.
- rename dataset preferences to dataset visual settings. It now contains some sliders to modify the point size and the min/max solid angles. It does not contain filters or dataset information anymore, as those were extracted to their own dialogs.
- add affine transformations to all datasets (particle group, star group, variable star group, billboard group, orbit elements group). These transformations are applied in the shaders so that they can be updated on the fly. The billboard group object has been moved inside the generic catalog archetype; the Milky Way appears as a dataset now.
- add min/max particle solid angle size and number of labels to particle dataset load dialog.
- add support for additional texture(s) in raymarching shaders.
- do not force safe mode on Macs powered by apple silicon anymore.

## Bug Fixes
- remove support for cloud SVT shadows, as this necessitates the cloud SVT and the diffuse SVT to be exactly the same (same depth, same available tiles, etc.), and this is not *usually* the case.
- concurrency error in procedural generation progress bar update actions.
- present filter results in dataset manager in expanded panes.
- prevent the creation of multiple dataset preferences window for the same dataset.
- prevent NPE crash during the creation of the error dialog. Part of [#765](https://codeberg.org/gaiasky/gaiasky/issues/765).
- prevent null pointer when updating star sets. Fixes [#766](https://codeberg.org/gaiasky/gaiasky/issues/766).
- typo in French translation.
- appimage actually includes unpacked JRE distribution correctly.

## Build System
- add pgp signature to build process instead of checksums.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.5.9.51d1305ab/).