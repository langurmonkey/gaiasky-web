+++
title = "Gaia Sky 3.9.0"
description = "Volumetric Milky Way, SMAA anti-aliasing, a reworked camera, and gaiasky:// URL support."
date = 2026-10-21
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
math = true
+++

It is time for another Gaia Sky release. Gaia Sky **3.9.0** brings volumetric rendering of the Milky Way, a new SMAA anti-aliasing implementation, a reworked camera, and support for `gaiasky://` URLs, among many more new features and bug fixes.

Here is a summary of what's new in this release:

- Volumetric rendering of the Milky Way, with dust that actually occludes the stars and other elements behind it.
- New SMAA anti-aliasing, now the default method.
- Reworked camera, especially close to planets and other bodies, and smoother gamepad input.
- `gaiasky://` URL protocol support on Windows, Linux, and macOS.
- The REST server now ships in the main application, with its own preferences section.
- Sesame name discovery.
- Light glow halos sized and graded from the physical properties of the light.

If you want to know more, keep reading.

{{< notice "Important" >}}
Gaia Sky 3.9.0 requires an update in the base data pack, which replaces the particle-based Milky Way with a volumetric one. You will be notified on startup that an update is available. Please, update!
{{</ notice >}}

{{< fig src1="img/2026/10/mw.jxl" type1="img/jxl" src2="img/2026/10/mw.avif" type2="img/avif" src="img/2026/10/mw.jpg" link="img/2026/10/mw.jpg" width="70%" class="fig-center fig-post" title="The new volumetric Milky Way in Gaia Sky 3.9.0." loading="lazy" >}}

<!--more-->

## Volumetric Milky Way

The Milky Way is no longer a set of particle billboards. It is now a three-dimensional volume, ray-marched per pixel, with two channels: an **emissive** one holding the light of the gas and the bulge, and an **occlusive** one holding the dust, which emits nothing but absorbs. See the [video preview](/news/2026/galaxy-preview/) for a first look at it in motion.

This is not only an aesthetic change. A particle-based galaxy has to be sorted against itself and against the stars, it falls apart when the camera flies through the dust layer, and it looks different from every distance. A volume has none of those failure modes, and the dust lanes now actually cut the light of the stars behind them, because the dust writes depth.

{{< fig src1="img/2026/10/mw-dust.jxl" type1="img/jxl" src="img/2026/10/mw-dust.jpg" link="img/2026/10/mw-dust.jpg" width="70%" class="fig-center fig-post" title="Dust lanes in the volumetric Milky Way occluding the elements behind them." loading="lazy" >}}

The 3.9.0 volume pipeline includes:

- **RGBA (color+density) format** -- supported through the whole pipeline, from the loader all the way to the shader, so the color can vary per voxel.
- **Non-cubic volumes** -- data such as the Milky Way are not cubic by nature. A flattened grid of \\(n \times m \times n\\) voxels, with \\(m\\) much smaller than \\(n\\), uses a small fraction of the memory for the same voxel size.
- **Per-slot occlusion** -- volumes write depth in a depth-only pre-pass, so dense dust lanes hide the stars behind them while the faint outer haze does not.
- **Memory and speed** -- unused parts of 3D volumes are cropped at load time, and the raymarcher skips empty bricks with a per-volume occupancy grid of 4x4x4 bricks.
- **More control from the JSON format** -- the ray-marching iteration count is exposed, either as a single integer or as an array of four integers for the low, normal, high, and ultra quality settings, and volumes support reference system transformations (`refSysTransform`).
- **Better tooling** -- the scripts that convert particle fields to 3D textures gain the RGBA format, a smoothing parameter, gzipped inputs, a script to combine several volumes into one texture, and another to render top and side views of a volume.

