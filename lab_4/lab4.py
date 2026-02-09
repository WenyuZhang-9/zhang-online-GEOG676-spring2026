# TAMU GIS Programming - Homework 04
# Fun with arcpy (ARCPY ONLY)
# Steps: CSV -> GDB -> Garages points -> Copy Structures -> Project -> Buffer -> Intersect -> CSV

import arcpy
import os

# -----------------------------
# 0) Settings (workspace)
# -----------------------------
arcpy.env.overwriteOutput = True


FOLDER_PATH = r"C:\Users\73934\Desktop\Course Assignment\zhang-online-GEOG676-spring2026\lab_4"
CSV_PATH = os.path.join(FOLDER_PATH, "garages.csv")          # garages.csv
CAMPUS_GDB = os.path.join(FOLDER_PATH, "Campus.gdb")         # Campus.gdb (put it in lab_4)


STRUCTURES_FC = os.path.join(CAMPUS_GDB, "Structures")

GDB_NAME = "HW04_FunWithArcpy.gdb"
GDB_PATH = os.path.join(FOLDER_PATH, GDB_NAME)

GARAGE_LAYER = "Garage_Points"              # XY Event Layer name
GARAGE_FC_WGS84 = os.path.join(GDB_PATH, "Garages_WGS84")
GARAGE_FC = os.path.join(GDB_PATH, "Garages")               # projected garages
BUILDINGS_FC = os.path.join(GDB_PATH, "Structures")         # copied buildings
BUFFER_FC = os.path.join(GDB_PATH, "Garages_Buffer")
INTERSECT_FC = os.path.join(GDB_PATH, "Buildings_Garages_Intersect")

OUT_CSV_NAME = "buildings_intersect_garages.csv"
OUT_CSV_PATH = os.path.join(FOLDER_PATH, OUT_CSV_NAME)


def count(fc_path: str) -> int:
    return int(arcpy.management.GetCount(fc_path)[0])


def safe_delete(path: str) -> None:
    if arcpy.Exists(path):
        arcpy.management.Delete(path)


def main():
    # -----------------------------
    # 1) Read X/Y coords from CSV (MakeXYEventLayer)
    # -----------------------------
    if not os.path.exists(CSV_PATH):
        raise FileNotFoundError(f"CSV not found: {CSV_PATH}")
    if not arcpy.Exists(STRUCTURES_FC):
        raise FileNotFoundError(f"Structures not found: {STRUCTURES_FC}")

    # -----------------------------
    # 2) Create geodatabase and add input layers
    # -----------------------------
    arcpy.env.workspace = FOLDER_PATH
    if not arcpy.Exists(GDB_PATH):
        arcpy.management.CreateFileGDB(FOLDER_PATH, GDB_NAME)

    # (optional "nice"): make scratchWorkspace your output gdb
    arcpy.env.workspace = GDB_PATH
    arcpy.env.scratchWorkspace = GDB_PATH

    # 2a) Garages: CSV (X,Y lon/lat) -> XY Event Layer (WGS84)
    wgs84 = arcpy.SpatialReference(4326)  # X=-96, Y=30 => lon/lat
    arcpy.management.MakeXYEventLayer(
        table=CSV_PATH,
        in_x_field="X",
        in_y_field="Y",
        out_layer=GARAGE_LAYER,
        spatial_reference=wgs84
    )

    # Save garages into GDB (feature class)
    safe_delete(GARAGE_FC_WGS84)
    arcpy.management.CopyFeatures(GARAGE_LAYER, GARAGE_FC_WGS84)

    # 2b) Copy Structures into our GDB
    safe_delete(BUILDINGS_FC)
    arcpy.management.CopyFeatures(STRUCTURES_FC, BUILDINGS_FC)

    print("✅ Step 1-2 done")
    print("   Garages_WGS84 count:", count(GARAGE_FC_WGS84))
    print("   Structures(copy) count:", count(BUILDINGS_FC))

    # -----------------------------
    # 3) Buffer the garages (distance from user, meters)
    # -----------------------------
    buildings_sr = arcpy.Describe(BUILDINGS_FC).spatialReference

    safe_delete(GARAGE_FC)
    arcpy.management.Project(
        in_dataset=GARAGE_FC_WGS84,
        out_dataset=GARAGE_FC,
        out_coor_system=buildings_sr
    )

    dist_m = input("Enter buffer distance in meters (e.g., 200): ").strip()
    try:
        float(dist_m)
    except ValueError:
        raise ValueError("Buffer distance must be a number (meters).")

    safe_delete(BUFFER_FC)
    arcpy.analysis.Buffer(
        in_features=GARAGE_FC,
        out_feature_class=BUFFER_FC,
        buffer_distance_or_field=f"{dist_m} Meters",
        dissolve_option="NONE"
    )

    print("✅ Step 3 done")
    print("   Garages(Projected) count:", count(GARAGE_FC))
    print("   Buffer count:", count(BUFFER_FC))

    # -----------------------------
    # 4) Intersect buildings with buffered garages
    # -----------------------------
    safe_delete(INTERSECT_FC)
    arcpy.analysis.Intersect(
        in_features=[BUILDINGS_FC, BUFFER_FC],
        out_feature_class=INTERSECT_FC,
        join_attributes="ALL"
    )

    print("✅ Step 4 done")
    print("   Intersect count:", count(INTERSECT_FC))

    # -----------------------------
    # 5) Output intersection attribute table to CSV
    # -----------------------------
    if os.path.exists(OUT_CSV_PATH):
        os.remove(OUT_CSV_PATH)

    arcpy.conversion.TableToTable(
        in_rows=INTERSECT_FC,
        out_path=FOLDER_PATH,
        out_name=OUT_CSV_NAME
    )

    print("✅ Step 5 done")
    print("\n FINAL OUTPUTS ✅")
    print("GDB:", GDB_PATH)
    print("CSV:", OUT_CSV_PATH)

    if count(INTERSECT_FC) == 0:
        print("\n⚠️ Note: Intersect result is empty.")
        print("Most common cause is coordinate mismatch. Check that garages.csv X/Y are lon/lat and were projected.")


if __name__ == "__main__":
    main()