from manim import *

class Test(Scene):
    def construct(self):
        text = Tex(r"Let's pick some random points", font_size=72).to_corner(UL)
        box = BackgroundRectangle(text, color=None, fill_opacity = 0.8)
        number_plane = NumberPlane(
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.6
            }
        )
        self.add(number_plane)
        self.play(Create(box))
        self.wait(2)
        self.play(Create(text))
        self.wait(2)

class AxesTemplate(Scene):
    def construct(self):
        graph = Axes(
            x_range=[-1,10,1],
            y_range=[-1,10,1],
            x_length=9,
            y_length=6,
            axis_config={"include_tip":False}
        )
        labels = graph.get_axis_labels()
        self.add(graph, labels)
        self.play(graph, run_time=5)

class TLabelExample(Scene):
    def construct(self):
        # defines the axes and linear function
        axes = Axes(x_range=[-1, 10], y_range=[-1, 10], x_length=9, y_length=6)
        func = axes.plot(lambda x: x, color=BLUE)
        # creates the T_label
        t_label = axes.get_T_label(x_val=4, graph=func, label=Tex("x-value"))
        self.add(axes)

        self.play(Create(func), Create(t_label), run_time=3)

# class CreateCircle(Scene):
#     def construct(self):
#         circle = Circle()  # create a circle
#         circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
#         self.play(Create(circle), run_time=2)  # show the circle on screen