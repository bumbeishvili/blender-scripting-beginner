# imports
import bpy
import math
import pprint




for obj in bpy.context.scene.objects:
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj;
    bpy.ops.object.delete()
    
    

points = 140
radius = 3

coords = [];

for i in range(points):
    angle = 2*math.pi/points
    x = radius*math.sin(angle*i)
    y = radius*math.cos(angle*i)
    coord = (x, y, i/points*4)
    coords.append(coord)
    bpy.ops.mesh.primitive_ico_sphere_add(radius=0.25, align='WORLD', location=coord, scale=(1, 1, 1))


pprint.pprint(coords)
