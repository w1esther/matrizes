from manim import *
import numpy as np

class Matriz(Scene):
    def construct(self):

        titulo = Text('Soma de Matrizes', font_size=32).shift(3*UP)

        self.play(Write(titulo), run_time = 2)

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

        igual1 = MathTex(r'=').shift(1*UP + 2*RIGHT)

        self.play(FadeIn(igual1))

        C = Matrix([
            ["?","?","?"],
            ["?","?","?"],
            ["?","?","?"]
        ]).shift(1*UP + 4.5*RIGHT)

        legenda_1 = Text('Somamos os elementos que ocupam a mesma posição.', font_size=26).shift(1*DOWN)

        self.play(Write(legenda_1), run_time = 2)

        self.wait(2)

        self.play(FadeIn(C))

        valores_A = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 3, 4]
        ]

        valores_B = [
            [5, 3, 7],
            [2, 5, 1],
            [3, 9, 6]
        ]

        valores_C = [
            [6, 5, 10],
            [6, 10, 7],
            [10, 12, 10]
        ]

        for n in range(3):
            for i in range(3):

                indice = (n*3+i)

                elemento_A = A.get_entries()[indice]
                elemento_B = B.get_entries()[indice]    

                destaque_A = SurroundingRectangle(elemento_A, buff=0.08)
                destaque_B = SurroundingRectangle(elemento_B, buff=0.08)

                self.play(Create(destaque_A), Create(destaque_B), run_time = 2)

                adicao_matriz = MathTex(f'{valores_A[n][i]} + {valores_B[n][i]} = {valores_C[n][i]}').shift(1*DOWN)

                self.play(Transform(legenda_1, adicao_matriz))

                elemento_antigo = C.get_entries()[indice]

                resultado = valores_C[n][i]

                elemento_novo = MathTex(str(resultado)).move_to(elemento_antigo)

                self.play(ReplacementTransform(elemento_antigo, elemento_novo))

                self.wait(1)

                self.play(FadeOut(destaque_A), FadeOut(destaque_B))
        
        legenda_2 = Tex(
            r"A adição de matrizes é uma operação matematicamente definida",
            r" se, e somente se, as matrizes envolvidas forem de mesma ordem $m \times n$."
            r" Isso significa que elas precisam ter o mesmo número de linhas e o mesmo número de colunas.").scale(0.7).shift(1.5*DOWN)

        self.play(Transform(legenda_1, legenda_2))

        self.wait(4)