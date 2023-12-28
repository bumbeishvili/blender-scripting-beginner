import bpy
import random

def partially_clean_the_scene():
    # select all object in the scene
    bpy.ops.object.select_all(action="SELECT")

    # delete all selected objects in the scene
    bpy.ops.object.delete()

    # make sure we remove data that was connected to the objects we just deleted
    bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
    
def create_material(name):
    # create new material
    material = bpy.data.materials.new(name=name)
    # enable creating a material via nodes
    material.use_nodes = True

    # get a reference to the Principled BSDF shader node
    principled_bsdf_node = material.node_tree.nodes["Principled BSDF"]

    # set the base color of the material
    principled_bsdf_node.inputs["Base Color"].default_value = (0.8, 0.120827, 0.0074976, 1)

    # set the metallic value of the material
    principled_bsdf_node.inputs["Metallic"].default_value = 1.0

    # set the roughness value of the material
    principled_bsdf_node.inputs["Roughness"].default_value = random.uniform(0.1, 1.0)

    return material
    
def main():
    partially_clean_the_scene()
    # create ico sphere
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=5,radius=10)
    bpy.ops.object.shade_smooth()
    mesh = bpy.context.active_object
    name = "my_generated_material"
    material = create_material(name)
    mesh.data.materials.append(material)

main()

