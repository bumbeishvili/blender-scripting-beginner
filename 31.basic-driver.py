import bpy
import mathutils


def custom_driver_a(x, y, z):
    base_loc = mathutils.Vector((0, 0, 0))
    world_loc = mathutils.Vector((x, y, z))
    return custom_driver(world_loc, base_loc)


def custom_driver_b(x, y, z):
    base_loc = mathutils.Vector((0, 10, 0))
    world_loc = mathutils.Vector((x, y, z))
    return custom_driver(world_loc, base_loc)


def custom_driver_c(x, y, z):
    base_loc = mathutils.Vector((0, 0, 10))
    world_loc = mathutils.Vector((x, y, z))
    return custom_driver(world_loc, base_loc)


def custom_driver(world_loc, base_loc):
    print('world_loc: ', world_loc)
    return mathutils.noise.noise(world_loc + base_loc)


# register the driver function
bpy.app.driver_namespace["custom_driver_a"] = custom_driver_a
bpy.app.driver_namespace["custom_driver_b"] = custom_driver_b
bpy.app.driver_namespace["custom_driver_c"] = custom_driver_c
