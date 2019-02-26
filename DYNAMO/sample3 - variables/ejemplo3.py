 
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
 #rectangulo
altura= IN[0]
anchura = IN[1]
area = altura*anchura
perimetro= 2*anchura+2*altura
salida=""
if (altura>0 and anchura>0):
    salida = 'El area es  {} y el perimetro es {}'.format(area,perimetro)
else:
    salida = "Los valores deben ser reales positivos distintos de Cero"
OUT= salida