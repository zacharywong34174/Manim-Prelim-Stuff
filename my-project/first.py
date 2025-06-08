from manim import *

'''
manim -qm -p file_name.py class_name (IF JUST IMAGE)
manim -pqh file_name.py class_name (IF ANIMATION)
'''

class TestScene(Scene):
    def construct(self):
        text_test = Tex(r'What is slope?')
        self.play(Create(text_test), run_time = 2)
        self.play(FadeOut(text_test), run_time=1.5)
        self.wait(1)

        ref_func_1 = Tex(r'$f(x) = x^2$')
        temp_height = ref_func_1.get_height()
        lead = Tex(r"Here's an example function:").shift(UP*temp_height)

        self.play(FadeIn(VGroup(lead, ref_func_1)), run_time = 1)
        self.wait(1)

        self.play(VGroup(ref_func_1, lead).animate.to_corner(UP).scale(0.7), run_time = 1.5)
        self.wait(1)

        ax = Axes(
            x_range = [-5, 5, 1],
            y_range = [-5, 5, 1],
            tips=False
        )

        ax = ax.shift(DOWN*0.5)

        self.play(FadeIn(ax), run_time=1)
        self.wait(1)

        graph = ax.plot(lambda x: x**2, x_range=[-2.35, 2.35], color=ORANGE)
        self.play(Create(graph), run_time=2)
        self.play(FadeOut(lead))
        self.play(ref_func_1.animate.shift(UP*0.5).set_color(YELLOW_C), run_time=1)
        self.wait(2)

        text = Tex(r"Let's pick some random points", font_size=72).shift(DOWN*2.5)
        box = BackgroundRectangle(text, color=None, fill_opacity=0.2)
        self.play(FadeIn(VGroup(text, box)), run_time = 2)
        self.wait(1)
        self.play(FadeOut(VGroup(text, box)), run_time = 0.3)

        text2 = Tex(r"Let's have one pair of dots at $(-2, 4)$ and $(0, 0)$.").shift(DOWN*2.5)
        green_dot = Dot(color=GREEN)
        another_green_dot = Dot(color=GREEN)
        text3 = Tex(r"Let's have another pair at $(-1, 1)$ and $(1, 1)$.").shift(DOWN*2.5)
        yellow_dot = Dot(color=YELLOW)
        another_yellow_dot = Dot(color=YELLOW)
        text4 = Tex(r"And finally another one at $(0, 0)$ and $(2, 4)$.").shift(DOWN*2.5)
        red_dot = Dot(color=RED)
        another_red_dot = Dot(color=RED)

        import itertools

        colors = ['GREEN', 'YELLOW', 'RED']
        color_cycle = itertools.cycle(colors)

        def rinse_and_repeat(text, dot1, dot2, x1, y1, x2, y2):
            box = BackgroundRectangle(text, color=None, fill_opacity=0.2)
            self.play(Create(VGroup(box, text)))
            self.play(dot1.animate.move_to(ax.coords_to_point(x1, y1)))
            self.play(dot2.animate.move_to(ax.coords_to_point(x2, y2)))
            line = Line(ax.coords_to_point(x1, y1), ax.coords_to_point(x2, y2))
            self.play(Create(line))
            self.play(line.animate.set_color(next(color_cycle)), run_time = 0.3)
            self.wait(2)
            self.play(FadeOut(VGroup(box, text)), run_time = 0.5)
        
        rinse_and_repeat(text2, green_dot, another_green_dot, -2, 4, 0, 0)
        rinse_and_repeat(text3, yellow_dot, another_yellow_dot, -1, 1, 1, 1)
        rinse_and_repeat(text4, red_dot, another_red_dot, 0, 0, 2, 4)

        '''
        Now let's temporarily take away the coordinate plane.
        '''

    