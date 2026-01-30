---
title: "Gaia Sky VR on Linux"
description: "Some tips as to how to best run Gaia Sky VR on Linux."
date: 2026-01-30
tags: ["VR", "Linux", "Valve Index", "NVIDIA", "OpenXR"]
author: "tsagrsita"
---

Running VR on Linux is notoriously "experimental," especially when mixing NVIDIA hardware with Wayland-native compositors like Hyprland. However, using the **Valve Index** via the open-source **Monado** runtime is now fully viable for Gaia Sky. 

Based on our recent testing, here is how to achieve a stable, high-performance, and color-accurate VR experience.

## Prerequisites

1.  **Monado Service**: The open-source OpenXR runtime (`paru -S monado` on Arch).
2.  **libsurvive**: For lighthouse and headset tracking.
3.  **xr-hardware**: Ensure your udev rules are installed (`paru -S xr-hardware` on Arch).

## The "Direct Mode" challenge

On NVIDIA hardware, Monado may attempt to use an X11-based "Direct Mode" that crashes on Wayland with a `vkAcquireXlibDisplayEXT` error. To fix this, you must force Monado to use the **Wayland DRM Lease** protocol.

### Optimized launch script

I have prepared a `justfile` to handle the environment variables correctly. This setup bypasses the crashing NVIDIA backend and fixes the "washed out" color issues common on Pascal (10-series) cards.

```justfile
monado-clean:
	-killall -9 monado-service vrcompositor vrmonitor survive-cli
	-rm -f /run/user/1000/monado_comp_ipc

monado: monado-clean
	env XRT_COMPOSITOR_FORCE_NVIDIA=0 \
	   XRT_COMPOSITOR_FORCE_WAYLAND_DIRECT=1 \
	   XRT_COMPOSITOR_FORCE_SRGB=1 \
	   SURVIVE_GLOBALSCENESOLVER=0 \
	   monado-service

monado-debug: monado-clean
	env XRT_COMPOSITOR_FORCE_NVIDIA=0 \
	   XRT_COMPOSITOR_FORCE_XCB=0 \
	   XRT_COMPOSITOR_FORCE_WAYLAND_DIRECT=1 \
	   XRT_COMPOSITOR_FORCE_SRGB=1 \
	   XRT_VULKAN_FORMAT=VK_FORMAT_B8G8R8A8_SRGB \
	   XRT_COMPOSITOR_GAMMA=0.45 \
	   SURVIVE_GLOBALSCENESOLVER=0 \
	   monado-service
```

Using the `monado` task should be enough to start the monado service properly. Then, you can run Gaia Sky with:

```bash
env XR_RUNTIME_JSON=/usr/share/openxr/1/openxr_monado.json gaiasky -vr
```


