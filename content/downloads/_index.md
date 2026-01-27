+++
title = "Downloads"
categories = ["Downloads"]
author = "tsagrista"
css = ["css/downloads.css"]
+++

<!-- SERVER NOTICE -->
<!-- <div class="hint" style="margin-top: 1em; background-color: #821"> -->
  <!-- <p class="hint-title"><i class="fa fa-info-circle"></i><strong>🚧 Server down &ndash; alternative downloads 🚧</strong></p> -->
<!-- <p class="hint-body">Due to the <a href="/news/2025/server-down-update">current server outage</a>, the usual Gaia Sky downloads are currently down. We recommend getting the Gaia Sky 3.7.0 packages from <a href="https://codeberg.org/gaiasky/gaiasky/releases/tag/3.7.0" title="Codeberg Releases - Gaia Sky 3.7.0" style="font-size: 1.2em; font-weight: 900; text-decoration: underline !important;" >Codeberg Releases</a>. More info <a href="/news/2026/workaround-server" >here</a>.</p> -->
<!-- </div> -->


{{< downloads-table >}}


## Verify package integrity

We sign the packages served from this website with our personal GPG key. Learn how to [verify them here]({{< ref "verifysig" >}}).

 

## System requirements

|                       |                                                               |
|-----------------------|---------------------------------------------------------------|
| **Operating system**  | Linux / Windows 10+ / macOS                                   |
| **Architecture**      | x86_64, ARM (only Apple silicon through compat layer)         |
| **CPU**               | Intel Core i5 3rd Generation. 4+ cores recommended            |
| **GPU**               | Support for OpenGL 3.3 (4.2 recommended), 1 GB VRAM           |
| **Memory**            | 4+ GB RAM (depends on loaded datasets)                        |
| **Hard drive**        | 1+ GB of free disk space (depends on downloaded datasets)     |

## Installation instructions

Find full installation and running instructions for every OS in our documentation:

- [Installation and running instructions](https://gaia.ari.uni-heidelberg.de/gaiasky/docs/master/Installation.html#installation-procedure).

## Gaia Sky VR

Gaia Sky supports **Virtual Reality** via **OpenXR** on Linux and Windows. Use the CLI argument `gaiasky -vr` or use the `gaiaskyvr.exe` executable (on Windows) to run it. You need a VR headset and runtime supporting OpenXR.

- [Gaia Sky VR documentation](https://gaia.ari.uni-heidelberg.de/gaiasky/docs/master/Gaia-sky-vr.html).

## Getting the data

The Gaia Sky installation only contains the raw program. If you actually need to run Gaia Sky you will need to download some data (catalogs, 3D models, textures, etc.). To do so, Gaia Sky contains an integrated [dataset manager](https://gaia.ari.uni-heidelberg.de/gaiasky/docs/master/Dataset-manager.html) to help you get the datasets you need. In case you need to run Gaia Sky in a machine without an internet connection or have problems with the built-in downloads, we offer direct downloads for all versions of all datasets. As a general rule of thumb, you should always get the most recent version.

- [Gaia Sky datasets](/resources/datasets/).
