# Getting Started: Build Your Virtual City (Python)

![Virtual City Example](http://nifty.stanford.edu/2024/tralie-vrtual-cities/ArtContests/F2022/walkthroughtown.gif)

## Overview

In this project, you will write Python code to generate 3D worlds. You'll create functions that draw specific city objects like trees and fire hydrants. These functions can then be called repeatedly to build complex scenes.

Your Python code will generate HTML files that you can view in your browser using VS Code's Live Server extension.

Watch the video below for a primer on this project:

[![Virtual Cities Introduction](https://img.youtube.com/vi/lhvl-rUBLO8/0.jpg)](https://www.youtube.com/watch?v=lhvl-rUBLO8)

---

## Setup

### Files You Need

- `Scene3D.py` - The library that provides functions for drawing 3D shapes
- `simplescene.py` - Starter code with an example scene

### Running Your Code

1. Open the `virtual-cities` folder in VS Code
2. Run your Python file:
   ```bash
   python simplescene.py
   ```
3. This generates an HTML file (e.g., `simplescene.html`)
4. Right-click the HTML file in VS Code and select **"Open with Live Server"**
5. Your 3D scene will open in your browser

> **Note:** You must use Live Server (not just double-clicking the HTML file) because the browser needs to load mesh files, which requires a web server.

### Controls in the Viewer

- **Mouse**: Click and drag to look around
- **W**: Forward
- **S**: Backwards
- **A**: Left
- **D**: Right
- **E**: Up
- **C**: Down

---

## Background: 3D Coordinate System

A point in 3D space is represented with three coordinates: x, y, and z. We use the OpenGL convention:

![3D Coordinate System](http://nifty.stanford.edu/2024/tralie-vrtual-cities/Coords3D.svg)

- **X-axis**: Left/Right
- **Y-axis**: Up/Down
- **Z-axis**: Forward/Backward (negative Z is "in front" of the camera)

---

## Background: RGB Colors

Colors are specified using RGB (Red, Green, Blue) values from 0-255:

- `(255, 0, 0)` = Red
- `(0, 255, 0)` = Green
- `(0, 0, 255)` = Blue
- `(255, 255, 0)` = Yellow
- `(127, 127, 127)` = Gray

---

## Available 3D Shapes

The `Scene3D` class provides methods for drawing various shapes. Here are the main ones:

### Box

```python
# Draw a green box centered at (0, 2, -6) that is 1 x 4 x 1 (width x height x depth)
scene.add_box(0, 2, -6, 1, 4, 1, 0, 255, 0, 1, 0)
```

Parameters: `add_box(cx, cy, cz, xlen, ylen, zlen, r, g, b, roughness, metalness)`

![Box Example](http://nifty.stanford.edu/2024/tralie-vrtual-cities/Box.png)

### Cylinder

```python
# Draw a yellow cylinder centered at (0, 1, -2) with radius 0.5 and height 2
scene.add_cylinder(0, 1, -2, 0.5, 2, 255, 255, 0, 1, 0)
```

Parameters: `add_cylinder(cx, cy, cz, radius, height, r, g, b, roughness, metalness)`

![Cylinder Example](http://nifty.stanford.edu/2024/tralie-vrtual-cities/Cylinder.png)

### Cone

```python
# Draw a blue cone centered at (4, 0, 0) with radius 0.5 and height 6
scene.add_cone(4, 0, 0, 0.5, 6, 0, 0, 255, 1, 0)
```

Parameters: `add_cone(cx, cy, cz, radius, height, r, g, b, roughness, metalness)`

![Cone Example](http://nifty.stanford.edu/2024/tralie-vrtual-cities/Cone.png)

### Sphere

```python
# Draw a cyan sphere with radius 1 centered at (-4, 4, 0)
scene.add_sphere(-4, 4, 0, 1, 0, 255, 255, 1, 0)
```

Parameters: `add_sphere(cx, cy, cz, radius, r, g, b, roughness, metalness)`

![Sphere Example](http://nifty.stanford.edu/2024/tralie-vrtual-cities/Sphere.png)

### Ellipsoid

An ellipsoid is a stretched sphere with different radii along each axis.

```python
# Draw a red ellipsoid with radii 1/2/1 centered at (0, 5, -10)
scene.add_ellipsoid(0, 5, -10, 1, 2, 1, 255, 0, 0, 1, 0)
```

Parameters: `add_ellipsoid(cx, cy, cz, radx, rady, radz, r, g, b, roughness, metalness)`

![Ellipsoid Example](http://nifty.stanford.edu/2024/tralie-vrtual-cities/Ellipsoid.png)

---

## Material Properties

The last two parameters for shapes control their appearance:

- **roughness** (0.0 - 1.0): How rough the surface is. 0.0 = smooth/shiny mirror, 1.0 = fully diffuse/matte
- **metalness** (0.0 - 1.0): How metallic the surface looks. 0.0 = wood/stone, 1.0 = metal

---

## Example: Drawing a Sign

Here's an example function that draws a street sign using a cylinder for the pole and a box for the sign:

```python
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
```

Notice how the function takes `cx` and `cz` parameters to position the sign anywhere in the scene. This lets you call the function multiple times to place signs in different locations:

```python
# Draw a red sign oriented east-west
draw_sign(scene, -2, -5, True, 255, 0, 0)

# Draw a green sign oriented north-south
draw_sign(scene, 0, -10, False, 0, 255, 0)
```

![Signs Example](http://nifty.stanford.edu/2024/tralie-vrtual-cities/Signs.png)

---

## Your Tasks

Create functions to draw the following objects. Each function should take position parameters (`cx`, `cz`) so objects can be placed anywhere in the scene.

### Task 1: Tree

Create a function `draw_tree(scene, cx, cz, height)` that draws a simple "lollipop" tree:

- A **brown trunk** (RGB: 102, 51, 0) made from a cylinder
- A **green ellipsoid** (RGB: 0, 255, 0) for the leaves on top
- The `height` parameter controls the total height of the tree

Example of an 8-meter tall tree next to a 6-meter tall tree:

![Tree Example](http://nifty.stanford.edu/2024/tralie-vrtual-cities/Tree.png)

### Task 2: Fire Hydrant

Create a function `draw_fire_hydrant(scene, cx, cz)` that draws a red fire hydrant (RGB: 255, 0, 0) roughly 1 meter tall:

- A small cylinder at the base
- A larger, thinner cylinder on top of the base
- A sphere on top
- Two small boxes sticking out from the sides (just below the sphere)

![Fire Hydrant Example](http://nifty.stanford.edu/2024/tralie-vrtual-cities/FireHydrant.png)

---

## Tips

1. **Start simple**: Get one shape working before adding more
2. **Use the viewer**: Keep your browser open with Live Server - it will auto-refresh when you regenerate the HTML
3. **Position objects above ground**: The ground is at y=0, so objects should have positive y values
4. **Think about centers**: Shape positions are their centers, so a cylinder with height 2 centered at y=1 will sit on the ground (y=0)
5. **Experiment**: Try different sizes and positions to get shapes looking right

---

## Meshes (Optional/Advanced)

For more complex objects, you can load pre-made 3D meshes from the `meshes/` folder:

```python
# Add a mesh with position, rotation, scale, and color
scene.add_mesh("meshes/homer.obj", 1, 1.4, -7, 0, 0, 0, 1, 1, 1, 255, 255, 0, 1, 1)
```

Parameters: `add_mesh(path, cx, cy, cz, rx, ry, rz, sx, sy, sz, r, g, b, roughness, metalness)`

Check the `meshes/` folder for available models including animals, people, and objects.

