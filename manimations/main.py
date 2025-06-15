from manim import *

class Test(Scene):
    def construct(self):
        circles = VGroup(*[Circle(color=RED, fill_opacity=0.5) for _ in range(20)]).arrange_in_grid(4,5).scale(0.75)
        self.play(AnimationGroup(*[Create(circle) for circle in circles], lag_ratio=0.5))

        # squares = VGroup(*[Square(color=RED) for j in range(20)]).arrange_in_grid(4,5).scale(0.75)
        # self.play(AnimationGroup(*[Create(s) for s in squares], lag_ratio = 0.15))
