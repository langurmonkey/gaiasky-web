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
- Add control for maximum number of velocity vectors per star set in preferences dialog, performance section.
- Add CLI flag to force HiDPI mode either to 'Logical' or 'Pixels'.
- Enable holding comma or period to slow down or speed up time. Map time speed up and slow down to d-pad up and down in game controllers.
- Add `trailMinOpacity` to trajectories. This raises the opacity of a trail to the given minimum value.
- Speeding up and slowing down time can be done by pressing and holding '.' and ',' respectively. No more frantically clicking a key. Also, the time warp change is smooth now.
- Add camera position/orientation named bookmarks, additionally to the already existing object bookmarks. Add bookmarks for many eclipses in the default bookmarks.txt.
- Use coordinates provider from objects to sample periodic orbits instead of hardcoded algorithms.
- Dim atmosphere w.r.t. camera, star and eclipsing body positions during eclipses.
- Initial support for ephemeris based on Chebyshev polynomials.
- Add support for VSOP2000.
- Add eclipses by projecting the shadow umbra and penumbra from moons to planets and vice-versa. The option to outline the umbra and penumbra is given as a checkbox in the preferences. Eclipses can be deactivated, also from the preferences window, graphics tab.
- Celestial sphere showcase script.
- Add a few showcase scripts.
- Scripts showing an object on a horseshoe orbit around Jupiter.
- Update wording on point and line styles in preferences dialog to make it more concise and clear.
- Use GPU lines as the default line renderer for trajectories. This results in a big performance improvement, especially when many lines are on display. GPU lines now also can use the geometry shader to render as polyline quad-strips.
- Use a geometry shader to generate the triangles in the polyline quadstrip renderer instead of the CPU. Performance is much improved.
- Add geometry shader stage (optional) to shader program provider and to extended shader program.
- Add alpha value to color map in the dataset highlight color picker.
- Adapt star cluster loader to use the new extended particle set features by default.
- Enable arbitrary models rendered with instancing in extended particle sets.
- Add extended particle sets. These support, in addition to positions, proper motions and sizes. They also can be rendered with icosahedron sphere models instead of quads. Add lazy initialization of render systems.
- Enable labels for regular particle sets.
- Improve unsharp mask shader to produce much cleaner and useful results.
- Remove non-instanced triangles mode (and renderers); they are a waste of memory and almost never faster than the instanced version. Use screen-aligned billboards in regular mode, and scene-aligned ones in any of the cubemap modes (360, planetarium, etc.).
- Add support for texture arrays in particle sets. Particle sets can now define a group of texture files taht will be applied to the particles at random.
- Activate v-sync by default during welcome and loading GUI (not in VR). Use busy wait to lock to the perfect target FPS, when active.
- Add maximum allowed distance as a hard limit, set at 50 Gpc, roughly twice the size of the observable universe.
- Top info interface date and time elements are clickable, and display the date/time edit dialog.
- Migrate VR version to OpenXR API.
- Add arbitrary warping mesh support to distor the final image according to a warping mesh file in PFM (portable float map) format.
- Replace lens flare checkbox with lens flare strength slider.
- Enable choosing the lens flare type (pseudo lens flare, real lens flare) in the settings. Make new lens flare the default.
- Proper lens flare post-processing effect.
- Add maximum number of virtual texture tile load operations per frame to settings file, and increase its default value from 3 to 8. Use a deque instead of a queue for the tiles waiting to be loaded, and add the newly observed tiles to the head instead of the tail.
- Increase chromatic aberration amount in lens flare effect.
- Add variations of API calls concerning positions using the distance units as an extra parameter.
- Move archetypes definition to JSON file to facilitate the automatic generation of documentation.
- Move attribute map definition to JSON file, which contains the definitions of all the attributes per component, and also a description for each of them. The aim is to generate part of the data format documentation from this JSON file.
- Enable implementing body coordinates directly from Python scripts. Add new API calls and a full script example with data files.
- Expose upscale filter setting to UI via a select box in the preferences window.
- Add chromatic aberration shader, together with a slider in the preferences window to disable it or control the amount.
- Enable proper motion for single particles, fix issues with tracking.
- Add support for ambient occlusion sampler (standalone and with metallic and roughness channels) in PBR normal and tessellation shaders.
- Add (partial) support for glTF, binary glTF and embedded glTF.
- Add (hidden) attribute "renderParticles" to star and particle sets to disable the rendering of particles and stars for that set.
- Add aliases to label position for pc and Km, remove unnecessary operations from shape updater.
- Add keyboard mapping and action to multiply the camera movement speed (mapped to 'Z' by default).
- Add actions and key bindings to toggle the camera mode and the cinematic behaviour.
- Support translation in Km with the 'translateKm' attribute.
- Directly support archetype names in JSON data format, additionally to the legacy class names.
- Enable affine transformation support for shape objects.
- Support 'standard' PBR attributes in OBJ loader.
- Add warp mesh file selector to preferences, to select the warping mesh for the new spherical mirror projection. Fix layout for file choosers in frame and screenshot locations.
- Add support for the spherical mirror projection in planetarium mode.
- Add upscale filter setting to preferences, add XBRZ upscale shader, filter and effect.
- Non user-prompted events (download fail, checkum error, etc.) create persistent notifications which need to be closed manually. Persistent notifications are accompanied with a close button to indicate they need to be closed manually.
- Add parallax demo script.
- Separate height scale from elevation multiplier in shaders. Decrease step of some sliders.
- Enable arbitrary parameter map injection in data loaders.
- Add `fadeDistanceUp` and `fadeDistanceDown` to trajectory objects to control the fading distances when a body is present.
- Add animations to all UI elements, add animation time to settings.
- Add in/out animations to gamepad GUI and maximize/minimize to debug and focus interfaces. Add animation time as a new setting in settings file. Promote date dialog to generic dialog.
- Add size attribute to ray-marching effects, enable absolute predicted positions for ray-marching effects, instead of only a static position.
- Add per-vertex colors (instead of per-segment) to polyline quadstrip renderer for smooth shading.
- Add shortcut to settings in context menu.
- More on input.
- First OpenXR test, not working on Linux over SteamVR due to unsupported swapchain formats.
- Add ambient level and color to individual models.
- Add 'fixed angular size' support for star datasets. It renders all stars with a fixed angular size. In the case of variable stars, if a fixed angular size is set, the variability is expressed via the opacity.

