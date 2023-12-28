# give Python access to Blender's functionality
import bpy

# extend Python functionality to generate random numbers
import random

# create a list of colors
colors = [
    [0.888, 0.515, 0.016, 1.0],
    [0.03, 0.376, 0.521, 1.0],
    [0.694, 0.019, 0.019, 1.0],
    [0.888, 0.03, 0.03, 1.0],
    [1.0, 0.22, 0.631, 1.0],
    [0.016, 0.491, 0.497, 1.0],
    [0.001, 0.694, 0.041, 1.0],
]

# add a plane
bpy.ops.mesh.primitive_plane_add()
plane_object = bpy.context.active_object

# create a new material
material = bpy.data.materials.new(name=f"random_diffuse_material")
material.diffuse_color = random.choice(colors)

# add material to object
plane_object.data.materials.append(material)