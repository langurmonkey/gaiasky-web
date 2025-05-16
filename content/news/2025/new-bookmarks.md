---
title: "New features in bookmarks"
description: "Location bookmarks level up making them more versatile"
date: 2025-04-14
draft: false
categories: ["devlog"]
tags: ["bookmarks", "session", "focus", "settings"]
author: "tsagrista"
---

We’ve just leveled up bookmarks in Gaia Sky! As of the latest update, location bookmarks are no longer limited to just camera position, orientation, and time. Now, they can **also store the full settings file** and the **focus object** — giving you a complete snapshot of your session. Additionally, on creation the user may choose what elements to persist as part of the bookmark.

This means that when you load a bookmark, Gaia Sky can restore **not only where you were**, but also **how things were configured** and **what object you were focused on**. Whether you’re setting up a custom visualization, preparing a presentation, or just exploring the cosmos, your environment can now be fully restored with a single click.

What’s more: all bookmark fields (except for the name) are now optional — you can selectively store in your bookmark only what matters to you.

{{< fig src="img/2025/04/new-location-bookmark.jpg" class="fig-center fig-post" title="The new location bookmark dialog allows for the selection of the elements to persist." loading="lazy" >}}

To learn more, check out the [Bookmarks documentation](https://gaia.ari.uni-heidelberg.de/gaiasky/docs/master/Bookmarks.html).

The new feature will make it into the next Gaia Sky release. As always, you can already test it by [running Gaia Sky from source](https://gaia.ari.uni-heidelberg.de/gaiasky/docs/master/Installation.html#run-from-source).