## Bug Fixes
- Correctly initialize camera focus and mode at gamepad/VR GUI creation.
- Restore functionality in archive/DB information window when selecting stars.
- Restore functionality of location log, lost in a regression during the ECS refactoring.
- Star set labels respect label fading factor.
- Move Gaia Sky logo over the title in help window.
- 'cancel download' catalan and spanish translation texts.
- Roughness and metallic colors and textures not being set correctly in wavefront loader.
- Look-up table paths in procedural generation window.
- Regression in go-to command with star and particle groups.
- Check for empty configuration file at startup and overwrite it if necessary.
- Orientation locking does not work in backwards time. Fixes [#718](https://codeberg.org/gaiasky/gaiasky/issues/718).
- Bump default safe mode OpenGL version to 3.3 to support instancing. GPUs from 2007 support it, so it should be safe. Also, do not attempt to compile double-precision geometry shaders in safe mode, since they are not used and may crash anyways.
- Line trail mapping in non-timestamped trajectories. Fixes [#715](https://codeberg.org/gaiasky/gaiasky/issues/715).
- Double-rebuilding of dataset manager on close. Also, closing the dataset manager does not persist the preferences.
- Shader version for normal shader from 410 to 330 to prevent crashes in old GPUs.
- Regression in texture binding introduced in 3.5.0-RC3 (commit 7db456cc).
- Adjust rotate/turn strength when using the arrow keys.
- Random bugs in label render system.
- Do not show collapse/expand buttons in collapsible windows if collapsing is disabled.
- Wrong key used in galactic latitude attribute in color map picker.
- Input multiplexer and welcome GUI initialization sequence may cause a startup crash in certain conditions.
- Initialization sequence for distance scale factor, and particle groups breaking in VR when using triangles.
- Do not skip processing of LOD-based object when it is the current camera focus.
- Adjust visibility and opacity determination for entities with active fade in map; mostly used for NEARGALCAT objects.
- Spread GPU streaming of multi-component billboard datasets over several frames.
- Billboard set texture array uniform setting.
- Pixel-perfect interaction in VR menus. Surface normal was being transformed with a matrix that contained a translation instead of only using rotations.
- Properly scale particle set particles in VR.
- Proper motions in VR mode.
- Interactive load of JSON datasets that contain objects with 3D models blocks main thread.
- Guard in `getLineObject()` calls with a timeout does not use the time out. Fixes [#711](https://codeberg.org/gaiasky/gaiasky/issues/711).
- Scale orbit element particles for VR, readjust size limits.
- Slider texture filtering issue in green, blue, orange and red themes.
- Star surface shader crash when motion blur is on.
- Non-canonical OpenGL parameters in some configuration calls.
- Headless mode crashes on start.
- Star billboard and quad positions in stereo mode.
- Absolute position method in particle set does not guard against null parameters. Fixes [#710](https://codeberg.org/gaiasky/gaiasky/issues/710).
- Dataset manager layout, especially on low-resolution displays.
- Move hardcoded billboard galaxy threshold to model initializer.
- Single star rendering from afar, spherical position determination, graph update sequence for proper motion and other objects, bypass area and loc update when components are off, camera position lock for stars in star sets.
- Several issues with single star rendering and magnitude initialization.
- Add mechanism to automatically disable certain post-processing effects on certain render modes (e.g. light glow on panorama/planetarium mode).
- Internal dataset loading operations out of order: move scene graph insertion before set-up.
- Enable model-less shape objects for label-only use cases.
- Removing objects with children only effectively removes the first children, leaving orphan objects in the scene graph which do not get updated but get added to the render lists.
- Removal of an object from the graph does not remove its children.
- Normals, bi-normals and tangents in icosphere creator.
- Crash with static light models, file filter in dataset loader.
- Cloud virtual textures not working due to missing shader attribute.
- Crash loading wrongly constructed cluster file.
- Trail attribute of orbits not always working. GPU non-trail orbits not working.

## Performance Improvements
- Improve performance of velocity vectors in LOD datasets by setting restrictions on the octant's solid angle before sending the star sets to the velocity vector renderer.
- Remove guard clauses in shader interpolation function that are already covered by `smoothstep()`.
- Distribute SVT render pass over 5 frames to split contribution over time and achieve more or less constant frame pacing.

## Code Refactoring
- Set 'useColor' in models to false by default, so that the object color is not passed to the 3D model unless explicitly stated.
- Remove dpendency on gdx-gltf, implement own modification which directly loads meshes using 32-bit integer indices instead of 16-bit shorts.
- Rename some classes to make them more concise. Fix and improve javadoc comments.
- Consolidate shader and resource disposing in post processors.
- Unify tessellation and regular shader infrastructure.
- Trigger star/particle set update task in updater systems instead of via the camera motion event. Shorten minimum times between metadata updates.
- Move particle and star set updater methods to consumers initialized at creation.
- Rename all math utilities converted from single to double precision from [name]d to [name]Double.
- Use solid angle component instead of hardcoded variables for star cluster thresholds.
- Move 'forceLabel' attribute to Label component.

## Build System
- AUR package dependency from `jre-openjdk` to `java-runtime`.
- Update bundled JRE to 20.0.1, update installer welcome image.
- Upgrade to LibGDX 1.12.0.
- Update build file tasks to latest gradle syntax recommendations.
- Update oshi-core from 5.8.7 to 6.4.1.
- Remove commons-math3 dependency by implementing own interpolator.
- Update STIL from 4.0.+ to 4.1.+, and Jackson from 2.13.2 to 2.15.+.
- Remove dependency on commons-imaging library for monochrome to RGB conversions.
- Update JCommander from 1.81 to 1.82; upgrade slf4j-nop from 1.7.+ to 2.0.+.
- Remove JPEG-XL support via external library (vavi-image), better wait for official support in Java Image I/O.
- Upgrade LWJGL version from 3.3.1 to 3.3.2.
- Improve format of release notes file in template.
- Upgrade to Gradle 8.1.1.

## Documentation
- Started writing test protocol document.
- Add package descriptions to all packages except for the `gaiasky.util` children.
- Add package descriptions, refactor API interfaces to own packages.
- Improve documentation of some API calls.
- Update AppStream metadata file with proper id and screenshots.

## Style
- Update style with new hard wrap length and new wrapping rules for function signature parameters.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.5.0.5b427a04f/).