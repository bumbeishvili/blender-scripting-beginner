import bpy;
import random;





n =  random.randint(1,10)

if n>=5:
    bpy.ops.mesh.primitive_monkey_add(size=1, enter_editmode=False, align='WORLD', location=(5.67885e-07, -1.49012e-08, -8.88659e-07), scale=(1, 1, 1))
else:
    bpy.ops.mesh.primitive_torus_add(align='WORLD', location=(5.67885e-07, -1.49012e-08, -8.88659e-07), rotation=(0, 0, 0))