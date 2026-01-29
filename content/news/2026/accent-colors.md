---
title: "Dynamic UI accent colors"
description: "Shader-based UI accent colors will replace static UI themes in the next release of Gaia Sky."
date: 2026-01-29
author: "tsagrista"
tags: ["development", "ui", "shaders"]
category: "Features"
---

For years, Gaia Sky's UI themes have been completely static: each theme required its own set of pre-rendered source images. Want a different color scheme? You'd need an entirely new theme with separately generated assets.

Not anymore.

For the next release, we've implemented a new theming system by creating a single base theme with purple motifs and applying runtime color transformation through shaders. The new system converts purple elements to any accent color you choose, all happening in real-time on the GPU. The old "Theme" property in the preferences window has been replaced with an "Accent color" color picker, as demonstrated in the video below.

{{< vid src="vid/2026/ui-accent-colors.mp4" poster="vid/2026/ui-accent-colors.jpg" class="fig-center vid-post" title="Switching accent colors in real time in the Gaia Sky UI." >}}

The magic happens in the fragment shader, which analyzes each pixel's color, extracts the purple hue and brightness values, and blends them with your chosen accent color using weighted averages. The result are smooth, natural-looking color transitions that preserve the original design's depth.

This shader-based approach is not only more flexible but also lets us focus on a single theme without having to update multiple places whenever something changes.
