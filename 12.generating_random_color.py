import bpy
import random

# add plane

bpy.ops.mesh.primitive_plane_add(size=20)
plane = bpy.context.active_object


# create color

r = random.random()
g = random.random()
b = random.random()
a = 1;

color = (r,g,b,a)

# add material and diffuse color
mat=bpy.data.materials.new('plane-mat')
mat.diffuse_color = color

# add material to plane
plane.data.materials.append(mat)

