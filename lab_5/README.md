# Lab 5 – Creating a Python Toolbox in ArcGIS Pro

## Objective
The purpose of this lab is to convert the HW04 script into an ArcGIS Pro Python toolbox (.pyt).  
The tool identifies campus buildings that intersect with a buffer created around garage centroid locations.

---

## ⚒️Tool Description
The toolbox performs the following operations:

1. Buffer garage centroid locations
2. Intersect the buffer with campus building footprints
3. Output buildings that fall within the specified buffer distance

This tool was created using arcpy and added into ArcGIS Pro as a Python toolbox.

---

## Input Data

- Garage centroid feature class
- Campus building feature class
- Buffer distance (user-defined)
- ⚠ The file geodatabases (.gdb) are NOT included in this repository.
---

## Output & Tool

- Feature class of buildings that intersect the garage buffer
![output_ArcgisPro](https://github.com/user-attachments/assets/e79bc08c-6be4-433a-96c7-048d1086f425)
![Database](https://github.com/user-attachments/assets/88f9e222-ef89-490a-9809-ef8f98d4abb6)

---

## Files Included

- `lab5.pyt` – Python toolbox
- `garages.csv` – Garage input data
- `Results/output_ArcgisPro.jpg` – Screenshot of tool in ArcGIS Pro

---

## Author
Wenyu Zhang  
GEOG 676 – Spring 2026
