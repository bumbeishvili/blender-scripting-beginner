import bpy

count = 10;
for i in range(count):
   bpy.ops.mesh.primitive_cube_add(size=20 , location=(i*30, 0, 0))
   bpy.ops.mesh.primitive_ico_sphere_add(radius=10, location=(i*30, 0, 50))
   bpy.ops.mesh.primitive_monkey_add(size=20, location=(i*30, 0, 100),)



cube_i = 1;
ico_i = 1
monkey_i = 1
for obj in bpy.data.objects:
    print(obj)
    if 'Cube' in obj.name:
        obj.name = f'obj.cube.{cube_i:03d}'
        obj.data.name  = f'obj.mesh.cube.{cube_i:03d}'
        cube_i += 1
    if 'Suzanne' in obj.name:
        obj.name = f'obj.monkey.{monkey_i:03d}'
        obj.data.name = f'obj.mesh.monkey.{cube_i:03d}'
        monkey_i+=1
    if 'Ico' in obj.name:
        obj.name = f'obj.ico.{ico_i:03d}'
        obj.data.name = f'obj.mesh.ico.{ico_i:03d}'
        ico_i+=1
        
        
        
# select objetcs and run following code
def rotateObjects (): 
    import math
    for obj in bpy.context.selected_objects:
        obj.rotation_euler.z = math.radians(45)

# select objects and run following code
def scaleObjects (): 
    for obj in bpy.context.selected_objects:
        obj.scale.x = 0.5
        obj.scale.y = 0.5
        obj.scale.z = 0.5

        


