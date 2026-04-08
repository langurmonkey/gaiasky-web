+++
title = "Gaia Sky 3.7.2"
description = "This version features new billboard shading types, a revamp in particle and orbital element groups, many user interface updates, new languages, and more."
date = 2026-04-08
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

Today is release day! We are proud to present **Gaia Sky 3.7.2**. This release contains many new features and bug fixes. We wrote [a post](/content/news/2026/3.7.2-new-features) covering most of them last week, so you may want to have a look at that. Nevertheless, below is a non exhaustive summary and further down a full list of all new features, bug fixes, and more.

- New shading types for billboards.
- Refactor of orbital element groups into particle groups.
- Dataset updates (FPR asteroids, Saturn rings).
- Anaglyph custom colors mode. 
- Logarithmic and reset UI sliders.
- New languages: Simplified Chinese, Japanese, Italian.
- OptFlowCam improvements.

If you want to know more, keep reading.

<!--more-->

## Billboard shading types

We have added three shading types to particle groups:

- `plain`---same old emissive shading.
  {{< fig src="img/2026/03/lighting-plain-thumb.jpg" link="/img/2026/03/lighting-plain.jpg" class="fig-center fig-post" title="Plain shading type. This was the only type we had up until now." loading="lazy" >}}
- `billboard_shading`---particles are shaded **uniformly** depending on the view and light directions. This creates the illusion of physical particles, especially when these are small.
  {{< fig src="img/2026/03/lighting-bb-thumb.jpg" link="/img/2026/03/lighting-bb.jpg" class="fig-center fig-post" title="In billboard shading type, particles are lit uniformly depending on their location with respect to the light." loading="lazy" >}}
- `spherical_shading`---particles are shaded using the Phong model as if they were spheres. Normals are computed for every fragment in the billboard, and light contributions are calculated according to those, taking into account the light and view vectors. This process shades the particles as if they were solid bodies.
  {{< fig src="img/2026/03/lighting-sph-thumb.jpg" link="/img/2026/03/lighting-sph.jpg" class="fig-center fig-post" title="Spherical shading approximates particles to a sphere and computes the resulting lighting. Here, flat billboards resemble bodies with volume." loading="lazy" >}}

## Orbital element groups refactor

We have merged orbital element groups into regular particle groups, consolidating the data model and gaining all the particle group goodies: filtering, indexing, focusing, texturing, and shading types.

- **Updated FPR asteroids catalog**---new version of FPR SSOs to use spherical lighting and textured particles.
{{< vid src="vid/2026/asteroids-dr3-video.s.mp4" poster="img/2026/03/gaia-sky-asteroids-dr3.jpg" class="fig-center vid-post" title="A trip through the asteroid belt with Gaia FPR data." caption="See the higher quality version on [YouTube](https://youtu.be/TF_PwZ8SncU)." >}}
- Add support for particle-based rings in ringed planets. This includes a number of refactorings and improvements.
- **Saturn rings**---new dataset containing 1.5 million particles of dust and rock in the rings of Saturn. They rotate realistically, as they were generated with physically plausible orbital elements.
{{< vid src="vid/2026/saturn-rings.ofc.speech.s.mp4" poster="img/2026/03/gaia-sky-saturn-rings.jpg" class="fig-center vid-post" title="Exploring the new Saturn rings dataset." caption="See the higher quality version on [YouTube](https://youtu.be/44bj9BdfvTk)." >}}
- **Diffuse scattering**---added the diffuse scattering property to particle groups, used in conjunction to global ambient light setting.
- Enable asteroids and other particle groups to use a different epoch per particle.


## Light glow effect rework

We have put some work into the star glow effect by adjusting its parameters and adding a time variability in the form of a polar mask.

- Add time-dependent polar mask to star glow effect. Update default star/glow texture indices and glow factor.
- Separate star from glow texture in settings. Add image next to select boxes to provide visual feedback about the selected textures.

{{< vid src="vid/2026/lightglow.mp4" poster="img/2026/04/light-glow-var.jpg" class="fig-center" title="Exploring the new Saturn rings dataset." caption="The time variability in the light glow effect." >}}

