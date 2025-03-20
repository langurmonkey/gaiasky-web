+++
title = "Towards smoother interstellar trips"
date = "2025-03-20T12:50:55Z"
tags = ["dev", "story"]
author = "tsagrista"
categories = ["devlog"]
math = true
+++

One of the items in our roadmap has long been the re-implementation of the speed scaling algorithm. This algorithm is a function that, given the current state of Gaia Sky, returns a number by which to scale the camera speed.

So far, we have used a pure function that only takes into account the distance to the focus object when the camera is in focus mode, or the distance to the closest object to the camera when it is in any other mode. This does not work very well in many situations. In this post, I explore the new developments in Gaia Sky that enable smoother interstellar trips by means of the camera speed scaling. 

<!--more-->

## The problem

The main issue with the current method is that its only dependency on the distance to the focus object makes it ignore all the (possibly closer to the camera) objects. We compute it like this,
$$
d_s = d_f * K,
$$

where \\(d_s\\) is the distance scale, \\(d_f\\) is the distance to the focus, and \\(K\\) is a constant.

Picture this: we are focused on Phobos in the Solar System, and the moon is in full view of our camera. In the background we spot an interesting star. We double-click on it to focus it, and then we click on the "Go to" button in the focus pane. With the current implementation, Phobos, Mars, and the entirety of the Solar System disappear in the first frame, because the first step towards our star focus is too large. This is because we are very far away from the star, and the speed scaling only depends on this distance. The speed is set to very high, so we are instantly thrown out of the Solar System.

{{< fig src="img/2025/03/frames.svg" class="fig-center fig-post" title="The problem with the current speed scaling. Note how the first frame is already well outside the Solar System." loading="lazy" >}}

How do we solve this?

## The solution

The first obvious solution is to *take into account objects other than the focus*. One possible solution is to compute the local density of objects in an arbitrary volume around the camera, but this is probably overkill. Another solution might be setting up the closest object to the camera with a smoothing radius, and mix its distance with that of the focus:

\begin{aligned}
d_s & = mix(d_c, d_f, a) \\\
a & = \frac{d_c - d_0}{d_1 - d_0},
\end{aligned}

where \\(d_c\\) is the distance to the closest object, and \\(d_0\\) and \\(d_1\\) define the smoothing radius outer and inner bounds. When the camera is further away from the closest object than \\(d_1\\), only the focus distance is used. When  the camera is closer to the object than \\(d_0\\), only the distance to the closest object is use. In between the two smoothing distances, a mix of both is used.

This method gives us a rather smooth transition from object to object. The camera is usually hooked to a single object, which may be the focus or the closest object. In the case that the camera is between \\(d_0\\) and \\(d_1\\) from the closest object, we mix the contributions to avoid stark transitions in speed.

The video below compares the old and the new methods:

{{< vid src="vid/2025/speed-scaling-comparison.mp4" poster="vid/2025/speed-scaling-comparison.jpg" class="fig-center vid-post" title="Comparison between the old method, based on focus distance, and the new method, that takes into account other objects." >}}


## Transition-based trips

The [Gaia Sky API](https://gaia.ari.uni-heidelberg.de/gaiasky/docs/javadoc/latest/gaiasky/script/IScriptingInterface.html) contains some methods to create frame-accurate camera transitions in both position and orientation. Those are smooth by design, as they can use [logit](https://en.wikipedia.org/wiki/Logit) and [logistic sigmoid](https://en.wikipedia.org/wiki/Logistic_function) mapping functions.

These methods interpolate the camera state (position, direction, and up vectors) from the current state to a user-defined final state. They do so in a provided amount of time, and using the provided mapping function. They end up calling something like this:

```java
void cameraTransition(double[] camPos,
                       String units,
                       double[] camDir,
                       double[] camUp,
                       double positionDurationSeconds,
                       String positionSmoothType,
                       double positionSmoothFactor,
                       double orientationDurationSeconds,
                       String orientationSmoothType,
                       double orientationSmoothFactor,
                       boolean sync)
```

[Here](https://gaia.ari.uni-heidelberg.de/gaiasky/docs/javadoc/latest/gaiasky/script/IScriptingInterface.html#cameraTransition(double[],java.lang.String,double[],double[],double,java.lang.String,double,double,java.lang.String,double,boolean)) is the documentation. For completion, the parameters are as follows:

- ``camPos`` -- final camera position.
- ``units`` -- final camera position units.
- ``camDir`` -- final camera direction vector.
- ``camUp`` -- final camera up vector.
- ``positionDurationSeconds`` -- duration of transition in position, in seconds.
- ``positionSmoothType`` -- mapping function, either "logisticsigmoid" or "logit".
- ``positionSmoothFactor`` -- smoothing factor for the mapping function.
- ``orientationDurationSeconds`` -- duration of the transition in orientation, in seconds.
- ``orientationSmoothType`` -- mapping function, either "logisticsigmoid" or "logit".
- ``orientationSmoothFactor`` -- smoothing factor for the mapping function.
- ``sync`` -- whether to run in synchronous mode, or return immediately and run asynchronously.

### Smooth go-to-object API call

Since we already have the ``goToObject(name)`` API call, which uses the regular speed scaling-based method described in the previous sections, I thought I would take advantage of the already implemented transitions and spin up a *better* go-to. I called it ``goToObjectSmooth(name, posDuration, orientationDuration)`` [[API reference](https://gaia.ari.uni-heidelberg.de/gaiasky/docs/javadoc/latest/gaiasky/script/IScriptingInterface.html#goToObjectSmooth(java.lang.String,double,double))]. This method uses camera transitions internally, and produces a fundamentally different result than its plain ``goToObject()`` counterpart. I happen to think that produces better results in most cases.

Here is a comparison video with both methods.

{{< vid src="vid/2025/goto-smooth.mp4" poster="vid/2025/goto-smooth.jpg" class="fig-center vid-post" title="The new goToObjectSmooth() API call produces a more pleasant trip from start to finish." >}}
