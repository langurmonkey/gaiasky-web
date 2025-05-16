+++
title = "Gaia Sky 3.3.0"
date = "2022-11-11T11:05:00"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 Gaia Sky 3.3.0 available now!

<!--more-->


## Code Refactoring
- The largest change in this version by far is the complete refactoring of the internal model. We have moved from an object-oriented inheritance hierarchy to an entity component system (ECS).
- Move render lists to Java collections.
- Flatten object hierarchy by removing some classes, merging their functionality upwards.
- Abstract attitude loading system, remove Gaia class, use heliotropic satellite.
- Add `I18nFormatter` to reformat i18n files.
- Remove old date formatting infrastructure (desktop, html, mobile) in favor of a direct approach.
- Remove useless number formatting infrastructure.

## Features
- Enable minimizing focus info interface.
- Adjust debug interface layout.
- Key bindings file versioning. If the key bindings file starts with the line `#v[version]`, that version is compared to the default one and overwritten when necessary. That makes updating key bindings much easier.
- Recompute UI scale at startup when starting with default config file.
- Add back-buffer scale API call.
- Add back-buffer scale controls to UI.
- Add repository to `-v` information.
- Rename fisheye post-processing effect and shader to reprojection. Update cubemap projection from fisheye to azimuthal equidistant.
- Add shaders for Lambert equal-area, orthographic and stereographic projections.
- Add re-projection GUI drop-down in preferences window. Add `setReprojectionMode()` scripting API call.
- Include orthographic projection in panorama mode. Includes both hemispheres on the screen, side by side. Can be cycled through with `ctrl`+`shift`+`k`.
- Include "orthosphere" panorama mode -- orthospherical projection with both hemispheres overlaid to give a view of the celestial sphere from the outside.
- Add new camera mode, orthosphere view, which includes the regular and the cross-eye orthosphere projections.
- Add cross-eye view of the orthographic projection of the celestial sphere.
- Add support for KTX and ZKTX textures.
- Change from thread to scheduled task to remove the mode change info pop-up.
- Add mode change pop-up setting to enable or disable showing a pop-up with information when changing modes (panorama, planetarium, stereo, etc.).
- Add GUI button to exit stereo mode.
- Add new object type, 'cosmic locations', to mark the positions of interesting areas or regions.
- Enable scene lights for shape objects when static light is off.
- New model attribute 'blendMode', which defaults to 'alpha' but can also be set to 'additive' to control the object blending.
- Enable gamepad operation in welcome GUI.
- Add zero-point to gamepad configuration.
- Introduce gamepad support for spacecraft mode, remove 'Gaia scene' camera mode (can be mimicked with focus mode), refactor input controllers, fix default SDL gamepad mappings file.
- Add several new functions to enable setting the camera state from scripts.
- Add time zone to settings. Time zone can be either UTC, or the system default. Update date dialog year limits, fix time component layout.
- Adapt raymarching effects work with ECS model.
- Light glow effect now works with ECS model.
- Expose post-processor properties as settings in configuration file.
- Save configuration when closing dataset manager window.
- Add popup notice when opening the keyframes window if component 'others' is not visible.
- Add full screen bit depth and refresh rate to fully qualify selected full screen modes.
- Improve layout and information of crash window.
- Add notice when there are no datasets.

