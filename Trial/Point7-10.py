from manim import *

class TransformPresentation(ThreeDScene):
    def construct(self):
        # Axes for the whole scene
        axes = ThreeDAxes()
        self.add(axes)
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES, distance=12)

        
        # ---------- 1. Homogeneous Coordinates ----------
        cube_h = Cube().set_fill(BLUE, opacity=0.5)
        self.add(cube_h)
        self.play(cube_h.animate.rotate_about_origin(PI/4), run_time=2)
        self.wait(2)
        self.remove(cube_h)
        self.play(cube_h.animate.rotate_about_origin(-PI/4), run_time=0.01)
        self.add(cube_h)
        self.play(cube_h.animate.rotate_about_origin(PI/4).shift(RIGHT*2 + UP), run_time=2)
        self.wait(2)
        self.remove(cube_h)

        # ---------- 2. Combining Transformations ----------
        cube1 = Cube().set_fill(GREEN, opacity=0.5).move_to(LEFT*3)
        cube2 = Cube().set_fill(RED, opacity=0.5).move_to(RIGHT*3)
        self.add(cube1, cube2)
        self.play(
            cube1.animate.scale(1.5),
            cube2.animate.shift(UP*2),
            run_time=1
        )
        self.play(
            cube1.animate.rotate_about_origin(PI/4),
            cube2.animate.rotate_about_origin(PI/4),
            run_time=1
        )
        self.play(
            cube1.animate.shift(UP*2),
            cube2.animate.scale(1.5),
            run_time=1
        )
        self.wait(2)
        self.remove(cube1, cube2)

        # ---------- 3. Local vs World Space ----------
        local_cube = Cube().set_fill(YELLOW, opacity=0.7).move_to(UP*1.5)
        world_cube = Cube().set_fill(GRAY, opacity=0.2)
        self.add(local_cube, world_cube)
        self.play(local_cube.animate.rotate_about_origin(PI/2), run_time=2)  # local
        self.wait(2)
        self.play(local_cube.animate.move_to(UP*1.5).rotate(PI/2, axis=Y_AXIS), run_time=2)  # world
        self.wait(2)
        self.remove(local_cube, world_cube)

        # ---------- 4. Hierarchical Transformations ----------
        body = Cube(side_length=2).set_fill(BLUE, opacity=0.5)
        arm = Cube(side_length=0.5).set_fill(RED, opacity=0.7).next_to(body, RIGHT, buff=0)
        group = VGroup(body, arm)
        self.add(group)
        self.play(group.animate.rotate_about_origin(PI/6), run_time=2)
        self.wait(2)
        self.play(group.animate.shift(UP*2), run_time=2)
        self.wait(2)
        self.remove(group)

        # ---------- 5. Camera Transformations ----------
        cube_cam = Cube().set_fill(PURPLE, opacity=0.5)
        self.add(cube_cam, axes)
        self.set_camera_orientation(phi=60*DEGREES, theta=-45*DEGREES, distance=10)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        self.remove(cube_cam)
