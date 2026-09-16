from manim import *
import numpy as np

class MatrizAdicao(MovingCameraScene):
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
            [termo_matriz('a', 3, 1), termo_matriz('a', 3, 2), termo_matriz('a', 3, 3)]]).shift(1*UP+6.6*LEFT)

        a_11 = MathTex("a_{11}").move_to(A_generica.get_entries()[0])
        a_12 = MathTex("a_{12}").move_to(A_generica.get_entries()[1])
        a_13 = MathTex("a_{13}").move_to(A_generica.get_entries()[2])
        a_21 = MathTex("a_{21}").move_to(A_generica.get_entries()[3])
        a_22 = MathTex("a_{22}").move_to(A_generica.get_entries()[4])
        a_23 = MathTex("a_{23}").move_to(A_generica.get_entries()[5])
        a_31 = MathTex("a_{31}").move_to(A_generica.get_entries()[6])
        a_32 = MathTex("a_{32}").move_to(A_generica.get_entries()[7])
        a_33 = MathTex("a_{33}").move_to(A_generica.get_entries()[8])

        elementos_a = [a_12, a_13, a_22, a_23, a_31, a_32, a_33]
        
        B_generica = MobjectMatrix([
            [termo_matriz('b', 1, 1), termo_matriz('b', 1, 2), termo_matriz('b', 1, 3)],
            [termo_matriz('b', 2, 1), termo_matriz('b', 2, 2), termo_matriz('b', 2, 3)],
            [termo_matriz('b', 3, 1), termo_matriz('b', 3, 2), termo_matriz('b', 3, 3)]], v_buff=0.75).shift(1*UP+1.9*LEFT)
        
        b_11 = MathTex("b_{11}").move_to(B_generica.get_entries()[0])
        b_12 = MathTex("b_{12}").move_to(B_generica.get_entries()[1])
        b_13 = MathTex("b_{13}").move_to(B_generica.get_entries()[2])
        b_21 = MathTex("b_{21}").move_to(B_generica.get_entries()[3])
        b_22 = MathTex("b_{22}").move_to(B_generica.get_entries()[4])
        b_23 = MathTex("b_{23}").move_to(B_generica.get_entries()[5])
        b_31 = MathTex("b_{31}").move_to(B_generica.get_entries()[6])
        b_32 = MathTex("b_{32}").move_to(B_generica.get_entries()[7])
        b_33 = MathTex("b_{33}").move_to(B_generica.get_entries()[8])

        elementos_b = [b_12, b_13, b_22, b_23, b_31, b_32, b_33]
        
        C_generica = MobjectMatrix([
            [MathTex(r"c_{11} + b_{11}"), MathTex(r"c_{12} + b_{12}"), MathTex(r"c_{13} + b_{13} + a_{13} + b_{11} + b_{11}")],
            [MathTex(r"c_{21} + b_{11}"), MathTex(r"c_{22} + b_{11}"), MathTex(r"c_{23} + b_{11} + a_{13} + b_{11} + b_{11}")],
            [MathTex(r"c_{31} + b_{11}"), MathTex(r"c_{32} + b_{11}"), MathTex(r"c_{33} + b_{11} + a_{13} + b_{11} + b_{11}")]
        ], v_buff=0.75).shift(1*UP+4.5*RIGHT)

        c_11 = MathTex("c_{11}", color=PINK).move_to(C_generica.get_entries()[0]).shift(1*LEFT)
        c_12 = MathTex("c_{12}", color=ORANGE).move_to(C_generica.get_entries()[1]).shift(0.5*LEFT)
        c_13 = MathTex("c_{13}", color=YELLOW).move_to(C_generica.get_entries()[2]).shift(1.8*RIGHT)
        c_21 = MathTex("c_{21}", color=BLUE).move_to(C_generica.get_entries()[3]).shift(1*LEFT)
        c_22 = MathTex("c_{22}", color=GREEN).move_to(C_generica.get_entries()[4]).shift(0.5*LEFT)
        c_23 = MathTex("c_{23}", color=PURPLE).move_to(C_generica.get_entries()[5]).shift(1.8*RIGHT)
        c_31 = MathTex("c_{31}", color=RED).move_to(C_generica.get_entries()[6]).shift(1*LEFT)
        c_32 = MathTex("c_{32}", color=GREY).move_to(C_generica.get_entries()[7]).shift(0.5*LEFT)
        c_33 = MathTex("c_{33}").move_to(C_generica.get_entries()[8]).shift(1.8*RIGHT)

        for entrada in C_generica.get_entries():
            entrada.set_opacity(0)
        
        mais2 = MathTex(r'+').shift(1*UP + 4.25*LEFT)
        igual2 = MathTex(r'=').shift(1*UP+0.6*RIGHT)

        mais3 = MathTex(r'+', color=PINK).shift(1.8*UP + 2.4*RIGHT).scale(0.7)
        mais4 = MathTex(r'+', color=ORANGE).shift(1.8*UP + 4.5*RIGHT).scale(0.7)
        mais5 = MathTex(r'+', color=YELLOW).shift(1.8*UP + 6.6*RIGHT).scale(0.7)

        mais6 = MathTex(r'+', color=BLUE).shift(1*UP + 2.4*RIGHT).scale(0.7)
        mais7 = MathTex(r'+', color=GREEN).shift(1*UP + 4.5*RIGHT).scale(0.7)
        mais8 = MathTex(r'+', color=PURPLE).shift(1*UP + 6.6*RIGHT).scale(0.7)

        mais9 = MathTex(r'+', color=RED).shift(0.2*UP + 2.4*RIGHT).scale(0.7)
        mais10 = MathTex(r'+', color=GREY).shift(0.2*UP + 4.5*RIGHT).scale(0.7)
        mais11 = MathTex(r'+').shift(0.2*UP + 6.6*RIGHT).scale(0.7)
        
        self.play(FadeIn(A_generica), FadeIn(B_generica),FadeIn(mais2),FadeIn(a_11),FadeIn(C_generica),FadeIn(igual2),FadeIn(b_11), run_time = 2)

        legenda_1 = Text('Somamos os elementos que ocupam a mesma posição.', font_size=26).shift(1.5*DOWN)

        self.play(Write(legenda_1), run_time = 2)

        for elemento in elementos_a:
            self.add(elemento)

        for elemento in elementos_b:
            self.add(elemento)

        self.play(a_11.animate.move_to(C_generica.get_entries()[0]).shift(1.9*LEFT).set_color(PINK), FadeIn(mais3), b_11.animate.move_to(C_generica.get_entries()[0]).shift(0.9*LEFT).set_color(PINK))

        self.wait(1)

        self.play(b_12.animate.move_to(C_generica.get_entries()[1]).shift(0.1*LEFT).set_color(ORANGE), a_12.animate.move_to(C_generica.get_entries()[1]).shift(1.1*LEFT).set_color(ORANGE), FadeIn(mais4))

        self.wait(1)

        legenda_2 = Tex(
            r"A adição de matrizes é uma operação matematicamente definida",
            r" se, e somente se, as matrizes envolvidas forem de mesma ordem $m \times n$."
            r" Isso significa que elas precisam ter o mesmo número de linhas e o mesmo número de colunas.").scale(0.7).shift(3.0*DOWN)
        
        self.play(FadeIn(legenda_2))

        self.play(b_13.animate.move_to(C_generica.get_entries()[2]).shift(2.6*RIGHT).set_color(YELLOW), a_13.animate.move_to(C_generica.get_entries()[2]).shift(1.6*RIGHT).set_color(YELLOW), FadeIn(mais5))

        self.wait(1)

        self.play(a_21.animate.move_to(C_generica.get_entries()[3]).shift(1.9*LEFT).set_color(BLUE), b_21.animate.move_to(C_generica.get_entries()[3]).shift(0.9*LEFT).set_color(BLUE), FadeIn(mais6))

        self.wait(1)

        self.play(b_22.animate.move_to(C_generica.get_entries()[4]).shift(0.1*LEFT).set_color(GREEN), a_22.animate.move_to(C_generica.get_entries()[4]).shift(1.1*LEFT).set_color(GREEN), FadeIn(mais7))

        self.wait(1)

        self.play(b_23.animate.move_to(C_generica.get_entries()[5]).shift(2.6*RIGHT).set_color(PURPLE), a_23.animate.move_to(C_generica.get_entries()[5]).shift(1.6*RIGHT).set_color(PURPLE), FadeIn(mais8))

        self.wait(1)

        self.play(a_31.animate.move_to(C_generica.get_entries()[6]).shift(1.9*LEFT).set_color(RED), b_31.animate.move_to(C_generica.get_entries()[6]).shift(0.9*LEFT).set_color(RED), FadeIn(mais9))

        self.wait(1)

        self.play(b_32.animate.move_to(C_generica.get_entries()[7]).shift(0.1*LEFT).set_color(GREY), a_32.animate.move_to(C_generica.get_entries()[7]).shift(1.1*LEFT).set_color(GREY), FadeIn(mais10))

        self.wait(1)

        self.play(b_33.animate.move_to(C_generica.get_entries()[8]).shift(2.6*RIGHT), a_33.animate.move_to(C_generica.get_entries()[8]).shift(1.6*RIGHT), FadeIn(mais11))

        grupo_11 = VGroup()
        grupo_11.add(a_11, b_11, mais3)

        self.play(Transform(grupo_11, c_11))

        self.wait(1)

        grupo_12 = VGroup()
        grupo_12.add(a_12, b_12, mais4)

        self.play(Transform(grupo_12, c_12))

        self.wait(1)

        grupo_13 = VGroup()
        grupo_13.add(a_13, b_13, mais5)

        self.play(Transform(grupo_13, c_13))

        self.wait(1)

        grupo_21 = VGroup()
        grupo_21.add(a_21, b_21, mais6)

        self.play(Transform(grupo_21, c_21))

        self.wait(1)

        grupo_22 = VGroup()
        grupo_22.add(a_22, b_22, mais7)

        self.play(Transform(grupo_22, c_22))

        self.wait(1)

        grupo_23 = VGroup()
        grupo_23.add(a_23, b_23, mais8)

        self.play(Transform(grupo_23, c_23))

        self.wait(1)

        grupo_31 = VGroup()
        grupo_31.add(a_31, b_31, mais9)

        self.play(Transform(grupo_31, c_31))

        self.wait(1)

        grupo_32 = VGroup()
        grupo_32.add(a_32, b_32, mais10)

        self.play(Transform(grupo_32, c_32))

        self.wait(1)

        grupo_33 = VGroup()
        grupo_33.add(a_33, b_33, mais11)

        self.play(Transform(grupo_33, c_33))

        self.wait(5)

        grupos = [grupo_11, grupo_12, grupo_21, grupo_13, grupo_22, grupo_23, grupo_31, grupo_32, grupo_33]

        for grupo in grupos:
            self.remove(grupo)

        self.play(FadeOut(A_generica), FadeOut(B_generica), FadeOut(mais2), FadeOut(a_11), FadeOut(C_generica), FadeOut(legenda_2), FadeOut(igual2), FadeOut(legenda_1))

        valores_C = MobjectMatrix([
            [MathTex(r"c_{11} + b_{11}"), MathTex(r"c_{12} + b_{12}"), MathTex(r"c_{13} + b_{13} + a_{13} + b_{11} + b_{11}")],
            [MathTex(r"c_{21} + b_{11}"), MathTex(r"c_{22} + b_{11}"), MathTex(r"c_{23} + b_{11} + a_{13} + b_{11} + b_{11}")],
            [MathTex(r"c_{31} + b_{11}"), MathTex(r"c_{32} + b_{11}"), MathTex(r"c_{33} + b_{11} + a_{13} + b_{11} + b_{11}")]
        ],v_buff=0.75 ).shift(1*UP+4.5*RIGHT)

        for entrada in valores_C.get_entries():
            entrada.set_opacity(0)

        A = Matrix([
            [1, 2, 3],
            [4, 5, 6],
            [7, 3, 4]
        ]).shift(1*UP+6*LEFT)

        B = Matrix([
            [5, 3, 7],
            [2, 5, 1],
            [3, 9, 6]
        ]).shift(1*UP + 1.5*LEFT)

        mais1 = MathTex(r'+').shift(1*UP + 3.7*LEFT)

        self.play(FadeIn(A),FadeIn(B),FadeIn(mais1), FadeIn(valores_C), run_time=2)
        self.wait(2)

        igual1 = MathTex(r'=').shift(1*UP + 0.8*RIGHT)

        self.play(FadeIn(igual1))

        C = MobjectMatrix([
            [termo_matriz('C', 1, 1),termo_matriz('C', 1, 2),termo_matriz('C', 1, 3)],
            [termo_matriz('C', 2, 1),termo_matriz('C', 2, 2),termo_matriz('C', 2, 3)],
            [termo_matriz('C', 3, 1),termo_matriz('C', 3, 2),termo_matriz('C', 3, 3)]
        ], h_buff=1.5, v_buff=1).shift(1*UP + 4.5*RIGHT)


        self.wait(2)

        # self.play(FadeIn(C))

        valores_A = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 3, 4]
        ]

        a_11_1 = MathTex(r"1").move_to(A.get_entries()[0])
        a_12_2 = MathTex(r"2").move_to(A.get_entries()[1])
        a_13_3 = MathTex(r"3").move_to(A.get_entries()[2])
        a_21_4 = MathTex(r"4").move_to(A.get_entries()[3])
        a_22_5 = MathTex(r"5").move_to(A.get_entries()[4])
        a_23_6 = MathTex(r"6").move_to(A.get_entries()[5])
        a_31_7 = MathTex(r"7").move_to(A.get_entries()[6])
        a_32_3 = MathTex(r"3").move_to(A.get_entries()[7])
        a_33_4 = MathTex(r"4").move_to(A.get_entries()[8])

        termos_a = [a_11_1, a_12_2, a_13_3, a_21_4, a_22_5, a_23_6, a_31_7, a_32_3, a_33_4]

        for elemento in termos_a:
            self.add(elemento) 

        valores_B = [
            [5, 3, 7],
            [2, 5, 1],
            [3, 9, 6]
        ]

        b_11_5 = MathTex(r"5").move_to(B.get_entries()[0])
        b_12_3 = MathTex(r"3").move_to(B.get_entries()[1])
        b_13_7 = MathTex(r"7").move_to(B.get_entries()[2])
        b_21_2 = MathTex(r"2").move_to(B.get_entries()[3])
        b_22_5 = MathTex(r"5").move_to(B.get_entries()[4])
        b_23_1 = MathTex(r"1").move_to(B.get_entries()[5])
        b_31_3 = MathTex(r"3").move_to(B.get_entries()[6])
        b_32_9 = MathTex(r"9").move_to(B.get_entries()[7])
        b_33_6 = MathTex(r"6").move_to(B.get_entries()[8])

        termos_b = [b_11_5, b_12_3, b_13_7, b_21_2, b_22_5, b_23_1, b_31_3, b_32_9, b_33_6]

        for elemento in termos_b:
            self.add(elemento) 

        mais3_1 = MathTex(r'+', color=PINK).shift(1.8*UP + 2.4*RIGHT).scale(0.7)
        mais4_1 = MathTex(r'+', color=ORANGE).shift(1.8*UP + 4.5*RIGHT).scale(0.7)
        mais5_1 = MathTex(r'+', color=YELLOW).shift(1.8*UP + 6.6*RIGHT).scale(0.7)

        mais6_1 = MathTex(r'+', color=BLUE).shift(1*UP + 2.4*RIGHT).scale(0.7)
        mais7_1 = MathTex(r'+', color=GREEN).shift(1*UP + 4.5*RIGHT).scale(0.7)
        mais8_1 = MathTex(r'+', color=PURPLE).shift(1*UP + 6.6*RIGHT).scale(0.7)

        mais9_1 = MathTex(r'+', color=RED).shift(0.2*UP + 2.4*RIGHT).scale(0.7)
        mais10_1 = MathTex(r'+',color=GREY).shift(0.2*UP + 4.5*RIGHT).scale(0.7)
        mais11_1 = MathTex(r'+').shift(0.2*UP + 6.6*RIGHT).scale(0.7)

        self.play(a_11_1.animate.move_to(valores_C.get_entries()[0]).shift(1.9*LEFT).set_color(PINK), FadeIn(mais3_1), b_11_5.animate.move_to(valores_C.get_entries()[0]).shift(0.9*LEFT).set_color(PINK))

        self.wait(1)

        self.play(b_12_3.animate.move_to(valores_C.get_entries()[1]).shift(0.1*LEFT).set_color(ORANGE), a_12_2.animate.move_to(valores_C.get_entries()[1]).shift(1.1*LEFT).set_color(ORANGE), FadeIn(mais4_1))

        self.wait(1)

        self.play(b_13_7.animate.move_to(valores_C.get_entries()[2]).shift(2.6*RIGHT).set_color(YELLOW), a_13_3.animate.move_to(valores_C.get_entries()[2]).shift(1.6*RIGHT).set_color(YELLOW), FadeIn(mais5_1))

        self.wait(1)

        self.play(a_21_4.animate.move_to(valores_C.get_entries()[3]).shift(1.9*LEFT).set_color(BLUE), b_21_2.animate.move_to(valores_C.get_entries()[3]).shift(0.9*LEFT).set_color(BLUE), FadeIn(mais6_1))

        self.wait(1)

        self.play(b_22_5.animate.move_to(valores_C.get_entries()[4]).shift(0.1*LEFT).set_color(GREEN), a_22_5.animate.move_to(valores_C.get_entries()[4]).shift(1.1*LEFT).set_color(GREEN), FadeIn(mais7_1))

        self.wait(1)

        self.play(b_23_1.animate.move_to(valores_C.get_entries()[5]).shift(2.6*RIGHT).set_color(PURPLE), a_23_6.animate.move_to(valores_C.get_entries()[5]).shift(1.6*RIGHT).set_color(PURPLE), FadeIn(mais8_1))

        self.wait(1)

        self.play(a_31_7.animate.move_to(valores_C.get_entries()[6]).shift(1.9*LEFT).set_color(RED), b_31_3.animate.move_to(C_generica.get_entries()[6]).shift(0.9*LEFT).set_color(RED), FadeIn(mais9_1))

        self.wait(1)

        self.play(b_32_9.animate.move_to(valores_C.get_entries()[7]).shift(0.1*LEFT).set_color(GREY), a_32_3.animate.move_to(valores_C.get_entries()[7]).shift(1.1*LEFT).set_color(GREY), FadeIn(mais10_1))

        self.wait(1)

        self.play(b_33_6.animate.move_to(valores_C.get_entries()[8]).shift(2.6*RIGHT), a_33_4.animate.move_to(valores_C.get_entries()[8]).shift(1.6*RIGHT), FadeIn(mais11_1))

        c_11_1 = MathTex("6", color=PINK).move_to(C_generica.get_entries()[0]).shift(1*LEFT)
        c_12_1 = MathTex("5", color=ORANGE).move_to(C_generica.get_entries()[1]).shift(0.5*LEFT)
        c_13_1 = MathTex("10", color=YELLOW).move_to(C_generica.get_entries()[2]).shift(1.8*RIGHT)
        c_21_1 = MathTex("6", color=BLUE).move_to(C_generica.get_entries()[3]).shift(1*LEFT)
        c_22_1 = MathTex("10", color=GREEN).move_to(C_generica.get_entries()[4]).shift(0.5*LEFT)
        c_23_1 = MathTex("7", color=PURPLE).move_to(C_generica.get_entries()[5]).shift(1.8*RIGHT)
        c_31_1 = MathTex("10", color=RED).move_to(C_generica.get_entries()[6]).shift(1*LEFT)
        c_32_1 = MathTex("12", color=GREY).move_to(C_generica.get_entries()[7]).shift(0.5*LEFT)
        c_33_1 = MathTex("10").move_to(C_generica.get_entries()[8]).shift(1.8*RIGHT)

        grupo_11_1 = VGroup()
        grupo_11_1.add(a_11_1, b_11_5, mais3_1)

        self.play(Transform(grupo_11_1, c_11_1))

        self.wait(1)

        grupo_12_1 = VGroup()
        grupo_12_1.add(a_12_2, b_12_3, mais4_1)

        self.play(Transform(grupo_12_1, c_12_1))

        self.wait(1)

        grupo_13_1 = VGroup()
        grupo_13_1.add(a_13_3, b_13_7, mais5_1)

        self.play(Transform(grupo_13_1, c_13_1))

        self.wait(1)

        grupo_21_1 = VGroup()
        grupo_21_1.add(a_21_4, b_21_2, mais6_1)

        self.play(Transform(grupo_21_1, c_21_1))

        self.wait(1)

        grupo_22_1 = VGroup()
        grupo_22_1.add(a_22_5, b_22_5, mais7_1)

        self.play(Transform(grupo_22_1, c_22_1))

        self.wait(1)

        grupo_23_1 = VGroup()
        grupo_23_1.add(a_23_6, b_23_1, mais8_1)

        self.play(Transform(grupo_23_1, c_23_1))

        self.wait(1)

        grupo_31_1 = VGroup()
        grupo_31_1.add(a_31_7, b_31_3, mais9_1)

        self.play(Transform(grupo_31_1, c_31_1))

        self.wait(1)

        grupo_32_1 = VGroup()
        grupo_32_1.add(a_32_3, b_32_9, mais10_1)

        self.play(Transform(grupo_32_1, c_32_1))

        self.wait(1)

        grupo_33_1 = VGroup()
        grupo_33_1.add(a_33_4, b_33_6, mais11_1)

        self.play(Transform(grupo_33_1, c_33_1))

        self.wait(2)
        # for n in range(3):
        #     for i in range(3):

        #         indice = (n*3+i)

        #         elemento_A = A.get_entries()[indice]
        #         elemento_B = B.get_entries()[indice]    

        #         destaque_A = SurroundingRectangle(elemento_A, buff=0.08)
        #         destaque_B = SurroundingRectangle(elemento_B, buff=0.08)

        #         self.play(Create(destaque_A), Create(destaque_B), run_time = 2)

        #         A_valor = valores_A[n][i]

        #         B_valor = valores_B[n][i]

        #         resultado_AB = A_valor + B_valor

        #         adicao_matriz = MathTex(f'{A_valor} + {B_valor} = {resultado_AB}').shift(1*DOWN)

        #         self.play(Transform(legenda_1, adicao_matriz))

        #         elemento_antigo = C.get_entries()[indice]

        #         resultado = valores_C[n][i]

        #         elemento_novo = MathTex(str(resultado)).move_to(elemento_antigo)

        #         self.play(ReplacementTransform(elemento_antigo, elemento_novo))

        #         self.wait(1)

        #         self.play(FadeOut(destaque_A), FadeOut(destaque_B))

        self.wait(4)