## Transparent handling of name conflicts

We have added a name conflicts window to inform the user of index conflicts in the current session. This prompted some dataset updates to make sure that there are no name conflicts in the essential catalogs:

- **Base dataset:** remove Lutetia and Steins. Fix typo in Hygie**i**a.
- **Asteroids/SSO FPR:** remove all objects that are already in the base dataset, which is always loaded (minor planets&mdash;Vesta, Ceres, Hygiea, Iris, ...&mdash;, and moons of Saturn, Jupiter, Uranus, and Neptune).
- **Nebulae:** fix internal naming issues and misnamed objects.
- **NEARGALCAT:** fix conflicts with constellation names by adding the " galaxy" suffix to some objects. Use procedural generation for Andromeda.

{{< fig src="img/2026/03/name-conflicts-thumb.jpg" link="/img/2026/03/name-conflicts.jpg" class="fig-center fig-post" title="The new name conflicts dialog pops up at startup if conflicts are detected." loading="lazy" >}}

## Internationalization and translations

We have received contributions to add Simplified Chinese, Italian, and Japanese (WIP) to the list of supported languages. We have also updated and completed the translation files for Slovenian, Turkish, and Russian.

{{< fig src="img/2026/03/sc-translation-thumb.jpg" link="/img/2026/03/sc-translation.jpg" class="fig-center fig-post" title="The user interface and objects can now be completely translated to Simplified Chinese." loading="lazy" >}}

## User interface updates

We have many user interface new features and updates:

- Move from static font files to `gdx-freetype` library. This enables us to support CJK languages and more.
- Remove monospace fonts from Gaia Sky UI and skin. They are used very sporadically and are not really needed.
- Maintain aspect ratio of background image in welcome and loading GUIs by letter-boxing.
- Add <kbd>Copy to clipboard</kbd> button to log window. Add text and icons to all buttons in the window.
- Read contributors from `CONTRIBUTORS.md` file instead of hardcoding the data in About Window.
- Add Mastodon and BlueSky icons and links in about window. Add tooltips with funding agencies' names.
- Update splash image. Add dark background to central table in loading GUI.
- Add <kbd>Overwrite</kbd> check box to file export dialogs.
- Use degrees for min/max particle size in dataset visual settings dialog.
- Improve reset sliders (sliders that have a button to reset their value).
- Directly connect events to sliders to handle updating/firing automatically.
- Move planetarium and cubemap settings to sliders from free-text input fields.
- Remember last camera file name in keyframes window to avoid having to enter it every time.
- Use reset sliders in settings window, and camera/visual settings panes.

## Stereoscopic and anaglyph 3D

We have added a new anaglyph profile which lets the user select custom colors for the left and right images. 

{{< fig src="img/2026/03/anaglyph-custom-thumb.jpg" link="/img/2026/03/anaglyph-custom.jpg" class="fig-center fig-post" title="In the new custom anaglyph mode, the user can pick and choose the colors for the left and right eyes." loading="lazy" >}}

## Camcorder and OptFlowCam export

We have fixed some bugs with the CatMullRom splines in the OptFlowCam export script that fix camera orientation discontinuities. This export method should now be much more reliable. Additionally, we have replaced the old manual dependency management with `uv`, which is faster and more secure.

## Dataset management

We have implemented a mechanism to mark datasets as obsolete or outdated whenever a newer, better dataset comes around. In the same fashion, we added `replaces` and `replacedBy` properties to dataset descriptors, so that the user is informed. Finally, we cross-check these new fields for both local and server datasets to ensure consistency.

## Bug Fixes

Please, refer to the [bug fixes section](/downloads/releases/v3.7.2/#bug-fixes) of the release changelog for the full list of bug fixes included in this version.
 
## More

See the [full changelog for 3.7.2](/downloads/releases/v3.7.2/#release-notes) for the full list of features, fixes, and more.

**You can grab the latest installer from the [downloads page](/downloads).**
