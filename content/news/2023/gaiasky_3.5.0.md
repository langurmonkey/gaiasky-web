+++
title = "Gaia Sky 3.5.0"
date = "2023-07-17T15:15:00"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 Gaia Sky 3.5.0 available now!

<!--more-->


## Features
- add control for maximum number of velocity vectors per star set in preferences dialog, performance section.
- add CLI flag to force HiDPI mode either to 'Logical' or 'Pixels'.
- enable holding comma or period to slow down or speed up time. Map time speed up and slow down to d-pad up and down in game controllers.
- add `trailMinOpacity` to trajectories. This raises the opacity of a trail to the given minimum value.
- speeding up and slowing down time can be done by pressing and holding '.' and ',' respectively. No more frantically clicking a key. Also, the time warp change is smooth now.
- add camera position/orientation named bookmarks, additionally to the already existing object bookmarks. Add bookmarks for many eclipses in the default bookmarks.txt.
- use coordinates provider from objects to sample periodic orbits instead of hardcoded algorithms.
- dim atmosphere w.r.t. camera, star and eclipsing body positions during eclipses.
- initial support for ephemeris based on Chebyshev polynomials.
- add support for VSOP2000.
- add eclipses by projecting the shadow umbra and penumbra from moons to planets and vice-versa. The option to outline the umbra and penumbra is given as a checkbox in the preferences. Eclipses can be deactivated, also from the preferences window, graphics tab.
- celestial sphere showcase script
- add a few showcase scripts
- scripts showing an object on a horseshoe orbit around Jupiter
- update wording on point and line styles in preferences dialog to make it more concise and clear.
- use GPU lines as the default line renderer for trajectories. This results in a big performance improvement, especially when many lines are on display. GPU lines now also can use the geometry shader to render as polyline quad-strips.
- use a geometry shader to generate the triangles in the polyline quadstrip renderer instead of the CPU. Performance is much improved.
- add geometry shader stage (optional) to shader program provider and to extended shader program.
- add alpha value to color map in the dataset highlight color picker.
- adapt star cluster loader to use the new extended particle set features by default.
- enable arbitrary models rendered with instancing in extended particle sets.
- add extended particle sets. These support, in addition to positions, proper motions and sizes. They also can be rendered with icosahedron sphere models instead of quads. Add lazy initialization of render systems.
- enable labels for regular particle sets.
- improve unsharp mask shader to produce much cleaner and useful results.
- remove non-instanced triangles mode (and renderers); they are a waste of memory and almost never faster than the instanced version. Use screen-aligned billboards in regular mode, and scene-aligned ones in any of the cubemap modes (360, planetarium, etc.).
- add support for texture arrays in particle sets. Particle sets can now define a group of texture files taht will be applied to the particles at random.
- activate v-sync by default during welcome and loading GUI (not in VR). Use busy wait to lock to the perfect target FPS, when active.
- add maximum allowed distance as a hard limit, set at 50 Gpc, roughly twice the size of the observable universe.
- top info interface date and time elements are clickable, and display the date/time edit dialog.
- migrate VR version to OpenXR API.
- add arbitrary warping mesh support to distor the final image according to a warping mesh file in PFM (portable float map) format.
- replace lens flare checkbox with lens flare strength slider.
- enable choosing the lens flare type (pseudo lens flare, real lens flare) in the settings. Make new lens flare the default.
- proper lens flare post-processing effect.
- add maximum number of virtual texture tile load operations per frame to settings file, and increase its default value from 3 to 8. Use a deque instead of a queue for the tiles waiting to be loaded, and add the newly observed tiles to the head instead of the tail.
- increase chromatic aberration amount in lens flare effect.
- add variations of API calls concerning positions using the distance units as an extra parameter.
- move archetypes definition to JSON file to facilitate the automatic generation of documentation.
- move attribute map definition to JSON file, which contains the definitions of all the attributes per component, and also a description for each of them. The aim is to generate part of the data format documentation from this JSON file.
- enable implementing body coordinates directly from Python scripts. Add new API calls and a full script example with data files.
- expose upscale filter setting to UI via a select box in the preferences window.
- add chromatic aberration shader, together with a slider in the preferences window to disable it or control the amount.
- enable proper motion for single particles, fix issues with tracking.
- add support for ambient occlusion sampler (standalone and with metallic and roughness channels) in PBR normal and tessellation shaders.
- add (partial) support for glTF, binary glTF and embedded glTF.
- add (hidden) attribute "renderParticles" to star and particle sets to disable the rendering of particles and stars for that set.
- add aliases to label position for pc and Km, remove unnecessary operations from shape updater.
- add keyboard mapping and action to multiply the camera movement speed (mapped to 'Z' by default).
- add actions and key bindings to toggle the camera mode and the cinematic behaviour.
- support translation in Km with the 'translateKm' attribute.
- directly support archetype names in JSON data format, additionally to the legacy class names.
- enable affine transformation support for shape objects.
- support 'standard' PBR attributes in OBJ loader.
- add warp mesh file selector to preferences, to select the warping mesh for the new spherical mirror projection. Fix layout for file choosers in frame and screenshot locations.
- add support for the spherical mirror projection in planetarium mode.
- add upscale filter setting to preferences, add XBRZ upscale shader, filter and effect.
- non user-prompted events (download fail, checkum error, etc.) create persistent notifications which need to be closed manually. Persistent notifications are accompanied with a close button to indicate they need to be closed manually.
- add parallax demo script.
- separate height scale from elevation multiplier in shaders. Decrease step of some sliders.
- enable arbitrary parameter map injection in data loaders.
- add `fadeDistanceUp` and `fadeDistanceDown` to trajectory objects to control the fading distances when a body is present.
- add animations to all UI elements, add animation time to settings.
- add in/out animations to gamepad GUI and maximize/minimize to debug and focus interfaces. Add animation time as a new setting in settings file. Promote date dialog to generic dialog.
- add size attribute to ray-marching effects, enable absolute predicted positions for ray-marching effects, instead of only a static position.
- add per-vertex colors (instead of per-segment) to polyline quadstrip renderer for smooth shading.
- add shortcut to settings in context menu.
- more on input.
- first OpenXR test, not working on Linux over SteamVR due to unsupported swapchain formats.
- add ambient level and color to individual models.
- add 'fixed angular size' support for star datasets. It renders all stars with a fixed angular size. In the case of variable stars, if a fixed angular size is set, the variability is expressed via the opacity.

