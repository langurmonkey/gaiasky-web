+++
title = "Gaia Sky 3.6.6"
description = "Performance improvements and bug fixes"
date = "2025-01-24T09:41:55Z"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 Today we publish the version 3.6.6 of Gaia Sky. This is a small update focused on fixing some bugs and improving performance. Also, it comes with proper handling of depth for volumes!

{{< vid src="vid/2025/3.6.6-release.mp4" poster="vid/2025/3.6.6-release.jpg" class="fig-center vid-post" title="The Trifid nebula (NGC6514) rendered as a volume with correct usage of the depth buffer." >}}

<!--more-->

## Features
- Move volumes earlier in the rendering pipeline, because they now write to the depth buffer.
- Check for dataset incompatibilities and ask user to confirm action when selecting incompatible datasets.
- Add window size and resolution of external view in settings, when the external view is active.

## Bug Fixes
- Attitude indicator not scaling with units-per-pixel value in spacecraft UI.
- Incorrect initialization of label threshold in volumes in VR mode.
- Entering panorama mode resets back-buffer scale. The issue was that the dynamic resolution reset routine was always applied, and not only when the dynamic resolution setting was on.

## Performance Improvements
- Replace arbitrary precision `add()` call with double-precision one to compute spherical coordinates of objects. Double-precision is more than sufficient for that purpose.

## Build System
- Update install4j template to version 11.

## Documentation
- Improve javadoc comments in settings class.

As always, you can grab it in the [downloads page]({{< ref "downloads" >}}).
