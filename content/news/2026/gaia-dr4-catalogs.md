---
title: "Gaia DR4 star catalogs in Gaia Sky"
date: 2026-09-24
author: "tsagrista"
tags: ["datasets", "catalogs", "data", "dr4", "gaiadr4"]
category: "Catalogs"
draft: false
---

In a little over a month, on December 2, [Gaia Data Release 4 (DR4)](https://www.cosmos.esa.int/en/web/gaia/data-release-4) will be made public. This data release will bring a new generation of star catalogs to Gaia Sky. Along with the release of DR4, we have taken the opportunity to simplify the way the Gaia catalogs are selected and presented.

The main changes are simple:

- **Fewer catalogs**
- **Clearer names**
- **Transparent relationship between catalog size and selection criteria**

In Gaia DR3, Gaia Sky offered a large collection of catalogs with names such as `tiny`, `weeny`, `small`, `medium`, `large`, `very large`, and `extra large`. While these names distinguished the datasets, they did not tell users how many stars they actually contained or what made one selection different from another.

For DR4, we have replaced this collection with a smaller set of **8 catalogs**, using names that indicate their approximate number of stars. This makes it easier to understand the available choices at a glance and to select a dataset according to the desired balance between catalog size, astrometric quality, and graphics-memory requirements.

## The new Gaia DR4 catalogs

The provisional selection currently consists of the following catalogs:

| Catalog name | Approx. stars | Selection |
|---|---:|---|
| **Gaia DR4 1M** | ~1+ million | Very precise parallaxes |
| **Gaia DR4 2M** | ~2 million | Very precise parallaxes, with more stars |
| **Gaia DR4 4M (LOD)** | ~4+ million | Higher star count, parallax-based selection |
| **Gaia DR4 14M (LOD)** | ~14 million | Large parallax-based selection |
| **Gaia DR4 850M (LOD)** | ~850 million | Very large, highly inclusive selection |
| **Gaia DR4 Bright, 10M (LOD)** | ~10 million | Selection focused on bright stars |
| **Gaia DR4 RUWE, 1.1B (LOD)** | ~1.1 billion | Stars satisfying a RUWE quality criterion |
| **Gaia DR4 GSP-Phot, 990M (LOD)** | ~990 million | Stars with GSP-Phot photometric distances |

The numbers in the names are approximate and are intended to give users an immediate idea of the size of each dataset. The actual number of stars can (and will) vary as the catalogs are processed and finalized.

### 1M: compact and very precise

**Gaia DR4 1M** is the default Gaia dataset in Gaia Sky. It contains around one million stars selected for particularly precise parallax measurements, together with all Hipparcos stars.

The selection is intentionally compact, making it suitable as a default dataset while providing high-quality geometric distances. Unlike the larger level-of-detail (LOD) catalogs, the complete catalog is loaded into graphics memory.

- This dataset replaces the Gaia DR3 **best** catalog.

### 2M: more stars, still very precise

**Gaia DR4 2M** contains around two million stars. It relaxes the parallax-precision selection compared with 1M in order to include more stars, while still maintaining a strict selection based on relative parallax error.

- This catalog replaces **both** the Gaia DR3 **weeny** and **tiny** catalogs, consolidating two of the smaller DR3 selections into a single, more clearly named dataset.

### 4M: a larger LOD catalog

**Gaia DR4 4M (LOD)** contains around four million stars selected according to parallax precision.

Unlike 1M and 2M, it uses Gaia Sky's LOD system. The catalog is divided into spatial sections and loaded progressively as required, so the complete dataset does not need to reside in graphics memory at once.

- The 4M catalog replaces the Gaia DR3 **small** catalog.

### 14M: the main large parallax catalog

**Gaia DR4 14M (LOD)** contains around fourteen million stars. It provides a substantially larger stellar sample, particularly at fainter magnitudes, while retaining a selection based on relative parallax precision.

As a LOD catalog, it can handle a considerably larger number of stars without requiring enough graphics memory to load the complete dataset simultaneously.

- The 14M catalog replaces the Gaia DR3 **default** catalog.

### 850M: very large stellar population

At the other end of the scale, **Gaia DR4 850M (LOD)** contains around 850 million stars.

This catalog uses a deliberately very permissive relative-parallax-error threshold resulting in a highly inclusive sample. Many stars in this selection therefore have substantial parallax uncertainties and should not be interpreted as having precise geometric distances. Its main purpose is to provide a very dense representation of the stellar population.

The LOD system is essential at this scale, allowing Gaia Sky to stream the required portions of the catalog rather than loading hundreds of millions of stars into graphics memory simultaneously.

- The 850M catalog consolidates the Gaia DR3 **very large** and **extra large** catalogs.

### Bright: a dedicated bright-star selection

**Gaia DR4 Bright, 10M (LOD)** contains around ten million stars and is designed to provide a relatively dense representation of the brighter stellar population.

It uses a different parallax-error selection for bright and faint stars and, like the other large catalogs, uses LOD to keep graphics-memory requirements manageable.

- This catalog replaces the Gaia DR3 **bright** catalog.

### RUWE: astrometric quality rather than parallax precision

**Gaia DR4 RUWE, 1.1B (LOD)** contains around 1.1 billion stars satisfying a RUWE (re-normalized unit weight error) criterion of 1.4 or less, together with all Hipparcos stars.

RUWE measures the quality of Gaia's astrometric solution rather than directly selecting stars according to the precision of their parallaxes. This makes the catalog complementary to the parallax-error-based selections above. A low RUWE indicates that the observations are in comparatively good agreement with the adopted astrometric model, but it does not by itself imply a highly precise parallax.

- The DR4 RUWE catalog replaces the Gaia DR3 **RUWE** catalog.

### GSP-Phot: an alternative to parallax distances

**Gaia DR4 GSP-Phot, 990M (LOD)** contains around 990 million stars with photometric distances from the GSP-Phot Aeneas best library, derived from Gaia BP/RP spectra.

Unlike geometric distances derived from parallaxes, these distances are inferred from the observed spectral energy distribution by estimating stellar properties and intrinsic luminosity and comparing them with the observed flux. They therefore provide a complementary distance estimate, particularly for stars whose parallaxes have large relative uncertainties.

- The catalog replaces the Gaia DR3 **photometric distances** catalog.

## What changed from Gaia DR3?

The biggest change is not simply the increase in the number of stars. It is the **simplification of the catalog selection**.

Gaia DR3 offered 14 Gaia catalog variants, ranging from *tiny* and *weeny* through *small*, *medium*, *large*, *very large*, and *extra large*, as well as specialized selections such as RUWE, fidelity, and different distance catalogs.

For DR4, we have reduced this to eight catalogs and consolidated several overlapping choices.

The main changes are:

- **1M replaces DR3 best.**
- **2M replaces both DR3 weeny and tiny**, giving users a single compact alternative with a slightly larger stellar sample.
- **4M replaces DR3 small.**
- **14M replaces DR3 default.**
- **850M replaces both DR3 very large and extra large.**
- **Bright replaces DR3 bright.**
- **RUWE replaces DR3 RUWE.**
- **GSP-Phot replaces DR3 photometric distances.**
- The DR3 **medium, large, extra small, fidelity, and Bayesian-distance** catalogs do not have direct counterparts in the new DR4 selection.

This means that users no longer need to remember what `tiny`, `weeny`, `small`, `medium`, or `large` mean, or which of those datasets is the appropriate choice for a particular graphics card. Instead, the catalog name itself gives an immediate indication of its approximate size.
The **LOD** suffix also makes an important technical distinction explicit. LOD catalogs are not loaded completely into graphics memory. Gaia Sky streams spatial portions of the catalog from disk as they are needed, allowing datasets containing millions or even billions of stars to be visualized without requiring the entire catalog to fit in graphics memory.

Note that everything discussed in this post is provisional, and the catalogs may still possibly change until release day.