## Bug Fixes
- correctly initialize camera focus and mode at gamepad/VR GUI creation.
- restore functionality in archive/DB information window when selecting stars.
- restore functionality of location log, lost in a regression during the ECS refactoring.
- star set labels respect label fading factor.
- move Gaia Sky logo over the title in help window.
- 'cancel download' catalan and spanish translation texts.
- roughness and metallic colors and textures not being set correctly in wavefront loader.
- look-up table paths in procedural generation window.
- regression in go-to command with star and particle groups.
- check for empty configuration file at startup and overwrite it if necessary.
- orientation locking does not work in backwards time. Fixes [#718](https://codeberg.org/gaiasky/gaiasky/issues/718).
- bump default safe mode OpenGL version to 3.3 to support instancing. GPUs from 2007 support it, so it should be safe. Also, do not attempt to compile double-precision geometry shaders in safe mode, since they are not used and may crash anyways.
- line trail mapping in non-timestamped trajectories. Fixes [#715](https://codeberg.org/gaiasky/gaiasky/issues/715).
- double-rebuilding of dataset manager on close. Also, closing the dataset manager does not persist the preferences.
- shader version for normal shader from 410 to 330 to prevent crashes in old GPUs.
- regression in texture binding introduced in 3.5.0-RC3 (commit 7db456cc).
- adjust rotate/turn strength when using the arrow keys.
- random bugs in label render system.
- do not show collapse/expand buttons in collapsible windows if collapsing is disabled.
- wrong key used in galactic latitude attribute in color map picker.
- input multiplexer and welcome GUI initialization sequence may cause a startup crash in certain conditions.
- initialization sequence for distance scale factor, and particle groups breaking in VR when using triangles.
- do not skip processing of LOD-based object when it is the current camera focus.
- adjust visibility and opacity determination for entities with active fade in map; mostly used for NEARGALCAT objects.
- spread GPU streaming of multi-component billboard datasets over several frames.
- billboard set texture array uniform setting.
- pixel-perfect interaction in VR menus. Surface normal was being transformed with a matrix that contained a translation instead of only using rotations.
- properly scale particle set particles in VR.
- proper motions in VR mode.
- interactive load of JSON datasets that contain objects with 3D models blocks main thread.
- guard in `getLineObject()` calls with a timeout does not use the time out. Fixes [#711](https://codeberg.org/gaiasky/gaiasky/issues/711).
- scale orbit element particles for VR, readjust size limits.
- slider texture filtering issue in green, blue, orange and red themes.
- star surface shader crash when motion blur is on.
- non-canonical OpenGL parameters in some configuration calls.
- headless mode crashes on start.
- star billboard and quad positions in stereo mode.
- absolute position method in particle set does not guard against null parameters. Fixes [#710](https://codeberg.org/gaiasky/gaiasky/issues/710).
- dataset manager layout, especially on low-resolution displays.
- move hardcoded billboard galaxy threshold to model initializer.
- single star rendering from afar, spherical position determination, graph update sequence for proper motion and other objects, bypass area and loc update when components are off, camera position lock for stars in star sets.
- several issues with single star rendering and magnitude initialization.
- add mechanism to automatically disable certain post-processing effects on certain render modes (e.g. light glow on panorama/planetarium mode).
- internal dataset loading operations out of order: move scene graph insertion before set-up.
- enable model-less shape objects for label-only use cases.
- removing objects with children only effectively removes the first children, leaving orphan objects in the scene graph which do not get updated but get added to the render lists.
- removal of an object from the graph does not remove its children.
- normals, bi-normals and tangents in icosphere creator.
- crash with static light models, file filter in dataset loader.
- cloud virtual textures not working due to missing shader attribute.
- crash loading wrongly constructed cluster file.
- trail attribute of orbits not always working. GPU non-trail orbits not working.

## Performance Improvements
- improve performance of velocity vectors in LOD datasets by setting restrictions on the octant's solid angle before sending the star sets to the velocity vector renderer.
- remove guard clauses in shader interpolation function that are already covered by `smoothstep()`.
- distribute SVT render pass over 5 frames to split contribution over time and achieve more or less constant frame pacing.

## Code Refactoring
- set 'useColor' in models to false by default, so that the object color is not passed to the 3D model unless explicitly stated.
- remove dpendency on gdx-gltf, implement own modification which directly loads meshes using 32-bit integer indices instead of 16-bit shorts.
- rename some classes to make them more concise. Fix and improve javadoc comments.
- consolidate shader and resource disposing in post processors.
- unify tessellation and regular shader infrastructure.
- trigger star/particle set update task in updater systems instead of via the camera motion event. Shorten minimum times between metadata updates.
- move particle and star set updater methods to consumers initialized at creation.
- rename all math utilities converted from single to double precision from [name]d to [name]Double.
- use solid angle component instead of hardcoded variables for star cluster thresholds.
- move 'forceLabel' attribute to Label component.

## Build System
- AUR package dependency from `jre-openjdk` to `java-runtime`.
- update bundled JRE to 20.0.1, update installer welcome image.
- upgrade to LibGDX 1.12.0.
- update build file tasks to latest gradle syntax recommendations.
- update oshi-core from 5.8.7 to 6.4.1.
- remove commons-math3 dependency by implementing own interpolator.
- update STIL from 4.0.+ to 4.1.+, and Jackson from 2.13.2 to 2.15.+.
- remove dependency on commons-imaging library for monochrome to RGB conversions.
- update JCommander from 1.81 to 1.82; upgrade slf4j-nop from 1.7.+ to 2.0.+.
- remove JPEG-XL support via external library (vavi-image), better wait for official support in Java Image I/O.
- upgrade LWJGL version from 3.3.1 to 3.3.2.
- improve format of release notes file in template.
- upgrade to Gradle 8.1.1.

## Documentation
- started writing test protocol document.
- add package descriptions to all packages except for the `gaiasky.util` children.
- add package descriptions, refactor API interfaces to own packages.
- improve documentation of some API calls.
- update AppStream metadata file with proper id and screenshots.

## Style
- update style with new hard wrap length and new wrapping rules for function signature parameters.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.5.0.5b427a04f/).