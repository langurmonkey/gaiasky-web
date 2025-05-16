+++
title = "Gaia Sky 3.5.2"
date = "2023-07-26T09:56:00"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 Gaia Sky 3.5.2 available now!

<!--more-->


## Features
- Improve keyframes window layout, with more space for keyframes and better sizing of keyframes table.
- Default to full screen for small displays, and refactor display resolution fetching process.
- Check AMD APU code name to detect Steam Deck.
- Steam deck programmatic detection to default to full screen at startup.

## Bug Fixes
- Exporting keyframes to camera path is missing the very last frame. Fixes [#729](https://codeberg.org/gaiasky/gaiasky/issues/729).
- Restore line rendering in keyframes, lost in a regression during the line refactoring campaign.
- Only deactivate main mouse/kbd listener if the current dialog is modal.
- Full-screen log item in translation files.
- Visual layout and information structure in about window, system tab.
- Apply patch provided by luzpaz fixing many typos in comments and strings. Fixes [#726](https://codeberg.org/gaiasky/gaiasky/issues/726).

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.5.2.f8a396004/).