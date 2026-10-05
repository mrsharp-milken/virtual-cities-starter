# Getting Started: Build Your Virtual City (Python)

![walkthroughtown (1)](https://gist.github.com/user-attachments/assets/11ea0994-ee9d-4796-9a5f-14416ce81d61)


## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
  - [Downloading the Starter Code](#downloading-the-starter-code)
  - [Files You'll Have](#files-youll-have)
  - [Running Your Code](#running-your-code)
  - [Controls in the Viewer](#controls-in-the-viewer)
- [Background: 3D Coordinate System](#background-3d-coordinate-system)
- [Background: RGB Colors](#background-rgb-colors)
- [Available 3D Shapes](#available-3d-shapes)
  - [Box](#box) | [Cylinder](#cylinder) | [Cone](#cone) | [Sphere](#sphere) | [Ellipsoid](#ellipsoid)
- [Material Properties](#material-properties)
- [Example: Drawing a Sign](#example-drawing-a-sign)
- [Your Tasks](#your-tasks)
  - [Milestone 1](#milestone-1)
    - [Task 1: Tree](#task-1-tree)
    - [Task 2: Fire Hydrant](#task-2-fire-hydrant)
  - [Milestone 2](#milestone-2)
    - [Task 3: Stop Light](#task-3-stop-light)
    - [Task 4: Sedan](#task-4-sedan)
    - [Task 5: City Block](#task-5-city-block)
    - [Task 6: Build Your City](#task-6-build-your-city)
  - [Milestone 3](#milestone-3)
    - [Art Contest](#art-contest)
- [Tips](#tips)
- [Meshes (Optional/Advanced)](#meshes-optionaladvanced)
- [Rotations (Optional/Advanced)](#rotations-optionaladvanced)

---

## Overview

In this project, you will write Python code to generate 3D worlds. You'll create functions that draw specific city objects like trees and fire hydrants. These functions can then be called repeatedly to build complex scenes.

Your Python code will generate HTML files that you can view in your browser using VS Code's Live Server extension.

<details>
<summary>Watch an optional video primer on this project (click to expand)</summary>

[![Virtual Cities Introduction](https://img.youtube.com/vi/lhvl-rUBLO8/0.jpg)](https://www.youtube.com/watch?v=lhvl-rUBLO8)

</details>

---

## Setup

### Downloading the Starter Code

Open VS Code and your cs50-workspace. Open a new terminal, and run:

**MacOS / Linux:**
```bash
git clone --depth 1 https://github.com/mrsharp-milken/virtual-cities-starter.git temp && rm -rf temp/.git && mv temp/{*,.*} . 2>/dev/null && rmdir temp
```

**Windows (PowerShell):**
```powershell
git clone --depth 1 https://github.com/mrsharp-milken/virtual-cities-starter.git temp; Remove-Item -Recurse -Force temp\.git; Get-ChildItem temp -Force | Move-Item -Destination .; Remove-Item -Recurse -Force temp
```

### Files You'll Have

- `Scene3D.py` - The library that provides functions for drawing 3D shapes
- `simplescene.py` - Starter code with an example scene
- `meshes/` - 3D models you can use
- `jsmodules/` - Required files for the viewer

### Running Your Code

1. Open your project folder in VS Code
2. Run your Python file:

   **MacOS / Linux:**
   ```bash
   python3 simplescene.py
   ```

   **Windows:**
   ```bash
   python simplescene.py
   ```
3. This generates an HTML file (e.g., `simplescene.html`)
4. Right-click the HTML file in VS Code and select **"Open with Live Server"**

<img height="330" alt="Screenshot 2025-12-15 at 1 32 19 AM" src="https://gist.github.com/user-attachments/assets/65799d86-1ca9-457f-a391-080cf26c51e6" />

<br>

<br>

5. Your 3D scene will open in your browser

> **Note:** You must use Live Server (not just double-clicking the HTML file) because the browser needs to load mesh files, which requires a web server.

You should be able to see a scene like this:

<img width="1559" height="1086" alt="image" src="https://gist.github.com/user-attachments/assets/c2be01e9-5cdd-47d7-ac16-c0e890be9834" />

<br>

<br>

<br>

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

# Draw a shiny, stone-like, yellow Homer Simpson and a smokestack
scene.add_mesh("meshes/homer.obj", 1, 1.4, -7, 0, 0, 0, 1, 1, 1, 255, 255, 0, 1, 1)
scene.add_textured_mesh("meshes/smokestack/medres.obj", "meshes/smokestack/medres.mtl",
                      0, 18, -20, 0, 180, 0, 10, 10, 10, 0)
```

_For kicks, I also threw in Homer Simpson and the painted smokestack!_

![Signs Example](http://nifty.stanford.edu/2024/tralie-vrtual-cities/Signs.png)

---

## Your Tasks

Create functions to draw the following objects. Each function should take position parameters (`cx`, `cz`) so objects can be placed anywhere in the scene.

---

### Milestone 1

Complete the following two tasks to build basic city objects.

#### Task 1: Tree

Create a function `draw_tree(scene, cx, cz, height)` that draws a simple "lollipop" tree:

- A **brown trunk** (RGB: 102, 51, 0) made from a cylinder
- A **green ellipsoid** (RGB: 0, 255, 0) for the leaves on top
- The `height` parameter controls the total height of the tree

Example of an 8-meter tall tree next to a 6-meter tall tree:

![Tree Example](http://nifty.stanford.edu/2024/tralie-vrtual-cities/Tree.png)

#### Task 2: Fire Hydrant

Create a function `draw_fire_hydrant(scene, cx, cz)` that draws a red fire hydrant (RGB: 255, 0, 0) roughly 1 meter tall:

- A small cylinder at the base
- A larger, thinner cylinder on top of the base
- A sphere on top
- Two small boxes sticking out from the sides (just below the sphere)

![Fire Hydrant Example](http://nifty.stanford.edu/2024/tralie-vrtual-cities/FireHydrant.png)

---

### Milestone 2

Now that you have basic objects, create more complex city elements.

#### Task 3: Stop Light

Create a function `draw_stop_light(scene, cx, cz)` that draws a traffic stop light:

- A **vertical pole** that is 8 meters tall (use a cylinder)
- A **horizontal pole** at the top that is 8 meters wide (use a rotated cylinder or thin box)
- A **box** attached to the horizontal pole to hold the lights
- Three spheres for the lights:
  - **Top light**: Red (RGB: 255, 0, 0)
  - **Middle light**: Yellow (RGB: 255, 255, 0)
  - **Bottom light**: Green (RGB: 0, 255, 0)

Below is an example stoplight with a fire hydrant next to it for scale:

![Stop Light Example](http://nifty.stanford.edu/2024/tralie-vrtual-cities/StopLight.png)

#### Task 4: Sedan

Create a function `draw_sedan(scene, cx, cz, is_east_west, r, g, b)` that draws a boxy car:

- **Bottom box** (car body): 4.5 meters long, 1.7 meters wide, 0.7 meters tall, in the specified color
- **Top box** (cabin): 3.5 meters long, 1.4 meters wide, 0.8 meters tall, slightly offset on top of the body
- **Four wheels**: Grey cylinders (RGB: 127, 127, 127) with radius 0.5 and appropriate height
  - For an east/west car, rotate the wheels 90 degrees around the x-axis
  - For a north/south car, rotate the wheels 90 degrees around both the x-axis and y-axis

The `is_east_west` parameter determines the car's orientation:
- `True`: Car faces east/west direction
- `False`: Car faces north/south direction

Below is an example of a red east/west car and a yellow north/south car, with a fire hydrant and stop light for scale:

![Sedan Example](http://nifty.stanford.edu/2024/tralie-vrtual-cities/Sedan.png)

> **Note:** To rotate shapes, use the rotated versions of the shape methods. For example, `add_cylinder` has a rotated version that takes additional rotation parameters (rx, ry, rz) for rotation in degrees around each axis.

#### Task 5: City Block

Create a function `draw_city_block(scene, cx, cz)` that creates a city block by calling your other functions. The city block should include:

- At least **two cars** (using `draw_sedan`)
- At least **two trees** of different heights (using `draw_tree`)
- At least **one fire hydrant** (using `draw_fire_hydrant`)
- At least **one stop light** (using `draw_stop_light`)
- At least **one sign** (using `draw_sign` from the example)
- At least **one building** (which can simply be a large box)

Here's an example city block:

![City Block Example](http://nifty.stanford.edu/2024/tralie-vrtual-cities/CityBlock.png)

#### Task 6: Build Your City

Now use the offset parameters (`cx`, `cz`) in your `draw_city_block` function to draw at least **two copies** of your city block at different positions, creating an entire city:

```python
# Example: Draw two city blocks at different positions
draw_city_block(scene, 0, 0)
draw_city_block(scene, 30, 0)
```

![City Block Repeated](http://nifty.stanford.edu/2024/tralie-vrtual-cities/CityBlockRepeated.png)

---

### Milestone 3

Time to get creative!

#### Art Contest

Create a new Python file called `artcontest.py` that generates a file called `artcontest.html` with any virtual world you want. Unleash your creativity! Your scene does not have to be a city - it can be anything you imagine.

Your scene will be evaluated on **Technical Implementation** and **Visual Creativity** as separate dimensions.

#### Tier 1: Foundational
- Create at least 3 custom functions that draw distinct objects
- Each function must accept position parameters (x, z or cx, cz)
- Functions are called at least twice each with different positions to demonstrate reusability
- All objects are created through function calls (no standalone objects in main code)

#### Tier 2: Intermediate
- Create multiple custom functions that draw distinct objects
- Several functions must accept additional parameters beyond position (e.g., size, height, color, or orientation)
- At least one function calls another custom function within it (composition)
- Functions are called multiple times with varying parameter values to show flexibility

#### Tier 3: Excellent
- Create several custom functions that draw distinct objects
- Multiple functions must accept multiple customization parameters (e.g., size AND color AND orientation)
- Multiple functions demonstrate composition (calling other custom functions)
- At least one function uses a complex parameter like rotation to create different orientations
- Functions demonstrate clear reusability with significantly different appearances based on parameters

#### Tier 4: Exceptional
- Create many custom functions that draw distinct objects
- Multiple functions accept several customization parameters with meaningful variety
- Clear hierarchy of functions: "primitive" functions (basic objects) are called by "composite" functions (complex objects/structures)
- Multiple functions use complex parameters (rotation, scaling, etc.)
- Demonstrates novel parameter usage (e.g., number of branches on a tree, number of windows in a building, detail level)
- Demonstrates sophisticated use of previously covered concepts (loops, conditionals, randomization, mathematical calculations)

#### Visual Creativity & Expressiveness

Evaluated separately based on:
- **Originality**: Is this a unique, interesting world/scene concept?
- **Cohesiveness**: Do the objects work together to create a unified scene?
- **Visual Interest**: Is the scene engaging to look at? Does it use color, scale, and positioning effectively?
- **Effort & Polish**: Does the scene feel complete and thoughtfully arranged?

You can use any combination of:
- The basic shapes you've learned (`add_box`, `add_cylinder`, `add_sphere`, etc.)
- The functions you've created (`draw_tree`, `draw_sedan`, etc.)
- Meshes from the `meshes/` folder for more complex objects

**Creating an Animation (Optional)**

You can create an animated GIF of your scene by selecting two camera positions and automatically flying between them:

![Selecting Cameras](http://nifty.stanford.edu/2024/tralie-vrtual-cities/SelectingCameras.gif)

The result looks like this:

![Animation Result](http://nifty.stanford.edu/2024/tralie-vrtual-cities/AnimationResult.gif)

> **Note:** Generating the GIF may take some time, and you may need to refresh the page after it finishes downloading.

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

## Rotations (Optional/Advanced)

Create a rotation group using `add_group(x, y, z, rx, ry, rz)`. All objects added to the group rotate together.

### Example: draw_tree

```python
def draw_tree(scene, cx, cz, height, rx=0, rz=0):
    # Create a group positioned at the tree's base, with rotation applied
    group = scene.add_group(cx, 0, cz, rx, 0, rz)
    
    # Add objects to the group (they rotate together)
    # x, y, z coords are relative to the group's center position
    group.add_cylinder(0, height/2, 0, 0.3, height, 102, 51, 0, 1, 0)
    group.add_ellipsoid(0, height, 0, 1, 1, 1, 0, 255, 0, 1, 0)
```

### Sample Calls

```python
# Straight up
draw_tree(scene, 5, 5, 6)

# Slightly tilted
draw_tree(scene, 10, 5, 7, rx=30)

# Horizontal
draw_tree(scene, 10, 5, 5, rz=90)
```