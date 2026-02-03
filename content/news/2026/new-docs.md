---
title: "Gaia Sky documentation upgrade"
description: "Update in documentation structure and look'n'feel"
date: 2026-02-03
author: "tsagrista"
categories: ["Documentation"]
tags: ["documentation", "sphinx", "website"]
---

If you’ve checked out our [documentation](https://gaia.ari.uni-heidelberg.de/gaiasky/docs/) lately, you’ll notice things look a bit different. We’ve just finished a major overhaul of how we build and host our docs. While we've had a version switcher for a while, the "engine" under the hood was getting a bit clunky, and some of the Sphinx extensions we used were unmaintained.

We moved away from the **Read The Docs theme** and `sphinx-multiversion` in favor of a custom, decoupled build system using the [**PyData Sphinx theme**](https://pydata-sphinx-theme.readthedocs.io). Previously, we had to re-generate the documentation for *every single version* of Gaia Sky every time we made a change to the master branch. As you can imagine, that didn't scale well. 

With the new setup, we have:

* **Incremental Builds:** We only build the version that actually changed (usually `master`). 
* **Dynamic Switching:** The version switcher now pulls from a central `switcher.json`. This means even old, archived documentation versions stay "connected" to the latest releases without us ever having to touch their HTML again.
* **Modern UI:** A much-improved sidebar, better search, cleaner look, and a beautiful new PDF layout.

This change saves us a ton of build time and ensures that the documentation is always snappier and easier to navigate. We've also gone into the actual structure of the documentation and changed and adapted it so that it flows better.

Check it out ([docs.gaiasky.space](https://gaia.ari.uni-heidelberg.de/gaiasky/docs/)) and let us know if you encounter any issues.


