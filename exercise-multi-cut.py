import bpy
import math

def select_one_object(obj):
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)

count = 15;
size = 10
farness =3
cutCircleRadius = 1.5
rows = 4

for i in range(count):
    x = (i%rows)*(size*2)*farness
    y = (math.ceil((i+1)/rows))*size*farness
    # create first rect and scale
    bpy.ops.mesh.primitive_cube_add(size=size, enter_editmode=False, align='WORLD', location=(x,y,0), scale=(1, 1, 1))
    obj1 = bpy.context.object
    obj1.scale.z = 3
    
    # add cilinder and cut obj1
    bpy.ops.mesh.primitive_cylinder_add(radius=cutCircleRadius, depth=200, enter_editmode=False, align='WORLD', location=(x, y, 0), scale=(1, 1, 1))
    cilinder1 = bpy.context.object;
    select_one_object(obj1)
    bpy.ops.object.modifier_add(type='BOOLEAN')
    bpy.context.object.modifiers["Boolean"].object = cilinder1
    
    # apply all modifiers
    bpy.ops.object.modifier_apply(modifier="Boolean")
    
    # bpy.ops.object.apply_all_modifiers()
    select_one_object(cilinder1)
    bpy.ops.object.delete(use_global=False)

    
    # create second obj, scale and rotate
    bpy.ops.mesh.primitive_cube_add(size=size, enter_editmode=False, align='WORLD', location=(x,y,size*1.5), scale=(1, 1, 1))
    obj2 = bpy.context.object
    obj2.scale.z = 4
    
    # add cilinder and cut obj2
    bpy.ops.mesh.primitive_cylinder_add(radius=cutCircleRadius, depth=200, enter_editmode=False, align='WORLD', location=(x, y, 0), scale=(1, 1, 1))
    cilinder2 = bpy.context.object;
    select_one_object(obj2)
    bpy.ops.object.modifier_add(type='BOOLEAN')
    bpy.context.object.modifiers["Boolean"].object = cilinder2
    bpy.ops.object.modifier_apply(modifier="Boolean")
    select_one_object(cilinder2)
    bpy.ops.object.delete(use_global=False)
    
    # rotate obj2 
    obj2.rotation_euler.x = math.radians(i*10)
    select_one_object(obj2)
    
    # add boolean modifier, union them together and delete glued obj
    bpy.ops.object.modifier_add(type='BOOLEAN')
    bpy.context.object.modifiers["Boolean"].object = obj1
    bpy.context.object.modifiers["Boolean"].operation = 'UNION'
    bpy.ops.object.modifier_apply(modifier="Boolean")
    select_one_object(obj1)
    bpy.ops.object.delete(use_global=False)
    
    # add thids substracting cube, and scale
    bpy.ops.mesh.primitive_cube_add(size=size, enter_editmode=False, align='WORLD', location=(x,y+size*2,0), scale=(1, 1, 1))
    obj3 = bpy.context.object
    obj3.scale.z = 10
    obj3.scale.y = 3
    obj3.scale.x = 1.5
    
    # add boolean diff modifier, delete used cube
    select_one_object(obj2)
    bpy.ops.object.modifier_add(type='BOOLEAN')
    bpy.context.object.modifiers["Boolean"].object = obj3
    bpy.ops.object.modifier_apply(modifier="Boolean")
    select_one_object(obj3)
    bpy.ops.object.delete(use_global=False)
    
    # rotatr
    obj2.rotation_euler.y = math.radians(-90)

    

