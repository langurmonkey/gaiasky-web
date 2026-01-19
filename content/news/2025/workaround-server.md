+++
title = "Workaround to get Gaia Sky running"
description = "A description to get Gaia Sky running during the current server outage."
date = "2026-01-19T06:01:55Z"
tags = ["server downtime", "access issues", "precautionary measures", "Gaia Sky"]
author = "tsagrista"
categories = ["website", "announcement"]
+++

In light of the current [server downtime](/news/server-down-update), we are creating this post describing how to get Gaia Sky up and running with the base data package. 



- **Gaia Sky installer** -- first, you will need to download the installer for Gaia Sky version 3.7.0. Since our server is currently inaccessible, we have made this version available for download at the following link:

  - [Gaia Sky 3.7.0 Installer](https://codeberg.org/gaiasky/gaiasky/releases/tag/3.7.0)

  Please choose the appropriate installer for your operating system and follow the installation steps as usual.

- **Base data package** -- once Gaia Sky is installed, you need the base data package, which includes the Solar System, the Milky Way, and other essential objects. Download it (either in `zip` or `tar.gz`) from the following link:

  - [Base Data Package v057](https://codeberg.org/gaiasky/gsdata-basedata/releases/tag/v057)

  After downloading, extract the package to any location on your computer.

- **Move the dataset to Gaia Sky’s data directory** -- next, go into the extracted directory, and in it you should find the `default-data` directory. Copy it into the Gaia Sky data directory. Where is the Gaia Sky data directory, you ask? Here's its location depending on your operating system:

  - **Windows**: `C:\Users\%username%\.gaiasky\data`
  - **Linux**: `~/.local/share/gaiasky/data`
  - **macOS**: `~/.gaiasky/data`

  Ensure that the `default-data` directory is placed directly within the `data` folder. This will allow Gaia Sky to load the necessary resources correctly.

- **Compatibility with older datasets** -- for older versions of Gaia Sky, most of the datasets for stars, galaxies, nebulae, clusters, and other celestial objects should still work. While the current server downtime means new datasets cannot be fetched, you can continue using previously downloaded datasets from older versions without issues.

### Final notes

This should give you a working Gaia Sky installation with the bare minimum. We appreciate your patience during this downtime and are working hard to restore full access to our services.
