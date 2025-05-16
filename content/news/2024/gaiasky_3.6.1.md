+++
title = "Gaia Sky 3.6.1"
date = "2024-05-29T11:54:00"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 Gaia Sky 3.6.1 available now!

<!--more-->


## Features
- Add input debug mode where all input events from input devices are logged to the info channel.
- Move camera and keyframes files times from long to ISO-8601 ('2011-12-03T10:15:30Z'), which is more readable. Add quaternion slerp orientation server, based on text files.
- Derive model span from vertex and transformation data instead of relying on values in the descriptor files.
- Add spectral type to camera info interface, computed for stars from the effective temperature.
- Add 'saturation' value to settings (under stars) to control the star saturation factor.
- Display effective temperature of body in camera info interface.
- Camera motion blur re-implementation using a pure post-processing approach, where the pixel positions are reconstructed from the depth buffer and the current and previous camera states. This does not require the velocity buffer anymore, so it is much faster. Add motion blur slider to regular and gamepad preferences.
- Add LVLH (local vertical local horizontal) attitude server, for objects like the ISS.
- Add support for gzipped streams in orbit file data provider.
- Add label bias attribute to label component to provide a way to artificially move the point at which the object's label is rendered.
- Add 'periodic' attribute to orbit coordinates objects.
- Improve UV grids so that their line width stays constant, they get subdivided when changing the field of view, and they get coordinates on the window frame.
- Improve recursive grid with constant-width lines and better distance value labels.
- Enable label rendering for invisibles, if labels are active for the object.
- Add option to display the time in no-UI mode (enter with Ctrl+U), and add checkbox to toggle setting in preferences dialog.
- Add support for binary file-backed VSOP87, and update data files. Needs update of base data package. Add versioning to bookmarks file.
- Add display information to help window, system tab.
- Add script to test object quaternion slerp provider.
- Add script to test camera orientation API calls that use quaternions.

## Bug Fixes
- Prevent activation of stereoscopic mode in VR.
- Position bookmarks do not work in VR.
- Check type of current model in gamepad GUI.
- Unescape HTML4.0 strings in wikipedia snippet title and body.
- Only load spacecraft GUI when the default data pack is there. Otherwise, the system crashes.
- Crash when the server response is not in JSON format, due to the server being down.
- REST server parameters matching does not check that the number of parameters is correct during matching.
- Warn about trying to bind reserved ports (<1024).
- Star absolute magnitude derivation.
- Land-at-location parameter check.
- Problem with shadow map frame buffers that sometimes corrupted shadows when two or more objects were in scene.
- Move initialization of derived particle attributes to the set-up stage, as it needs the coordinates object to be in place.
- Orientation lock with quaternion-based objects.
- Use color alpha channel to scale transparency in models.
- Optflowcam script to use formatted times.
- Use own parser to convert keyframe times. Fixes [#768](https://codeberg.org/gaiasky/gaiasky/issues/768).
- Prevent index retrieval in particle sets while the index is being generated or updated.
- Initial determination of screen size and UI scale factor.
- Initial fetch of screen size in macOS, attempt a method involving graphics device and max window bounds that should work with macOS.

## Performance Improvements
- Substitute commons-compress with jtar, saving ~2 MB of space.
- Reduce size of skin and image files.
- Adapt number of labels in octree star sets according to current octant view angle. Add fast linear interpolator functions that skips some checks, for cases where we can guarantee that x0 <= x1.
- Speed up star position computation (for labels and billboards), cap number of labels per octree star group, reduce precision of arbitrary precision numbers. These measures result in a drastic increase in overall performance.

## Code Refactoring
- Shadow mapping shaders rearranged, fix shadow blending in PBR fragment shader to work well with atmosphere ground colors.
- Rename post-processing filters for consistency.

## Documentation
- Update OptFlowCam reference.
- Complete library acknowledgements.
- Add descriptions for all custom gradle tasks.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.6.1.f3a379a3d/).