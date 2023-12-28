# import bp and maths
import bpy;
import math;



for obj in bpy.context.scene.objects:
    obj.select_set(True)    
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.delete()
    
 

tcount = 50;

for i in range(tcount):

    # triangle mesh
    bpy.ops.mesh.primitive_circle_add(vertices=6, radius=0.1+i*0.1)

    # reference
    triangle_mesh = bpy.context.active_object

    # rotate along x
    triangle_mesh.rotation_euler.x = math.radians(-90)
    triangle_mesh.rotation_euler.z = math.radians(i*7)

    # convert mesh to curve
    bpy.ops.object.convert(target='CURVE')
    triangle_mesh.data.bevel_depth = 0.12
    triangle_mesh.data.bevel_resolution = 16
    
    #shade smooth
    bpy.ops.object.shade_smooth()

