from manim import *

class TransformPresentation(ThreeDScene):
    def construct(self):
        # Axes for the whole scene
        axes = ThreeDAxes()
        self.add(axes)
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES, distance=12)
        

        # ---------- 3. Local vs World Space ----------
        local_cube = Cube().set_fill(YELLOW, opacity=0.7).move_to(UP*1.5)
        world_cube = Cube().set_fill(GRAY, opacity=0.2)
        self.add(local_cube, world_cube)
        self.play(local_cube.animate.rotate_about_origin(PI/2), run_time=2)  # local
        self.wait(2)
        self.play(local_cube.animate.rotate_about_origin(-PI/2), run_time=0.02)
        self.play(local_cube.animate.rotate(PI/2, axis=Z_AXIS), run_time=2)  # world
        self.wait(2)
        self.remove(local_cube, world_cube)