# give Python access to Blender's functionality
import bpy

# give Python access to Blender's mesh editing functionality
import bmesh

# extend Python functionality to generate random numbers
import random


def generate_random_material():
    '''generate a random color'''
    red = random.random()  # creates a value from 0.0 to 1.0
    green = random.random()
    blue = random.random()
    alpha = 1.0
    color = (red, green, blue, alpha)
    
    # create a new material
    mat = bpy.data.materials.new(name=f"face_{i}")
    mat.diffuse_color = color
    return mat;


# add an ico sphere
bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=3)
ico_object = bpy.context.active_object

# generate materials
material_count = 30
for i in range(material_count):
    # generate material
    mat = generate_random_material();
    
    # add the material to the object
    ico_object.data.materials.append(mat)
    

# turn ON Edit Mode
bpy.ops.object.editmode_toggle()

# deselect all faces
bpy.ops.mesh.select_all()

# get geometry data from mesh object
ico_bmesh = bmesh.from_edit_mesh(ico_object.data)

# iterate through each face of the mesh
for face in ico_bmesh.faces:

    # set active material
    ico_object.active_material_index = random.randint(0,material_count)

    # select the face and assign the active material
    face.select = True
    bpy.ops.object.material_slot_assign()
    face.select = False

# turn OFF Edit Mode
bpy.ops.object.editmode_toggle()