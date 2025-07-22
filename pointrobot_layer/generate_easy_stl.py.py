import trimesh

# Create a small sphere mesh
sphere = trimesh.creation.icosphere(subdivisions=2, radius=0.2)

# Save as STL
sphere.export('meshes/pointrobot_link_0.stl')
sphere.export('meshes/pointrobot_link_1.stl')
sphere.export('meshes/pointrobot_link_2.stl')