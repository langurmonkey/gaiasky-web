+++
title = "Moon 32K topography virtual texture"
description = "We just published a new 32K Moon VT dataset"
date = "2025-02-18T09:15:20Z"
tags = ["vt", "moon", "virtualtexture", "dataset"]
author = "tsagrista"
categories = ["Dataset"]
+++

We'd like to announce that we just published a new virtual texture dataset. This dataset is based on NASA's [Scientific Visualization Studio CGI Moon Kit](https://svs.gsfc.nasa.gov/4720). Constructed from the DEM (Digital Elevation Map) in LRO/LOLA, it contains a 32K virtual texture for the Moon topography (elevation). When you have tessellation activated, this represents elevation in the Moon by vertex displacement and subdivision.

{{< fig src="img/2025/02/32k-vt-moon.thumb.jpg" link="/img/2025/02/32k-vt-moon.jpg" class="fig-center fig-post" title="The new 32K topography virtual texture applied to the Moon in Gaia Sky." loading="lazy" >}}

<!--more-->

You can get it from the **dataset manager** in Gaia Sky. Just look up "32K Moon Topography" and it should just pop right up.

The repository for this dataset is [codeberg.org/gaiasky/gsdata-vt-moon-topography-nasa](https://codeberg.org/gaiasky/gsdata-vt-moon-topography-nasa).

Original [credits](https://svs.gsfc.nasa.gov/4720#section_credits) go to Ernie Wright (USRA) and Noah Petro (NASA/GSFC).
