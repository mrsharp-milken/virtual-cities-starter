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
- [Example: Drawing a Snowman](#example-drawing-a-snowman)
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
- [Rotations](#rotations-groups)

---

## Overview

In this project, you will write Python code to generate 3D worlds. You'll create functions that draw specific city objects like trees and fire hydrants. These functions can then be called repeatedly to build complex scenes.

Your Python code will generate HTML files that you can view in your browser using VSCodium's Five Server extension.

<details>
<summary>Watch an optional video primer on this project (click to expand)</summary>

[![Virtual Cities Introduction](https://img.youtube.com/vi/lhvl-rUBLO8/0.jpg)](https://www.youtube.com/watch?v=lhvl-rUBLO8)

</details>

---

## Setup

### Downloading the Starter Code

Open VSCodium and your cs50-workspace. Open a new terminal, and run:

**MacOS / Linux:**
```bash
git clone --depth 1 https://github.com/mrsharp-milken/virtual-cities-starter.git virtual-cities && rm -rf virtual-cities/.git
```

**Windows (PowerShell):**
```powershell
git clone --depth 1 https://github.com/mrsharp-milken/virtual-cities-starter.git virtual-cities; if ($?) { Remove-Item -Recurse -Force virtual-cities\.git }
```

This creates a new `virtual-cities` folder inside your workspace. The last part of the command deletes the starter code's own `.git` folder so that it doesn't interfere with your workspace's existing git setup. You should now see a `virtual-cities` folder in the file explorer.

### Files You'll Have

These are inside your `virtual-cities` folder:

- `Scene3D.py` - The library that provides functions for drawing 3D shapes
- `simplescene.py` - Starter code with an example scene
- `meshes/` - 3D models you can use
- `jsmodules/` - Required files for the viewer

### Running Your Code

1. Open your project folder in VSCodium
2. In the terminal, move into the starter folder: `cd virtual-cities`
3. Run your Python file:

   **MacOS / Linux:**
   ```bash
   python3 simplescene.py
   ```

   **Windows:**
   ```bash
   python simplescene.py
   ```
4. This generates an HTML file (e.g., `simplescene.html`)
5. Right-click the HTML file in VSCodium and select **"Open with Five Server"**

<img height="330" alt="Screenshot 2025-12-15 at 1 32 19 AM" src="https://gist.github.com/user-attachments/assets/65799d86-1ca9-457f-a391-080cf26c51e6" />

<br>

<br>

6. Your 3D scene will open in your browser

> **Note:** You must use Five Server (not just double-clicking the HTML file) because the browser needs to load mesh files, which requires a web server.

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
scene.add_box(0, 2, -6, 1, 4, 1, 0, 255, 0)
```

Parameters: `add_box(cx, cy, cz, xlen, ylen, zlen, r, g, b)` (plus optional `roughness` and `metalness`, see [Material Properties](#material-properties))

![Box Example](http://nifty.stanford.edu/2024/tralie-vrtual-cities/Box.png)

### Cylinder

```python
# Draw a yellow cylinder centered at (0, 1, -2) with radius 0.5 and height 2
scene.add_cylinder(0, 1, -2, 0.5, 2, 255, 255, 0)
```

Parameters: `add_cylinder(cx, cy, cz, radius, height, r, g, b)` (plus optional `roughness` and `metalness`)

![Cylinder Example](http://nifty.stanford.edu/2024/tralie-vrtual-cities/Cylinder.png)

### Cone

```python
# Draw a blue cone centered at (4, 0, 0) with radius 0.5 and height 6
scene.add_cone(4, 0, 0, 0.5, 6, 0, 0, 255)
```

Parameters: `add_cone(cx, cy, cz, radius, height, r, g, b)` (plus optional `roughness` and `metalness`)

![Cone Example](http://nifty.stanford.edu/2024/tralie-vrtual-cities/Cone.png)

### Sphere

```python
# Draw a cyan sphere with radius 1 centered at (-4, 4, 0)
scene.add_sphere(-4, 4, 0, 1, 0, 255, 255)
```

Parameters: `add_sphere(cx, cy, cz, radius, r, g, b)` (plus optional `roughness` and `metalness`)

![Sphere Example](http://nifty.stanford.edu/2024/tralie-vrtual-cities/Sphere.png)

### Ellipsoid

An ellipsoid is a stretched sphere with different radii along each axis.

```python
# Draw a red ellipsoid with radii 1/2/1 centered at (0, 5, -10)
scene.add_ellipsoid(0, 5, -10, 1, 2, 1, 255, 0, 0)
```

Parameters: `add_ellipsoid(cx, cy, cz, radx, rady, radz, r, g, b)` (plus optional `roughness` and `metalness`)

![Ellipsoid Example](http://nifty.stanford.edu/2024/tralie-vrtual-cities/Ellipsoid.png)

---

## Material Properties

Shapes have two optional parameters that control their appearance. If you leave them out, you get a matte, non-metallic surface (`roughness=1`, `metalness=0`).

- **roughness** (0.0 - 1.0): How rough the surface is. 0.0 = smooth/shiny mirror, 1.0 = fully diffuse/matte (default 1.0)
- **metalness** (0.0 - 1.0): How metallic the surface looks. 0.0 = wood/stone, 1.0 = metal (default 0.0)

To set one, name it when you call the function:

```python
# A shiny, metallic gray sphere
scene.add_sphere(0, 1, -5, 1, 127, 127, 127, roughness=0.1, metalness=1)
```

---

## Example: Drawing a Snowman

Here's an example function from `simplescene.py` that draws a snowman using two white spheres and a black box for a hat:

```python
def simple_snowman(scene, cx, cz):
    # Big white bottom ball (radius 1, so its center is 1 above the ground)
    scene.add_sphere(cx, 1, cz, 1, 255, 255, 255)
    # Smaller white ball on top (radius 0.7), resting on the bottom ball
    scene.add_sphere(cx, 2.5, cz, 0.7, 255, 255, 255)
    # Black box for a hat, sitting on top of the head
    scene.add_box(cx, 3.4, cz, 0.7, 0.4, 0.7, 0, 0, 0)
```

### Anatomy of a function

- **`def simple_snowman(...)`** defines a new function. Everything indented below it is the function's body.
- **`scene`** is the 3D world you are drawing into. Every shape is added with `scene.add_...`, so a function can only draw if you hand it the scene. That's why `scene` is always the **first parameter**, and why you pass `scene` along whenever you call one of your functions.
- **`cx` and `cz`** are the position parameters. Inside the function, every shape uses `cx` and `cz` for its x and z coordinates, so the whole snowman moves when you change them. The y values are fixed because the snowman always stands on the ground.

Because the position is a parameter, you can call the function as many times as you like to put snowmen in different places:

```python
simple_snowman(scene, -4, -8)
simple_snowman(scene, 0, -12)
simple_snowman(scene, 5, -6)
```

Here's one more example, which loads meshes instead of building shapes:

```python
# Draw a shiny, stone-like, yellow Homer Simpson and a smokestack
scene.add_mesh("meshes/homer.obj", 1, 1.4, -7, 0, 0, 0, 1, 1, 1, 255, 255, 0, roughness=1, metalness=1)
scene.add_textured_mesh("meshes/smokestack/medres.obj", "meshes/smokestack/medres.mtl",
                      0, 18, -20, 0, 180, 0, 10, 10, 10, 0)
```

_For kicks, I also threw in Homer Simpson and the painted smokestack!_

---

## Your Tasks

Create functions to draw the following objects. Each function should take position parameters (`cx`, `cz`) so objects can be placed anywhere in the scene.

---

### Milestone 1

Complete the following two tasks to build basic city objects.

#### Task 1: Tree

In `simplescene.py`, finish the function `draw_tree(scene, cx, cz, height)`. It's already started for you, so complete the two TODOs: fill in the function body, and call `draw_tree` in `main()`. It should draw a simple "lollipop" tree:

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

Create a function `draw_sedan(scene, cx, cz, r, g, b, ry=0)` that draws a boxy car:

- **Bottom box** (car body): 4.5 meters long, 1.7 meters wide, 0.7 meters tall, in the specified color
- **Top box** (cabin): 3.5 meters long, 1.4 meters wide, 0.8 meters tall, slightly offset on top of the body
- **Four wheels**: Grey cylinders (RGB: 127, 127, 127) with radius 0.5 and appropriate height. A cylinder stands upright by default, so rotate each wheel 90 degrees around the x-axis to put it on its side.

The `ry` parameter is the car's rotation around the y-axis (the vertical axis), in degrees. It is optional and defaults to 0:
- `ry=0`: The car faces east/west
- `ry=90`: The car faces north/south

> **Do it in two steps:** First get the car working with no rotation, drawn facing east/west. Once it looks right, add the `ry` rotation so the car can face other directions. Use groups to do this: see [Rotations](#rotations-groups) at the bottom, but rotate only around `ry`. A car doesn't tilt, so you don't need `rx` or `rz` for the whole car.

Below is an example of a red east/west car and a yellow north/south car, with a fire hydrant and stop light for scale:

![Sedan Example](http://nifty.stanford.edu/2024/tralie-vrtual-cities/Sedan.png)

> **Note:** To rotate shapes, use the rotated versions of the shape methods. For example, `add_cylinder` takes optional rotation parameters (rx, ry, rz) for rotation in degrees around each axis.

#### Task 5: City Block

Create a function `draw_city_block(scene, cx, cz)` that creates a city block by calling your other functions. The city block should include:

- At least **two cars** (using `draw_sedan`)
- At least **two trees** of different heights (using `draw_tree`)
- At least **one fire hydrant** (using `draw_fire_hydrant`)
- At least **one stop light** (using `draw_stop_light`)
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
- Demonstrates sophisticated use of previously covered concepts (loops, randomization, mathematical calculations)

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
2. **Use the viewer**: Keep your browser open with Five Server - it will auto-refresh when you regenerate the HTML
3. **Position objects above ground**: The ground is at y=0, so objects should have positive y values
4. **Think about centers**: Shape positions are their centers, so a cylinder with height 2 centered at y=1 will sit on the ground (y=0)
5. **Experiment**: Try different sizes and positions to get shapes looking right

---

## Meshes (Optional/Advanced)

For more complex objects, you can load pre-made 3D meshes from the `meshes/` folder:

```python
# Add a mesh with position, rotation, scale, and color
scene.add_mesh("meshes/homer.obj", 1, 1.4, -7, 0, 0, 0, 1, 1, 1, 255, 255, 0, roughness=1, metalness=1)
```

Parameters: `add_mesh(path, cx, cy, cz, rx, ry, rz, sx, sy, sz, r, g, b)` (plus optional `roughness` and `metalness`)

Check the `meshes/` folder for available models including animals, people, and objects.

## Rotations (Groups)

Create a rotation group using `add_group(x, y, z, rx, ry, rz)`. All objects added to the group rotate together.

### Example: draw_tree

```python
def draw_tree(scene, cx, cz, height, rx=0, rz=0):
    # Create a group positioned at the tree's base, with rotation applied
    group = scene.add_group(cx, 0, cz, rx, 0, rz)
    
    # Add objects to the group (they rotate together)
    # x, y, z coords are relative to the group's center position
    group.add_cylinder(0, height/2, 0, 0.3, height, 102, 51, 0)
    group.add_ellipsoid(0, height, 0, 1, 1, 1, 0, 255, 0)
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