+++
title = "Procedural galaxy generation preview"
description = "A short sneek peak into current state of the development of the new procedural galaxy generation system."
date = "2025-11-21"
tags = ["galaxy", "compute shader", "visualization", "astronomy"]
categories = ["astronomy", "visualization"]
author = "tsagrista"
+++


This post introduces an experimental galaxy generation system currently in development, which generates and visualizes galaxies in real time. By leveraging multiple channels, such as stars, gas, dust, H II regions, and the galactic bulge, the system generates diverse galaxy types, each with distinct structural features. 

Below is a preview of this system’s capabilities, showcasing the generated galaxies through a series of images. This is an early look at the technology and a demonstration of how we’re using the power of GPU-based compute shaders to create somewhat realistic galaxies very rapidly. Keep in mind that this is still a work in progress, with many improvements and additional features planned before release.

<!--more-->

{{< fig src="img/2025/11/hubble_grid_small.thumb.jpg" link="/img/2025/11/hubble_grid_small.jpg" class="fig-center fig-post" title="Procedural generation of several galaxy morphologies in Gaia Sky. [Full resolution image (12K)](https://i.postimg.cc/h4sNWVFH/hubble-grid.jpg)" loading="lazy" >}}

Every galaxy is modeled using different physical components, each represented by a separate "channel" in the compute shader. These channels simulate different aspects of the galaxy:

- **Stars** -- The luminous stars that make up the galaxy.
- **H II Regions** -- Areas of ionized hydrogen, often seen as nebulae.
- **Gas** -- The interstellar gas that fills the galaxy.
- **Dust** -- The small particles scattered throughout the galaxy, contributing to the galaxy's opacity.
- **Bulge** -- The central region of the galaxy, typically composed of older stars.

Each channel is processed individually by the compute shader, which performs complex calculations to generate a unique galaxy based on these inputs. The distribution of particles in each channel can be one of the following:

- **Sphere** -- Uniformly distributed sphere.
- **Gaussian sphere** -- Sphere following a radial Gaussian distribution.
- **Disk** -- Uniformly distributed disk.
- **Gaussian disk** -- A disk with a radial Gaussian distribution.
- **Spiral** -- A spiral distribution following the [density wave theory](https://physicsfeed.com/post/density-wave-theory-spiral-arms/) of spiral arms.
- **Logarithmic spiral** -- A logarithmic spiral.
- **Bar** -- A bar.
- **Ellipsoid** -- Uniformly distributed ellipsoid with two eccentricities.
- **Cone** -- A cone distribution.
- **Irregular** -- Irregular shape.

The results are visualized in a grid of galaxy images, as shown above. The images represent various types of galaxies based on the Hubble sequence, which includes elliptical, spiral, and irregular galaxies. The generated visualizations provide a clear representation of how different components (stars, gas, dust) contribute to the overall structure of a galaxy.

## Interface

In order to play around with the generation and make fine adjustments to galaxies, we provide a comprehensive graphical user interface in Gaia Sky itself. From it, one can modify virtually all parameters that go into the generation. There is a section at the top to define the global properties of the galaxy (size, transformation, morphology, etc.), and then there are collapsible panes for each of the channels. New channels can be added, and existing channels can be deleted. Each channel contains the attributes of the chosen distribution for the channel.

{{< fig src="img/2025/11/procedural-galaxy-ui.jpg" class="fig-center fig-post" title="Procedural galaxy generation window." loading="lazy" >}}


As mentioned, this is still work in progress. The system is being developed in the [compute branch](https://codeberg.org/gaiasky/gaiasky/src/branch/compute) of our repository. ~~The procedural galaxy generation system is based on compute shaders, so sadly macOS is not supported.~~ *Edit:* The procedural galaxy generation system uses compute shaders for optimal performance, while providing a CPU-based fallback path for compatibility with systems that do not support OpenGL 4.3 or later--most notably, macOS.
