# -*- coding: utf-8 -*-
import arcpy
import os
import traceback


class Toolbox(object):
    def __init__(self):
        self.label = "Toolbox"
        self.alias = ""
        self.tools = [tool]


class tool(object):
    def __init__(self):
        self.label = "Lab 5"
        self.description = "Buffers garage points and intersects with campus buildings (Structures)."
        self.canRunInBackground = False
        self.category = "Building Tools"

    def getParameterInfo(self):
        # 0 GDB Folder
        param0 = arcpy.Parameter(
            displayName="GDB Folder",
            name="GDBFolder",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input"
        )

        # 1 GDB Name
        param1 = arcpy.Parameter(
            displayName="GDB Name",
            name="GDBName",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        param1.value = "GarageBuildingIntersection.gdb"

        # 2 Garage CSV File
        param2 = arcpy.Parameter(
            displayName="Garage CSV File",
            name="GarageCSVFile",
            datatype="DEFile",
            parameterType="Required",
            direction="Input"
        )
        param2.filter.list = ["csv"]

        # 3 Garage Layer Name
        param3 = arcpy.Parameter(
            displayName="Garage Layer Name",
            name="GarageLayerName",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        param3.value = "Garages"

        # 4 Campus GDB  (Fix: use DEWorkspace, not DEType)
        param4 = arcpy.Parameter(
            displayName="Campus GDB",
            name="CampusGDB",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input"
        )

        # 5 Buffer Distance (meters)
        # Keep numeric like demo UI (150), then we append "Meters"
        param5 = arcpy.Parameter(
            displayName="Buffer Distance (meters)",
            name="BufferDistance",
            datatype="GPDouble",
            parameterType="Required",
            direction="Input"
        )
        param5.value = 150

        return [param0, param1, param2, param3, param4, param5]

    def isLicensed(self):
        return True

    def execute(self, parameters, messages):
        arcpy.env.overwriteOutput = True

        try:
            # ---- Read parameters ----
            folder_path = parameters[0].valueAsText
            gdb_name = parameters[1].valueAsText.strip()
            csv_path = parameters[2].valueAsText
            garage_layer_name = parameters[3].valueAsText.strip()
            campus_gdb = parameters[4].valueAsText
            buffer_distance_m = float(parameters[5].value)

            # ---- Normalize GDB name ----
            if not gdb_name.lower().endswith(".gdb"):
                gdb_name += ".gdb"

            gdb_path = os.path.join(folder_path, gdb_name)

            arcpy.AddMessage("Step 1/6: Creating (or reusing) output GDB...")
            if not arcpy.Exists(gdb_path):
                arcpy.management.CreateFileGDB(folder_path, gdb_name)
            else:
                arcpy.AddMessage("Output GDB already exists. Reusing it.")

            # ---- CSV -> XY Event Layer ----
            arcpy.AddMessage("Step 2/6: Creating XY event layer from CSV (X, Y)...")
            # Demo assumes X/Y fields exist
            garages_layer = arcpy.management.MakeXYEventLayer(
                table=csv_path,
                in_x_field="X",
                in_y_field="Y",
                out_layer=garage_layer_name
            )

            # Export XY layer into the output gdb
            arcpy.AddMessage("Step 3/6: Writing garage points into output GDB...")
            arcpy.conversion.FeatureClassToGeodatabase([garages_layer], gdb_path)
            garage_points = os.path.join(gdb_path, garage_layer_name)

            # ---- Copy Structures into output gdb as Buildings ----
            arcpy.AddMessage("Step 4/6: Copying Structures from Campus GDB...")
            buildings_campus = os.path.join(campus_gdb, "Structures")
            if not arcpy.Exists(buildings_campus):
                raise arcpy.ExecuteError(f"Cannot find 'Structures' in Campus GDB: {buildings_campus}")

            buildings = os.path.join(gdb_path, "Buildings")
            if arcpy.Exists(buildings):
                arcpy.management.Delete(buildings)
            arcpy.management.Copy(buildings_campus, buildings)

            # ---- Project garage points to match buildings SR ----
            arcpy.AddMessage("Step 5/6: Projecting garage points to match buildings...")
            spatial_ref = arcpy.Describe(buildings).spatialReference
            garage_proj = os.path.join(gdb_path, "Garage_Points_reprojected")
            if arcpy.Exists(garage_proj):
                arcpy.management.Delete(garage_proj)
            arcpy.management.Project(garage_points, garage_proj, spatial_ref)

            # ---- Buffer + Intersect ----
            arcpy.AddMessage("Step 6/6: Buffer + Intersect...")
            garage_buffer = os.path.join(gdb_path, "Garage_Points_buffered")
            if arcpy.Exists(garage_buffer):
                arcpy.management.Delete(garage_buffer)

            buffer_dist_str = f"{buffer_distance_m} Meters"
            arcpy.analysis.Buffer(garage_proj, garage_buffer, buffer_dist_str)

            intersect_fc = os.path.join(gdb_path, "Garage_Building_Intersection")
            if arcpy.Exists(intersect_fc):
                arcpy.management.Delete(intersect_fc)

            arcpy.analysis.Intersect([garage_buffer, buildings], intersect_fc, join_attributes="ALL")

            arcpy.AddMessage("=== Done ===")
            arcpy.AddMessage(f"GDB: {gdb_path}")
            arcpy.AddMessage(f"Outputs: {garage_proj}, {garage_buffer}, {intersect_fc}, {buildings}")

        except Exception as e:
            tb = traceback.format_exc()
            arcpy.AddError("Tool failed.")
            arcpy.AddError(str(e))
            arcpy.AddError(tb)
            raise