import bpy
import math

bpy.ops.mesh.primitive_cube_add(size=20, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

cube = bpy.context.active_object;

# start keyframe
cube.keyframe_insert("rotation_euler",frame=0)

bpy.context.object.rotation_euler.z = math.radians(90)

cube.keyframe_insert("rotation_euler",frame=90)

bpy.context.object.rotation_euler.x = math.radians(90)

cube.keyframe_insert("rotation_euler",frame=180)


