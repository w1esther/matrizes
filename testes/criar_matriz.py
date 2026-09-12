from manim import *
import numpy as np

class Matriz(MovingCameraScene):
    def construct(self):

        self.play(self.camera.frame.animate.scale(1.5))

        titulo = Text('Soma de Matrizes', font_size=32).shift(3*UP)

        self.play(Write(titulo), run_time = 2)

        def termo_matriz(p, m, n):
            termo = MathTex(f"{p}_{{{m}{n}}}")
            return termo
        
        A_generica = MobjectMatrix([
            [termo_matriz('a', 1, 1), termo_matriz('a', 1, 2), termo_matriz('a', 1, 3)],
            [termo_matriz('a', 2, 1), termo_matriz('a', 2, 2), termo_matriz('a', 2, 3)],
            [termo_matriz('a', 3, 1), termo_matriz('a', 3, 2), termo_matriz('a', 3, 3)]]).shift(1*UP+5*LEFT)

        a_11 = MathTex("a_{11}").move_to(A_generica.get_entries()[0])
        
        B_generica = MobjectMatrix([
            [termo_matriz('b', 1, 1), termo_matriz('b', 1, 2), termo_matriz('b', 1, 3)],
            [termo_matriz('b', 2, 1), termo_matriz('b', 2, 2), termo_matriz('b', 2, 3)],
            [termo_matriz('b', 3, 1), termo_matriz('b', 3, 2), termo_matriz('b', 3, 3)]], v_buff=0.75).shift(1*UP+0.5*LEFT)
        
        C_generica = MobjectMatrix([
            [MathTex(r"c_{11} + b_{11}"), MathTex(r"c_{12} + b_{12}"), MathTex(r"c_{13} + b_{13} + a_{13} + b_{11} + b_{11}")],
            [MathTex(r"c_{21} + b_{11}"), MathTex(r"c_{22} + b_{11}"), MathTex(r"c_{23} + b_{11}")],
            [MathTex(r"c_{31} + b_{11}"), MathTex(r"c_{32} + b_{11}"), MathTex(r"c_{33} + b_{11}")]
        ], v_buff=0.75).shift(1*UP+5*RIGHT)

        for entrada in C_generica.get_entries():
            entrada.set_opacity(0)
        
        mais2 = MathTex(r'+').shift(1*UP + 2.75*LEFT)
        
        self.play(FadeIn(A_generica), FadeIn(B_generica),FadeIn(mais2),FadeIn(a_11),FadeIn(C_generica), run_time = 2)
        self.play(a_11.animate.move_to(C_generica.get_entries()[0]).shift(0.5*LEFT))

        self.wait(5)

        self.play(FadeOut(A_generica), FadeOut(B_generica), FadeOut(mais2), FadeOut(a_11), FadeOut(C_generica))

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

        C = MobjectMatrix([
            [termo_matriz('C', 1, 1),termo_matriz('C', 1, 2),termo_matriz('C', 1, 3)],
            [termo_matriz('C', 2, 1),termo_matriz('C', 2, 2),termo_matriz('C', 2, 3)],
            [termo_matriz('C', 3, 1),termo_matriz('C', 3, 2),termo_matriz('C', 3, 3)]
        ], h_buff=1.5, v_buff=1).shift(1*UP + 4.5*RIGHT)

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

                A_valor = valores_A[n][i]

                B_valor = valores_B[n][i]

                resultado_AB = A_valor + B_valor

                adicao_matriz = MathTex(f'{A_valor} + {B_valor} = {resultado_AB}').shift(1*DOWN)

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