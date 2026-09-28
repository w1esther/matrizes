from manim import *


class MultiplicacaoDeMatrizes(MovingCameraScene):

    def construct(self):

        self.play(self.camera.frame.animate.scale(1.5))

        titulo = Tex(
            r'Multiplicação de Matrizes',
            font_size=46
        ).shift(3.5 * UP)

        self.play(Write(titulo))
        self.wait()

        legenda_1 = Tex(
            r"Para multiplicar duas matrizes A e B,",
            r" é necessário que o número de colunas da primeira matriz "
            r"seja igual ao número de linhas da segunda matriz."
        ).shift(1.5 * UP).scale(0.85)

        self.play(Write(legenda_1))
        self.wait(2)

        legenda_2 = MathTex(
            r"A_{m\times n}\times B_{n\times p}"
        ).next_to(
            legenda_1,
            DOWN,
            buff=1
        )

        self.play(FadeIn(legenda_2))
        self.wait(2)

        linha_1 = Line(
            start=0.1 * LEFT,
            end=0.1 * RIGHT,
            color=YELLOW
        ).next_to(
            legenda_2,
            DOWN,
            buff=0.1
        ).shift(0.425 * LEFT)

        linha_2 = Line(
            start=0.1 * LEFT,
            end=0.1 * RIGHT,
            color=YELLOW
        ).next_to(
            legenda_2,
            DOWN,
            buff=0.1
        ).shift(0.85 * RIGHT)

        self.play(
            Create(linha_1),
            Create(linha_2)
        )

        self.wait(2)

        legenda_3 = Tex(
            r"Dessa forma, o número de linhas da matriz resultante "
            r"será igual ao número de linhas da primeira matriz e "
            r"o número de colunas será igual ao número de colunas "
            r"da segunda matriz.").next_to(legenda_2,DOWN,buff=1).scale(0.85)

        self.play(Write(legenda_3))
        self.wait(2)

        legenda_4 = MathTex(
            r"A_{m\times n}\times B_{n\times p}"
            r"=C_{m\times p}"
        ).next_to(legenda_3,DOWN,buff=1)

        self.play(Write(legenda_4))
        self.wait(4)

        objetos_1 = [legenda_1,legenda_2,linha_1,linha_2,legenda_3,legenda_4]

        for objeto in objetos_1:
            self.play(FadeOut(objeto))

        def termo_matriz(p, m, n):
            return MathTex(f"{p}_{{{m}{n}}}")

        self.play(titulo.animate.shift(1.5 * UP))

        A_generica = MobjectMatrix([
            [termo_matriz('a', 1, 1),termo_matriz('a', 1, 2),termo_matriz('a', 1, 3)],
            [termo_matriz('a', 2, 1),termo_matriz('a', 2, 2),termo_matriz('a', 2, 3)],
            [termo_matriz('a', 3, 1),termo_matriz('a', 3, 2),termo_matriz('a', 3, 3)]
        ]).next_to(titulo,DOWN,buff=1).shift(2.5 * LEFT)

        a_11 = MathTex("a_{11}").move_to(A_generica.get_entries()[0])
        a_12 = MathTex("a_{12}").move_to(A_generica.get_entries()[1])
        a_13 = MathTex("a_{13}").move_to(A_generica.get_entries()[2])
        a_21 = MathTex("a_{21}").move_to(A_generica.get_entries()[3])
        a_22 = MathTex("a_{22}").move_to(A_generica.get_entries()[4])
        a_23 = MathTex("a_{23}").move_to(A_generica.get_entries()[5])
        a_31 = MathTex("a_{31}").move_to(A_generica.get_entries()[6])
        a_32 = MathTex("a_{32}").move_to(A_generica.get_entries()[7])
        a_33 = MathTex("a_{33}").move_to(A_generica.get_entries()[8])

        a_11_1 = a_11.copy()
        a_12_1 = a_12.copy()
        a_13_1 = a_13.copy()
        a_11_2 = a_11.copy()
        a_12_2 = a_12.copy()
        a_13_2 = a_13.copy()

        a_21_1 = a_21.copy()
        a_22_1 = a_22.copy()
        a_23_1 = a_23.copy()
        a_21_2 = a_21.copy()
        a_22_2 = a_22.copy()
        a_23_2 = a_23.copy()

        a_31_1 = a_31.copy()
        a_32_1 = a_32.copy()
        a_33_1 = a_33.copy()
        a_31_2 = a_31.copy()
        a_32_2 = a_32.copy()
        a_33_2 = a_33.copy()

        multiplicacao_1 = MathTex(r'\cdot').next_to(A_generica,RIGHT,buff=0.4)

        B_generica = MobjectMatrix([
            [termo_matriz('b', 1, 1),termo_matriz('b', 1, 2)],
            [termo_matriz('b', 2, 1),termo_matriz('b', 2, 2)],
            [termo_matriz('b', 3, 1),termo_matriz('b', 3, 2)]
        ], v_buff=0.75).next_to(A_generica,RIGHT,buff=1)

        b_11 = MathTex("b_{11}").move_to(B_generica.get_entries()[0])
        b_12 = MathTex("b_{12}").move_to(B_generica.get_entries()[1])
        b_21 = MathTex("b_{21}").move_to(B_generica.get_entries()[2])
        b_22 = MathTex("b_{22}").move_to(B_generica.get_entries()[3])
        b_31 = MathTex("b_{31}").move_to(B_generica.get_entries()[4])
        b_32 = MathTex("b_{32}").move_to(B_generica.get_entries()[5])

        b_11_1 = b_11.copy()
        b_21_1 = b_21.copy()
        b_31_1 = b_31.copy()

        b_12_1 = b_12.copy()
        b_22_1 = b_22.copy()
        b_32_1 = b_32.copy()

        b_11_2 = b_11.copy()
        b_21_2 = b_21.copy()
        b_31_2 = b_31.copy()

        b_12_2 = b_12.copy()
        b_22_2 = b_22.copy()
        b_32_2 = b_32.copy()

        b_11_3 = b_11.copy()
        b_21_3 = b_21.copy()
        b_31_3 = b_31.copy()

        b_12_3 = b_12.copy()
        b_22_3 = b_22.copy()
        b_32_3 = b_32.copy()

        igual_1 = MathTex(r'=').next_to(B_generica,RIGHT,buff=0.8)

        legenda_5 = Tex(
            r"Multiplica-se cada elemento de uma linha da primeira matriz "
            r"pelos elementos correspondentes de uma coluna da segunda "
            r"matriz e soma-se os resultados."
        ).scale(0.85)

        self.play(Write(legenda_5))

        C_generica = MobjectMatrix([
             [MathTex(r"a_{11} \cdot b_{11} + a_{12} \cdot b_{21}) + a_{13} \cdot b_{31} + a_{12} \cdot b_{21})"), MathTex(r"a_{11} \cdot b_{11} + a_{12} \cdot b_{21}) + a_{13} \cdot b_{31} + a_{12} \cdot b_{21})")],
            [MathTex(r"a_{11} \cdot b_{11} + a_{12} \cdot b_{21}) + a_{13} \cdot b_{31} + a_{12} \cdot b_{21})"), MathTex(r"a_{11} \cdot b_{11} + a_{12} \cdot b_{21}) + a_{13} \cdot b_{31} + a_{12} \cdot b_{21})")],
            [MathTex(r"a_{11} \cdot b_{11} + a_{12} \cdot b_{21}) + a_{13} \cdot b_{31} + a_{12} \cdot b_{21})"), MathTex(r"a_{11} \cdot b_{11} + a_{12} \cdot b_{21}) + a_{13} \cdot b_{31} + a_{12} \cdot b_{21})")]
        ], v_buff=0.75, h_buff=7.0).next_to(legenda_5,DOWN,buff=0.7)

        for entrada in C_generica.get_entries():
            entrada.set_opacity(0)

        self.play(FadeIn(A_generica),FadeIn(multiplicacao_1),FadeIn(B_generica),FadeIn(C_generica),FadeIn(igual_1))

        for elemento in [a_11, a_12, a_13,a_21, a_22, a_23,a_31, a_32, a_33]:
            self.add(elemento)

        for elemento in [b_11, b_12,b_21, b_22,b_31, b_32]:
            self.add(elemento)

        self.wait(2)

        def animar_resultado(centro, termos, cor):

            a1, b1, a2, b2, a3, b3 = termos

            ponto_1 = MathTex(r'\cdot', color=cor)
            ponto_2 = MathTex(r'\cdot', color=cor)
            ponto_3 = MathTex(r'\cdot', color=cor)

            mais_1 = MathTex(r'+', color=cor)
            mais_2 = MathTex(r'+', color=cor)

            produto_1 = VGroup(a1.copy(),ponto_1.copy(),b1.copy()
            ).arrange(RIGHT,buff=0.18)

            produto_2 = VGroup(a2.copy(),ponto_2.copy(),b2.copy()
            ).arrange(RIGHT,buff=0.10)

            produto_3 = VGroup(a3.copy(),ponto_3.copy(),b3.copy()
            ).arrange(RIGHT,buff=0.10)

            mais_1_layout = mais_1.copy()
            mais_2_layout = mais_2.copy()

            layout = VGroup(produto_1,mais_1_layout,produto_2,mais_2_layout,produto_3
            ).arrange(RIGHT,buff=0.28)

            layout.move_to(centro)

            posicoes = [
                produto_1[0].get_center().copy(),
                produto_1[1].get_center().copy(),
                produto_1[2].get_center().copy(),
                mais_1_layout.get_center().copy(),
                produto_2[0].get_center().copy(),
                produto_2[1].get_center().copy(),
                produto_2[2].get_center().copy(),
                mais_2_layout.get_center().copy(),
                produto_3[0].get_center().copy(),
                produto_3[1].get_center().copy(),
                produto_3[2].get_center().copy()
            ]

            self.add(a1, b1,a2, b2,a3, b3,ponto_1, ponto_2, ponto_3,mais_1, mais_2)

            ponto_1.move_to(centro).set_opacity(0)
            ponto_2.move_to(centro).set_opacity(0)
            ponto_3.move_to(centro).set_opacity(0)
            mais_1.move_to(centro).set_opacity(0)
            mais_2.move_to(centro).set_opacity(0)

            self.play(
                a1.animate.move_to(posicoes[0]).set_color(cor),
                b1.animate.move_to(posicoes[2]).set_color(cor),run_time=0.8)

            self.play(ponto_1.animate.move_to(posicoes[1]).set_opacity(1),run_time=0.25)

            self.play(mais_1.animate.move_to(posicoes[3]).set_opacity(1),
            a2.animate.move_to(posicoes[4]).set_color(cor),
            b2.animate.move_to(posicoes[6]).set_color(cor),run_time=0.8)

            self.play(ponto_2.animate.move_to(posicoes[5]).set_opacity(1),run_time=0.25)

            self.play(mais_2.animate.move_to(posicoes[7]).set_opacity(1),
            a3.animate.move_to(posicoes[8]).set_color(cor),
            b3.animate.move_to(posicoes[10]).set_color(cor),run_time=0.8)

            self.play(ponto_3.animate.move_to(posicoes[9]).set_opacity(1),run_time=0.25)

            self.wait(1)

        # C11 - PINK

        elemento_c11_A = VGroup(a_11,a_12,a_13)

        elemento_c11_B = VGroup(b_11,b_21,b_31)

        destaque_A = SurroundingRectangle(elemento_c11_A,buff=0.08,color=PINK)

        destaque_B = SurroundingRectangle(elemento_c11_B,buff=0.08,color=PINK)

        self.play(Create(destaque_A),Create(destaque_B))

        animar_resultado(
            C_generica.get_entries()[0].get_center(),
            (
                a_11_1, b_11_1,
                a_12_1, b_21_1,
                a_13_1, b_31_1
            ),
            PINK
        )

        self.play(FadeOut(destaque_A), FadeOut(destaque_B))

        # C12 - BLUE

        elemento_c12_A = VGroup(a_11,a_12,a_13)

        elemento_c12_B = VGroup(b_12,b_22,b_32)

        destaque_A = SurroundingRectangle(elemento_c12_A,buff=0.08,color=BLUE)

        destaque_B = SurroundingRectangle(elemento_c12_B,buff=0.08,color=BLUE)
