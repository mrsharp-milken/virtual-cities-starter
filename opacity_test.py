from Scene3D import Scene3D

scene = Scene3D()
scene.add_point_light(5, 10, 5, 255, 255, 255, 1.0)
scene.add_directional_light(0, 10, 10, 255, 255, 255, 0.5)
scene.add_camera(0, 3, 8, 0)
scene.add_box(0, -0.5, -5, 30, 1, 30, 100, 160, 100)  # ground

# Solid red box behind a see-through blue box
scene.add_box(-2, 1, -8, 2, 2, 2, 255, 0, 0)
scene.add_box(-2, 1, -6, 2, 2, 2, 0, 100, 255, opacity=0.4)

# Opacity levels on spheres: 1.0, 0.7, 0.4, 0.15
for i, o in enumerate([1.0, 0.7, 0.4, 0.15]):
    scene.add_sphere(-3 + 2 * i, 4, -5, 0.8, 255, 200, 0, opacity=o)

# Other shapes
scene.add_cylinder(3, 1, -6, 1, 2, 200, 0, 200, opacity=0.5)
scene.add_cone(5, 1, -6, 1, 2, 0, 200, 200, opacity=0.5)
scene.add_ellipsoid(4, 1, -9, 1.5, 1, 1, 255, 255, 255, opacity=0.3)

# Inside a group
g = scene.add_group(-6, 1, -5)
g.add_box(0, 0, 0, 2, 2, 2, 255, 100, 0, opacity=0.5)
g.add_sphere(0, 0, 0, 0.5, 0, 0, 0)

scene.save_scene("opacity_test.html", "Opacity Test")
