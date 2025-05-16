+++
title = "Gaia Sky 3.3.2"
date = "2022-12-18T09:11:00"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 Gaia Sky 3.3.2 available now!

<!--more-->


## Bug Fixes
- Stop intercepting data location in paths, implementation did not work for Windows when the original path contained '*', and it was useless anyway, as we always use fully-defined paths.
- Avoid expanding dataset file paths in dataset manager to prevent horizontal overflow.

## Features
- Improve drag rotation behaviour when very close to objects.

You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.3.2.b5202d46f/).