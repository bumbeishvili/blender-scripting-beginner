import bpy
import math
obj = bpy.ops.mesh.primitive_cube_add(size=20,  scale=(1, 0.4, 0.1))
bpy.ops.object.transform_apply(scale=True)

count = 40
i=0
multiplier = 5

while i<count:
    bpy.ops.object.duplicate(linked=True)
    obj = bpy.context.active_object;
    obj.location.z = obj.dimensions.z*(i+1)
    obj.rotation_euler.z=math.radians(i*multiplier)
    i+=1