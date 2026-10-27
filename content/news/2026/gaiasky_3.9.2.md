+++
title = "Gaia Sky 3.9.2"
description = "Yet another small bugfix update"
date = 2026-10-27
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
math = true
+++

We are here yet again with another bugfix update that adds some polish to 3.9.0 and 3.9.1. Gaia Sky 3.9.2 includes a few bugfixes in volumes, UV grid labels, rendering, and the camera system. Now the new Milky Way is drawn at the right size and position, the background grid annotations are back, and a camera teleport when focusing large objects is fixed.

<!--more-->

## Bug Fixes

{{< notice "Important" >}}
Gaia Sky 3.9.2 comes with a new release of the base data pack that fixes the volumetric galaxy position and mends some issues.
{{</ notice >}}

### Volumes
- The Milky Way volume is drawn at the correct size and position (it was too small and off-centre). Volumes generated with an older `particles-to-volume.py` must be regenerated.
- Volume labels are no longer 10 times too large. Fixes [#943](https://codeberg.org/gaiasky/gaiasky/issues/943).

### Labels and grids
- The latitude/longitude annotations of the equatorial, ecliptic and galactic grids are visible again.

### Rendering
- Fixed-function GL state no longer leaks between render groups, and render-group teardown no longer skips state restoration on failure.

### Camera and focus
- Focusing an object that opts out of camera collision (e.g. the Milky Way) no longer teleports the camera out of it.
- Focus resolution no longer jumps to the first particle of a set when a name is not in its index.
