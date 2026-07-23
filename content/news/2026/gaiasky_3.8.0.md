+++
title = "Gaia Sky 3.8.0"
description = "Procedural planet generation overhaul, new high-res icons, and lots of fixes."
date = 2026-07-23
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

We are proud to announce the release of Gaia Sky **3.8.0**. This release brings a mainor overhaul of the procedural planet generation system, with domain warping, 3D biome LUTs, new presets, and a consolidated single-pass generation pipeline. It also introduces higher resolution icons for HiDPI, custom view mode panes, and many bug fixes.

{{< fig src="img/2026/07/procedural-grid.s.jpg" link="/img/2026/07/procedural-grid.jpg" width="70%" class="fig-center fig-post" title="Procedural planet generation in 3.8.0 featuring lava, tropical, and desert presets." loading="lazy" >}}

<!--more-->

## Procedural planet generation

The procedural planet generation system has received a substantial overhaul. The noise engine now supports domain warping, where the noise coordinates are perturbed by another noise layer before evaluation, producing much more organic and natural-looking terrain. The internal FBM noise code has been unified and streamlined.

We have added many new features to the generation pipeline:

- **3D biome LUTs** — Biomes are now indexed by moisture (X), elevation (Y), and temperature (Z) using a 3D texture lookup, enabling far richer and more diverse biome transitions. The LUTs are loaded from disk and support multiple presets.
- **Consolidated single-pass pipeline** — The old two-pass biome + surfacegen pipeline has been merged into a single `proceduralsurface` render pass. This halves GPU bandwidth per generation, eliminates 8-bit noise quantization artifacts from the intermediate biome texture, and makes the entire pipeline simpler and faster.
- **New planet presets** — Lava, tropical, desert, and several other presets have been added, each with its own 3D biome LUT and noise parameters.
- **Plains and latitude influence** — New procedural controls for plains terrain and latitude-based climate influence, enabling realistic polar ice caps and equatorial bands.
- **Colored atmospheres** — New controls to generate atmospheres with custom colors.
- **Tessellation capability detection** — The system now detects whether tessellation shaders are supported and enables them only when available.
- **New noise types** — Added blocky (city) noise, grid noise, and crater noise, alongside the existing Perlin and simplex.

{{< fig src="img/2026/07/procedural-surface.jpg" link="/img/2026/07/procedural-surface.jpg" width="40%" class="fig-center fig-post" title="The procedural planet window, with the surface tab visible." loading="lazy" >}}

## UI & icons

All marker icons, component type icons, and most UI icons have been updated to higher resolution versions for better rendering on HiDPI displays. The camera info pane now starts collapsed by default, and can be toggled with the 'N' key. The layout of the procedural planet generation window has been improved, separating presets from generation parameters.

## View modes

Custom panes have been implemented for the Stereo, Panorama, Planetarium, and Orthosphere view modes. Each pane contains its own settings and an exit button. The Stereo GUI has been disabled in favor of the new pane.

{{< fig src="img/2026/07/planetarium-pane.jpg" link="/img/2026/07/planetarium-pane.jpg" width="70%" class="fig-center fig-post" title="A view of the planetarium mode in Gaia Sky with the new UI pane open." loading="lazy" >}}


## Particles & catalogs

Particle sets now support a `renderTarget` attribute that allows them to be rendered to the second (layer) buffer, like lines and labels. A new component type, **Pulsars**, has been added for pulsar catalogs and objects. Proximity descriptors now support on-focus loading.

## Bug fixes

This release fixes a number of important issues:

- **VR** — Fix regression where VR UI would not be added correctly to the scene graph (affected 3.7.3 and 3.7.4). Remove diffuse color from VRUI and VR models to avoid them looking washed out.
- **Cube-spheres and octahedron-spheres** — Both are now properly UV-mapped and their tangents/bitangents are correctly set, making them work with procedural generation and regular texturing.
- **Star point size** — Adjusting the point size of one star dataset no longer affects all star datasets. Fixes [#921](https://codeberg.org/gaiasky/gaiasky/issues/921).
- **Light glow in cubemap mode** — Disabled light glow in cubemap modes, and billboard scale is now correctly set with respect to light glow. Fixes [#917](https://codeberg.org/gaiasky/gaiasky/issues/917).
- **Label seams in cubemap modes** — Labels now use true global orientation to prevent visible seams.
- **`colorIfTexture` attribute** — Fixed material attribute handling so that `base.color` is not mixed in when a diffuse texture is already present.
- **Ray-marching opacity** — Component type visibility now affects post-processing effects in ray-marching objects, with a new `u_opacity` uniform.
- **Occlusion clouds** — Fixed occlusion clouds not working correctly when an external clouds URL is defined but `pullCloudData` is off.
- **Compute shader reload** — Fixed a bug where the compute shader would be compiled a second time in `reload()` when compute is not supported.

## Code refactoring

Moved libGDX overwrites to the render package and renamed the Noise effect and filter to Biome for clarity.

## Build system

- Updated LWJGL3 to version 3.3.4.
- Upgraded to Gradle 9.6.1.
- Upgraded JRE bundle to JDK-26.0.1+8 in the install4j build file.
