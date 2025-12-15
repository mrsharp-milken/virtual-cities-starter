"""
This code creates flat hierarchy scene for three.js
Ported from Scene3D.java / Scene3D.h
"""

HTML_PREFIX = '''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
    </head>
    <body>
        <!-- three.js scripts -->
        <!-- startup three.js -->
        <script src="jsmodules/three.min.js"></script>
        <script src="jsmodules/three.module.js"></script>
        <script src="jsmodules/gif.js"></script>
        <!-- load models and look at them-->
        <script src="jsmodules/OBJLoader.js"></script>
        <script src="jsmodules/MTLLoader.js"></script>
        <!-- postprocessing -->
        <script src="jsmodules/CopyShader.js"></script>
        <script src="jsmodules/Pass.js"></script>
        <script src="jsmodules/ShaderPass.js"></script>
        <script src="jsmodules/MaskPass.js"></script>
        <script src="jsmodules/EffectComposer.js"></script>
        <script src="jsmodules/RenderPass.js"></script>
        <script src="jsmodules/DigitalGlitch.js"></script>
        <script src="jsmodules/GlitchPass.js"></script>

        <!--Other outside libraries -->
        <script type="text/javascript" src="jsmodules/jquery-3.5.1.min.js"></script>
        <script type="text/javascript" src="jsmodules/dat.gui.min.js"></script>
        <script type="text/javascript" src="jsmodules/gl-matrix-min.js"></script>

        <!-- Our code -->
        <script type="text/javascript" src="cameras3d.js"></script>
        <script type="text/javascript" src="scenecanvas.js"></script>


'''

HTML_END = '''<table cellpadding>
    <tr>
        <td>
            <h3>Controls</h3>
            <ul>
                <li><b>Mouse</b>: Click and drag to look around</li>
                <li><b>W:</b> Forward</li>
                <li><b>S:</b> Backwards</li>
                <li><b>A:</b> Left</li>
                <li><b>D:</b> Right</li>
                <li><b>E:</b> Up</li>
                <li><b>C:</b> Down</li>
            </ul>
        </td>
    </tr>
</table>
    </body>
</html>'''


