+++
title = "Gaia Sky 3.7.3"
description = "This version focuses on quality of life features and includes many bugfixes."
date = 2026-06-02
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

About a couple of months after the last release, today we are proud to announce **Gaia Sky 3.7.3**. This release focuses on quality-of-life features and on important bug fixes.

Here is a summary of what's new in this release:

- Complete redesign of "Load dataset" dialog.
- Improve file picker with proper history stack and more goodies.
- New line shading method based on screen-space derivatives.
- [PBR](@ "Physically Based Rendering") extensions to wavefront format.
- Improve index creation speed for particle and star sets.
- Fix breaking bug in 3.7.2 where model-based sets (e.g. star clusters) were not positioned correctly.

If you want to know more, keep reading.

<!--more-->

## Dataset loader

We have redesigned the load dataset dialog. Before, it included only a file picker which had to be pointed at a particular `dataset.json` file, or at a catalog file, to load a dataset.

We have now separated the dataset hot-loading dialog into two categories, represented by tabs:

- **Load installed dataset**: lists all installed (and not currently loaded) datasets and lets you load them on-demand.
- **Load file (.vot, .csv, etc.)**: the good old file picker to directly load catalog files.

{{< fig src="img/2026/06/load-dataset.jpg" link="/img/2026/06/load-dataset.jpg" width="30%" class="fig-center fig-post" title="The new 'Load dataset' dialog has two tabs for installed datasets and files." loading="lazy" >}}

We have also improved the layout of the datasets component, and added a shortcut to load datasets directly from within. We have added (optional) dataset type icons to the catalog descriptors, and they show up in the datasets component as well.

Dataset cards have received some love too. Apart from the icons, datasets can now have feature images. These are displayed in the dataset manager, and also in the dataset information pane.

{{< fig src="img/2026/06/dataset-images-thumb.jpg" link="/img/2026/06/dataset-images.jpg" class="fig-center fig-post" title="The new Gaia mission dataset, featuring some dataset images, in the dataset manager." loading="lazy" >}}

Mission datasets can now be 'selected' via a special action. Selecting a mission dataset sets the time to the start of the mission and focuses the camera on the spacecraft. We have reorganized most missions into mission datasets, and we have extracted the Gaia mission from the base data pack to its own dataset.
## File picker

We have added a proper history stack to the file picker. Also, we have done a little bit of refactoring in order to extract it as a reusable component outside of the default generic dialog. This way, it can be added to the abovementioned Load dataset dialog, and still be used as a standalone dialog.

## Rendering

We have updated the default line rendering shader to a method that uses screen-space derivatives instead of a power function for higher quality line rendering. This produces pixel-perfect line edges at all line width settings and in all screen resolutions.

  {{< fig src="img/2026/06/line-comparison-thumb.jpg" link="/img/2026/06/line-comparison.jpg" class="fig-center fig-post" title="The old glow-based lines (left), and the new derivative-based lines (right)." loading="lazy" >}}

  
Additionally, we added limb fade to the cloud layers, also based on screen-space pixel counts. This prevents cloud layers from appearing overly flat at the edges of planets.

We have added PBR support in wavefront `.mtl` material files via common extensions. For instance, one of those handles packed PBR textures (occlusion, roughness, metallic) as `map_PBR`. Still in materials, we added intrinsic opacity to materials, and used it in the default model sorter for proper transparency ordering. This enables proper glass rendering, like in the windows of the Orion capsule in the Artemis mission.

## User interface and formats

There have been a number of improvements in the user interface:

- The Japanese translation is now fully complete. It has been proofread and edited by our newest contributor, Hiromasa Yauchi.
- We added a generic updater helper to dispatch update events. This enables using callbacks in the star and particle loaders for proper progress reporting during loading.
- Finally, we added support for *camelCase* names in dataset description properties (e.g., `nObjects`, `numObjects`, `sizeBytes`, `releaseNotes`).

## Bug fixes

Here are some of the most important bugfixes in this release.

- Fix crash caused by asterisks in Windows paths when the shader cache is enabled.
- Add a scroll pane to the datasets component, which could grow beyond screen bounds.
- Consolidate the parser used in the color picker to avoid inconsistent accepted formats that led to a crash.
- Shader positioning bugs in model-based particle sets (e.g. star clusters).
- Fix expanding/collapsing dataset widgets to resize the scroll pane and component pane correctly.
- Fix double index initialization issue in star and particle groups loaded on the fly.
- Ensure the bookmarks manager has an up-to-date bookmark list before reloading the component view.
- Fix uninitialized star textures in the main post-processor reload caused by a settings bookmark.

## Performance improvements

We have improved the indexing speed of particle and star groups by rewiring the way in which object name translations are queried and fetched.

## More

See the [full changelog for 3.7.3](/downloads/releases/v3.7.3/#release-notes) for the full list of features, fixes, and more.

**You can grab the latest installer from the [downloads page](/downloads).**
