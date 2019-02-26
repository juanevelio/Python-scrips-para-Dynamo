 
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
 
x1 = IN[0]
x2 = IN[1]
x3 = IN[2]
punto1 = Point.ByCoordinates(x1,x2,x3)
OUT = punto1