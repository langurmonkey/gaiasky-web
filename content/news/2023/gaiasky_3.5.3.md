+++
title = "Gaia Sky 3.5.3"
date = "2023-09-14T12:31:00"
tags = ["release"]
author = "tsagrista"
categories = ["release", "version"]
+++

📢 Gaia Sky 3.5.3 available now!

<!--more-->


## Features
- use quaternion spherical linear interpolation for the camera orientation when exporting keyframes. The old setting 'camrecorder > keyframe > orientation' is not used anymore. 
- use quaternion interpolation for the camera transition methods in the scripting API implementation. 
- add direct playback capability to camera keyframe system. 
- keyframe system to use new camera path object in export operation. 
- add skip back/fwd, step back/fwd, play/pause buttons and timeline slider. 
- move keyframes logic and model to keyframe manager. 
- add tooltips to keyframe playback buttons. 
- add check for keyframe timings (t_kf * fps % 1 == 0) and respective notice. 
- add new visibility type 'Keyframes', which controls the keyframe points and lines. Add new keyboard mapping SHIFT+K to toggle it. 
- move `onlyBody` trajectory attribute to `bodyRepresentation`, which is an enum that enables the representation of only body, only orbit or both. The `onlyBody` attribute is still kept as a proxy. Rename `pointColor` to `bodyColor` in trajectories. `pointColor` is kept as an alias. 
- move from buffered file-backed recording and playback to model-backed solutions for the camrecorder. This means that, during recording, the data is captured and stored in memory and persisted to disk when the recording finishes. During playback, the data is loaded to memory at once at the beginning and played from there. 
- new welcome screen title design and splash. 

## Bug Fixes
- mismatch in bundled JRE versions in install4j script. Fixes [#737](https://codeberg.org/gaiasky/gaiasky/issues/737). 
- clean editing keyframe on deletion. Fixes [#734](https://codeberg.org/gaiasky/gaiasky/issues/734). 
- check keyboard focus state when polling cursors in main mouse/kdb listener. Fixes [#733](https://codeberg.org/gaiasky/gaiasky/issues/733). 
- exit JVM process with a proper status code depending on application state. 
- glitches and artifacts in atmosphere ground tessellation shader. 
- base opacity applied to model bodies when rendered as billboards. 
- update minimum required JRE in install4j script to 15. Fix version tag. 
- use camrecorder target frame rate instead of frame output system one in keyframes. 
- raymarching event description. 
- small improvements in UCD parser for IDs and magnitudes. 
- do not preemptively check display resolution in macOS, as it usually runs a headless JVM. 
- do not render keyframe lines/points when camcorder is playing. Fix index issue in path linear interpolator. Fixes [#735](https://codeberg.org/gaiasky/gaiasky/issues/735). 
- atmosphere object distance falloff. 

## Merge Requests
- Merge branch 'keyframes'


You can get this release in [our repository](https://gaia.ari.uni-heidelberg.de/gaiasky/releases//3.5.3.d076b1659/).