## Bug Fixes
- Disable tessellation on macOS by default.
- Bug in latest version determination in version checker.
- Remove unnecessary spacing in layout of focus info interface.
- Trajectory size determination algorithm not accurate, breaks when adding points close to the origin.
- Add model size attribute to compute solid angle for model objects more accurately.
- Correctly query graphics device for resolution and apply scaling.
- Toggling SSR and motion blur does not update depth state in some shaders.
- Double definitions in shader libraries.
- Render constellation boundaries as closed polygons in order to avoid artifacts.
- Index errors in keybaord in controller GUI.
- Back-buffer scale is now applied correctly (and only once), works with external view.
- Remove angle from zenith from cubemap renderer in planetarium, use shader-based solution.
- Prevent rendering titles if panorama mode is on.
- Initialize position from coordinates object during initialization phase.
- Land at location never returns. [#674](https://codeberg.org/gaiasky/gaiasky/issues/674).
- Set foucs with `FocusView` object type. [#671](https://codeberg.org/gaiasky/gaiasky/issues/671).
- Provide a correct index mapping for arbitrary attributes with string values.
- Particle size of interactively loaded point cloud datasets.
- Vertically flip UV coordinates of two-faced billboard to correct texture orientation.
- Regression in billboard group rendering. [#663](https://codeberg.org/gaiasky/gaiasky/issues/663).
- Update coordinates in invisible only when present. [#662](https://codeberg.org/gaiasky/gaiasky/issues/662).
- Prevent runtime error due to non-invertible matrix in spacecraft entity.
- Diffuse color contribution calculated incorrectly when nLights > 1 in normal shaders.
- Names in star groups can now be localized, fix focus name in panel.
- Translate strings of filters, shapes, datasets and minimap. [#403](https://codeberg.org/gaiasky/gaiasky/issues/403).
- Moon orbits are recomputed more often.
- Filters crash with instanced star renderers.
- Modal windows made not collapsible by default.
- Hotkey tooltip backgrounds.
- Jump in Pluto's orbit due to deviation between full periods.
- Highlight 'all visible' setting in quad-based star renderers.
- Frame sequence number synchronized, value updated when opening preferences.
- Use view angle instead of view angle apparent in go to object API call.
- Increase number of vertices of minimap shape renderer, fixes crash in heliosphere minimap.
- Typo in Jupiter English translation file, add meshes to data descriptor file.
- Break link in dataset manager if too long.
- Make sure direction and up vectors are orthogonal in camera transition call.
- Increase size star point buffer when needed.
- Null-check satellite attitude before getting quaternion. [#402](https://codeberg.org/gaiasky/gaiasky/issues/402).
- Empty tips may crash Gaia Sky at startup.
- 'add scene graph object' event missing source object. [#400](https://codeberg.org/gaiasky/gaiasky/issues/400).
- Remove phase of pi radians in default-model orbital elements.
- Regression with libgdx 1.11.0 that caused vertical tooltips.
- Null-check settings in crash reporter.
- Workaround for libgdx backslash bug in asset manager. Fixes [#398](https://codeberg.org/gaiasky/gaiasky/issues/398).
- Hide system cursor correctly with GLFW until libgdx 1.10.1 is released.
- Use minimum width for debug interface to prevent dynamic resizing depending on content.

## Build System
- Move repository from Gitlab to Codeberg.
- Update Gitlab references to Codeberg, when possible. Use Codeberg API for version checking.
- Update changelog template repository to Codeberg.
- Remove Gitlab CI file.
- Extract documentation to own project, which is no longer a submodule.
- Upgrade to libgdx 1.11.0 and LWJGL 3.3.1 --- this adds M1 Mac support.
- Add aarch64 JRE to macOS bundle for M1 machines. Move to macOS single bundle archive from deprecated old single bundle.
- Force safe graphics mode on M1 macOS.
- Use default GC (G1) in favor of Shenandoah (only LTS).
- Upgrade gradle wrapper version to 7.5.1.

## Documentation
- Update repository pointers to Codeberg.
- Update in-app mastodon reference from cat to social, as it's in English.
- Remove twitter link, add mastodon hashtag.
- Improve comments on color maps GLSL code.
- Add new panorama orthographic projection to API Javadocs.
- Remove wrong license (leftover from old copy-paste) in fisheye fragment shader code.
- Add contributor.
- Typos and so.

## Style
- Mend variable names in about window to follow camel case.
- Fix linter stylistic warnings in GUI and interfaces.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.3.0.aca9fadc2/).