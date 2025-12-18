from manim import *

class TransformExample(ThreeDScene):
    def construct(self):
        # Create 3D axes
        axes = ThreeDAxes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            z_range=[-5, 5, 1]
        )
        self.add(axes)

        # Better camera orientation for presentation
        self.set_camera_orientation(phi=70*DEGREES, theta=-60*DEGREES, distance=12)

        # -------- ROTATION --------
        cube1 = Cube(side_length=2)
        cube1.set_fill(BLUE, opacity=0.3)
        cube1.move_to(ORIGIN)
        self.add(cube1)

        self.play(cube1.animate.rotate_about_origin(PI / 4))
        self.wait(1)

        self.play(FadeOut(cube1))  # Remove cube before next case

        # -------- SCALING --------
        cube2 = Cube(side_length=2)
        cube2.set_fill(GREEN, opacity=0.5)
        cube2.move_to(ORIGIN)
        self.add(cube2)

        self.play(cube2.animate.scale(1.5))
        self.wait(1)

        self.play(FadeOut(cube2))  # Remove cube before next case

        # -------- TRANSLATION --------
        cube3 = Cube(side_length=2)
        cube3.set_fill(RED, opacity=0.5)
        cube3.move_to(ORIGIN)
        self.add(cube3)

        self.play(cube3.animate.shift(UP*2 + RIGHT*2))
        self.wait(1)

        self.play(FadeOut(cube3))

        # -------- COMBINATION --------
        # Show all transformations together
        combined_cube = Cube(side_length=2)
        combined_cube.set_fill(PURPLE, opacity=0.5)
        combined_cube.move_to(ORIGIN)
        self.add(combined_cube)

        self.play(
            combined_cube.animate.rotate_about_origin(PI / 3)
            .scale(0.5)
            .shift(DOWN*2 + LEFT*2)
        )
        self.wait(2)
