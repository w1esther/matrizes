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
            r"da segunda matriz."
        ).next_to(
            legenda_2,
            DOWN,
            buff=1
        ).scale(0.85)

        self.play(Write(legenda_3))
        self.wait(2)

        legenda_4 = MathTex(
            r"A_{m\times n}\times B_{n\times p}"
            r"=C_{m\times p}"
        ).next_to(
            legenda_3,
            DOWN,
            buff=1
        )

        self.play(Write(legenda_4))
        self.wait(4)

        objetos_1 = [
            legenda_1,
            legenda_2,
            linha_1,
            linha_2,
            legenda_3,
            legenda_4
        ]

        for objeto in objetos_1:
            self.play(FadeOut(objeto))

        # ==========================================================
        # FUNÇÃO PARA TERMOS DAS MATRIZES
        # ==========================================================

        def termo_matriz(p, m, n):
            return MathTex(
                f"{p}_{{{m}{n}}}"
            )

        # ==========================================================
        # TÍTULO
        # ==========================================================

        self.play(
            titulo.animate.shift(1.5 * UP)
        )

        # ==========================================================
        # MATRIZ A
        # ==========================================================

        A_generica = MobjectMatrix([
            [
                termo_matriz('a', 1, 1),
                termo_matriz('a', 1, 2),
                termo_matriz('a', 1, 3)
            ],
            [
                termo_matriz('a', 2, 1),
                termo_matriz('a', 2, 2),
                termo_matriz('a', 2, 3)
            ],
            [
                termo_matriz('a', 3, 1),
                termo_matriz('a', 3, 2),
                termo_matriz('a', 3, 3)
            ]
        ]).next_to(
            titulo,
            DOWN,
            buff=1
        ).shift(2.5 * LEFT)

        # ==========================================================
        # ELEMENTOS ORIGINAIS DE A
        # ==========================================================

        a_11 = MathTex("a_{11}").move_to(
            A_generica.get_entries()[0]
        )

        a_12 = MathTex("a_{12}").move_to(
            A_generica.get_entries()[1]
        )

        a_13 = MathTex("a_{13}").move_to(
            A_generica.get_entries()[2]
        )

        a_21 = MathTex("a_{21}").move_to(
            A_generica.get_entries()[3]
        )

        a_22 = MathTex("a_{22}").move_to(
            A_generica.get_entries()[4]
        )

        a_23 = MathTex("a_{23}").move_to(
            A_generica.get_entries()[5]
        )

        a_31 = MathTex("a_{31}").move_to(
            A_generica.get_entries()[6]
        )

        a_32 = MathTex("a_{32}").move_to(
            A_generica.get_entries()[7]
        )

        a_33 = MathTex("a_{33}").move_to(
            A_generica.get_entries()[8]
        )

        # ==========================================================
        # CÓPIAS DE A
        # ==========================================================

        # C11
        a_11_1 = a_11.copy()
        a_12_1 = a_12.copy()
        a_13_1 = a_13.copy()

        # C12
        a_11_2 = a_11.copy()
        a_12_2 = a_12.copy()
        a_13_2 = a_13.copy()

        # C21
        a_21_1 = a_21.copy()
        a_22_1 = a_22.copy()
        a_23_1 = a_23.copy()

        # C22
        a_21_2 = a_21.copy()
        a_22_2 = a_22.copy()
        a_23_2 = a_23.copy()

        # C31
        a_31_1 = a_31.copy()
        a_32_1 = a_32.copy()
        a_33_1 = a_33.copy()

        # C32
        a_31_2 = a_31.copy()
        a_32_2 = a_32.copy()
        a_33_2 = a_33.copy()

        # ==========================================================
        # MULTIPLICAÇÃO
        # ==========================================================

        multiplicacao_1 = MathTex(
            r'\cdot'
        ).next_to(
            A_generica,
            RIGHT,
            buff=0.4
        )

        # ==========================================================
        # MATRIZ B
        # ==========================================================

        B_generica = MobjectMatrix([
            [
                termo_matriz('b', 1, 1),
                termo_matriz('b', 1, 2)
            ],
            [
                termo_matriz('b', 2, 1),
                termo_matriz('b', 2, 2)
            ],
            [
                termo_matriz('b', 3, 1),
                termo_matriz('b', 3, 2)
            ]
        ], v_buff=0.75).next_to(
            A_generica,
            RIGHT,
            buff=1
        )

        # ==========================================================
        # ELEMENTOS ORIGINAIS DE B
        # ==========================================================

        b_11 = MathTex("b_{11}").move_to(
            B_generica.get_entries()[0]
        )

        b_12 = MathTex("b_{12}").move_to(
            B_generica.get_entries()[1]
        )

        b_21 = MathTex("b_{21}").move_to(
            B_generica.get_entries()[2]
        )

        b_22 = MathTex("b_{22}").move_to(
            B_generica.get_entries()[3]
        )

        b_31 = MathTex("b_{31}").move_to(
            B_generica.get_entries()[4]
        )

        b_32 = MathTex("b_{32}").move_to(
            B_generica.get_entries()[5]
        )

        # ==========================================================
        # CÓPIAS DE B
        # ==========================================================

        # C11
        b_11_1 = b_11.copy()
        b_21_1 = b_21.copy()
        b_31_1 = b_31.copy()

        # C12
        b_12_1 = b_12.copy()
        b_22_1 = b_22.copy()
        b_32_1 = b_32.copy()

        # C21
        b_11_2 = b_11.copy()
        b_21_2 = b_21.copy()
        b_31_2 = b_31.copy()

        # C22
        b_12_2 = b_12.copy()
        b_22_2 = b_22.copy()
        b_32_2 = b_32.copy()

        # C31
        b_11_3 = b_11.copy()
        b_21_3 = b_21.copy()
        b_31_3 = b_31.copy()

        # C32
        b_12_3 = b_12.copy()
        b_22_3 = b_22.copy()
        b_32_3 = b_32.copy()

        # ==========================================================
        # IGUAL
        # ==========================================================

        igual_1 = MathTex(
            r'='
        ).next_to(
            B_generica,
            RIGHT,
            buff=0.8
        )

        # ==========================================================
        # LEGENDA
        # ==========================================================

        legenda_5 = Tex(
            r"Multiplica-se cada elemento de uma linha da primeira matriz "
            r"pelos elementos correspondentes de uma coluna da segunda "
            r"matriz e soma-se os resultados."
        ).scale(0.85)

        self.play(
            Write(legenda_5)
        )

        # ==========================================================
        # MATRIZ RESULTANTE C
        # ==========================================================

        C_generica = MobjectMatrix([
            [
                MathTex(r"C_{11}"),
                MathTex(r"C_{12}")
            ],
            [
                MathTex(r"C_{21}"),
                MathTex(r"C_{22}")
            ],
            [
                MathTex(r"C_{31}"),
                MathTex(r"C_{32}")
            ]
        ], v_buff=0.75).next_to(
            legenda_5,
            DOWN,
            buff=0.7
        )

        # Esconde os elementos de C
        for entrada in C_generica.get_entries():
            entrada.set_opacity(0)

        # ==========================================================
        # MOSTRA TUDO
        # ==========================================================

        self.play(
            FadeIn(A_generica),
            FadeIn(multiplicacao_1),
            FadeIn(B_generica),
            FadeIn(C_generica),
            FadeIn(igual_1)
        )

        # Coloca os elementos originais por cima das matrizes
        for elemento in [
            a_11, a_12, a_13,
            a_21, a_22, a_23,
            a_31, a_32, a_33
        ]:
            self.add(elemento)

        for elemento in [
            b_11, b_12,
            b_21, b_22,
            b_31, b_32
        ]:
            self.add(elemento)

        self.wait(2)

        # ==========================================================
        # CONFIGURAÇÃO DAS POSIÇÕES
        # ==========================================================

        # Cada expressão ficará centralizada em sua célula.
        #
        # a · b + a · b + a · b
        #
        # As posições são relativas ao centro da célula.

        # ==========================================================
        # C11 - PINK
        # ==========================================================

        elemento_c11_A = VGroup(
            a_11,
            a_12,
            a_13
        )

        elemento_c11_B = VGroup(
            b_11,
            b_21,
            b_31
        )

        destaque_A = SurroundingRectangle(
            elemento_c11_A,
            buff=0.08,
            color=PINK
        )

        destaque_B = SurroundingRectangle(
            elemento_c11_B,
            buff=0.08,
            color=PINK
        )

        self.play(
            Create(destaque_A),
            Create(destaque_B)
        )

        centro = C_generica.get_entries()[0].get_center()

        self.play(
            a_11_1.animate
            .move_to(centro + 3.6 * LEFT)
            .set_color(PINK),

            b_11_1.animate
            .move_to(centro + 2.5 * LEFT)
            .set_color(PINK)
        )

        ponto_1 = MathTex(
            r'\cdot',
            color=PINK
        ).move_to(
            centro + 3.05 * LEFT
        )

        self.play(FadeIn(ponto_1))

        self.play(
            a_12_1.animate
            .move_to(centro + 1.5 * LEFT)
            .set_color(PINK),

            b_21_1.animate
            .move_to(centro + 0.4 * LEFT)
            .set_color(PINK)
        )

        ponto_2 = MathTex(
            r'\cdot',
            color=PINK
        ).move_to(
            centro + 0.95 * LEFT
        )

        mais_1 = MathTex(
            r'+',
            color=PINK
        ).move_to(
            centro + 1.95 * LEFT
        )

        self.play(
            FadeIn(ponto_2),
            FadeIn(mais_1)
        )

        self.play(
            a_13_1.animate
            .move_to(centro + 1.0 * RIGHT)
            .set_color(PINK),

            b_31_1.animate
            .move_to(centro + 2.1 * RIGHT)
            .set_color(PINK)
        )

        ponto_3 = MathTex(
            r'\cdot',
            color=PINK
        ).move_to(
            centro + 1.55 * RIGHT
        )

        mais_2 = MathTex(
            r'+',
            color=PINK
        ).move_to(
            centro + 0.65 * RIGHT
        )

        self.play(
            FadeIn(ponto_3),
            FadeIn(mais_2)
        )

        self.wait(2)

        # ==========================================================
        # C12 - BLUE
        # ==========================================================

        elemento_c12_A = VGroup(
            a_11,
            a_12,
            a_13
        )

        elemento_c12_B = VGroup(
            b_12,
            b_22,
            b_32
        )

        destaque_A = SurroundingRectangle(
            elemento_c12_A,
            buff=0.08,
            color=BLUE
        )

        destaque_B = SurroundingRectangle(
            elemento_c12_B,
            buff=0.08,
            color=BLUE
        )

        self.play(
            Create(destaque_A),
            Create(destaque_B)
        )

        centro = C_generica.get_entries()[1].get_center()

        self.play(
            a_11_2.animate
            .move_to(centro + 3.6 * LEFT)
            .set_color(BLUE),

            b_12_1.animate
            .move_to(centro + 2.5 * LEFT)
            .set_color(BLUE)
        )

        ponto_1 = MathTex(
            r'\cdot',
            color=BLUE
        ).move_to(
            centro + 3.05 * LEFT
        )

        self.play(FadeIn(ponto_1))

        self.play(
            a_12_2.animate
            .move_to(centro + 1.5 * LEFT)
            .set_color(BLUE),

            b_22_1.animate
            .move_to(centro + 0.4 * LEFT)
            .set_color(BLUE)
        )

        ponto_2 = MathTex(
            r'\cdot',
            color=BLUE
        ).move_to(
            centro + 0.95 * LEFT
        )

        mais_1 = MathTex(
            r'+',
            color=BLUE
        ).move_to(
            centro + 1.95 * LEFT
        )

        self.play(
            FadeIn(ponto_2),
            FadeIn(mais_1)
        )

        self.play(
            a_13_2.animate
            .move_to(centro + 1.0 * RIGHT)
            .set_color(BLUE),

            b_32_1.animate
            .move_to(centro + 2.1 * RIGHT)
            .set_color(BLUE)
        )

        ponto_3 = MathTex(
            r'\cdot',
            color=BLUE
        ).move_to(
            centro + 1.55 * RIGHT
        )

        mais_2 = MathTex(
            r'+',
            color=BLUE
        ).move_to(
            centro + 0.65 * RIGHT
        )

        self.play(
            FadeIn(ponto_3),
            FadeIn(mais_2)
        )

        self.wait(2)

        # ==========================================================
        # C21 - GREEN
        # ==========================================================

        elemento_c21_A = VGroup(
            a_21,
            a_22,
            a_23
        )

        elemento_c21_B = VGroup(
            b_11,
            b_21,
            b_31
        )

        destaque_A = SurroundingRectangle(
            elemento_c21_A,
            buff=0.08,
            color=GREEN
        )

        destaque_B = SurroundingRectangle(
            elemento_c21_B,
            buff=0.08,
            color=GREEN
        )

        self.play(
            Create(destaque_A),
            Create(destaque_B)
        )

        centro = C_generica.get_entries()[2].get_center()

        self.play(
            a_21_1.animate
            .move_to(centro + 3.6 * LEFT)
            .set_color(GREEN),

            b_11_2.animate
            .move_to(centro + 2.5 * LEFT)
            .set_color(GREEN)
        )

        ponto_1 = MathTex(
            r'\cdot',
            color=GREEN
        ).move_to(
            centro + 3.05 * LEFT
        )

        self.play(FadeIn(ponto_1))

        self.play(
            a_22_1.animate
            .move_to(centro + 1.5 * LEFT)
            .set_color(GREEN),

            b_21_2.animate
            .move_to(centro + 0.4 * LEFT)
            .set_color(GREEN)
        )

        ponto_2 = MathTex(
            r'\cdot',
            color=GREEN
        ).move_to(
            centro + 0.95 * LEFT
        )

        mais_1 = MathTex(
            r'+',
            color=GREEN
        ).move_to(
            centro + 1.95 * LEFT
        )

        self.play(
            FadeIn(ponto_2),
            FadeIn(mais_1)
        )

        self.play(
            a_23_1.animate
            .move_to(centro + 1.0 * RIGHT)
            .set_color(GREEN),

            b_31_2.animate
            .move_to(centro + 2.1 * RIGHT)
            .set_color(GREEN)
        )

        ponto_3 = MathTex(
            r'\cdot',
            color=GREEN
        ).move_to(
            centro + 1.55 * RIGHT
        )

        mais_2 = MathTex(
            r'+',
            color=GREEN
        ).move_to(
            centro + 0.65 * RIGHT
        )

        self.play(
            FadeIn(ponto_3),
            FadeIn(mais_2)
        )

        self.wait(2)

        # ==========================================================
        # C22 - PURPLE
        # ==========================================================

        elemento_c22_A = VGroup(
            a_21,
            a_22,
            a_23
        )

        elemento_c22_B = VGroup(
            b_12,
            b_22,
            b_32
        )

        destaque_A = SurroundingRectangle(
            elemento_c22_A,
            buff=0.08,
            color=PURPLE
        )

        destaque_B = SurroundingRectangle(
            elemento_c22_B,
            buff=0.08,
            color=PURPLE
        )

        self.play(
            Create(destaque_A),
            Create(destaque_B)
        )

        centro = C_generica.get_entries()[3].get_center()

        self.play(
            a_21_2.animate
            .move_to(centro + 3.6 * LEFT)
            .set_color(PURPLE),

            b_12_2.animate
            .move_to(centro + 2.5 * LEFT)
            .set_color(PURPLE)
        )

        ponto_1 = MathTex(
            r'\cdot',
            color=PURPLE
        ).move_to(
            centro + 3.05 * LEFT
        )

        self.play(FadeIn(ponto_1))

        self.play(
            a_22_2.animate
            .move_to(centro + 1.5 * LEFT)
            .set_color(PURPLE),

            b_22_2.animate
            .move_to(centro + 0.4 * LEFT)
            .set_color(PURPLE)
        )

        ponto_2 = MathTex(
            r'\cdot',
            color=PURPLE
        ).move_to(
            centro + 0.95 * LEFT
        )

        mais_1 = MathTex(
            r'+',
            color=PURPLE
        ).move_to(
            centro + 1.95 * LEFT
        )

        self.play(
            FadeIn(ponto_2),
            FadeIn(mais_1)
        )

        self.play(
            a_23_2.animate
            .move_to(centro + 1.0 * RIGHT)
            .set_color(PURPLE),

            b_32_2.animate
            .move_to(centro + 2.1 * RIGHT)
            .set_color(PURPLE)
        )

        ponto_3 = MathTex(
            r'\cdot',
            color=PURPLE
        ).move_to(
            centro + 1.55 * RIGHT
        )

        mais_2 = MathTex(
            r'+',
            color=PURPLE
        ).move_to(
            centro + 0.65 * RIGHT
        )

        self.play(
            FadeIn(ponto_3),
            FadeIn(mais_2)
        )

        self.wait(2)

        # ==========================================================
        # C31 - ORANGE
        # ==========================================================

        elemento_c31_A = VGroup(
            a_31,
            a_32,
            a_33
        )

        elemento_c31_B = VGroup(
            b_11,
            b_21,
            b_31
        )

        destaque_A = SurroundingRectangle(
            elemento_c31_A,
            buff=0.08,
            color=ORANGE
        )

        destaque_B = SurroundingRectangle(
            elemento_c31_B,
            buff=0.08,
            color=ORANGE
        )

        self.play(
            Create(destaque_A),
            Create(destaque_B)
        )

        centro = C_generica.get_entries()[4].get_center()

        self.play(
            a_31_1.animate
            .move_to(centro + 3.6 * LEFT)
            .set_color(ORANGE),

            b_11_3.animate
            .move_to(centro + 2.5 * LEFT)
            .set_color(ORANGE)
        )

        ponto_1 = MathTex(
            r'\cdot',
            color=ORANGE
        ).move_to(
            centro + 3.05 * LEFT
        )

        self.play(FadeIn(ponto_1))

        self.play(
            a_32_1.animate
            .move_to(centro + 1.5 * LEFT)
            .set_color(ORANGE),

            b_21_3.animate
            .move_to(centro + 0.4 * LEFT)
            .set_color(ORANGE)
        )

        ponto_2 = MathTex(
            r'\cdot',
            color=ORANGE
        ).move_to(
            centro + 0.95 * LEFT
        )

        mais_1 = MathTex(
            r'+',
            color=ORANGE
        ).move_to(
            centro + 1.95 * LEFT
        )

        self.play(
            FadeIn(ponto_2),
            FadeIn(mais_1)
        )

        self.play(
            a_33_1.animate
            .move_to(centro + 1.0 * RIGHT)
            .set_color(ORANGE),

            b_31_3.animate
            .move_to(centro + 2.1 * RIGHT)
            .set_color(ORANGE)
        )

        ponto_3 = MathTex(
            r'\cdot',
            color=ORANGE
        ).move_to(
            centro + 1.55 * RIGHT
        )

        mais_2 = MathTex(
            r'+',
            color=ORANGE
        ).move_to(
            centro + 0.65 * RIGHT
        )

        self.play(
            FadeIn(ponto_3),
            FadeIn(mais_2)
        )

        self.wait(2)

        # ==========================================================
        # C32 - RED
        # ==========================================================

        elemento_c32_A = VGroup(
            a_31,
            a_32,
            a_33
        )

        elemento_c32_B = VGroup(
            b_12,
            b_22,
            b_32
        )

        destaque_A = SurroundingRectangle(
            elemento_c32_A,
            buff=0.08,
            color=RED
        )

        destaque_B = SurroundingRectangle(
            elemento_c32_B,
            buff=0.08,
            color=RED
        )

        self.play(
            Create(destaque_A),
            Create(destaque_B)
        )

        centro = C_generica.get_entries()[5].get_center()

        self.play(
            a_31_2.animate
            .move_to(centro + 3.6 * LEFT)
            .set_color(RED),

            b_12_3.animate
            .move_to(centro + 2.5 * LEFT)
            .set_color(RED)
        )

        ponto_1 = MathTex(
            r'\cdot',
            color=RED
        ).move_to(
            centro + 3.05 * LEFT
        )

        self.play(FadeIn(ponto_1))

        self.play(
            a_32_2.animate
            .move_to(centro + 1.5 * LEFT)
            .set_color(RED),

            b_22_3.animate
            .move_to(centro + 0.4 * LEFT)
            .set_color(RED)
        )

        ponto_2 = MathTex(
            r'\cdot',
            color=RED
        ).move_to(
            centro + 0.95 * LEFT
        )

        mais_1 = MathTex(
            r'+',
            color=RED
        ).move_to(
            centro + 1.95 * LEFT
        )

        self.play(
            FadeIn(ponto_2),
            FadeIn(mais_1)
        )

        self.play(
            a_33_2.animate
            .move_to(centro + 1.0 * RIGHT)
            .set_color(RED),

            b_32_3.animate
            .move_to(centro + 2.1 * RIGHT)
            .set_color(RED)
        )

        ponto_3 = MathTex(
            r'\cdot',
            color=RED
        ).move_to(
            centro + 1.55 * RIGHT
        )

        mais_2 = MathTex(
            r'+',
            color=RED
        ).move_to(
            centro + 0.65 * RIGHT
        )

        self.play(
            FadeIn(ponto_3),
            FadeIn(mais_2)
        )

        self.wait(3)