from manim import *
import numpy as np

class MassSpringDamper(Scene):
    def construct(self):
        # -----------------------------
        # Parameters
        # -----------------------------
        m = 2
        c = 1
        k = 10

        omega_n = np.sqrt(k / m)
        zeta = c / (2 * np.sqrt(m * k))
        omega_d = omega_n * np.sqrt(1 - zeta**2)

        # -----------------------------
        # Static elements
        # -----------------------------
        wall = Line(LEFT * 5, LEFT * 4, stroke_width=6)

        mass = Square(
            side_length=0.8,
            fill_color=BLUE,
            fill_opacity=1
        )

        mass.move_to(RIGHT * 1)

        spring = always_redraw(
            lambda: self.get_spring(
                start=LEFT * 4,
                end=mass.get_left(),
                coils=8
            )
        )

        self.add(wall, spring, mass)

        # -----------------------------
        # Equation display
        # -----------------------------
        equation = MathTex(
            r"m x''(t)",
            r"+",
            r"c x'(t)",
            r"+",
            r"k x(t)",
            r"= 0",
        )

        # Color coding
        equation[0].set_color(RED)     # m x''(t)
        equation[2].set_color(GREEN)   # c x'(t)
        equation[4].set_color(BLUE)    # k x(t)

        # Make it big and visible
        equation.scale(1.3)
        equation.to_edge(UP)

        self.play(Write(equation))
        self.wait(1)

        # -----------------------------
        # Motion function
        # -----------------------------
        def displacement(t):
            return np.exp(-zeta * omega_n * t) * np.cos(omega_d * t)

        tracker = ValueTracker(0)

        mass.add_updater(
            lambda m: m.move_to(
                RIGHT * (1 + displacement(tracker.get_value()))
            )
        )

        # -----------------------------
        # Animate motion
        # -----------------------------
        self.play(
            tracker.animate.set_value(10),
            run_time=10,
            rate_func=linear
        )

        mass.clear_updaters()
        self.wait(2)

    def get_spring(self, start, end, coils=8):
        points = []
        length = end[0] - start[0]
        dx = length / (coils * 2)

        for i in range(coils * 2 + 1):
            x = start[0] + i * dx
            y = 0.15 * (-1)**i
            points.append(np.array([x, y, 0]))

        points[0][1] = 0
        points[-1][1] = 0

        return VMobject().set_points_smoothly(points).set_color(WHITE)
    


class UndampedMassSpring(Scene):
    def construct(self):
        # -----------------------------
        # Parameters
        # -----------------------------
        m = 3
        k = 7
        A = 2
        omega = np.sqrt(k / m)

        # -----------------------------
        # Static objects
        # -----------------------------
        wall = Line(LEFT * 5, LEFT * 4, stroke_width=6)

        mass = Square(
            side_length=0.8,
            fill_color=RED,
            fill_opacity=1,
            stroke_color=BLACK
        ).move_to(RIGHT * 1)

        spring = always_redraw(
            lambda: self.get_spring(
                start=LEFT * 4,
                end=mass.get_left(),
                coils=8
            )
        )

        self.camera.background_color =  "#FFF6EB"

        self.add(wall, mass, spring)

        # -----------------------------
        # Equation
        # -----------------------------
        equation = MathTex(
            r"m x''(t)",
            r"+",
            r"k x(t)",
            r"= 0"
        ).scale(1.4).to_edge(UP)

        equation[0].set_color("#500000")     # m x''(t)
        equation[1].set_color(BLACK)
        equation[2].set_color("#000050")   # c x'(t)
        equation[3].set_color(BLACK)

        self.add(equation)

        # -----------------------------
        # Motion
        # -----------------------------
        tracker = ValueTracker(0)

        def x(t):
            return A * np.cos(omega * t)

        mass.add_updater(
            lambda m: m.move_to(
                RIGHT * (1 + x(tracker.get_value()))
            )
        )

        self.play(
            tracker.animate.set_value(8 * np.pi),
            run_time=10,
            rate_func=linear
        )

        mass.clear_updaters()
        self.wait(1)

    def get_spring(self, start, end, coils=8):
        points = []
        length = end[0] - start[0]
        dx = length / (coils * 2)

        for i in range(coils * 2 + 1):
            x = start[0] + i * dx
            y = 0.15 * (-1)**i
            points.append(np.array([x, y, 0]))

        points[0][1] = 0
        points[-1][1] = 0

        return VMobject().set_points_smoothly(points).set_color(BLACK)

