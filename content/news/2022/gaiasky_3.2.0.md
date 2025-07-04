+++
title = "Gaia Sky 3.2.0"
date = "2022-06-07T15:07:00"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 Gaia Sky 3.2.0 available now!

<!--more-->


## Build System

- Java minimum version set to 15 in build script check.
- Add Linux archive for [itch.io](itch.io).
- Add Windows archive to `install4j` template for uploading to [itch.io](itch.io).
- Add aarch64 JRE to macOS bundle for M1 machines. Move to macOS single bundle archive from deprecated old single bundle.
- Automatically generate release notes during build.
- Downgrade jamepad to 2.0.14.2 as the newer 2.0.20.0 does not work with ARM macs.
- Force safe graphics mode on M1 macOS.
- Remove deprecated features from build files.
- Remove gson dependency version.
- Remove old run targets.
- Remove run tasks, use `--args` gradle argument instead.
- Sign Windows packages with self-sigend certificate.
- Update appimage JDK version to 16.0.2+7.
- Update gradle wrapper version to 7.3.
- Update gradlew version.
- Update install4j script to latest version, use bundled JRE for .deb, upgrade to Java 17.
- Upgrade jackson library version.
- Upgrade to libgdx 1.11.0 and LWJGL 3.3.1 --- this adds M1 Mac support.
- Use default GC (G1) in favor of Shenandoah (only LTS).

## Documentation

- Update contributing document to reflect new objects file.

## Features

