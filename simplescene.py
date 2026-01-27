"""
Virtual Cities!

Instructions and Documentation:
https://gist.github.com/mrsharp-milken/21c48a631c51849a83bf6f05ea9c8b86
"""

from Scene3D import Scene3D

def main():
    scene = Scene3D()

    setup_lights(scene)
    setup_cameras(scene)
    add_ground(scene)

    # Draw a red sign oriented east-west
    draw_sign(scene, -2, -5, True, 255, 0, 0)  # Red (255, 0, 0)

    # Draw a green sign oriented north-south
    draw_sign(scene, 0, -10, False, 0, 255, 0)  # Green (0, 255, 0)

    my_shape_func(scene, 5, 15)

    # Draw a cyan cow
    add_meshes(scene)

    scene.save_scene("simplescene.html", "Simple Sample Scene")

# ADD YOUR OWN FUNCTIONS!

# All functions need "scene" as the first parameter
def my_shape_func(scene, cx, cy):
    scene.add_ellipsoid(cx, cy, -10, 1, 2, 1, 255, 0, 0, 1, 0)


# Example of a working function with lots of parameters
def draw_sign(scene, cx, cz, is_east_west, r, g, b):
    # Draw the main pole
    scene.add_cylinder(cx, 1, cz, 0.05, 2, 127, 127, 127, 1, 0)
    if is_east_west:
        # Draw a 0.5 x 0.5 box in the X/Y plane, with a thin dimension in Z
        scene.add_box(cx, 2, cz, 0.5, 0.5, 0.1, r, g, b, 1, 0)
    else:
        # Draw a 0.5 x 0.5 box in the Y/Z plane, with a thin dimension in X
        scene.add_box(cx, 2, cz, 0.1, 0.5, 0.5, r, g, b, 1, 0)


def setup_lights(scene):
    scene.add_point_light(-100, 200, 0, 200, 200, 200, 1.0)
    scene.add_point_light(100, 200, 0, 200, 200, 200, 1.0)
    scene.add_point_light(0, 0, -100, 200, 200, 200, 1.0)
    scene.add_point_light(0, 0, 100, 200, 200, 200, 1.0)

def setup_cameras(scene):
    scene.add_camera(0, 2, 0, 0)
    scene.add_camera(0, 2, -40, 180)

def add_ground(scene):
    # Add a large gray box for the ground
    scene.add_box(0, -25, 0, 1000, 50, 1000, 100, 100, 100, 1, 0)

def add_meshes(scene):
    scene.add_mesh("meshes/cow.obj", 1, 1, -7, 0, 0, 0, 1, 1, 1, 0, 255, 255, 1, 0)
    scene.add_textured_mesh("meshes/smokestack/medres.obj", "meshes/smokestack/medres.mtl",
                            0, 18, -20, 0, 180, 0, 10, 10, 10, 0)

main()