The [data format documentation](https://gaia.ari.uni-heidelberg.de/gaiasky/docs/master/Data-format.html#volumes) has a new section describing volumes, and the [3D texture format](https://gaia.ari.uni-heidelberg.de/gaiasky/docs/master/Format-3d-textures.html) page covers the files themselves.

## Anti-aliasing

We have added **SMAA**, subpixel morphological anti-aliasing, with its shaders, presets, area and search textures, and the CPU-side passes. It is now the default anti-aliasing method, and it can be selected in the preferences window with three quality levels. This release also fixes assorted issues with the NFAA and FXAA shaders.

{{< fig src1="img/2026/10/aa-comparison.jxl" type1="img/jxl" src="img/2026/10/aa-comparison.jpg" link="/img/2026/10/aa-comparison.jpg" width="40%" class="fig-center fig-post" title="Visual comparison between the different anti-aliasing algorithms." loading="lazy" >}}

## Camera & controls

The camera has received a fair amount of work:

- The camera stop behaviour in cinematic and regular modes has been reworked for better responsiveness and damping.
- Camera movement close to planets and other bodies is improved, with bounded near-surface damping, a cap decoupled from the floor, and logarithmic speed scaling.
- A camera damp factor scaler has been added to the camera component, and the defaults for camera speed, rotation, and turn have been modified.
- Focus locking is fixed by incorporating the focus delta position into the camera delta position `dCam`.
- Gamepad axis and RB/LB vertical input are smoothed with a configurable smoothing setting, and the controls in game mode have been recalibrated. Low-pass smoothing for mouse movement has been reduced.

## `gaiasky://` URL protocol

Gaia Sky can now be launched from a URL, so that a web page can hand a dataset over to the application.

- The `gaiasky://` protocol is registered and handled on Windows (at install time), Linux (desktop files and `x-scheme-handler`), and macOS.
- URLs are dispatched reflectively through the APIv2, and the `gaiasky://load?dataset=` protocol loads a dataset by URL. External URLs are accepted automatically if they match any of the data mirrors; otherwise, user confirmation is required.
- A single-instance manager makes sure that a URL forwarded from a second instance, or from a macOS open event, reaches the running application and hot-loads the dataset.
- A URL protocol handler dialog has been added, with translations.

## REST server

The REST server has moved from the desktop launcher to the main Gaia Sky core, and it now has a **REST server** section in the preferences dialog, where it can be started and stopped with a given port, and where its status and API endpoints are shown. A new setting enables or disables the loopback-only binding of the server; it defaults to `true` for safety.

{{< fig src1="img/2026/10/rest.jxl" type1="img/jxl" src="img/2026/10/rest.jpg" link="/img/2026/10/rest.jpg" width="60%" class="fig-center fig-post" title="The new REST server section in the preferences window." loading="lazy" >}}

## Sesame name discovery

As an initial implementation, Sesame appears at the bottom of the autocomplete list in the search dialog; when selected, the query is sent and the result is shown in a new window. If it succeeds, all names for the object are listed.

## Light glow

The light glow has been reworked so that the halos follow the physics of the light instead of the contents of the frame:

- Each halo is sized from the angular size of the light instead of its intensity, so it grows as the camera approaches a star and stays proportional at any field of view.
- The intensity of each light is derived from its apparent magnitude, on a linear-in-magnitude scale that runs from the faintest glowing star to the Sun at 1 AU.
- The light-glow pre-pass is replaced by a depth-buffer test in the post-process filter.
- The time-driven angular mask of the halos is restored, and driven by the frame-time accumulator, so that captures and camcorder recordings animate at the target frame rate.

## User interface & other

- Datasets accept 4 images, with horizontal scrolling.
- The default star visual settings have been updated. A new settings version forces the configuration file to be updated.
- The installer image now contains only the Gaia Sky logo.
- Missing Japanese characters have been added to the character set, and the fonts have been re-generated.
- The back-buffer scale slider step is now 0.01 instead of 0.1.

## Bug fixes

Here are some of the most important bugfixes in this release:

- **Camera motion blur** -- fixed the catastrophic cancellation issue in the blur shader, reconstructed world positions from the log depth buffer, and preserved the peak brightness of point-like sources along the trail. The atmosphere shader now writes constant depth, so that the motion blur reconstructs a consistent world position for all fragments.
- **Star surface shader** -- fixed a crash. Fixes [#934](https://codeberg.org/gaiasky/gaiasky/issues/934).
- **Fast-moving particles** -- emulated double-precision time is now used also for particles with epoch=0, such as the rings of Saturn. Fixes [#930](https://codeberg.org/gaiasky/gaiasky/issues/930). Part of [#933](https://codeberg.org/gaiasky/gaiasky/issues/933).
- **Labels** -- the global label enable flag is now used correctly. It defaults to `true`, and objects can turn it off.
- **Ringed planets** -- fixed the detection when computing the occlusion attribute in the elements group renderer, which gave stars with accretion discs the incorrect illumination model.
- **Light glow pop-in** -- fixed by adjusting the minimum halo size.
- **Dataset manager** -- concurrency issues in dataset updates fixed, dataset extraction serialized with a finish lock so that concurrent downloads cannot clash on the shared data directory, update error handling hardened, and a crash on corrupted image downloads fixed. Fixes [#929](https://codeberg.org/gaiasky/gaiasky/issues/929). Part of [#928](https://codeberg.org/gaiasky/gaiasky/issues/928).
- **`TextFormatter`** -- made thread-safe, which prevents crashes due to concurrent usage of `MessageFormat`. Part of [#928](https://codeberg.org/gaiasky/gaiasky/issues/928).
- **Octants** -- fixed the NPE and memory leak when octants fade out, guarded against NPEs in octree nodes, and fixed the thread-safety issues in the camera module. The octree loader now sets the component type of the octree wrapper as 'stars'.
- **Extrasolar orbits** -- fixed the orientation inheritance.
- **Galaxies added via the UI** -- the parent is now populated correctly.
- **Empty object names** -- added a guard to prevent NPEs during focus change. Fixes [#931](https://codeberg.org/gaiasky/gaiasky/issues/931).
- **REST server** -- the port no longer disappears on the stop event, and security fixes have been applied to the server, the URL protocol, and dataset downloads.
- **Textures** -- fixed the double upload of mip level 0 when mip maps are enabled.
- **`--skip-welcome`** -- when no datasets are present, it now exits and prints a message instead of showing the recommended datasets welcome screen.
- **Shader reload** -- the shader source code is now actually reloaded on <kbd>CTRL</kbd>+<kbd>SHIFT</kbd>+<kbd>Y</kbd>, whenever possible.

## Code refactoring

The dataset download code has been decoupled from the dataset manager window into its own dataset download service, which is used in the URL handler and in the batch download window. Part of [#935](https://codeberg.org/gaiasky/gaiasky/issues/935). The old string model types have been replaced with a proper enum.

## Build system

- Upgraded to install4j 13.1.1, with pre-uninstall and post-install scripts in the UNIX installer.
- Updated to Gradle 9.8.0.
- Upgraded jCommander to 3.+, and oshi to 7.4.+ (now using the base `oshi-core` instead of `oshi-core-java11`).
- Excluded the x86 LWJGL Windows natives from the build, since only x86_64 is supported and they are flagged by Windows Defender as a potential threat.

## More

See the [full changelog for 3.9.0](/downloads/releases/v3.9.0/#release-notes) for the full list of features, fixes, and more.

**You can grab the latest installer from the [downloads page](/downloads).**
