import bmesh
import bpy


def partially_clean_the_scene():
    # select all object in the scene
    bpy.ops.object.select_all(action="SELECT")

    # delete all selected objects in the scene
    bpy.ops.object.delete()

partially_clean_the_scene()

bpy.ops.mesh.primitive_cube_add(
    size=20, enter_editmode=False, align="WORLD", location=(0, 0, 0), scale=(1, 1, 1)
)

mesh_obj = bpy.context.active_object

# Go to edit mode
bpy.ops.object.mode_set(mode="EDIT")

bm = bmesh.from_edit_mesh(mesh_obj.data)

# bevel based on edges
bmesh.ops.bevel(
    bm,
    geom=bm.edges,
    offset=1,
    segments=5,
    affect="EDGES",
)

bm.normal_update()

bmesh.update_edit_mesh(mesh_obj.data)

bm.free()

