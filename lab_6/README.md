# Lab 6 – Map Generation Toolbox  
GEOG 676 – Spring 2026  

## Overview

This lab demonstrates how to build a Python Toolbox (.pyt) in ArcGIS Pro that generates a thematic map.

The tool allows the user to:

- Create a **Graduated Color Map**
- (or Unique Value Map, if implemented)

The tool is accessible from the Geoprocessing pane in ArcGIS Pro.
![results](https://github.com/user-attachments/assets/98e774fa-6136-44e9-a8e6-bd838503a2cb)

---

## Features

- Built as a **Python Toolbox (.pyt)**
- Uses `arcpy.mp` to modify layer symbology
- Implements a **progressor** to show tool progress
- Saves the updated project

---

## How It Works

1. User selects:
   - An ArcGIS Pro project
   - A feature layer
   - A classification field
2. The script updates the layer’s symbology.
3. A progress bar displays tool status.
4. The updated project is saved.

---

## Repository Contents

- `lab6_maptool.pyt` – Python Toolbox
- `screenshot.png` – Resulting map screenshot
