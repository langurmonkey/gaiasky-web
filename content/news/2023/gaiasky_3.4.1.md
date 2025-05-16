+++
title = "Gaia Sky 3.4.1"
date = "2023-03-09T08:31:00"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 Gaia Sky 3.4.1 available now!

<!--more-->


## Features

- Initial implementation of a proper in-scene VR user interface with mouse interaction.
- Use gamepad UI in VR.
- VR controllers use same mappings format as gamepads.
- Add specific mappings for Valve Index VR controllers.
- Add generic VR controller model.
- Welcome and loading VR screens are now 3D surfaces in-scene.
- Add VR controller interaction in VR welcome screen.
- SRGB setting enables SRGB format only in VR frame buffers.

## Bug Fixes

- Typo in German translation file. Fixes [#706](https://codeberg.org/gaiasky/gaiasky/issues/706).
- Remove unused configuration setting `scriptsLocation`.
- Tooltip and layout issues in datasets component.
- Invalid focus state in natural camera.
- Add object name checks to most API calls.
- Omit regular gamepad window bindings in gamepad configuration window.
- First loading frame produced in VR with incorrect sizing.
- Connect visibility buttons in gamepad GUI to global visibility event, and add tooltips with name.
- Remove `IVRHeadsetView` interface from OpenVR initialization so that Gaia Sky works with OpenComposite, which translates OpenVR to OpenXR.
- Properly close file stream when done with them.
- Prevent hang on close due to daemon thread notify() calls.
- Incorrect filtering in slider backgrounds.
- Incorrect filtering in UI table baground image.
- Script with wrong loader name. Fixes [#703](https://codeberg.org/gaiasky/gaiasky/issues/703).

## Code Refactoring

- Update VR controllers in their own system.
- Move VR UI classes to own package.

## Documentation

- Update API call fade in/out descriptions.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.4.1.0cf299d94/).