##########################
        self.play(Create(destaque_A),Create(destaque_B))

        animar_resultado(
            C_generica.get_entries()[1].get_center(),
            (
                a_11_2, b_12_1,
                a_12_2, b_22_1,
                a_13_2, b_32_1
            ),
            BLUE
        )

        self.play(FadeOut(destaque_A), FadeOut(destaque_B))

        # C21 - GREEN

        elemento_c21_A = VGroup(a_21,a_22,a_23)

        elemento_c21_B = VGroup(b_11,b_21,b_31)

        destaque_A = SurroundingRectangle(elemento_c21_A,buff=0.08,color=GREEN)

        destaque_B = SurroundingRectangle(elemento_c21_B,buff=0.08,color=GREEN)

        self.play(Create(destaque_A),Create(destaque_B))

        animar_resultado(
            C_generica.get_entries()[2].get_center(),
            (
                a_21_1, b_11_2,
                a_22_1, b_21_2,
                a_23_1, b_31_2
            ),
            GREEN
        )

        self.play(FadeOut(destaque_A), FadeOut(destaque_B))

        # C22 - PURPLE

        elemento_c22_A = VGroup(a_21,a_22,a_23)

        elemento_c22_B = VGroup(b_12,b_22,b_32)

        destaque_A = SurroundingRectangle(elemento_c22_A,buff=0.08,color=PURPLE)

        destaque_B = SurroundingRectangle(elemento_c22_B,buff=0.08,color=PURPLE)

        self.play(Create(destaque_A),Create(destaque_B))

        animar_resultado(
            C_generica.get_entries()[3].get_center(),
            (
                a_21_2, b_12_2,
                a_22_2, b_22_2,
                a_23_2, b_32_2
            ),
            PURPLE
        )

        self.play(FadeOut(destaque_A), FadeOut(destaque_B))

        # C31 - ORANGE

        elemento_c31_A = VGroup(a_31,a_32,a_33)

        elemento_c31_B = VGroup(b_11,b_21,b_31)

        destaque_A = SurroundingRectangle(elemento_c31_A,buff=0.08,color=ORANGE)

        destaque_B = SurroundingRectangle(elemento_c31_B,buff=0.08,color=ORANGE)

        self.play(Create(destaque_A),Create(destaque_B))

        animar_resultado(
            C_generica.get_entries()[4].get_center(),
            (
                a_31_1, b_11_3,
                a_32_1, b_21_3,
                a_33_1, b_31_3
            ),
            ORANGE
        )

        self.play(FadeOut(destaque_A), FadeOut(destaque_B))

        # C32 - RED

        elemento_c32_A = VGroup(a_31,a_32,a_33)

        elemento_c32_B = VGroup(b_12,b_22,b_32)

        destaque_A = SurroundingRectangle(elemento_c32_A,buff=0.08,color=RED)

        destaque_B = SurroundingRectangle(elemento_c32_B,buff=0.08,color=RED)

        self.play(Create(destaque_A),Create(destaque_B))

        animar_resultado(
            C_generica.get_entries()[5].get_center(),
            (
                a_31_2, b_12_3,
                a_32_2, b_22_3,
                a_33_2, b_32_3
            ),
            RED
        )

        self.play(FadeOut(destaque_A), FadeOut(destaque_B))

        self.wait(3)