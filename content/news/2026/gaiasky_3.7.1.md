+++
title = "Gaia Sky 3.7.1"
description = "This release introduces a new system to generate galaxies procedurally using compute shaders, alongside a total overhaul of our light model, and much more"
date = 2026-02-04
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

We are excited to announce the release of **Gaia Sky 3.7.1**. This release was planned for last Christmas, but we had to postpone it due to the server outage issue. Now it is here! While there are many under-the-hood fixes, the highlights of this version are:

- The new procedural galaxy generation system,
- the PBR shader overhaul,
- some notable UI improvements,
- a revision of the atmospheric scattering algorithm,
- new 3D anaglyph modes,
- and improvements in eclipses.

Interested? Keep reading to know more.

<!--more-->

## Procedural galaxies

We have implemented a full pipeline to generate galaxies on the fly. This system uses GPU compute shaders to handle the heavy lifting, allowing you to create complex galactic structures in real-time. It falls back to a CPU method in macOS and systems that do not support OpenGL compute shaders.

{{< fig src="img/2025/11/hubble_grid_small.thumb.jpg" link="/img/2025/11/hubble_grid_small.jpg" class="fig-center fig-post" title="Procedural generation of several galaxy morphologies in Gaia Sky. [Full resolution image (12K)](https://i.postimg.cc/h4sNWVFH/hubble-grid.jpg)" loading="lazy" >}}

* **Hubble types:** The system can generate different galaxy morphologies based on Hubble types. Whether you need a tightly wound spiral or a diffuse elliptical, the generator handles the math.
* **New generation UI:** We added a dedicated procedural generation window. It gives you direct control over "channels": individual components like the bulge, stars, HII regions, and dust. You can adjust particle counts, distribution patterns, and warp strength and see the results immediately.
* **Smart rendering:** We've improved the rendering performance too. We render some channels to lower-resolution buffers, and combined them with the full-resolution main buffer in a later stage.
* **Volume rendering:** We have built the infrastructure to handle volumes and ground them in the scene. We provide a sample shader as example.

{{< fig src="img/2026/02/galaxies-ui.jpg" link="/img/2026/02/galaxies-ui.jpg" class="fig-center fig-post" title="Generating a procedural galaxy with the new UI dialog." loading="lazy" >}}

## Physical light and shading
We spent a lot of time rewriting how light works in Gaia sky to make it follow real-world physics (PBR).
* **Energy conservation:** We moved to a Cook-Torrance model. This means that surfaces reflect light more accurately based on their material, and they won't appear unnaturally bright because the math now ensures that reflected light never exceeds the incoming light.
* **Better reflections:** The metallic/roughness workflow has been revisited. Metals look more like metals, and rougher surfaces scatter light more realistically.
* **Full PBR overhaul:** We've written new PBR shaders essentially from scratch.

## Performance and VR
* **OpenXR and instancing:** VR performance is much better now. We optimized how textures are attached to frame buffers and moved desktop mirroring to its own pass. We also started using instanced rendering for orbits and billboards, which significantly reduces the load on your VRAM.
* **VR demo mode:** If you are showing Gaia sky to others, you can enable the new demo mode. It simplifies the controls so a new user can't accidentally open menus or change settings while they are exploring.

## Other notable changes
* **New 3D anaglyph modes:** We've added new anaglyph modes: red/cyan Dubois-style, amber/blue, and amber/blue Dubois style. Improve regular red/cyan method with a separate gamma operation on each channel that boosts red and mutes green.
* **Interface colors:** You can now pick a custom accent color for the UI, which updates instantly.
* **Mirror support:** The startup process can check multiple server mirrors to find the fastest connection for data downloads. We're working on procuring at least an external mirror.
* **Atmospheric scattering:** The scattering math is now calculated per-pixel (fragment shader), which makes planetary atmospheres look better even on simpler 3D models.

For the full technical breakdown and a list of all bug fixes, check the [full changelog for 3.7.1](/downloads/releases/v3.7.1/#release-notes).

**You can grab the latest installer from the [downloads page](/downloads).**
