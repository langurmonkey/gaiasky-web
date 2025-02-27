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
- add Linux archive for [itch.io](itch.io).
- add Windows archive to `install4j` template for uploading to [itch.io](itch.io).
- add aarch64 JRE to macOS bundle for M1 machines. Move to macOS single bundle archive from deprecated old single bundle.
- automatically generate release notes during build.
- downgrade jamepad to 2.0.14.2 as the newer 2.0.20.0 does not work with ARM macs.
- force safe graphics mode on M1 macOS.
- remove deprecated features from build files.
- remove gson dependency version.
- remove old run targets.
- remove run tasks, use `--args` gradle argument instead.
- sign Windows packages with self-sigend certificate.
- update appimage JDK version to 16.0.2+7.
- update gradle wrapper version to 7.3.
- update gradlew version.
- update install4j script to latest version, use bundled JRE for .deb, upgrade to Java 17.
- upgrade jackson library version.
- upgrade to libgdx 1.11.0 and LWJGL 3.3.1 --- this adds M1 Mac support.
- use default GC (G1) in favor of Shenandoah (only LTS).

## Documentation

- update contributing document to reflect new objects file.

## Features

- add 'New directory' button to file chooser, fix event propagation with generic dialogs.
- add 'randomize all' function to totally randomize planet surfaces.
- add API call to set label colors.
- add API calls to configure and take screenshots.
- add GUI control to edit object fade time [ms].
- add `--headless` flag to run in headless mode (hidden window).
- add an arbitrary number of load progress bars.
- add asteroids/sso catalog types.
- add background thread count and pool size to debug information.
- add buttons to launch preferences dialog and to quit at the bottom right of the welcome screen.
- add camera distance from Sun in the camera section of the focus information pane.
- add catalog info goodies to asteroids catalogs.
- add collapsible entry and use it for datasets in datasets component.
- add context menu to dataset items in dataset component.
- add cubemap diffuse texturing capability to models.
- add cyrillic characters to `main-font`, `font2d` and `font3d` fonts.
- add dynamic resolution checkbox to preferences dialog.
- add file list and scroll pane to dataset information in dataset manager.
- add full screen bit depth and refresh rate to fully qualify selected full screen modes.
- add individual size scale factor to star/particle group datasets.
- add interactive surface generation from the GUI.
- add meshes as datasets, connect dataset visibility to per-object visibility controls for meshes.
- add method to inject transformation matrix directly into orbit, add change of basis matrix creation utility.
- add new red-blue anaglyph profile mode, additionally to the pre-existing red-cyan.
- add notice when there are no datasets.
- add number of samples to orbit objects.
- add offline mode, activated in configuration file.
- add pixel lighting shading to meshes.
- add popup notice when opening the keyframes window if component 'others' is not visible.
- add popup notifications for certain important actions and events. These popup notifications can be closed by clicking on them, and they stay on screen for 8 seconds by default.
- add provider parameters to data providers.
- add proxy configuration directly in Gaia Sky's config file.
- add roughness texture and value to normal shader, enable mipmaps in skybox.
- add scaffolding to translate welcome tips and funny sentences. Add Catalan translation for those.
- add setting to select preferred units (ly/pc).
- add shapes around objects Fixes [#378](https://gitlab.com/langurmonkey/gaiasky/issues/378).
- add shift to biome LUT, improve procedural generation.
- add specular, normal, emissive, metallic, roughness and height cubemap support to default and tessellation shaders.
- add the possibility to track objects.
- add translation status code and task, update catalan translation file.
- add variability to close-up stars and star models.
- add variable stars as a new dataset type.
- additional API call to load star datasets.
- allow spherical coordinates in StaticCoordinates, additional fixes.
- asteroids get full dataset controls (except for colormaps) like highlighting, coloring and sizing.
- complete catalan translation file, add neat options to translation status utility.
- convert provider parameters to dataset options for STIL provider.
- enable label colors for all objects. Always defaults to white.
- enable loading internal JSON descriptor files from UI.
- enable orbit trails in `GPU` VBO mode and remove the "orbit style" setting, for now the "GPU lines" line style setting uses VBOs.
- enable translation of object names, and add first translation files for most common objects like planets, constellations, etc.
- expand/collapse panes by clicking on title.
- expose SSR to preferences dialog, experimental section.
- finish dynamic resolution implementation with an arbitrary number of levels.
- generate normal map from elevation data if needed.
- get Gaia Sky ready for star systems with proper orbits.
- implement mosaic cubemaps, quad-based star group renderer.
- implement the use of cubemaps in skyboxes. Fix cubemap reflection directions.
- imporove CA,DE,ES translations.
- improve bookmarks, add missing i18n keys Fixes [#380](https://gitlab.com/langurmonkey/gaiasky/issues/380).
- improve layout and UX of datasets component.
- improve layout and information of crash window.
- improve layout of welcome and loading GUIs.
- improve mode switching dialogs with a few goodies and QOL updates.
- interactive procedural generation of cloud and atmosphere components from the GUI.
- interactive procedural generation of planetary surfaces, clouds and atmospheres.
- materials overhaul.
- new 'force label visibility' flag for model objects. This flag causes the label of the object to always be rendered, regardless of the solid angle and other constraints. The flag is controlled by new button at the top of the focus information pane (bottom-right) and via two new scripting API calls.
- new API call: `setDatasetPointSizeMultiplier(String, Double)`.
- new non-constant-density fog shader which approximates physical fog much better than before.
- planet generation with elevation, diffuse and specular textures.
- redesign dataset manager. The old download manager/catalog selection duo is phased out in favor of the new dataset manager. This is more usable and less confusing, while allowing for parallel downloads.
- save session log file to.
- screen space reflections Merge branch 'ssr'.
- shapes (spheres, cones, cylinders, etc.) of arbitrary sizes can now be added around any object, with the possibility of tracking the object's size. This is an extension of [#378](https://gitlab.com/langurmonkey/gaiasky/issues/378) which includes many more options plus an API entry point.
- show release notes at startup after a version update.
- simplify loading mechanism by joining catalog files with object files. No distinction is necessary anymore, for all of them work in the same way and are loaded by the same entities.
- update splash.
- update welcome GUI background image.
- updated the Bulgarian translation.

## Bug Fixes

- 'add scene graph object' event missing source object. Fixes [#400](https://gitlab.com/langurmonkey/gaiasky/issues/400).
- Gaia fov modes with triangle-based stars.
- JSON output of REST API server.
- VR controller info positioning, settings crash.
- add default values for orbit line and point colors.
- add notice whenever a `default-data` update is available.
- add null-checks for some OpenVR properties (required by Oculus 2). Add VR information in crash reporter. Fixes [#393](https://gitlab.com/langurmonkey/gaiasky/issues/393) (again).
- add vr offset to reflection view direction.
- big refactor that fixes the runtime activation and deactivation of both motion blur and ssr. Lots of little fixes and improvements to the render system.
- broken `setObjectVisibility()` API call. Fixes [#391](https://gitlab.com/langurmonkey/gaiasky/issues/391).
- cloud rendering artifacts.
- color picker listener stops working after first click.
- compute mu automatically if period is set in orbital elements.
- configure crash window size with same code as regular window.
- correctly shut down background worker and manager threads so that JVM can finish gently.
- correctly update label text when setting `SliderPlus` values.
- crosshair in cubemap, planetarium, stereo and VR modes.
- data manager misbehavior when data location path is a symlink.
- dataset manager path handling on Windows.
- default style of headline and subhead messages, as well as their positioning.
- directional lights from stars still applied when stars are made invisible.
- do not add objects that already exist (have same names and same type) to scene graph.
- effective temperature array initialization bug in STIL loader.
- empty tips may crash Gaia Sky at startup.
- escape path before sending SAMP metadata. Fixes [#392](https://gitlab.com/langurmonkey/gaiasky/issues/392).
- fix star clusters fade between model and billboard.
- focus info interface width jitters when moving in free mode on occasions.
- getting particle position no longer results in null pointer.
- hide system cursor correctly with GLFW until libgdx 1.10.1 is released.
- highlight dataset API call.
- improve check box layout in preferences dialog.
- improve error handling in dataset manager.
- increase size star point buffer when needed.
- initial VR gui distance.
- issues with dataset loading via scripting.
- julian date algorithm.
- layout of version line table.
- lighting bug when multiple stars cast a light on an object.
- make sure direction and up vectors are orthogonal in camera transition call.
- null-check satellite attitude before getting quaternion. Fixes [#402](https://gitlab.com/langurmonkey/gaiasky/issues/402).
- null-check settings in crash reporter.
- particle dataset loading default size limits when using tris.
- prevent repeated entries in search suggestions.
- reflected cubemap orientation (was upside down).
- reflections in tessellation shaders.
- regression adding bookmarks. Fixes [#390](https://gitlab.com/langurmonkey/gaiasky/issues/390).
- regression in apparent magnitude resource bundle key.
- regression with libgdx 1.11.0 that caused vertical tooltips.
- reload data files when data path changes.
- remove phase of pi radians in default-model orbital elements.
- remove usage of deprecated Java APIs.
- rename old configuration files after conversion to new format.
- restore correct values on cancel in preferences dialog.
- restrict the rendering of pointer guides and cross-hairs in stereo and cubemap modes.
- set argument of pericenter to zero when the epoch is not the reference epoch in the SSO converter for DR3.
- set encoding of i18n files to UTF-8, update formatting.
- show warn message when trying to select object from invisible dataset in search dialog.
- some data paths using forward slashes '/' instead of '\' on Windows.
- time offset (6711 yr) in Moon's position lookup.
- update `VRControllerRole` values from `ETrackedControllerRole` from SteamVR spec. Fixes [#393](https://gitlab.com/langurmonkey/gaiasky/issues/393).
- update directory permissions error message to make it easier to understand.
- use minimum width for debug interface to prevent dynamic resizing depending on content.
- workaround for libgdx backslash bug in asset manager. Fixes [#398](https://gitlab.com/langurmonkey/gaiasky/issues/398).
- wrong scale factor in orbital elements-based orbits in VR.

## Performance Improvements

- improve performance of orbital elements particles by treating them as whole groups in the CPU using new model object and renderer.
- initially size index hash maps to avoid resize operations.
- separate UI reload from localized name updates.

## Refactoring

- abstract attitude loading system, remove `Gaia` class, use heliotropic satellite.
- add `I18nFormatter` to reformat i18n files.
- add source object to events by default.
- flatten object hierarchy by removing some classes, merging their functionality upwards.
- improve service thread implementation.
- improve shader combination and lookup (from ssr branch).
- move all text from -v flag to i18n keys.
- move double array to `gaiasky.util` package.
- move tips and funny texts to main bundle, add some dangling hard-coded strings to bundle, enable translation of keyboard keys.
- move update process to runnable, protect render lists from outer access.
- old milky way renderer converted to general-purpose billboard group infrastructure to enable representation of any quad-based point data.
- remove old date formatting infrastructure (desktop, html, mobile) in favor of a direct approach.
- remove some warnings, clean up code.
- remove unused and obsolete Jython fix.
- remove unused id from components, fix skybox orientation.
- remove useless number formatting infrastructure.
- rename `u_environmentCubemap` to `u_diffuseCubemap` in shaders.
- rename setting `data::skyboxLocation` to `data::reflectionSkyboxLocation`.
- rename some packages and move some code around.
- use bit mask instead of 64-bit integer as attributes mask so that we can register more than 64 attributes. Add proper 3-component specular color to materials. Add diffuse cubemaps for models and clouds. Fix a number of shader issues.

## Style

- consolidate normal shader vertex data into struct.
- organize imports in whole codebase.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.2.0.84c0fc728/).