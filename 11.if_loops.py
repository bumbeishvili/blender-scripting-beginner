import bpy;
import random;


count=20;

for i in range(count):
    size = 20
    loc = (i-count/2)*size+size/2
    if random.randint(0,1):
        bpy.ops.mesh.primitive_cube_add(size=size,location=(0,loc,loc))
    else:
        bpy.ops.mesh.primitive_uv_sphere_add(radius=size/2,location=(0,loc,loc))
        