# TAMU GIS Programming – Homework 04  
## Fun with arcpy

### Overview
This assignment uses **ArcPy** to identify campus buildings that spatially intersect with parking garage service areas on the Texas A&M University main campus.  
The workflow demonstrates how to set up a workspace, create a geodatabase, manipulate feature layers, and perform basic spatial analysis using buffering and intersection.

All final outputs are stored in the `results/` folder:
---

### Data
- **garages.csv**  
  Contains X/Y coordinates (longitude/latitude, WGS84) of campus parking garages.

- **Campus.gdb – Structures feature class**  
  Polygon layer representing campus buildings.

---

### Workflow
The analysis follows the steps below:

1. Read garage X/Y coordinates from the provided CSV file.
2. Create a file geodatabase and store all output layers.
3. Convert the CSV into a point feature layer using `MakeXYEventLayer`.
4. Copy the campus **Structures** layer into the working geodatabase.
5. Project the garage points to match the spatial reference of the buildings layer.
6. Buffer the garage points using a user-defined distance (meters).
7. Intersect the buffered garages with the buildings layer.
8. Export the intersection attribute table to a CSV file.

All spatial operations are performed using **arcpy**.

---

### Output

- **HW04_FunWithArcpy.gdb**  
  - Garages (point features)  
  - Buffered garage service areas  
  - Intersected buildings layer  

- **results\buildings_intersect_garages.csv**  
  Attribute table listing all buildings that fall within the buffer distance of one or more parking garages.

Each row in the CSV represents a spatial relationship between a specific garage buffer and a campus building.  
Buildings may appear multiple times if they intersect buffers from multiple garages.

<img width="2727" height="2020" alt="output_Screenshot" src="https://github.com/user-attachments/assets/13d4cd07-31ee-4192-a02d-0a0a9265979b" />

- **results\output_Screenshot.png**

<img width="3544" height="1733" alt="image" src="https://github.com/user-attachments/assets/bb71b8b2-c1ec-4fcb-a3a3-4cf3fcd6ceeb" />

---

### How to Run
1. Ensure ArcGIS Pro (or ArcGIS Desktop) with ArcPy is properly installed.
2. Update file paths in `lab4.py` if needed.
3. Run the script:
   ```bash
   python lab4.py
