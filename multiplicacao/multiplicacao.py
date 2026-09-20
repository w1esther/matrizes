from manim import *

class MultiplicacaoDeMatrizes(MovingCamera):
    def construct(self):

        self.play(self.camera.frame.animate.scale(1.5))
        
        titulo = Tex(r'Multiplicação de Matrizes', font_size=32).shift(3.5*UP)

        self.play(Write(titulo))

        self.wait()