+++
title = "Gaia Sky 3.7.4"
description = "This version brings a new atmospheric scattering model and many bugfixes."
date = 2026-06-17
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

We are proud to announce the release of Gaia Sky **3.7.4**.  This release brings a major overhaul of the atmospheric scattering model with ozone absorption, Bruneton's density scale, a unified ground/sky integrator, and a physically-grounded parametrization. It also includes important bugfixes for the keyframe system, and build system updates.

{{< fig src="img/screenshots/earth-thumb.jpg" link="/img/screenshots/earth.jpg" width="50%" class="fig-center fig-post" title="The revised atmospheric scattering model in 3.7.4 at work." loading="lazy" >}}

<!--more-->

## Atmospheric scattering

The atmospheric scattering model has received an almost complete overhaul. The previous O'Neil-based implementation used separate, divergent code paths for the ground and sky (atmosphere dome) shaders, leading to unstable behavior when parameters changed and visible banding artifacts at low sample counts. The new implementation consolidates both into a single unified `integrateAtmosphere()` function shared by the ground and sky shaders. It adopts Bruneton's 4th-order polynomial approximation of the Chapman function for the density scale, which eliminates artifacts at grazing angles. The scattering color is correctly blended using glow and transmittance, and the tone mapping exposure is unified across both paths.

We have also added some more stuff:

- Consider elevation displacement in scattering calculations. The vertex shader now correctly accounts for the terrain height offset when computing the vertex position for atmospheric scattering.
- Add ozone (O₃) absorption to atmospheric scattering. Ozone is modeled as a Gaussian density profile centered in the stratosphere (default peak at 25 km altitude, \~20 km width). The absorption coefficients match the Chappuis band shape (peaking at \~600 nm in the red, with significant absorption in green and minimal in blue). Parametrization adopts O₃ optical depth, the vertical optical depth of ozone at red (\~600 nm, Chappuis peak). The Earth reference value us \~0.025.
- Expose ozone optical depth in the procedural planet dialog. Adds new slider to the procedural planet generation window.

## Bug Fixes

This release fixes a regression in the keyframe system, and includes some other important items:

- Fix regression in which the keyframe visual representation was not visible.
- Fix locale initialization sequence by passing the settings object. At startup, the `GaiaSky` instance has not been initialized, so i18n always defaulted to the system locale regardless of the settings.
- Check for SSBO extension additionally to the compute shader one in `isComputeShaderSupported()`. Avoids a crash when the driver supports compute shaders but not OpenGL 4.3 nor SSBO.
- Fix dependency on Java >=26 in AUR package. Required for compact object headers support without `UnlockExperimentalVMOptions`.
- Fix directory selection in file picker. The file picker dialog now correctly selects directories instead of files when a directory path is provided.

## Localization

We have updated the translation files with missing keys, bringing all locale files to 100% completion. Additionally, we updated screenshot URLs in the metainfo file to point to the current hosting locations.

## Build System

Finally, we updated the libGDX framework library to 1.14.2 and the Gradle wrapper to 9.5.1.
