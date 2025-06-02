+++
title = "Gaia Sky 3.6.8"
description = "Tons of new features and improvements"
date = 2025-06-02
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

Today we release **Gaia Sky 3.6.8**. It brings a major UI refresh, significant performance improvements, and many new features and bug fixes. Keep reading to know more.

{{< fig src1="img/2025/05/3.6.8-release.jxl" type1="image/jxl" src2="img/2025/05/3.6.8-release.avif" type2="image/avif" src="img/2025/05/3.6.8-release.jpg" class="fig-center fig-post" title="The new welcome window in Gaia Sky 3.6.8." width="70%" loading="lazy" >}}
<!--more-->

## New Features & Improvements

### User Interface
- Major UI overhaul: consolidated fonts, updated themes, removed deprecated components.
- Improved visual quality: increased padding and higher image resolution in UI.
- Switched to Inter as the default label font.
- Panels in the main UI now expand when the mouse hovers over the buttons.
- Welcome window enhancements:
  - Displays the list of enabled datasets.
  - New *"Recommended Datasets"* option for one-click download and launch.
  - Updated background image.

### Usability Enhancements
- Time and calendar:
  - Julian date tab added to date/time dialog.
  - Time zone support improved; system-default time zone now used.
- Dialogs remember the last opened tab (e.g. Preferences, About).
- New star texture selector added to Preferences.
- New object debug tool available via the debug panel—inspect and edit component fields.
- Pointer coordinates display disabled by default (can be re-enabled in Preferences).
- Console output:
  - Messages and full log can now be copied to the clipboard.
- Bookmark improvements:
  - Bookmarks can now include camera position, orientation, time, and settings.
  - Bookmark information dialog added (accessible via right-click).
  - Empty folder bookmarks are removed automatically.
  - Bookmark operations persist immediately.
  - Invalid characters are now restricted in bookmark and folder names.
  - See [this blog post](/news/2025/new-bookmarks).

### API & Scripting
- Added:
  - `setCameraDirectionEquatorial()` and `setCameraDirectionGalactic()`
  - Enhanced `goToObjectSmooth()` with solid angle and sync options
- Stars and particles now support a new shading style: `default` or `twinkle`.
- Added Thiele-Innes conversion script and support in the Gaia NSS processor.

---

## Bug Fixes

- Fixed incorrect formatting of uptime duration.
- Julian vs Gregorian calendar automatically selected based on date.
- Fixed layout issues in Preferences and other dialogs.
- UI components:
  - Image button alignment corrected.
  - Anchoring of the top info interface improved to prevent jitter.
  - First UI text size adjusted.
- Fixed crash when setting data directory to a root drive in Windows ([#825](https://codeberg.org/gaiasky/gaiasky/issues/825)).
- Fixed crash due to early resolution of `attitudeindicator.png` path when changing data directory ([#795](https://codeberg.org/gaiasky/gaiasky/issues/795)).
- Improved orbit rendering:
  - Constant true anomaly spacing used for high-eccentricity orbits.
  - Better handling of edge cases in Keplerian-to-Cartesian conversion.
- Reused GZipped file streams no longer break on non-gzipped JSON files.
- Context menu in bookmarks pane now positioned correctly.
- Error window layout made consistent.
- Visibility dialog now properly handles 'Invisible' object types.

---

## Performance Improvements

- Replaced `Apfloat` with `Quadruple`: faster 128-bit floating point math with adequate precision. See [this](https://tonisagrista.com/blog/2025/quadruple-joins-party/) and [this](https://tonisagrista.com/blog/2025/quadruple-joins-party/) for some performance benchmarks.
- Reduced short-lived object allocations in many systems.
- Major speed-up in label rendering via task refactoring.
- Star size factors now cached instead of recalculated per frame.
- Internal maps replaced with faster, boxing-free versions.
- Half-precision (16-bit) floats now used for non-critical star/particle magnitudes.
- Particle updates split over multiple frames to reduce frame drops.
- Old particle and variable record types unified into a compact, immutable `Particle` record.
- `PointCloudData` reimplemented using records with a more compact memory footprint.

[This blog post](/news/2025/performance-improvements) covers some of these performance improvements in more detail.

---

## Code Refactoring

- Removed duplicate star/particle index arrays.
- Replaced boxed integers with primitives.
- Top-K particle sorting now uses a priority queue.
- All shader files renamed to use the `.glsl` extension.

---

## Build System

- Upgraded to libGDX 1.13.5.
- Default builds now use JRE 24 with Generational ZGC for lower latency.
- Java source compatibility updated from 17 to 20.
- Gradle upgraded to 8.13.
- Install4j AUR package URL updated to `gaiasky.space`.
- Added test infrastructure:
  - Includes tests for Keplerian-to-Cartesian conversions.
  - Enabled JUnit dependencies.
- `gdx-tools` moved to compile-only dependency.
- Enabled logging for Gradle test runs.

---

## Documentation

- Improved descriptions for many fields in the attribute map JSON file.

---

## Merge Requests

- Merged `quadruple` branch (128-bit math support).
- Merged `particle-update-refactor` branch (particle update system overhaul).
