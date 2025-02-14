+++
title = "New Flatpak app ID"
description = "We have a new app ID for our Flatpak package"
date = "2025-02-14T08:20:02"
tags = ["flatpak", "appid", "linux"]
author = "tsagrista"
categories = ["Flatpak"]
+++

Our Flatpak package, published via [Flathub](https://flathub.org), has been updated to a new app ID `space.gaiasky.GaiaSky`. This has been done to match the domain of our new website [gaiasky.space](https://gaiasky.space). Additionally, this has enabled us to verify the application, which was impossible with the old `de.uni_heidelberg.zah.GaiaSky` ID, as we did not control that domain.

{{< fig src="img/2025/02/flathub.jpg" class="fig-center fig-post" title="Gaia Sky is now veryfied on Flathub." loading="lazy" >}}

Essentially, I needed to contact the [uni-heidelberg.de](https://uni-heidelberg.de) domain owner and ask them to add their domain to a PSL (public suffix list). They were initially cooperative, but after a few department redirections my requests must have fallen down the bureaucracy cracks, for they stopped being responsive. If you want the full story, check out [this issue](https://github.com/flathub/de.uni_heidelberg.zah.GaiaSky/issues/57), and [this one](https://github.com/flathub-infra/website/issues/3844). 

Anyway, creating a proper website for Gaia Sky was already on the to-do list. In fact, the  initial commit to the project was made [a long time ago](https://codeberg.org/gaiasky/gaiasky-web/commit/61d9802b4d9506920d53411a8e722062f2ef7eaf). Almost exactly 4 years ago, to be precise.