- Add 'New directory' button to file chooser, fix event propagation with generic dialogs.
- Add 'randomize all' function to totally randomize planet surfaces.
- Add API call to set label colors.
- Add API calls to configure and take screenshots.
- Add GUI control to edit object fade time [ms].
- Add `--headless` flag to run in headless mode (hidden window).
- Add an arbitrary number of load progress bars.
- Add asteroids/sso catalog types.
- Add background thread count and pool size to debug information.
- Add buttons to launch preferences dialog and to quit at the bottom right of the welcome screen.
- Add camera distance from Sun in the camera section of the focus information pane.
- Add catalog info goodies to asteroids catalogs.
- Add collapsible entry and use it for datasets in datasets component.
- Add context menu to dataset items in dataset component.
- Add cubemap diffuse texturing capability to models.
- Add cyrillic characters to `main-font`, `font2d` and `font3d` fonts.
- Add dynamic resolution checkbox to preferences dialog.
- Add file list and scroll pane to dataset information in dataset manager.
- Add full screen bit depth and refresh rate to fully qualify selected full screen modes.
- Add individual size scale factor to star/particle group datasets.
- Add interactive surface generation from the GUI.
- Add meshes as datasets, connect dataset visibility to per-object visibility controls for meshes.
- Add method to inject transformation matrix directly into orbit, add change of basis matrix creation utility.
- Add new red-blue anaglyph profile mode, additionally to the pre-existing red-cyan.
- Add notice when there are no datasets.
- Add number of samples to orbit objects.
- Add offline mode, activated in configuration file.
- Add pixel lighting shading to meshes.
- Add popup notice when opening the keyframes window if component 'others' is not visible.
- Add popup notifications for certain important actions and events. These popup notifications can be closed by clicking on them, and they stay on screen for 8 seconds by default.
- Add provider parameters to data providers.
- Add proxy configuration directly in Gaia Sky's config file.
- Add roughness texture and value to normal shader, enable mipmaps in skybox.
- Add scaffolding to translate welcome tips and funny sentences. Add Catalan translation for those.
- Add setting to select preferred units (ly/pc).
- Add shapes around objects Fixes [#378](https://gitlab.com/langurmonkey/gaiasky/issues/378).
- Add shift to biome LUT, improve procedural generation.
- Add specular, normal, emissive, metallic, roughness and height cubemap support to default and tessellation shaders.
- Add the possibility to track objects.
- Add translation status code and task, update catalan translation file.
- Add variability to close-up stars and star models.
- Add variable stars as a new dataset type.
- Additional API call to load star datasets.
- Allow spherical coordinates in StaticCoordinates, additional fixes.
- Asteroids get full dataset controls (except for colormaps) like highlighting, coloring and sizing.
- Complete catalan translation file, add neat options to translation status utility.
- Convert provider parameters to dataset options for STIL provider.
- Enable label colors for all objects. Always defaults to white.
- Enable loading internal JSON descriptor files from UI.
- Enable orbit trails in `GPU` VBO mode and remove the "orbit style" setting, for now the "GPU lines" line style setting uses VBOs.
- Enable translation of object names, and add first translation files for most common objects like planets, constellations, etc.
- Expand/collapse panes by clicking on title.
- Expose SSR to preferences dialog, experimental section.
- Finish dynamic resolution implementation with an arbitrary number of levels.
- Generate normal map from elevation data if needed.
- Get Gaia Sky ready for star systems with proper orbits.
- Implement mosaic cubemaps, quad-based star group renderer.
- Implement the use of cubemaps in skyboxes. Fix cubemap reflection directions.
- Imporove CA,DE,ES translations.
- Improve bookmarks, add missing i18n keys Fixes [#380](https://gitlab.com/langurmonkey/gaiasky/issues/380).
- Improve layout and UX of datasets component.
- Improve layout and information of crash window.
- Improve layout of welcome and loading GUIs.
- Improve mode switching dialogs with a few goodies and QOL updates.
- Interactive procedural generation of cloud and atmosphere components from the GUI.
- Interactive procedural generation of planetary surfaces, clouds and atmospheres.
- Materials overhaul.
- New 'force label visibility' flag for model objects. This flag causes the label of the object to always be rendered, regardless of the solid angle and other constraints. The flag is controlled by new button at the top of the focus information pane (bottom-right) and via two new scripting API calls.
- New API call: `setDatasetPointSizeMultiplier(String, Double)`.
- New non-constant-density fog shader which approximates physical fog much better than before.
- Planet generation with elevation, diffuse and specular textures.
- Redesign dataset manager. The old download manager/catalog selection duo is phased out in favor of the new dataset manager. This is more usable and less confusing, while allowing for parallel downloads.
- Save session log file to.
- Screen space reflections Merge branch 'ssr'.
- Shapes (spheres, cones, cylinders, etc.) of arbitrary sizes can now be added around any object, with the possibility of tracking the object's size. This is an extension of [#378](https://gitlab.com/langurmonkey/gaiasky/issues/378) which includes many more options plus an API entry point.
- Show release notes at startup after a version update.
- Simplify loading mechanism by joining catalog files with object files. No distinction is necessary anymore, for all of them work in the same way and are loaded by the same entities.
- Update splash.
- Update welcome GUI background image.
- Updated the Bulgarian translation.

## Bug Fixes

- 'add scene graph object' event missing source object. Fixes [#400](https://gitlab.com/langurmonkey/gaiasky/issues/400).
- Gaia fov modes with triangle-based stars.
- JSON output of REST API server.
- VR controller info positioning, settings crash.
- Add default values for orbit line and point colors.
- Add notice whenever a `default-data` update is available.
- Add null-checks for some OpenVR properties (required by Oculus 2). Add VR information in crash reporter. Fixes [#393](https://gitlab.com/langurmonkey/gaiasky/issues/393) (again).
- Add vr offset to reflection view direction.
- Big refactor that fixes the runtime activation and deactivation of both motion blur and ssr. Lots of little fixes and improvements to the render system.
- Broken `setObjectVisibility()` API call. Fixes [#391](https://gitlab.com/langurmonkey/gaiasky/issues/391).
- Cloud rendering artifacts.
- Color picker listener stops working after first click.
- Compute mu automatically if period is set in orbital elements.
- Configure crash window size with same code as regular window.
- Correctly shut down background worker and manager threads so that JVM can finish gently.
- Correctly update label text when setting `SliderPlus` values.
- Crosshair in cubemap, planetarium, stereo and VR modes.
- Data manager misbehavior when data location path is a symlink.
- Dataset manager path handling on Windows.
- Default style of headline and subhead messages, as well as their positioning.
- Directional lights from stars still applied when stars are made invisible.
- Do not add objects that already exist (have same names and same type) to scene graph.
- Effective temperature array initialization bug in STIL loader.
- Empty tips may crash Gaia Sky at startup.
- Escape path before sending SAMP metadata. Fixes [#392](https://gitlab.com/langurmonkey/gaiasky/issues/392).
- Fix star clusters fade between model and billboard.
- Focus info interface width jitters when moving in free mode on occasions.
- Getting particle position no longer results in null pointer.
- Hide system cursor correctly with GLFW until libgdx 1.10.1 is released.
- Highlight dataset API call.
- Improve check box layout in preferences dialog.
- Improve error handling in dataset manager.
- Increase size star point buffer when needed.
- Initial VR gui distance.
- Issues with dataset loading via scripting.
- Julian date algorithm.
- Layout of version line table.
- Lighting bug when multiple stars cast a light on an object.
- Make sure direction and up vectors are orthogonal in camera transition call.
- Null-check satellite attitude before getting quaternion. Fixes [#402](https://gitlab.com/langurmonkey/gaiasky/issues/402).
- Null-check settings in crash reporter.
- Particle dataset loading default size limits when using tris.
- Prevent repeated entries in search suggestions.
- Reflected cubemap orientation (was upside down).
- Reflections in tessellation shaders.
- Regression adding bookmarks. Fixes [#390](https://gitlab.com/langurmonkey/gaiasky/issues/390).
- Regression in apparent magnitude resource bundle key.
- Regression with libgdx 1.11.0 that caused vertical tooltips.
- Reload data files when data path changes.
- Remove phase of pi radians in default-model orbital elements.
- Remove usage of deprecated Java APIs.
- Rename old configuration files after conversion to new format.
- Restore correct values on cancel in preferences dialog.
- Restrict the rendering of pointer guides and cross-hairs in stereo and cubemap modes.
- Set argument of pericenter to zero when the epoch is not the reference epoch in the SSO converter for DR3.
- Set encoding of i18n files to UTF-8, update formatting.
- Show warn message when trying to select object from invisible dataset in search dialog.
- Some data paths using forward slashes '/' instead of '\' on Windows.
- Time offset (6711 yr) in Moon's position lookup.
- Update `VRControllerRole` values from `ETrackedControllerRole` from SteamVR spec. Fixes [#393](https://gitlab.com/langurmonkey/gaiasky/issues/393).
- Update directory permissions error message to make it easier to understand.
- Use minimum width for debug interface to prevent dynamic resizing depending on content.
- Workaround for libgdx backslash bug in asset manager. Fixes [#398](https://gitlab.com/langurmonkey/gaiasky/issues/398).
- Wrong scale factor in orbital elements-based orbits in VR.

## Performance Improvements

- Improve performance of orbital elements particles by treating them as whole groups in the CPU using new model object and renderer.
- Initially size index hash maps to avoid resize operations.
- Separate UI reload from localized name updates.

## Refactoring

- Abstract attitude loading system, remove `Gaia` class, use heliotropic satellite.
- Add `I18nFormatter` to reformat i18n files.
- Add source object to events by default.
- Flatten object hierarchy by removing some classes, merging their functionality upwards.
- Improve service thread implementation.
- Improve shader combination and lookup (from ssr branch).
- Move all text from -v flag to i18n keys.
- Move double array to `gaiasky.util` package.
- Move tips and funny texts to main bundle, add some dangling hard-coded strings to bundle, enable translation of keyboard keys.
- Move update process to runnable, protect render lists from outer access.
- Old milky way renderer converted to general-purpose billboard group infrastructure to enable representation of any quad-based point data.
- Remove old date formatting infrastructure (desktop, html, mobile) in favor of a direct approach.
- Remove some warnings, clean up code.
- Remove unused and obsolete Jython fix.
- Remove unused id from components, fix skybox orientation.
- Remove useless number formatting infrastructure.
- Rename `u_environmentCubemap` to `u_diffuseCubemap` in shaders.
- Rename setting `data::skyboxLocation` to `data::reflectionSkyboxLocation`.
- Rename some packages and move some code around.
- Use bit mask instead of 64-bit integer as attributes mask so that we can register more than 64 attributes. Add proper 3-component specular color to materials. Add diffuse cubemaps for models and clouds. Fix a number of shader issues.

## Style

- Consolidate normal shader vertex data into struct.
- Organize imports in whole codebase.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.2.0.84c0fc728/).