class Scene3D:
    def __init__(self):
        self._scene_code = "let canvas = new SceneCanvas();\n"

    def add_box(self, cx, cy, cz, xlen, ylen, zlen, r, g, b,
                roughness, metalness, rx=0, ry=0, rz=0):
        """
        Add a box to the scene

        Args:
            cx: X center of box
            cy: Y center of box
            cz: Z center of box
            xlen: Length of box along x-axis
            ylen: Length of box along y-axis
            zlen: Length of box along z-axis
            r: Red component in [0, 255]
            g: Green component in [0, 255]
            b: Blue component in [0, 255]
            roughness: How rough the material appears. 0.0 means a smooth mirror
                       reflection, 1.0 means fully diffuse.
            metalness: How much the material is like a metal. Non-metallic materials
                       such as wood or stone use 0.0, metallic use 1.0.
            rx: Rotation about x-axis, in degrees (default 0)
            ry: Rotation about y-axis, in degrees (default 0)
            rz: Rotation about z-axis, in degrees (default 0)
        """
        self._scene_code += f"canvas.addBox({cx},{cy},{cz},{xlen},{ylen},{zlen},{r},{g},{b},{roughness},{metalness},{rx},{ry},{rz});\n"

    def add_cylinder(self, cx, cy, cz, radius, height, r, g, b,
                     roughness, metalness, rx=0, ry=0, rz=0, sx=1, sy=1, sz=1):
        """
        Add a cylinder to the scene

        Args:
            cx: X center of cylinder
            cy: Y center of cylinder
            cz: Z center of cylinder
            radius: Radius of the cylinder
            height: Height of the cylinder
            r: Red component in [0, 255]
            g: Green component in [0, 255]
            b: Blue component in [0, 255]
            roughness: How rough the material appears. 0.0 means a smooth mirror
                       reflection, 1.0 means fully diffuse.
            metalness: How much the material is like a metal. Non-metallic materials
                       such as wood or stone use 0.0, metallic use 1.0.
            rx: Rotation about x-axis, in degrees (default 0)
            ry: Rotation about y-axis, in degrees (default 0)
            rz: Rotation about z-axis, in degrees (default 0)
            sx: Scale about x-axis (default 1)
            sy: Scale about y-axis (default 1)
            sz: Scale about z-axis (default 1)
        """
        self._scene_code += f"canvas.addCylinder({cx},{cy},{cz},{radius},{height},{r},{g},{b},{roughness},{metalness},{rx},{ry},{rz},{sx},{sy},{sz});\n"

    def add_cone(self, cx, cy, cz, radius, height, r, g, b,
                 roughness, metalness, rx=0, ry=0, rz=0, sx=1, sy=1, sz=1):
        """
        Add a cone to the scene

        Args:
            cx: X center of cone
            cy: Y center of cone
            cz: Z center of cone
            radius: Radius of the cone
            height: Height of the cone
            r: Red component in [0, 255]
            g: Green component in [0, 255]
            b: Blue component in [0, 255]
            roughness: How rough the material appears. 0.0 means a smooth mirror
                       reflection, 1.0 means fully diffuse.
            metalness: How much the material is like a metal. Non-metallic materials
                       such as wood or stone use 0.0, metallic use 1.0.
            rx: Rotation about x-axis, in degrees (default 0)
            ry: Rotation about y-axis, in degrees (default 0)
            rz: Rotation about z-axis, in degrees (default 0)
            sx: Scale about x-axis (default 1)
            sy: Scale about y-axis (default 1)
            sz: Scale about z-axis (default 1)
        """
        self._scene_code += f"canvas.addCone({cx},{cy},{cz},{radius},{height},{r},{g},{b},{roughness},{metalness},{rx},{ry},{rz},{sx},{sy},{sz});"

    def add_ellipsoid(self, cx, cy, cz, radx, rady, radz, r, g, b,
                      roughness, metalness, rx=0, ry=0, rz=0):
        """
        Add an ellipsoid to the scene

        Args:
            cx: X center of ellipsoid
            cy: Y center of ellipsoid
            cz: Z center of ellipsoid
            radx: Semi-axis x radius
            rady: Semi-axis y radius
            radz: Semi-axis z radius
            r: Red component in [0, 255]
            g: Green component in [0, 255]
            b: Blue component in [0, 255]
            roughness: How rough the material appears. 0.0 means a smooth mirror
                       reflection, 1.0 means fully diffuse.
            metalness: How much the material is like a metal. Non-metallic materials
                       such as wood or stone use 0.0, metallic use 1.0.
            rx: Rotation about x-axis, in degrees (default 0)
            ry: Rotation about y-axis, in degrees (default 0)
            rz: Rotation about z-axis, in degrees (default 0)
        """
        self._scene_code += f"canvas.addEllipsoid({cx},{cy},{cz},{radx},{rady},{radz},{r},{g},{b},{roughness},{metalness},{rx},{ry},{rz});\n"

    def add_sphere(self, cx, cy, cz, radius, r, g, b, roughness, metalness):
        """
        Add a sphere to the scene

        Args:
            cx: X center of the sphere
            cy: Y center of the sphere
            cz: Z center of the sphere
            radius: Radius of the sphere
            r: Red component in [0, 255]
            g: Green component in [0, 255]
            b: Blue component in [0, 255]
            roughness: How rough the material appears. 0.0 means a smooth mirror
                       reflection, 1.0 means fully diffuse.
            metalness: How much the material is like a metal. Non-metallic materials
                       such as wood or stone use 0.0, metallic use 1.0.
        """
        self.add_ellipsoid(cx, cy, cz, radius, radius, radius, r, g, b, roughness, metalness)

    def add_mesh(self, path, cx, cy, cz, rx, ry, rz, sx, sy, sz, r, g, b,
                 roughness, metalness):
        """
        Add a mesh to the scene

        Args:
            path: File path to special mesh, relative to this directory
            cx: Offset in x
            cy: Offset in y
            cz: Offset in z
            rx: Rotation around x-axis
            ry: Rotation around y-axis
            rz: Rotation around z-axis
            sx: Scale along x-axis
            sy: Scale along y-axis
            sz: Scale along z-axis
            r: Red component in [0, 255]
            g: Green component in [0, 255]
            b: Blue component in [0, 255]
            roughness: How rough the material appears. 0.0 means a smooth mirror
                       reflection, 1.0 means fully diffuse.
            metalness: How much the material is like a metal. Non-metallic materials
                       such as wood or stone use 0.0, metallic use 1.0.
        """
        self._scene_code += f'canvas.addMesh("{path}",{cx},{cy},{cz},{rx},{ry},{rz},{sx},{sy},{sz},{r},{g},{b},{roughness},{metalness});\n'

    def add_textured_mesh(self, path, matpath, cx, cy, cz, rx, ry, rz,
                          sx, sy, sz, shininess):
        """
        Add a textured mesh to the scene

        Args:
            path: File path to mesh, relative to this directory
            matpath: File path to material, relative to this directory
            cx: Offset in x
            cy: Offset in y
            cz: Offset in z
            rx: Rotation around x-axis
            ry: Rotation around y-axis
            rz: Rotation around z-axis
            sx: Scale along x-axis
            sy: Scale along y-axis
            sz: Scale along z-axis
            shininess: A number in [0, 255] describing how shiny the mesh is
        """
        self._scene_code += f'canvas.addTexturedMesh("{path}","{matpath}",{cx},{cy},{cz},{rx},{ry},{rz},{sx},{sy},{sz},{shininess});\n'

    def add_camera(self, x, y, z, rot):
        """
        Add a particular camera to the scene

        Args:
            x: X position of camera
            y: Y position of camera
            z: Z position of camera
            rot: Rotation in degrees about y-axis
        """
        self._scene_code += f"canvas.addCamera({x},{y},{z},{rot});\n"

    def add_point_light(self, x, y, z, r, g, b, intensity):
        """
        Add a point light to the scene at a particular (x, y, z) position
        and with a particular (r, g, b) color

        Args:
            x: X position of light
            y: Y position of light
            z: Z position of light
            r: Red component of light in [0, 255]
            g: Green component of light in [0, 255]
            b: Blue component of light in [0, 255]
            intensity: The intensity of the light, in [0, 1]
        """
        self._scene_code += f"canvas.addPointLight({x},{y},{z},{r},{g},{b},{intensity});\n"

    def add_directional_light(self, x, y, z, r, g, b, intensity):
        """
        Add a directional light to the scene at a particular (x, y, z) position,
        pointing with parallel rays towards the origin (0, 0, 0)
        and with a particular (r, g, b) color

        Args:
            x: X position of light
            y: Y position of light
            z: Z position of light
            r: Red component of light in [0, 255]
            g: Green component of light in [0, 255]
            b: Blue component of light in [0, 255]
            intensity: The intensity of the light, in [0, 1]
        """
        self._scene_code += f"canvas.addDirectionalLight({x},{y},{z},{r},{g},{b},{intensity});\n"

    def save_scene(self, filename, scene_name):
        """
        Save this scene to a file

        Args:
            filename: Path to which to save file (should end with .html)
            scene_name: Title of the scene to display in the viewer
        """
        html_str = HTML_PREFIX + "<script>\n"
        html_str += self._scene_code
        html_str += f'canvas.name = "{scene_name}";\n'
        html_str += "canvas.repaint();\n</script>"
        html_str += HTML_END

        with open(filename, 'w') as f:
            f.write(html_str)

