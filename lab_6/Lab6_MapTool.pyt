import arcpy

class Toolbox(object):
    def __init__(self):
        self.label = "Map Generation Toolbox"
        self.alias = "maptoolbox"
        self.tools = [GenerateMap]


class GenerateMap(object):

    def __init__(self):
        self.label = "Generate Color Map"
        self.description = "Creates a unique value or graduated color map"

    def getParameterInfo(self):

        param0 = arcpy.Parameter(
            displayName="Input Feature Layer",
            name="in_layer",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input"
        )

        param1 = arcpy.Parameter(
            displayName="Classification Field",
            name="classificationField",
            datatype="Field",
            parameterType="Required",
            direction="Input"
        )
        param1.parameterDependencies = [param0.name]

        param2 = arcpy.Parameter(
            displayName="Map Type",
            name="mapType",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        param2.filter.list = ["UniqueValue", "GraduatedColors"]

        return [param0, param1, param2]

    def execute(self, parameters, messages):

        arcpy.SetProgressor("step", "Generating Map...", 0, 3, 1)

        in_layer = parameters[0].valueAsText
        field = parameters[1].valueAsText
        map_type = parameters[2].valueAsText

        aprx = arcpy.mp.ArcGISProject("CURRENT")
        m = aprx.activeMap
        layer = m.listLayers(in_layer)[0]

        arcpy.SetProgressorPosition()

        sym = layer.symbology

        if map_type == "UniqueValue":
            sym.updateRenderer("UniqueValueRenderer")
            sym.renderer.fields = [field]

        else:
            sym.updateRenderer("GraduatedColorsRenderer")
            sym.renderer.classificationField = field

        layer.symbology = sym

        arcpy.SetProgressorPosition()

        aprx.save()

        arcpy.SetProgressorPosition()

        arcpy.SetProgressorLabel("Done.")