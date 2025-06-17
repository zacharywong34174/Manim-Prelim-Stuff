from manim import *

'''
manim -qm -p file_name.py class_name (IF JUST IMAGE)
manim -pqh file_name.py class_name (IF ANIMATION)
'''

'''
Notes:
Change mobjects: transform...
Emphasize mobjects: indicate, circumscribe...
Draw border then fill 

.next_to()
.align_to()

.arrange()
.arrange_in_grid()

rate_func
AnimationGroup and lag_ratio

move_to_target!!!
    mob.generate_target()
    modify mob.target()
    animate with MoveToTarget(mob)
restore!!!
    mob.save_state()
    modify mob
    animate with Restore(mob)

UpdateFromAlphaFunc(mobject, function, run_time)
Where function takes mobject as first arg, alpha completion ratio second arg


Updater functions, inline and with dt 

Mobject updaters 
Scene updaters

Suspend updating, resume updating

ValueTracker


Interactivity

manim.opengl 
set_euler_angles with camera mobject; theta and phi 

surface 
surface mesh 
self.camera.light_source

OpenGLTexturedSurface

self.interactive_embed()
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
        self.play(ref_func_1.animate.shift(UP*0.5).set_color(ORANGE), run_time=1)
        self.wait(2)

        text = Tex(r"Let's pick some random points", font_size=72).shift(DOWN*2.5)
        box = BackgroundRectangle(text, color=None, fill_opacity=0.5)
        self.play(FadeIn(VGroup(text, box)), run_time = 2)
        self.wait(1)
        self.play(FadeOut(VGroup(text, box)), run_time = 0.3)

        text2 = Tex(r"Let's have one pair of dots at $(-2, 4)$ and $(0, 0)$.", substrings_to_isolate=["$(-2, 4)$", "$(0, 0)$"]).shift(DOWN*2.5)
        text2.set_color_by_tex("$(-2, 4)$", GREEN)
        text2.set_color_by_tex("$(0, 0)$", GREEN)
        green_dot = Dot(color=GREEN)
        another_green_dot = Dot(color=GREEN)
        text3 = Tex(r"Let's have another pair at $(-1, 1)$ and $(1, 1)$.", substrings_to_isolate=["$(-1, 1)$", "$(1, 1)$"]).shift(DOWN*2.5)
        text3.set_color_by_tex("$(-1, 1)$", YELLOW)
        text3.set_color_by_tex("$(1, 1)$", YELLOW)
        yellow_dot = Dot(color=YELLOW)
        another_yellow_dot = Dot(color=YELLOW)
        text4 = Tex(r"And finally another one at $(0, 0)$ and $(2, 4)$.", substrings_to_isolate=["$(0, 0)$", "$(2, 4)$"]).shift(DOWN*2.5)
        text4.set_color_by_tex("$(0, 0)$", RED)
        text4.set_color_by_tex("$(2, 4)$", RED)
        red_dot = Dot(color=RED)
        another_red_dot = Dot(color=RED)

        import itertools

        colors = ['GREEN', 'YELLOW', 'RED']
        color_cycle = itertools.cycle(colors)

        list_of_lines = []

        def rinse_and_repeat(text, dot1, dot2, x1, y1, x2, y2):
            box = BackgroundRectangle(text, color=None, fill_opacity=0.2)
            self.play(Create(VGroup(box, text)))
            self.play(dot1.animate.move_to(ax.coords_to_point(x1, y1)))
            self.play(dot2.animate.move_to(ax.coords_to_point(x2, y2)))
            line = Line(ax.coords_to_point(x1, y1), ax.coords_to_point(x2, y2))
            list_of_lines.append(line)
            self.play(Create(line))
            self.play(line.animate.set_color(next(color_cycle)), run_time = 0.3)
            self.wait(2)
            self.play(FadeOut(VGroup(box, text)), run_time = 0.5)
        
        rinse_and_repeat(text2, green_dot, another_green_dot, -2, 4, 0, 0)
        rinse_and_repeat(text3, yellow_dot, another_yellow_dot, -1, 1, 1, 1)
        rinse_and_repeat(text4, red_dot, another_red_dot, 0, 0, 2, 4)

        self.wait(2)

        transformation_group_1 = VGroup(ax, graph, ref_func_1, yellow_dot, another_yellow_dot, green_dot, another_green_dot, red_dot, another_red_dot)
        transformation_group_1.save_state()
        transformation_group_2 = VGroup(*list_of_lines)
        transformation_group_2.save_state()
        self.play(FadeOut(transformation_group_1), transformation_group_2.animate.arrange(RIGHT, buff=1), run_time=2)

        self.wait(2)

        text = Tex(r"What do you notice about the lines?").to_edge(UP).shift(DOWN)
        self.play(FadeIn(text), run_time=3)

        self.wait(1)

        text1 = Tex(r"Let's put \textit{balls} in the middle of each of these lines.", substrings_to_isolate=["balls"]).to_edge(UP).shift(DOWN)
        text1.set_color_by_tex("balls", YELLOW)
        gigachad = ImageMobject("media\\images\\first\\gigachad.jpg").scale(0.4)
        self.play(FadeTransform(text, text1, run_time=2), transformation_group_2.animate.arrange(RIGHT, buff=1.2))
        self.play(FadeIn(gigachad), run_time=0.3)
        self.play(FadeOut(gigachad), run_time=0.3)

        self.wait(1)

        line_centers = [line.get_center() for line in list_of_lines]

        positions = [UP*0.1414+RIGHT*0.1414, UP*0.2, UP*0.1414+LEFT*0.1414]
        positions_cycle = itertools.cycle(positions)

        list_dots = []

        for line_center in line_centers:
            dot = Dot(line_center, color=WHITE).shift(next(positions_cycle))
            list_dots.append(dot)
        self.play(Create(VGroup(*list_dots)), run_time = 0.5)

        self.wait(4.3)

        text2 = Tex(r"Where will the balls roll?").to_edge(UP).shift(DOWN)

        '''
        Question should be: What happens to the height of the balls as they go to the right? (word in small pieces, though)
        Which would be the easiest to walk across??
        '''

        text3b = Tex(r"What do you notice about the lines?").to_edge(UP).shift(DOWN)
        text3a = Tex(r"So the question again:").scale(0.8).next_to(text3b, UP)
        self.play(FadeTransform(text1, text2, run_time=2))
        self.wait(3)
        self.play(FadeTransform(text2, text3a, run_time=2), Uncreate(VGroup(*list_dots), run_time=1))
        self.play(FadeIn(text3b, run_time=2))

        self.wait(3)

        text4a = Tex(r"Fine, let's ask a different question.").scale(0.8).to_edge(UP)
        self.play(FadeTransform(VGroup(text3a, text3b), text4a, run_time=2), Uncreate(VGroup(*list_dots)))

        # Define the head as a circle
        head = Circle(radius=0.2, color=WHITE)

        # Define the body as a line
        body = Line(ORIGIN, DOWN, color=WHITE, stroke_width=3)
        body.next_to(head, DOWN, buff=0)

        # Define the arms as lines
        arm1 = Line(UP*0.5, LEFT * 0.75 * 0.5, color=WHITE, stroke_width=3)
        arm1.next_to(body.get_center(), LEFT, buff=0)
        arm2 = Line(UP*0.5, RIGHT * 0.75 * 0.5, color=WHITE, stroke_width=3)
        arm2.next_to(body.get_center(), RIGHT, buff=0)

        # # Define the legs as lines
        leg1 = Line(DOWN * 0.5, LEFT * 0.75 * 0.5, color=WHITE, stroke_width=3)
        leg2 = Line(DOWN * 0.5, RIGHT * 0.75 * 0.5, color=WHITE, stroke_width=3)
        leg2.next_to(body.get_center()+body.get_length()/2*DOWN*1.41, LEFT, buff=0)
        leg1.next_to(body.get_center()+body.get_length()/2*DOWN*1.41, RIGHT, buff=0)

        # # Group the parts of the figure
        # stick_figure = VGroup(head, body, arm1, arm2, leg1, leg2)
        # stick_figure.arrange_in_grid(row_spacing=0.1, col_spacing=0.1) # Arrange the parts
        # stick_figure.scale(1.5) # scale up the figure

        stick_figure = VGroup(head, body, arm1, arm2, leg1, leg2).scale(0.7)
        stick_figure_copy1 = stick_figure.copy()
        stick_figure_copy2 = stick_figure.copy()

        #can probably use an ANIMATE GROUP for this
        self.play(stick_figure.animate.move_to(list_of_lines[0].get_start()).rotate(-PI/4).shift(UP*0.3+RIGHT*0.8), 
            stick_figure_copy1.animate.move_to(list_of_lines[2].get_start()).rotate(PI/4).shift(UP*0.8+LEFT*0.3), 
            stick_figure_copy2.animate.move_to(line_centers[1]).shift(UP*body.get_length()+LEFT*list_of_lines[1].get_length()/2+RIGHT*0.2)
        )
        self.wait(3)
        text4b = Tex(r"How do these \textit{alpha males} \textbf{move} across these lines?").next_to(text4a, DOWN)
        self.play(FadeIn(text4b))
        self.wait(5)

        # def stick_updater(mobject, dt):
        #     bottom = mobject.get_bottom()
        
        # stick_figure.add_updater(
        #     lambda mob: mob.move_to(list_of_lines[0].get_start()).shift(list_of_lines[0].get_start()-mob.get_bottom())
        # )

        self.play(
            stick_figure.animate.move_to(list_of_lines[0].get_end()).shift(UP*0.63+RIGHT*0.25),
            stick_figure_copy1.animate.move_to(list_of_lines[2].point_from_proportion(1)).shift(UP*0.27+LEFT*0.65),
            stick_figure_copy2.animate.move_to(list_of_lines[1].point_from_proportion(1)).shift(UP*0.7+LEFT*0.28)
        )

        self.play(AnimationGroup(*[FadeOut(mob) for mob in VGroup(stick_figure, stick_figure_copy2, stick_figure_copy1)], lag_ratio=0.5, run_time=2))
        text5a = Tex(r"Answer: Person A is moving down, person B is staying level, and person C is moving up.").scale(0.75).to_edge(UP).shift(DOWN)
        self.play(FadeTransform(VGroup(text4a, text4b), text5a))

        self.wait(2)
        self.play(Restore(transformation_group_1), Restore(transformation_group_2), FadeOut(text5a))
        self.wait(2)

        text6a = Tex(r"So the green line has a \textbf{negative} slope (person goes down),").scale(0.75).to_edge(DOWN).shift(UP).set_color(GREEN)
        text6b = Tex(r"the yellow line has a \textbf{zero} slope (person's level doesn't change),").scale(0.75).to_edge(DOWN).shift(UP).set_color(YELLOW)
        text6c = Tex(r"and the red line has a \textbf{positive} slope (person goes up).").scale(0.75).to_edge(DOWN).shift(UP).set_color(RED)

        self.play(Create(VGroup(box, text6a)), run_time = 3)
        self.wait()
        self.play(Transform(VGroup(box, text6a), VGroup(box, text6b)), run_time = 3)
        self.wait()
        self.play(Transform(VGroup(box, text6a), VGroup(box, text6c)), run_time = 3)
        self.wait()
        self.play(FadeOut(VGroup(box, text6a)), run_time = 0.5)
        self.wait(2)

        text7a = Tex(r"But how do we \textit{numerically} measure\\ how \textbf{positive} or \textbf{negative} the slope is?").scale(0.75).to_edge(DOWN).shift(UP)
        self.play(Create(text7a), run_time = 3)
        self.play(FadeOut(transformation_group_1), transformation_group_2.animate.arrange(RIGHT, buff=1), FadeOut(text7a))
        self.wait()
        self.play(FadeOut(VGroup(list_of_lines[1], list_of_lines[2])))
        self.play(list_of_lines[0].animate.move_to([0,0,0]))
        self.wait(2)

        line0_copy1 = list_of_lines[0].copy()
        line0_copy2 = list_of_lines[0].copy()
        self.play(VGroup(list_of_lines[0], line0_copy1, line0_copy2).animate.scale(0.7))
        self.play(VGroup(list_of_lines[0], line0_copy1, line0_copy2).animate.arrange(RIGHT, buff=1.5).shift(DOWN*1.5), run_time = 2.5)
        self.play(Rotate(list_of_lines[0], PI/8), Rotate(line0_copy2, -PI/8))

        text8 = Tex(r"What are the signs of the slopes?").to_edge(UP).shift(DOWN*1.35).scale(0.9)
        text8a = Tex(r"\underline{Negative}").next_to(list_of_lines[0], UP).scale(0.5)
        text8b = text8a.copy().next_to(line0_copy1, UP)
        text8c = text8a.copy().next_to(line0_copy2, UP)
        self.play(Create(text8))
        self.wait(3)
        self.play(AnimationGroup(Create(text8a), Create(text8b), Create(text8c)), lag_ratio=1)
        self.play(AnimationGroup(FadeOut(text8a), FadeOut(text8b), FadeOut(text8c)), lag_ratio=1)
        self.wait(2)

        text9 = Tex(r"So \textit{how negative} are they?").to_edge(UP).shift(DOWN*1.35).scale(0.9)
        self.play(Transform(text8, text9), run_time=2.5)
        self.wait()
        self.play(Uncreate(text9))
        self.play(VGroup(list_of_lines[0], line0_copy1, line0_copy2).animate.shift(UP*1.5))

        x_min = list_of_lines[0].get_start()[0]
        x_max = list_of_lines[0].get_end()[0]
        y_min = min(list_of_lines[0].get_start()[1], list_of_lines[0].get_end()[1])
        y_max = max(list_of_lines[0].get_start()[1], list_of_lines[0].get_end()[1])
        temp_ax = Axes(
            x_range=[0, x_max-x_min+0.5, 0.25],
            y_range=[0, y_max-y_min+0.5, 0.25],
            x_length=x_max - x_min+0.5,
            y_length=y_max - y_min+0.5,
            tips=False,
            axis_config={"include_numbers": True,"font_size": 12}
        ).move_to(list_of_lines[0], LEFT).shift(LEFT*0.70+DOWN*0.15)#.align_to(list_of_lines[0], DL)

        self.play(Create(temp_ax))

        x_min_1 = line0_copy1.get_start()[0]
        x_max_1 = line0_copy1.get_end()[0]
        y_min_1 = min(line0_copy1.get_start()[1], line0_copy1.get_end()[1])
        y_max_1 = max(line0_copy1.get_start()[1], line0_copy1.get_end()[1])
        temp_ax_1 = Axes(
            x_range=[0, x_max_1-x_min_1+0.5, 0.25],
            y_range=[0, y_max_1-y_min_1+0.5, 0.25],
            x_length=x_max_1 - x_min_1+0.5,
            y_length=y_max_1 - y_min_1+0.5,
            tips=False,
            axis_config={"include_numbers": True,"font_size": 12}
        ).move_to(line0_copy1, LEFT).shift(LEFT*0.70+DOWN*0.15)
        
        self.play(Create(temp_ax_1))

        x_min_2 = line0_copy2.get_start()[0]
        x_max_2 = line0_copy2.get_end()[0]
        y_min_2 = min(line0_copy2.get_start()[1], line0_copy2.get_end()[1])
        y_max_2 = max(line0_copy2.get_start()[1], line0_copy2.get_end()[1])
        temp_ax_2 = Axes(
            x_range=[0, x_max_2-x_min_2+0.5, 0.25],
            y_range=[0, y_max_2-y_min_2+0.5, 0.25],
            x_length=x_max_2 - x_min_2+0.5,
            y_length=y_max_2 - y_min_2+0.5,
            tips=False,
            axis_config={"include_numbers": True,"font_size": 12}
        ).move_to(line0_copy2, LEFT).shift(LEFT*0.70+DOWN*0.15)

        self.play(Create(temp_ax_2))

        self.wait(2)

        '''
        Do formula. Then do the same for the other sloped graphs.
        What to do if 100 animations max?
        '''
    