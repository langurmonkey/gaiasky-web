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
- the largest change in this version by far is the complete refactoring of the internal model. We have moved from an object-oriented inheritance hierarchy to an entity component system (ECS).
- move render lists to Java collections. 
- flatten object hierarchy by removing some classes, merging their functionality upwards. 
- abstract attitude loading system, remove Gaia class, use heliotropic satellite. 
- add `I18nFormatter` to reformat i18n files. 
- remove old date formatting infrastructure (desktop, html, mobile) in favor of a direct approach. 
- remove useless number formatting infrastructure. 

## Features
- enable minimizing focus info interface.
- adjust debug interface layout. 
- key bindings file versioning. If the key bindings file starts with the line `#v[version]`, that version is compared to the default one and overwritten when necessary. That makes updating key bindings much easier. 
- recompute UI scale at startup when starting with default config file.
- add back-buffer scale API call. 
- add back-buffer scale controls to UI. 
- add repository to `-v` information. 
- rename fisheye post-processing effect and shader to reprojection. Update cubemap projection from fisheye to azimuthal equidistant. 
- add shaders for Lambert equal-area, orthographic and stereographic projections. 
- add re-projection GUI drop-down in preferences window. Add `setReprojectionMode()` scripting API call. 
- include orthographic projection in panorama mode. Includes both hemispheres on the screen, side by side. Can be cycled through with `ctrl`+`shift`+`k`. 
- Include "orthosphere" panorama mode -- orthospherical projection with both hemispheres overlaid to give a view of the celestial sphere from the outside. 
- add new camera mode, orthosphere view, which includes the regular and the cross-eye orthosphere projections. 
- add cross-eye view of the orthographic projection of the celestial sphere 
- add support for KTX and ZKTX textures. 
- change from thread to scheduled task to remove the mode change info pop-up. 
- add mode change pop-up setting to enable or disable showing a pop-up with information when changing modes (panorama, planetarium, stereo, etc.). 
- add GUI button to exit stereo mode. 
- add new object type, 'cosmic locations', to mark the positions of interesting areas or regions. 
- enable scene lights for shape objects when static light is off. 
- new model attribute 'blendMode', which defaults to 'alpha' but can also be set to 'additive' to control the object blending. 
- enable gamepad operation in welcome GUI. 
- add zero-point to gamepad configuration. 
- introduce gamepad support for spacecraft mode, remove 'Gaia scene' camera mode (can be mimicked with focus mode), refactor input controllers, fix default SDL gamepad mappings file. 
- add several new functions to enable setting the camera state from scripts. 
- add time zone to settings. Time zone can be either UTC, or the system default. Update date dialog year limits, fix time component layout. 
- adapt raymarching effects work with ECS model. 
- light glow effect now works with ECS model. 
- expose post-processor properties as settings in configuration file. 
- save configuration when closing dataset manager window. 
- add popup notice when opening the keyframes window if component 'others' is not visible. 
- add full screen bit depth and refresh rate to fully qualify selected full screen modes. 
- improve layout and information of crash window. 
- add notice when there are no datasets. 

## Bug Fixes
- disable tessellation on macOS by default. 
- bug in latest version determination in version checker. 
- remove unnecessary spacing in layout of focus info interface. 
- trajectory size determination algorithm not accurate, breaks when adding points close to the origin. 
- add model size attribute to compute solid angle for model objects more accurately. 
- correctly query graphics device for resolution and apply scaling. 
- toggling SSR and motion blur does not update depth state in some shaders. 
- double definitions in shader libraries. 
- render constellation boundaries as closed polygons in order to avoid artifacts. 
- index errors in keybaord in controller GUI. 
- back-buffer scale is now applied correctly (and only once), works with external view. 
- remove angle from zenith from cubemap renderer in planetarium, use shader-based solution. 
- prevent rendering titles if panorama mode is on. 
- initialize position from coordinates object during initialization phase. 
- land at location never returns. [#674](https://codeberg.org/gaiasky/gaiasky/issues/674) 
- set foucs with `FocusView` object type. [#671](https://codeberg.org/gaiasky/gaiasky/issues/671) 
- provide a correct index mapping for arbitrary attributes with string values. 
- particle size of interactively loaded point cloud datasets. 
- vertically flip UV coordinates of two-faced billboard to correct texture orientation. 
- regression in billboard group rendering. [#663](https://codeberg.org/gaiasky/gaiasky/issues/663) 
- update coordinates in invisible only when present. [#662](https://codeberg.org/gaiasky/gaiasky/issues/662) 
- prevent runtime error due to non-invertible matrix in spacecraft entity. 
- diffuse color contribution calculated incorrectly when nLights > 1 in normal shaders. 
- names in star groups can now be localized, fix focus name in panel. 
- translate strings of filters, shapes, datasets and minimap. [#403](https://codeberg.org/gaiasky/gaiasky/issues/403) 
- moon orbits are recomputed more often. 
- filters crash with instanced star renderers. 
- modal windows made not collapsible by default. 
- hotkey tooltip backgrounds. 
- jump in Pluto's orbit due to deviation between full periods. 
- highlight 'all visible' setting in quad-based star renderers. 
- frame sequence number synchronized, value updated when opening preferences. 
- use view angle instead of view angle apparent in go to object API call. 
- increase number of vertices of minimap shape renderer, fixes crash in heliosphere minimap. 
- typo in Jupiter English translation file, add meshes to data descriptor file. 
- break link in dataset manager if too long. 
- make sure direction and up vectors are orthogonal in camera transition call. 
- increase size star point buffer when needed. 
- null-check satellite attitude before getting quaternion. [#402](https://codeberg.org/gaiasky/gaiasky/issues/402) 
- empty tips may crash Gaia Sky at startup. 
- 'add scene graph object' event missing source object. [#400](https://codeberg.org/gaiasky/gaiasky/issues/400) 
- remove phase of pi radians in default-model orbital elements. 
- regression with libgdx 1.11.0 that caused vertical tooltips. 
- null-check settings in crash reporter. 
- workaround for libgdx backslash bug in asset manager. Fixes [#398](https://codeberg.org/gaiasky/gaiasky/issues/398) 
- hide system cursor correctly with GLFW until libgdx 1.10.1 is released. 
- use minimum width for debug interface to prevent dynamic resizing depending on content. 

## Build System
- move repository from Gitlab to Codeberg.
- update Gitlab references to Codeberg, when possible. Use Codeberg API for version checking. 
- update changelog template repository to Codeberg. 
- remove Gitlab CI file. 
- extract documentation to own project, which is no longer a submodule. 
- upgrade to libgdx 1.11.0 and LWJGL 3.3.1 --- this adds M1 Mac support. 
- add aarch64 JRE to macOS bundle for M1 machines. Move to macOS single bundle archive from deprecated old single bundle. 
- force safe graphics mode on M1 macOS. 
- use default GC (G1) in favor of Shenandoah (only LTS). 
- upgrade gradle wrapper version to 7.5.1. 

## Documentation
- update repository pointers to Codeberg. 
- update in-app mastodon reference from cat to social, as it's in English. 
- remove twitter link, add mastodon hashtag. 
- improve comments on color maps GLSL code. 
- add new panorama orthographic projection to API Javadocs. 
- remove wrong license (leftover from old copy-paste) in fisheye fragment shader code. 
- add contributor.
- typos and so. 

## Style
- mend variable names in about window to follow camel case. 
- fix linter stylistic warnings in GUI and interfaces. 

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.3.0.aca9fadc2/).