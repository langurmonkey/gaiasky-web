+++
title = "Gaia Sky 3.5.7-3"
date = "2023-11-29T09:15:00"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 Gaia Sky 3.5.7-3 available now!

<!--more-->


## Bug Fixes
- Columns corresponding to the same UCD maintain the order of appearance in the source table when used.
- Use concurrent hash set in 'selecting' list in the OpenXR input listener to prevent concurrent modification errors.
- Resizing log window does not resize contents. Fixes [#749](https://codeberg.org/gaiasky/gaiasky/issues/749).
- Prevent getting name from second closest object if it is invalid. Fixes [#750](https://codeberg.org/gaiasky/gaiasky/issues/750).
- Use logical keys instead of key codes by converting GDX's codes to GLFW, which uses the logical keyboard layout. Fixes [#748](https://codeberg.org/gaiasky/gaiasky/issues/748).
- Rename makefile, update build script to detect `/opt/gaiasky` installation.
- Use default mappings file if the configured one does not exist.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.5.7-3.8be0b0add/).