from Scene3D import Scene3D

scene = Scene3D()
scene.add_point_light(5, 10, 5, 255, 255, 255, 1.0)
scene.add_directional_light(0, 10, 10, 255, 255, 255, 0.5)
scene.add_camera(0, 4, 12, 0)
scene.add_box(0, -0.5, -5, 40, 1, 30, 100, 160, 100)  # ground

# Box beam: 5x5x5 box with a 4x4 hole running top to bottom
scene.add_box(-9, 2.5, -6, 5, 5, 5, 180, 180, 190, wall=0.5)

# Same beam lying on its side
scene.add_box(-9, 8, -6, 5, 5, 5, 180, 180, 190, wall=0.5, rz=90)

# Pipe, and a pipe lying down
scene.add_cylinder(-3, 2.5, -6, 2, 5, 120, 120, 130, roughness=0.3, metalness=1, wall=0.4)
scene.add_cylinder(-3, 6.5, -6, 1, 4, 200, 120, 60, wall=0.3, rz=90)

# Hollow cone
scene.add_cone(2, 2.5, -6, 2, 5, 220, 180, 50, wall=0.3)

# Sealed hollow shapes, seen through opacity
scene.add_sphere(7, 2.5, -6, 2, 100, 150, 220, wall=0.3, opacity=0.4)
scene.add_box(12, 2.5, -6, 4, 4, 4, 180, 180, 190, wall=0.5, closed=True, opacity=0.4)
scene.add_cylinder(7, 7, -6, 1.5, 3, 200, 100, 200, wall=0.4, closed=True, opacity=0.4)
scene.add_ellipsoid(12, 7, -6, 2.5, 1.5, 1.5, 255, 200, 0, wall=0.3, opacity=0.4)

# Inside a group
g = scene.add_group(-3, 0, -12)
g.add_cylinder(0, 2.5, 0, 1.5, 5, 150, 150, 150, wall=0.3)
g.add_box(0, 5.5, 0, 4, 1, 4, 150, 150, 150, wall=0.5)

scene.save_scene("hollow_test.html", "Hollow Test")
