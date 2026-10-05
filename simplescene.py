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

    # Draw three snowmen in different places
    simple_snowman(scene, -4, -8)
    simple_snowman(scene, 0, -12)
    simple_snowman(scene, 5, -6)

    # TODO (Task 1): call draw_tree to plant a tree. Remember to pass scene first!


    # Draw a cyan cow and a smokestack with "meshes"
    add_meshes(scene)

    scene.save_scene("simplescene.html", "Simple Sample Scene")

# Task 1: finish this function (delete "pass" once you add your code)
def draw_tree(scene, cx, cz, height):
    # TODO: draw a brown cylinder for the trunk

    # TODO: draw a green ellipsoid for the leaves

    pass

# Task 2 and beyond: define your own functions!





# All functions need "scene" as the first parameter
# cx and cz say where the snowman's center goes
def simple_snowman(scene, cx, cz):
    # Big white bottom ball (radius 1, so its center is 1 above the ground)
    scene.add_sphere(cx, 1, cz, 1, 255, 255, 255)
    # Smaller white ball on top (radius 0.7), resting on the bottom ball
    scene.add_sphere(cx, 2.5, cz, 0.7, 255, 255, 255)
    # Black box for a hat, sitting on top of the head
    scene.add_box(cx, 3.4, cz, 0.7, 0.4, 0.7, 0, 0, 0)


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
    scene.add_box(0, -25, 0, 1000, 50, 1000, 100, 100, 100)

def add_meshes(scene):
    scene.add_mesh("meshes/cow.obj", 1, 1, -7, 0, 0, 0, 1, 1, 1, 0, 255, 255)
    scene.add_textured_mesh("meshes/smokestack/medres.obj", "meshes/smokestack/medres.mtl",
                            0, 18, -20, 0, 180, 0, 10, 10, 10, 0)

main()
