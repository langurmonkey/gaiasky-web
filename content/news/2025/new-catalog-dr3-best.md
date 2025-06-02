---
title: "New Catalog: Gaia DR3 Best"
description: "Contains only the very best stars in terms of parallax relative error"
date: 2025-06-02
author: "Gaia Sky Team"
categories: ["Data", "Gaia DR3"]
tags: ["Gaia", "catalog", "parallax", "astrometry", "stars"]
author: "tsagrista"
---

Today we make available a brand new catalog in **Gaia Sky**, derived from the [Gaia Data Release 3 (DR3)](https://www.cosmos.esa.int/web/gaia/dr3) dataset. This catalog is a **handpicked collection of the most precise stellar measurements** available in DR3, designed for applications where **accuracy in parallax and astrometric fidelity** is essential. This catalog includes a total of 646,400 stars, with a clear bias toward brighter magnitudes. It is a small, non-LOD (non-Level-of-Detail) catalog, designed for broad compatibility. It will be the recommended star dataset starting from Gaia Sky 3.6.8.

 It is ideal for:

- Laptops
- VR
- Embedded systems
- Devices without dedicated GPUs
- Use cases where performance and simplicity matter more than completeness

<br>
{{< fig src1="img/2025/05/dr3-best-hammer.jxl" type1="image/jxl" src2="img/2025/05/dr3-best-hammer.avif" type2="image/avif" src="img/2025/05/dr3-best-hammer.jpg" class="fig-center fig-post" title="Hammer projection of the new Gaia DR3 Best catalog." width="70%" loading="lazy" >}}

<!--more-->

## What does it include?

The *Gaia DR3 Best* catalog includes:

- **646,400 stars**, carefully selected from the 1.8+ billion in Gaia DR3.
- All stars with **relative parallax error ≤ 0.4%** for bright stars (`gMag` < 13.1).
- All stars with **relative parallax error ≤ 0.002%** for faint stars (`gMag` >= 13.1).
- The full set of **Hipparcos** stars, cross-matched and merged into the dataset.

This makes it ideal for high-precision visualization, distance estimation, nearby star studies, or any work requiring only the cleanest subset of the Gaia DR3 catalog.

## Why another Gaia catalog?

Gaia DR3 is a treasure trove, but not all stars are created equal when it comes to measurement quality. This dataset is **suitable for low-end devices**, and distills the **most trustworthy data** from the full release, eliminating sources with:

- Negative or low-quality parallaxes
- Non-finite magnitudes
- Poor astrometric solutions

Here's a breakdown of how we got from 1.8 billion stars to 646k:

| Step | Count |
|------|-------|
| Initial Gaia DR3 entries | 1,811,709,771 |
| Rejected due to parallax (criteria + negatives) | 1,805,626,704 |
| Rejected due to non-finite magnitude | 5,455,190 |
| Final stars selected | **646,400** |

This dataset loads fast, uses less memory, and is *visually cleaner* in 3D than the full Gaia DR3 catalog.

## Magnitude distribution

The stars span a wide range of magnitudes, with the majority in the range **8 to 12**. Here's a snippet of the magnitude histogram:


{{< fig src="img/2025/05/dr3-best-histogram.png" class="fig-center fig-post" title="Magnitude distribution of Gaia DR3 Best catalog." width="90%" loading="lazy" >}}

{{< details title="Click for raw data" >}}
| Magnitude | Count   | Percentage |
| --------- | ------- | ---------- |
| 0         | 20      | 0.003%     |
| 1         | 49      | 0.007%     |
| 2         | 257     | 0.034%     |
| 3         | 994     | 0.133%     |
| 4         | 3,347   | 0.449%     |
| 5         | 9,839   | 1.319%     |
| 6         | 27,198  | 3.647%     |
| 7         | 60,012  | 8.046%     |
| 8         | 90,040  | 12.072%    |
| 9         | 91,461  | 12.263%    |
| 10        | 107,119 | 14.362%    |
| 11        | 152,413 | 20.435%    |
| 12        | 199,507 | 26.750%    |
| 13        | 3,546   | 0.475%     |
| 14        | 5       | 0.001%     |
| 15        | 2       | 0.000%     |
| 16        | 3       | 0.000%     |
| 17        | 11      | 0.001%     |
| 18        | 4       | 0.001%     |
| 19        | 3       | 0.000%     |
| 20        | 1       | 0.000%     |
| 21        | 1       | 0.000%     |
{{< /details >}}

As expected, the catalog skews toward brighter stars with more accurate parallaxes.

## Technical notes

- Catalog size: **~54.5 MB**
- Epoch: **J2016**
- Format: **Gaia Sky binary octree**
- Tree depth: **1** (single octant for all stars)
- Max distance: **100,000 parsecs**

You can find the dataset under the key `gaia-dr3-best` in the Gaia Sky catalog selector. The full path in disk is:

```bash
$data/catalog-gaia-dr3-best
```

Direct download: [Gaia DR3 Best Catalog](https://gaia.ari.uni-heidelberg.de/gaiasky/files/repository/catalog/dr3/014-best/v01_20250530/)

## Use cases

This catalog is especially suited for:

- Running **Gaia Sky** on lower-end machines without sacrificing precision
- Creating **interactive educational content**
- Building **realistic local universe models**
- Studying **nearby star neighborhoods**

{{< vid src="vid/2025/dr3-best.mp4" poster="vid/2025/dr3-best.jpg" class="fig-center vid-post" title="Short video showcasing the Gaia DR3 Best catalog in Gaia Sky." >}}
