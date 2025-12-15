"""
A class that holds methods to draw different 3D objects and piece
together scenes
"""

from Scene3D import Scene3D


def draw_sign(scene, cx, cz, is_east_west, r, g, b):
    """
    Draw a simple sign that consists of a 2 meter tall cylinder for the
    pole and a 0.5x0.5x0.02 meter box for the sign itself

    Args:
        scene: The scene to which to add the sign
        cx: Center of the sign in x
        cz: Center of the sign in z
        is_east_west: If True, the sign is oriented from east to west.
                      Otherwise, the sign is oriented from north to south
        r: Red component of the sign
        g: Green component of the sign
        b: Blue component of the sign
    """
    # Draw the main pole
    scene.add_cylinder(cx, 1, cz, 0.05, 2, 127, 127, 127, 1, 0)
    if is_east_west:
        # Draw a 0.5 x 0.5 box in the X/Y plane, with a thin dimension in Z
        scene.add_box(cx, 2, cz, 0.5, 0.5, 0.1, r, g, b, 1, 0)
    else:
        # Draw a 0.5 x 0.5 box in the Y/Z plane, with a thin dimension in X
        scene.add_box(cx, 2, cz, 0.1, 0.5, 0.5, r, g, b, 1, 0)


def draw_scene():
    """
    Draw a city block repeated several times
    """
    scene = Scene3D()

    # LIGHTS
    scene.add_point_light(-100, 200, 0, 200, 200, 200, 1.0)
    scene.add_point_light(100, 200, 0, 200, 200, 200, 1.0)
    scene.add_point_light(0, 0, -100, 200, 200, 200, 1.0)
    scene.add_point_light(0, 0, 100, 200, 200, 200, 1.0)

    # CAMERA
    scene.add_camera(0, 2, 0, 0)
    scene.add_camera(0, 2, -40, 180)

    # ACTION
    # Add a large gray box for the ground
    scene.add_box(0, -25, 0, 1000, 50, 1000, 100, 100, 100, 1, 0)

    # Draw a red sign 5 units in front in z and two units to
    # the left in x that's oriented from east to west
    draw_sign(scene, -2, -5, True, 255, 0, 0)  # Red (255, 0, 0)

    # Draw a green sign 10 units in front of z that's
    # oriented from north to south
    draw_sign(scene, 0, -10, False, 0, 255, 0)  # Green (0, 255, 0)
    
    # Draw a cyan cow and a smokestack
    scene.add_mesh("meshes/cow.obj", 1, 1, -7, 0, 0, 0, 1, 1, 1, 0, 255, 255, 1, 0)
    scene.add_textured_mesh("meshes/smokestack/medres.obj", "meshes/smokestack/medres.mtl",
                            0, 18, -20, 0, 180, 0, 10, 10, 10, 0)

    scene.save_scene("simplescene.html", "Simple Sample Scene")


if __name__ == "__main__":
    draw_scene()

