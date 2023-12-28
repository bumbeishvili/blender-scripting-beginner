# libs
import bpy
import bmesh
import random

# ico 
bpy.ops.mesh.primitive_ico_sphere_add(radius=10)
ico = bpy.context.active_object

# edit
bpy.ops.object.editmode_toggle()

# deselect
bpy.ops.mesh.select_all()

# retrieve faces using bmesh
ico_bmesh = bmesh.from_edit_mesh(ico.data)

#  iterate
for face in ico_bmesh.faces:
    
    # create color and material
    color = (random.random(),random.random(), random.random(),1);
    mat = bpy.data.materials.new(f"face_{face.index}")
    mat.diffuse_color = color;
    
    # add material to the object
    ico.data.materials.append(mat)
    
    # set active material
    ico.active_material_index = face.index
    
    # select face and 
    face.select = True
    bpy.ops.object.material_slot_assign()
    face.select = False
    
    
# edid mode set
bpy.ops.object.editmode_toggle()
        