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

- initial implementation of a proper in-scene VR user interface with mouse interaction.
- use gamepad UI in VR.
- VR controllers use same mappings format as gamepads.
- add specific mappings for Valve Index VR controllers.
- add generic VR controller model.
- welcome and loading VR screens are now 3D surfaces in-scene.
- add VR controller interaction in VR welcome screen.
- sRGB setting enables SRGB format only in VR frame buffers.

## Bug Fixes

- typo in German translation file. Fixes [#706](https://codeberg.org/gaiasky/gaiasky/issues/706).
- remove unused configuration setting `scriptsLocation`.
- tooltip and layout issues in datasets component.
- invalid focus state in natural camera.
- add object name checks to most API calls.
- omit regular gamepad window bindings in gamepad configuration window.
- first loading frame produced in VR with incorrect sizing.
- connect visibility buttons in gamepad GUI to global visibility event, and add tooltips with name.
- remove `IVRHeadsetView` interface from OpenVR initialization so that Gaia Sky works with OpenComposite, which translates OpenVR to OpenXR.
- properly close file stream when done with them.
- prevent hang on close due to daemon thread notify() calls.
- incorrect filtering in slider backgrounds.
- incorrect filtering in UI table baground image.
- script with wrong loader name. Fixes [#703](https://codeberg.org/gaiasky/gaiasky/issues/703).

## Code Refactoring

- update VR controllers in their own system.
- move VR UI classes to own package.

## Documentation

- update API call fade in/out descriptions.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.4.1.0cf299d94/).