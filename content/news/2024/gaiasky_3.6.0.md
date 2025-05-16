+++
title = "Gaia Sky 3.6.0"
date = "2024-03-12T08:51:00"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 Gaia Sky 3.6.0 available now!

<!--more-->


## Features
- Add support for OptFlowCam (Piotrowski 2024) method to convert keyframes into camera path files. Gaia Sky calls the local python3 interpreter to process the keyframe files, so a local python3 installation (with numpy) needs to be in place for it to work.
- Add support for B-splines, additionally to Catmull-Rom splines, as a method for interpolating positions between keyframes.
- Reorganize keyframes window layout for better use of space.
- Add different durations for the transitions in position and orientation in the API call.
- Add smooth interpolation methods to `cameraTransition()` calls. The new methods can use either a logistic sigmoid or a logit function. Smoothing factor is configurable via a parameter.
- Add 'textureAttribute' to particle sets, so that textures are selected with respect to the value of an attribute.
- Use local dataset descriptors to construct catalog infos, when they are not explicitly set.
- Enable local data information in the '+ info' window. This displays the local data on an object. In particle and star groups, the extra attributes are also offered.
- Enable extra arguments of type string for star and particle sets.
- Rename 'star systems' group to 'exoplanets \& extrasolar systems'. Add icons to group title in dataset manager.
- Add support for multiple key sets bound to actions in hotkey tooltip.
- Keyframes and camera path file saving no longer overwrites existing files. Instead, it generates a new unique file name based on the given one.
- Support comma- as well as whitespace-separated values for camera and keyframes files. Default to comma-separated values for writing.
- Add API call to get the window coordinates of an object, in pixels.
- Add API calls to do camera transitions only in position and orientation.
- Add time transition API call and test script.

## Bug Fixes
- Check leap years in date dialog.
- Prevent NaNs in some camera operations.
- Clean up test scripts a bit.
- `startRecordingCameraPath(String filename)` does not use the filename correctly.

## Build System
- Update dependency library versions.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.6.0.afdd9547d/).