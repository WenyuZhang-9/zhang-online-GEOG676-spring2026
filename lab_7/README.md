# Lab 7 – Raster Analysis  
GEOG 676 – Spring 2026  

## Overview

This lab demonstrates raster analysis using Landsat imagery and a digital elevation model (DEM).  
All processing was completed using Python and ArcPy.

The workflow included:

- Creating a true-color composite raster
- Generating a hillshade raster
- Generating a slope raster

---

## Data Sources

- Landsat imagery (USGS EarthExplorer)
- SRTM DEM (NASA, 30m resolution)

*Note: Original raster files are large and are not included in this repository. Only output screenshots are provided.*

---

## Repository Contents

- `lab7.py` – Python script
- `results/` – Screenshots of:
  
  - Composite raster
<img width="2836" height="1641" alt="23838ae34ae08822bd2607157c5a5750" src="https://github.com/user-attachments/assets/eb7cedb2-ca4a-489c-93d9-de28380df8ae" />

  - Hillshade raster
    
<img width="2873" height="1762" alt="142c88d67f1e85764bb1fb8945fe81ab" src="https://github.com/user-attachments/assets/d23b3ad2-a716-49fb-9094-baa75c307597" />

  - Slope raster
    
<img width="2862" height="1775" alt="80e5aea20bab9e5572df5283aabd9e59" src="https://github.com/user-attachments/assets/e131a6d3-de01-43dd-93b2-64bd8f2880dc" />


---

## Methods Summary

1. Combined Landsat bands into a true-color composite (Red, Green, Blue).
2. Used the DEM to create:
   - Hillshade raster (315° azimuth, 45° altitude)
   - Slope raster (degrees)
