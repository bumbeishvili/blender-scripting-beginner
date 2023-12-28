import bpy;

verts = [
  (-1,-1,-1),(-1,1,-1),(1,1,-1),(1,-1,-1),
  (0,0,1)
];
edges = []
faces = [
  (0,1,2,3),
  (0,3,4),
  (1,0,4),
  (2,1,4),
  (3,2,4)
];




mesh = bpy.data.meshes.new("pyramid")
mesh.from_pydata(verts,edges,faces)


mesh_obj = bpy.data.objects.new("pyramid",mesh)



bpy.context.collection.objects.link(mesh_obj)