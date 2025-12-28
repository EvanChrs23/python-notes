from manim import *
import numpy as np

class InverseLaplaceContour(Scene):
    def construct(self):

        # =====================================================
        # 1. Complex Plane
        # =====================================================
        plane = ComplexPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            background_line_style={"stroke_opacity": 0.4}
        ).add_coordinates()

        self.play(Create(plane))
        self.wait(1)

        # =====================================================
        # 2. Poles of F(s) = 1/(s^2 + 1)
        # =====================================================
        pole_top = Dot(plane.c2p(0, 1), color=RED)
        pole_bot = Dot(plane.c2p(0, -1), color=RED)

        pole_top_label = MathTex("s=i").next_to(pole_top, LEFT)
        pole_bot_label = MathTex("s=-i").next_to(pole_bot, LEFT)

        self.play(FadeIn(pole_top, pole_bot))
        self.play(Write(pole_top_label), Write(pole_bot_label))
        self.wait(1)

        # =====================================================
        # 3. Bromwich Contour Re(s) = gamma
        # =====================================================
        gamma = 1.5
        bromwich = Line(
            plane.c2p(gamma, -3.5),
            plane.c2p(gamma, 3.5),
            color=YELLOW
        )

        bromwich_label = MathTex(r"\text{Re}(s)=\gamma").next_to(bromwich, RIGHT)

        self.play(Create(bromwich), Write(bromwich_label))
        self.wait(1)

        # =====================================================
        # 4. Close the contour (LEFT half-plane)
        # =====================================================
        arc = Arc(
            radius=3.5,
            start_angle=-PI/2,
            angle=PI,
            arc_center=plane.c2p(0, 0),
            color=BLUE
        )

        closing_text = Text(
            "Close contour (t > 0)",
            font_size=30
        ).to_corner(UL)

        self.play(Create(arc), FadeIn(closing_text))
        self.wait(1)

        # =====================================================
        # 5. Show exponential decay on arc (Jordan's Lemma)
        # =====================================================
        decay_text = MathTex(
            r"e^{st} = e^{\sigma t}e^{i\omega t}",
            r"\quad \sigma < 0 \Rightarrow e^{\sigma t} \to 0"
        ).next_to(closing_text, DOWN)

        self.play(Write(decay_text))
        self.wait(2)

        self.play(FadeOut(arc))
        self.wait(1)

        # =====================================================
        # 6. Highlight enclosed poles
        # =====================================================
        self.play(
            pole_top.animate.set_color(YELLOW),
            pole_bot.animate.set_color(YELLOW)
        )

        inside_text = Text(
            "Only poles inside the contour contribute",
            font_size=30
        ).to_corner(UR)

        self.play(FadeIn(inside_text))
        self.wait(2)

        # =====================================================
        # 7. Residue explanation
        # =====================================================
        residue_formula = MathTex(
            r"\oint_{\mathcal C} f(s)\,ds",
            "=",
            r"2\pi i \sum \mathrm{Res}(f,s_k)"
        ).to_edge(UP)

        self.play(Write(residue_formula))
        self.wait(2)

        # =====================================================
        # 8. Local behavior near a pole (linearization)
        # =====================================================
        local_text = MathTex(
            r"f(s) \approx \frac{A}{s-s_0}",
            r"\quad \text{near a simple pole}"
        ).next_to(residue_formula, DOWN)

        self.play(Write(local_text))
        self.wait(2)

        # =====================================================
        # 9. Residue contribution to time domain
        # =====================================================
        time_domain = MathTex(
            r"f(t) = \sum_k e^{s_k t}\,\mathrm{Res}(F,s_k)"
        ).to_edge(DOWN)

        self.play(Write(time_domain))
        self.wait(3)
