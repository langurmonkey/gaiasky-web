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
- stop intercepting data location in paths, implementation did not work for Windows when the original path contained '*', and it was useless anyway, as we always use fully-defined paths.
- avoid expanding dataset file paths in dataset manager to prevent horizontal overflow.

## Features
- improve drag rotation behaviour when very close to objects.
