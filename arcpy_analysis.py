
import arcpy

arcpy.env.workspace = r"C:\EsriTraining\CrimeAnalysisInfoProd\Products\Products.gdb"

arcpy.analysis.Buffer(
    "Crime_Dec2016",
    r"C:\EsriTraining\CrimeAnalysisInfoProd\Products\Products.gdb\Crime_Dec2016_Buffer3",
    "100 Meters",
    "FULL",
    "ROUND",
    "NONE",
    None,
    "PLANAR"
)

arcpy.ca.EightyTwentyAnalysis(
    "Chicago_Crime",
    r"C:\EsriTraining\CrimeAnalysisInfoProd\Products\Products.gdb\Chicago_Crime_8020Analysis2",
    None,
    "Chicago_Crime_District"
)
