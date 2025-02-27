+++
title = "Gaia Sky 3.6.5"
date = "2025-01-15T09:41:55Z"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 Today, coinciding with the end of the sky-scanning phase of Gaia, we publish GaiaSky 3.6.5. The most noteworthy addition is the introduction of the volume rendering infrastructure.

{{< fig src="img/2025/01/3.6.5-release.jpg" class="fig-center fig-post" title="Gaia Sky 3.6.5 welcome screen." loading="lazy" >}}

<!--more-->

## Features
- add support for volume rendering. The infrastructure is in place with an new archetype `Volume`. This is necessary for the new volumetric aurora dataset and volume nebulae in NGC2000.
- add 'volumes and effects' catalog type.
- enable `"flip"` attribute for `box`es/`cube`s in mesh builders.
- add `"cameraCollision"` attribute to bodies.
- shader include statement now supports targets in datasets.
- add on-demand re-compilation of post-processing shaders from their source files, in runtime.
- add new attribute 'renderLabel' to label component. This enables/disables the actual rendering of the label.
- increase default quality of FXAA filter, provide a simpler implementation (disabled by default), and enable hot shader reloading for FXAA effect.
- update Gaia Sky icon.
- add bluesky link to readme file and about page.

## Bug Fixes
- position of context menu in dataset manager is off.
- unknown dataset types crash Gaia Sky. Fixes [#787](https://codeberg.org/gaiasky/gaiasky/issues/787).
- do not crash when reloading non-compiling glsl shaders.
- wrong size initialization for raymarched objects.
- prevent non-focusable objects to appear in search results and to be set as camera focus.
- enable atmosphere/cloud procedural generation even when the surface is disabled due to cubemaps being used.
- do not attempt setting a window icon in Wayland, it is not supported and results in a (harmless) crash.
- position tracking does not work with objects in orbital elements group.
- correctly populate window width and height in preferences dialog.

## Build System
- update configuration file version number. This implies that your old configuration file gets overriden with the new version during the first startup of the new Gaia Sky version.
- update to Libgdx 1.13.1.


As always, you can grab it [right here]({{< ref "downloads" >}}) ([link to repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases/3.6.5.a7ae14f4d)).
