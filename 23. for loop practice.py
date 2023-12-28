# give Python access to Blender's functionality
import bpy

# extend Python's math functionality
import math
import random

# add a cube mesh into the scene
bpy.ops.mesh.primitive_cube_add()

# get a reference to the currently active object
obj = bpy.context.active_object

# scale the cube mesh
obj.scale.x = obj.scale.x * 0.5
obj.scale.y = obj.scale.y * 2
obj.scale.z = obj.scale.z * 0.1

# apply the scale
bpy.ops.object.transfor m_apply()

# create variables for stacking and rotating
angle_step = 3
current_angle = angle_step

cubes = [obj]

# stack and rotate the mesh
while current_angle <= 360:
    # duplicate the mesh
    bpy.ops.object.duplicate(linked=True)

    # get a reference to the currently active object
    obj = bpy.context.active_object

    # update the location of the object on the Z axis
    obj.location.z += obj.dimensions.z

    # update the rotation
    obj.rotation_euler.z = math.radians(current_angle)

    # update the angle for the next iteration
    current_angle += angle_step
    
    cubes.append(obj)

   
frames = 80;
bpy.context.scene.frame_end = frames
for i,cube in enumerate(cubes):
     # start keyframe
    startFrame = round(i/len(cubes)*frames/2);
    cube.keyframe_insert("rotation_euler",frame=startFrame);

    rotation_angle = 360 if i%2==0 else -360
    cube.rotation_euler.z += math.radians(rotation_angle)

    endFrame = startFrame + frames/2
    cube.keyframe_insert("rotation_euler",frame=endFrame)

    
   


