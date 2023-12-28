import bpy
import math

# add cube obj
bpy.ops.mesh.primitive_cube_add(size=20)
cube = bpy.context.active_object

# define empty points
empty_counts = 20
prev_empty = None
first_empty = None
rolling_coords = [
    (0,0,0),
    (cube.dimensions.x,0,0),
    (cube.dimensions.x,0,cube.dimensions.z),
    (0,0,cube.dimensions.z)
]

# set full frame  and define prev empty
full_frame = 100
bpy.context.scene.frame_end = full_frame
frame_duration = full_frame/empty_counts
bpy.context.scene.frame_current = 0


for i in range(empty_counts):
    loc = rolling_coords[i%len(rolling_coords)];
    empty = bpy.ops.object.empty_add(type='PLAIN_AXES',location=loc)
    empty = bpy.context.active_object
    startFrame = frame_duration * i
    end_frame = startFrame+frame_duration
    empty.keyframe_insert("rotation_euler",frame=startFrame)
    empty.rotation_euler.y = math.radians(90 if i else 0)
    empty.keyframe_insert("rotation_euler",frame=end_frame)
    if prev_empty != None:
        empty.parent = prev_empty;
        empty.matrix_parent_inverse = prev_empty.matrix_world.inverted()
    else:
        first_empty = empty
    empty.rotation_euler.y=0
    prev_empty = empty
   
cube.location = (cube.dimensions.x/2,0,-cube.dimensions.z/2)
cube.parent = prev_empty;  

first_empty.location.z = 10