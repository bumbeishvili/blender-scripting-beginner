import bpy
import math

count = 10
end_frame = 300
offset = 40

# set end frame
bpy.context.scene.frame_end = end_frame

# add cubes
for i in range(count):
    bpy.ops.mesh.primitive_cube_add(size=20, location=(0, offset*i, 0));


# add empty
bpy.ops.object.empty_add(location=(offset,0, 0))
empty =  bpy.context.active_object;

# add camera
bpy.ops.object.camera_add( location=(offset*2, 0-(count-1)*offset*0.05, 0))
camera = bpy.context.active_object;
bpy.ops.object.constraint_add(type='TRACK_TO')
bpy.context.object.constraints["Track To"].target = empty

# set key frame and final empty obj location
empty.keyframe_insert(data_path="location", frame=1)
camera.keyframe_insert(data_path="location", frame=1)
empty.location.y = (count-1)*offset
camera.location.y = (count-1)*offset*1.05
empty.keyframe_insert(data_path="location", frame=end_frame)
camera.keyframe_insert(data_path="location", frame=end_frame)









