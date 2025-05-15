---
title: "Performance boost in 3.6.8"
subtitle: "Memory and CPU usage optimizations"
date: 2025-05-14
draft: false
categories: ["devlog"]
tags: ["performance", "cpu", "memory", "GC", "java"]
author: "tsagrista"
---

The upcoming release of **Gaia Sky 3.6.8** brings significant performance improvements, focusing on memory optimization and CPU usage reduction. In this post, we'll take a closer look at these enhancements and how they translate into smoother and faster performance.

<!--more-->

## Memory Usage Optimization

Gaia Sky 3.6.8 introduces multiple changes aimed at reducing memory footprint:

* **Quadruple Library Integration:** The `Apfloat` library has been replaced with `Quadruple`, a compact 128-bit floating point library that offers sufficient precision while minimizing memory allocations. It is also much faster! Find more details in [this blog post](https://tonisagrista.com/blog/2025/quadruple-joins-party/).
* **Data Structure Refinement:** Particle data holders (for particle and star sets) are now flattened into Java records, consolidating several data structures and eliminating unnecessary attributes.
* **Memory Compaction:** The `PointCloudData` and `ParticleRecord` classes have been refactored into compact records, reducing memory overhead.
* **16-bit Floating Point Usage:** Non-critical attributes, such as star magnitudes, now use 16-bit precision, striking a balance between precision and memory consumption.

Below are the heap memory usage comparisons between Gaia Sky 3.6.7 (top) and 3.6.8 (bottom):

{{< fig src="img/2025/05/release-heap.svg" class="fig-center fig-post" title="Heap memory usage for Gaia Sky 3.6.7 over a \~350 second session with the small Gaia DR3 dataset (\~1.9 M stars loaded). Notice that the heap grows very fast and the garbage collector needs to act very often. The base memory usage sits at around 1.33 GB." width="80%" loading="lazy" >}}
{{< fig src="img/2025/05/master-heap.svg" class="fig-center fig-post" title="Heap memory usage for Gaia Sky 3.6.8 over a \~350 second session with the small Gaia DR3 dataset (\~2.5 M stars loaded). Minimizing allocations helps the heap grow super slowly, with a lower baseline of \~0.95 GB. Only two garbage collections were recorded during this session." width="80%" loading="lazy" >}}

Note the much lower profile and drastically reduced garbage collector interventions (37 vs 2) in Gaia Sky 3.6.8. Observe that the allocated memory is now roughly half of what it used to be. Also, switching to the Generational ZGC caused the GC stops to go from \~10-100 ms to \~10 μs.  All this results in a higher latency, better memory utilization and more responsive experience.

## CPU Usage Reduction

Several optimizations have been implemented to reduce CPU load and improve frame rates:

* **Custom Data Structures:** Gaia Sky now uses `FastObjectIntMap` and `FastStringObjectMap` for the indices to eliminate the overhead of generic collections. This helps avoid allocating boxed `Integer`s and `Node`s, and perform much faster lookups.
* **Background Processing:** The background particle/star updater has been re-implemented from the ground up, leading to significant CPU savings.
* **Frame Distribution:** Metadata updates and sorting operations for star/particle sets are now spread across multiple frames to prevent frame spikes.
* **Generational ZGC:** The JRE has been upgraded to version 24, utilizing Generational ZGC by default. This modern garbage collector offers much shorter pauses and reduced latency.
* **Float-128 vs Apfloat:** One of the worse hot-spots in Gaia Sky has been the arbitrary floating-point arithmetic. So far, we've used `Apfloat`. In this release, we switched to `Quadruple`, a 128-float implementation that performs much [faster](https://tonisagrista.com/blog/2025/quadruple-joins-party/) that both `Apfloat` and `BigDecimal`.

Here are the CPU usage comparisons using `btop` for both versions:

{{< fig class="fig-center fig-post" src1="img/2025/05/gs-cpu-3.6.7.avif" type1="image/avif" src2="img/2025/05/gs-cpu-3.6.7.jxl" type2="image/jxl" src="img/2025/05/gs-cpu-3.6.7.jpg" title="CPU usage with Gaia Sky 3.6.7." width="80%" loading="lazy" >}}
{{< fig class="fig-center fig-post" src1="img/2025/05/gs-cpu-3.6.8.avif" type1="image/avif" src2="img/2025/05/gs-cpu-3.6.8.jxl" type2="image/jxl" src="img/2025/05/gs-cpu-3.6.8.jpg" title="CPU usage with Gaia Sky 3.6.8." width="80%" loading="lazy" >}}

Note the top image shows the CPU usage of Gaia Sky at 292%. This means that it is using 3 CPUs at full (the load is distributed between the 8 CPUs). At the bottom, I stopped version 3.6.7 and started version 3.6.8. You can see in the top pane the difference in CPU usage profile (annotated in red). The CPU usage sits at about 45% with Gaia Sky 3.6.8. A great improvement.
Curiously, and related to the previous section, the allocated memory in 3.6.7 sits at 6.2 GB, while it is below 3 GB in 3.6.8. The workload for both sessions was exactly the same, with the same datasets and settings.

## Conclusion

The performance improvements in Gaia Sky 3.6.8 not only make it more memory-efficient but also significantly reduce CPU overhead. The result is a smoother and more responsive experience, particularly for systems dealing with large datasets or multiple particle/star sets.

Stay tuned for the official release and explore these enhancements firsthand!
