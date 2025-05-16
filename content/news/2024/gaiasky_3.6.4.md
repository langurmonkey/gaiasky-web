+++
title = "Gaia Sky 3.6.4"
description = "In-app console, new locations revamp, and more"
date = "2024-10-08"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 Gaia Sky 3.6.4 released! It comes with a new in-app console, a revamp in the locations feature, and some under-the-hood rendering improvements.

{{< fig src="img/2024/10/3.6.4/3.6.4-release.jpg" class="fig-center fig-post" title="Gaia Sky 3.6.4 welcome screen." loading="lazy" >}}

<!--more-->

## Features
- Add location markers to pinpoint the exact position of each location. Add custom marker textures and custom label and marker colors.
- Add new attribute to locations, `ignoreSolidAngleLimit`, which disregards the limits when computing visibility. Cap angular sizes for all locations.
- Add location type attribute to location objects. This attribute is used to categorize locations by groups in the individual visibility window. Remove 'cosmic locations' content type, and move it to regular locations (requires default data pack update.).
- Separate scene frame buffer from meta-elements rendering (labels, lines, etc.) to be able to apply different post-processing effects to each.
- Add an implementation of console/terminal, which accepts commands to interact directly with the Gaia Sky API. Use `~` or `:` to launch the console.
- Add a generic map in the base component to store 'unrecognized' attributes; these get displayed in the object info window.
- Improve on-screen keyboard in controller UI.
- Add session type (X11, Wayland) to system information (Linux only).

{{< fig src="/img/2024/10/3.6.4/3.6.4-markers.jpg" class="fig-center fig-post" title="The new markers on the Moon." loading="lazy" >}}

## Bug Fixes
- Prevent virtual objects (hooks, invisibles, catalogs, etc.) from appearing in the individual visibility window. Hide meta-components (atmospheres, key frames, etc.) from buttons list. Fix layout.
- Always load HIP numbers if present in the STIL data loader, even if there are other identifiers.
- Update jEtty, JSON and XMLRPC libraries to secure versions (the old versions contain known vulnerabilities).
- Inform user of unsupported cubemap textured objects with procedural generation.

## Build System
- Update versions of `jCommander`, STIL and `Apfloat`, remove `Joise`.
- Update OSHI library version.

{{< fig src="/img/2024/10/3.6.4/3.6.4-console.jpg" class="fig-center fig-post" title="The console allows direct interaction with the API." loading="lazy" >}}

## Documentation
- Add architectures to download table.
- Fix typos and spelling errors in changelog file.
- Move VR info into README.md from VR.md.


As always, you can grab it [right here]({{< ref "downloads" >}}) ([link to repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases/3.6.4-2.3bfeec0f9)).
