import bpy

def partially_clean_the_scene():
    # select all object in the scene
    bpy.ops.object.select_all(action="SELECT")

    # delete all selected objects in the scene
    bpy.ops.object.delete()

    # make sure we remove data that was connected to the objects we just deleted
    bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
def create_noise_mask(material):
    """Add a set of nodes to create a noise mask using:
    * Texture Coordinate node
    * Mapping node
    * Noise Texture node
    * Color Ramp node
    """
    x_step = 300;
    node_x = -x_step
    # color_ramping
    c_node = material.node_tree.nodes.new(type="ShaderNodeValToRGB")
    c_node.location.x = node_x
    node_x -= x_step
    
    # texturing
    nt_node = material.node_tree.nodes.new(type="ShaderNodeTexNoise")
    nt_node.location.x = node_x
    node_x -= x_step
     
    # mapping
    m_node = material.node_tree.nodes.new(type="ShaderNodeMapping")
    m_node.location.x = node_x
    node_x -= x_step
    
    # texture coords node
    tc_node = material.node_tree.nodes.new(type="ShaderNodeTexCoord")
    tc_node.location.x = node_x
    
    # connect nodes
    material.node_tree.links.new(nt_node.outputs['Color'], c_node.inputs['Fac'])
    material.node_tree.links.new(m_node.outputs['Vector'], nt_node.inputs['Vector'])
    material.node_tree.links.new(tc_node.outputs['Generated'], m_node.inputs['Vector'])
    
    return c_node    
    
def create_material(name):
    # creating a new material
    material = bpy.data.materials.new(name=name)
    #enable creating a material via nodes
    material.use_nodes = True
    # get a reference to the Principled BSDF shader node
    principled_bsdf_node = material.node_tree.nodes["Principled BSDF"]
    # set the base color of the material
    principled_bsdf_node.inputs["Base Color"].default_value = (0.8, 0.120827, 0.0074976, 1)
    principled_bsdf_node.inputs["Metallic"].default_value = 1
    
    # create color ramp node and link with roughness
    c_node = create_noise_mask(material)
    material.node_tree.links.new(c_node.outputs['Color'], principled_bsdf_node.inputs['Roughness'])
    
    return material;

def add_mesh():
    # create an ico sphere
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=5)
    # shade smooth
    bpy.ops.object.shade_smooth()
    # get reference to mesh object
    mesh_obj = bpy.context.active_object

    return mesh_obj 

def main():
    partially_clean_the_scene()
    name = "my_generated_material"
    material = create_material(name)
    mesh_obj = add_mesh()
    mesh_obj.data.materials.append(material)
    
    
main()