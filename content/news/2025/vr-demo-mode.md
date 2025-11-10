+++
title = "Gaia Sky VR Demo Mode"
date = "2025-11-10"
description = "A new Demo Mode in Gaia Sky VR locks down controls to prevent common user errors during public demonstrations and outreach events."
author = "tsagrista"
categories = ["vr"]
tags = ["demo-mode", "vr", "controls", "outreach", "public-demo"]
+++

Last Saturday, at the [16. Koblenzer Nacht der Technik](https://www.hwk-koblenz.de/artikel/16-koblenzer-nacht-der-technik-am-8-november-2025-52,0,181.html), we had the opportunity to present Gaia Sky VR to a large and enthusiastic audience. With big queues forming and a constant stream of people eager to try the experience, we were presented with a perfect, real-world test lab. We learned a good amount by watching so many first-time users interact with the cosmos in VR. One lesson became crystal clear: the standard control scheme, while powerful for experienced users, can be a source of confusion during fast-paced public demos.

This direct experience led us to introduce a new feature for VR: **Demo Mode**.

Public demonstrations of virtual reality usually come with unique challenges. When a new user puts on the headset for the first time, their unfamiliarity with the controllers can lead to unintended actions, breaking the flow of your presentation and potentially causing confusion.

Based on feedback we received, we've identified two common pain points:

1. **Accidental Lateral Movement**: Users inadvertently pushing the joystick sideways, causing unexpected and often disorienting lateral drifts instead of a smooth forward or backward motion.

2. **Unintended Button Presses**: Users accidentally pulling the trigger or pressing buttons, leading to the selection of random objects, toggling of visibility filters, or bringing up the in-world UI at inopportune times.

When activated, Demo mode restricts the controller inputs to create a more curated and foolproof experience:

- **Restricted Joystick Movement**: The X-axis (left and right) on the VR controller joysticks is disabled. Users can only move forwards and backwards along the direction their controller is pointing. This makes it significantly easier for you, the presenter, to guide users toward a specific star, planet, or galaxy without them accidentally veering off course.

- **Controller Buttons Disabled**:All actions mapped to the VR controllers (triggers, grips, menu buttons, etc.) are temporarily deactivated. This prevents users from accidentally selecting objects, opening menus, or changing settings, ensuring your narrative remains the focus.

The result is a streamlined, "kiosk-like" experience where you can confidently hand over the headset, knowing that the user's exploration will be focused and free from disruptive misclicks.

## How to activate demo mode

Enabling Demo Mode is simple. You can activate it in two places:

- **Welcome Screen**: On the initial welcome GUI, simply check the "VR demo mode" checkbox before entering the simulation.

- **Settings Menu**: You can also toggle it on the fly from the main Settings window, under the Controls section.

{{< fig src="img/2025/11/vr-demo-mode.jpg" width="70%" class="fig-center fig-post" title="Activate Demo Mode right from the welcome screen for a hassle-free session from the start." loading="lazy" >}}

We hope this new feature makes your public outreach with Gaia Sky VR smoother. It will be available in the next public release of Gaia Sky.

As always, we welcome your feedback. If you have suggestions for further improvements or run into any issues, please let us know.
