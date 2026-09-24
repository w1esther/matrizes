from manim import *

class MultiplicacaoDeMatrizes(MovingCameraScene):
    def construct(self):

        self.play(self.camera.frame.animate.scale(1.5))
        
        titulo = Tex(r'Multiplicação de Matrizes', font_size=46).shift(3.5*UP)

        self.play(Write(titulo))

        self.wait()

        legenda_1 = Tex(
            r"Para multiplicar duas matrizes AxB",
            r" é necessário que o número de colunas da primeira matriz seja igual ao número de linhas da segunda matriz.").shift(1.5*UP).scale(0.85)

        self.play(Write(legenda_1))

        self.wait(2)

        legenda_2 = MathTex(r' A_{m\times n}\times B_{n\times p}').next_to(legenda_1, DOWN, buff=1)

        self.play(FadeIn(legenda_2))

        self.wait(2)

        linha_1 = Line(
            start=0.1*LEFT,
            end=0.1*RIGHT, color=YELLOW
        ).next_to(legenda_2, DOWN, buff=0.1).shift(0.425*LEFT)

        linha_2 = Line(
            start=0.1*LEFT,
            end=0.1*RIGHT, color=YELLOW
        ).next_to(legenda_2, DOWN, buff=0.1).shift(0.85*RIGHT)

        self.play(Create(linha_1), Create(linha_2))

        self.wait(2)

        lengenda_3 = Tex(r'Dessa forma, teremos que o número de linhas da matriz resultante será igual ao número de linha da primeira matriz e o número de colunas da matriz resultante será igual ao número de colunas da segunda matriz.').next_to(legenda_2, DOWN, buff=1).scale(0.85)

        self.play(Write(lengenda_3))

        self.wait(2)

        legenda_4 = MathTex(r'A_{m\times n}\times B_{n\times p} = C_{m\times p}').next_to(lengenda_3, DOWN, buff=1)

        self.play(Write(legenda_4))

        self.wait(4)

        objetos_1 = [legenda_1, legenda_2,linha_1, linha_2, lengenda_3, legenda_4,]

        for objeto in objetos_1:
            self.play(FadeOut(objeto))

        def termo_matriz(p, m, n):
            termo = MathTex(f"{p}_{{{m}{n}}}")
            return termo
        
        self.play(titulo.animate.shift(1.5*UP))

        A_generica = MobjectMatrix([
            [termo_matriz('a', 1, 1), termo_matriz('a', 1, 2), termo_matriz('a', 1, 3)],
            [termo_matriz('a', 2, 1), termo_matriz('a', 2, 2), termo_matriz('a', 2, 3)],
            [termo_matriz('a', 3, 1), termo_matriz('a', 3, 2), termo_matriz('a', 3, 3)]]).next_to(titulo, DOWN, buff=1).shift(2.5*LEFT)

        a_11 = MathTex("a_{11}").move_to(A_generica.get_entries()[0])
        a_12 = MathTex("a_{12}").move_to(A_generica.get_entries()[1])
        a_13 = MathTex("a_{13}").move_to(A_generica.get_entries()[2])
        a_21 = MathTex("a_{21}").move_to(A_generica.get_entries()[3])
        a_22 = MathTex("a_{22}").move_to(A_generica.get_entries()[4])
        a_23 = MathTex("a_{23}").move_to(A_generica.get_entries()[5])
        a_31 = MathTex("a_{31}").move_to(A_generica.get_entries()[6])
        a_32 = MathTex("a_{32}").move_to(A_generica.get_entries()[7])
        a_33 = MathTex("a_{33}").move_to(A_generica.get_entries()[8])
       

        a_11_1 = MathTex("a_{11}").move_to(A_generica.get_entries()[0])
        a_12_1 = MathTex("a_{12}").move_to(A_generica.get_entries()[1])
        a_13_1 = MathTex("a_{13}").move_to(A_generica.get_entries()[2])
        a_21_1 = MathTex("a_{21}").move_to(A_generica.get_entries()[3])
        a_22_1 = MathTex("a_{22}").move_to(A_generica.get_entries()[4])
        a_23_1 = MathTex("a_{23}").move_to(A_generica.get_entries()[5])
        a_31_1 = MathTex("a_{31}").move_to(A_generica.get_entries()[6])
        a_32_1 = MathTex("a_{32}").move_to(A_generica.get_entries()[7])
        a_33_1 = MathTex("a_{33}").move_to(A_generica.get_entries()[8])

        elementos_a = [a_12, a_13, a_22, a_23, a_11, a_21, a_12_1, a_13_1, a_22_1, a_23_1, a_11_1, a_21_1, a_31, a_31_1, a_32, a_32_1, a_33, a_33_1]
        
        multiplicacao_1 = MathTex(r'\dot').next_to(A_generica, RIGHT, buff=0.4)
        
        B_generica = MobjectMatrix([
            [termo_matriz('b', 1, 1), termo_matriz('b', 1, 2)],
            [termo_matriz('b', 2, 1), termo_matriz('b', 2, 2)],
            [termo_matriz('b', 3, 1), termo_matriz('b', 3, 2)]], v_buff=0.75).next_to(A_generica, RIGHT, buff=1)
        
        b_11 = MathTex("b_{11}").move_to(B_generica.get_entries()[0])
        b_12 = MathTex("b_{12}").move_to(B_generica.get_entries()[1])
        b_21 = MathTex("b_{21}").move_to(B_generica.get_entries()[2])
        b_22 = MathTex("b_{22}").move_to(B_generica.get_entries()[3])
        b_31 = MathTex("b_{31}").move_to(B_generica.get_entries()[4])
        b_32 = MathTex("b_{32}").move_to(B_generica.get_entries()[5])

        b_11_1 = MathTex("b_{11}").move_to(B_generica.get_entries()[0])
        b_12_1 = MathTex("b_{12}").move_to(B_generica.get_entries()[1])
        b_21_1 = MathTex("b_{21}").move_to(B_generica.get_entries()[2])
        b_22_1 = MathTex("b_{22}").move_to(B_generica.get_entries()[3])
        b_31_1 = MathTex("b_{31}").move_to(B_generica.get_entries()[4])
        b_32_1 = MathTex("b_{32}").move_to(B_generica.get_entries()[5])

        elementos_b = [b_12, b_22,b_31, b_32, b_11, b_21, b_12_1, b_22_1, b_31_1, b_32_1, b_11_1, b_21_1]
        
        igual_1 = MathTex(r'=').next_to(B_generica, RIGHT, buff=0.8)

        legenda_5 = Tex(r'multiplica-se cada elemento de uma linha da primeira matriz pelos elementos correspondentes de uma coluna da segunda matriz e soma-se os resultados.').scale(0.85)

        self.play(Write(legenda_5))
        
        C_generica = MobjectMatrix([
            [MathTex(r"a_{11} \cdot b_{11} + a_{12} \cdot b_{21}) + a_{13} \cdot b_{31} + a_{12} \cdot b_{21}) + a_{13} \cdot b_{31}"), MathTex(r"a_{11} \cdot b_{11} + a_{12} \cdot b_{21}) + a_{13} \cdot b_{31} + a_{12} \cdot b_{21}) + a_{13} \cdot b_{31}")],
            [MathTex(r"a_{11} \cdot b_{11} + a_{12} \cdot b_{21}) + a_{13} \cdot b_{31} + a_{12} \cdot b_{21}) + a_{13} \cdot b_{31}"), MathTex(r"a_{11} \cdot b_{11} + a_{12} \cdot b_{21}) + a_{13} \cdot b_{31} + a_{12} \cdot b_{21}) + a_{13} \cdot b_{31}")],
            [MathTex(r"a_{11} \cdot b_{11} + a_{12} \cdot b_{21}) + a_{13} \cdot b_{31} + a_{12} \cdot b_{21}) + a_{13} \cdot b_{31}"), MathTex(r"a_{11} \cdot b_{11} + a_{12} \cdot b_{21}) + a_{13} \cdot b_{31} + a_{12} \cdot b_{21}) + a_{13} \cdot b_{31}")]
        ], v_buff=0.75).next_to(legenda_5, DOWN, buff=0.7)

        mais3 = MathTex(r'\cdot', color=PINK).shift(1.6*DOWN + 4.6*LEFT)
        mais4 = MathTex(r'\cdot', color=PINK).shift(1.6*DOWN + 2.7*LEFT)
        mais5 = MathTex(r'+', color=YELLOW).shift(1.8*UP + 6.6*RIGHT).scale(0.7)

        mais6 = MathTex(r'+', color=BLUE).shift(1*UP + 2.4*RIGHT).scale(0.7)
        mais7 = MathTex(r'+', color=GREEN).shift(1*UP + 4.5*RIGHT).scale(0.7)
        mais8 = MathTex(r'+', color=PURPLE).shift(1*UP + 6.6*RIGHT).scale(0.7)

        mais3_1 = MathTex(r'+', color=PINK).shift(1.6*DOWN + 3.6*LEFT).scale(0.7)
        mais4_1 = MathTex(r'+', color=PINK).shift(1.6*DOWN + 1.4*LEFT).scale(0.7)
        mais5_1 = MathTex(r'+', color=YELLOW).shift(1.8*UP + 6.6*RIGHT).scale(0.7)

        mais6_1 = MathTex(r'+', color=BLUE).shift(1*UP + 2.4*RIGHT).scale(0.7)
        mais7_1 = MathTex(r'+', color=GREEN).shift(1*UP + 4.5*RIGHT).scale(0.7)
        mais8_1 = MathTex(r'+', color=PURPLE).shift(1*UP + 6.6*RIGHT).scale(0.7)

        for entrada in C_generica.get_entries():
            entrada.set_opacity(0)

        self.play(FadeIn(A_generica), FadeIn(multiplicacao_1), FadeIn(B_generica), FadeIn(C_generica), FadeIn(igual_1))

        for elemento in elementos_a:
            self.add(elemento)

        for elemento in elementos_b:
            self.add(elemento)

        self.wait(2)

        elemento_c11 = VGroup()
        elemento_c11.add(a_11, a_12, a_13)

        elemento_c12 = VGroup()
        elemento_c12.add(b_11, b_21, b_31)

        destaque_A = SurroundingRectangle(elemento_c11, buff=0.08, color=PINK)
        destaque_B = SurroundingRectangle(elemento_c12, buff=0.08, color=PINK)

        self.play(Write(destaque_A), Write(destaque_B))

        self.play(a_11.animate.move_to(C_generica.get_entries()[0]).shift(4.4*LEFT).set_color(PINK), FadeIn(mais3), b_11.animate.move_to(C_generica.get_entries()[0]).shift(3.5*LEFT).set_color(PINK), FadeIn(mais3_1))

        self.play(a_12.animate.move_to(C_generica.get_entries()[0]).shift(2.4*LEFT).set_color(PINK), FadeIn(mais4), b_21.animate.move_to(C_generica.get_entries()[0]).shift(1.5*LEFT).set_color(PINK), FadeIn(mais4_1))

        self.wait(2)