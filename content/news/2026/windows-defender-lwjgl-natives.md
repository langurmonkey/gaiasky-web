---
title: "Windows Defender false positive for LWJGL 3.3.4 in Gaia Sky 3.8.0"
date: 2026-10-05
author: "tsagrista"
tags: ["security", "disclosure", "natives", "lwjgl"]
category: "Announcements"
draft: false
---

We have received reports that Windows Defender may detect the file `lwjgl-3.3.4-natives-windows-x86.jar` included with Gaia Sky as a threat.

We investigated the issue and found strong evidence that this is a **false positive affecting the upstream LWJGL 3.3.4 library**. The LWJGL project has an issue documenting antivirus detections of its 3.3.4 release, including a `Trojan:Win32/Vigorf.A` detection by Windows Security:

<https://github.com/LWJGL/lwjgl3/issues/1005>

Similar reports were also made by users of [Necesse](https://store.steampowered.com/app/1169040/Necesse/), another application using LWJGL. In that case, antivirus software specifically detected the same `lwjgl-3.3.4-natives-windows-x86.jar` file. The developers subsequently removed the file because it is only needed for 32-bit Windows:

<https://steamcommunity.com/app/1169040/discussions/0/4840896797471293566/>

As an additional check, we downloaded the LWJGL library directly from Maven Central and compared it with the copy included in Gaia Sky. The files are identical byte-for-byte, including their SHA-256 checksum. The file shipped with Gaia Sky is therefore the official LWJGL artifact and has not been modified by our build process.

---

This issue made us detect a real bug in our build process: The affected file contains the Windows x86 (32-bit) native libraries, but Gaia Sky **does not support 32-bit Windows**, and this file is never used by Gaia Sky.

If you already have this file in your Gaia Sky installation, it can safely be quarantined or removed.

Removing it does not affect Gaia Sky's operation. There is no need to add an antivirus exclusion for the file.

We have updated the Gaia Sky build process so that the unnecessary Windows x86 native library is no longer included in the base distribution. The other platform-specific native libraries remain in the distribution as before, since Gaia Sky uses the same base distribution to create packages for Windows, Linux, and macOS.

This means that future Gaia Sky releases will not contain the affected 32-bit Windows LWJGL library. We thank the users who reported this issue. The reports helped us identify both the false positive in the upstream LWJGL library and an unnecessary file in our own distribution.

