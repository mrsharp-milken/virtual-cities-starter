from Scene3D import Scene3D

# Tubes lying along the view axis so you can look into their openings
scene = Scene3D()
scene.add_point_light(5, 10, 8, 255, 255, 255, 1.0)
scene.add_directional_light(0, 10, 10, 255, 255, 255, 0.5)
scene.add_camera(0, 2, 8, 0)
scene.add_box(0, -0.5, -5, 40, 1, 30, 100, 160, 100)  # ground

scene.add_box(-6, 2, 0, 3, 5, 3, 180, 180, 190, wall=0.5, rx=90)        # box beam
scene.add_cylinder(-1.5, 2, 0, 1.5, 5, 120, 120, 200, wall=0.4, rx=90)  # pipe
scene.add_cone(3, 2, 0, 1.5, 5, 220, 180, 50, wall=0.3, rx=-90)         # opens toward camera
scene.add_box(7, 2, 0, 3, 3, 3, 255, 255, 255, wall=0.5, closed=True, opacity=0.5)
scene.save_scene("hollow_inside_test.html", "Hollow Looking Inside")

# Camera inside sealed, opaque hollow shapes
room = Scene3D()
room.add_point_light(0, 3, 0, 255, 255, 255, 1.0)
room.add_camera(0, 0, 0, 0)
room.add_box(0, 0, 0, 20, 10, 20, 200, 120, 120, wall=1, closed=True)
room.add_box(0, -4, -6, 2, 2, 2, 255, 255, 0)
room.save_scene("hollow_room_test.html", "Camera Inside a Hollow Box")

dome = Scene3D()
dome.add_point_light(0, 3, 0, 255, 255, 255, 1.0)
dome.add_camera(0, 0, 0, 0)
dome.add_sphere(0, 0, 0, 20, 100, 150, 220, wall=1)
dome.add_box(0, -2, -6, 2, 2, 2, 255, 255, 0)
dome.save_scene("hollow_dome_test.html", "Camera Inside a Hollow Sphere")
