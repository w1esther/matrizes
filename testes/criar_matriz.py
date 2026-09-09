from manim import *
import numpy as np

class Matriz(Scene):
    def construct(self):

        A = Matrix([
            [1, 2, 3],
            [4, 5, 6],
            [7, 3, 4]
        ]).shift(1*UP+5*LEFT)

        B = Matrix([
            [5, 3, 7],
            [2, 5, 1],
            [3, 9, 6]
        ]).shift(1*UP + 0.5*LEFT)

        mais1 = MathTex(r'+').shift(1*UP + 2.7*LEFT)

        self.play(FadeIn(A),FadeIn(B),FadeIn(mais1), run_time=2)
        self.wait(2)

        igual1 = MathTex(r'=').shift(1*UP + 1.7*RIGHT)

        self.play(FadeIn(igual1))

        C = Matrix([
            ['1+5', '2+3', '3+7'],
            ['4+2', '5+5', '1+6'],
            ['7+3', '3+9', '4+6']
        ]).shift(1*UP + 4.5*RIGHT)

        self.play(FadeIn(C))

        self.wait(2)