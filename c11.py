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

        # A matriz C usa células de tamanho controlado.
        # Os termos serão colocados dentro dessas células
        # durante a animação.

        C_generica = MobjectMatrix([
            [
                MathTex(r"\phantom{a_{11}\cdot b_{11}+a_{12}\cdot b_{21}+a_{13}\cdot b_{31}}"),
                MathTex(r"\phantom{a_{11}\cdot b_{12}+a_{12}\cdot b_{22}+a_{13}\cdot b_{32}}")
            ],
            [
                MathTex(r"\phantom{a_{21}\cdot b_{11}+a_{22}\cdot b_{21}+a_{23}\cdot b_{31}}"),
                MathTex(r"\phantom{a_{21}\cdot b_{12}+a_{22}\cdot b_{22}+a_{23}\cdot b_{32}}")
            ],
            [
                MathTex(r"\phantom{a_{31}\cdot b_{11}+a_{32}\cdot b_{21}+a_{33}\cdot b_{31}}"),
                MathTex(r"\phantom{a_{31}\cdot b_{12}+a_{32}\cdot b_{22}+a_{33}\cdot b_{32}}")
            ]
        ], v_buff=0.75).next_to(
            legenda_5,
            DOWN,
            buff=0.7
        )

        # Esconde os elementos internos de C.
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
        # FUNÇÃO PARA ANIMAR CADA ELEMENTO DA MATRIZ RESULTADO
        # ==========================================================

        def animar_resultado(
            centro,
            a1, b1,
            a2, b2,
            a3, b3,
            cor
        ):

            # ------------------------------------------------------
            # POSIÇÕES
            #
            #       a1 · b1 + a2 · b2 + a3 · b3
            #
            # Tudo é distribuído em torno do centro da célula.
            # ------------------------------------------------------

            # Primeiro produto
            pos_a1 = centro + 2.25 * LEFT
            pos_b1 = centro + 1.55 * LEFT
            pos_p1 = centro + 1.90 * LEFT

            # Segundo produto
            pos_a2 = centro + 0.55 * LEFT
            pos_b2 = centro + 0.10 * LEFT
            pos_p2 = centro + 0.32 * LEFT

            # Terceiro produto
            pos_a3 = centro + 1.15 * RIGHT
            pos_b3 = centro + 1.85 * RIGHT
            pos_p3 = centro + 1.50 * RIGHT

            # Sinais de soma
            pos_mais1 = centro + 0.90 * LEFT
            pos_mais2 = centro + 0.82 * RIGHT

            # ------------------------------------------------------
            # PRIMEIRO PRODUTO
            # ------------------------------------------------------

            self.play(
                a1.animate
                .move_to(pos_a1)
                .set_color(cor)
                .scale(0.55),

                b1.animate
                .move_to(pos_b1)
                .set_color(cor)
                .scale(0.55)
            )

            ponto_1 = MathTex(
                r'\cdot',
                color=cor
            ).scale(0.55).move_to(pos_p1)

            self.play(
                FadeIn(ponto_1)
            )

            # ------------------------------------------------------
            # SEGUNDO PRODUTO
            # ------------------------------------------------------

            self.play(
                a2.animate
                .move_to(pos_a2)
                .set_color(cor)
                .scale(0.55),

                b2.animate
                .move_to(pos_b2)
                .set_color(cor)
                .scale(0.55)
            )

            ponto_2 = MathTex(
                r'\cdot',
                color=cor
            ).scale(0.55).move_to(pos_p2)

            mais_1 = MathTex(
                r'+',
                color=cor
            ).scale(0.55).move_to(pos_mais1)

            self.play(
                FadeIn(ponto_2),
                FadeIn(mais_1)
            )

            # ------------------------------------------------------
            # TERCEIRO PRODUTO
            # ------------------------------------------------------

            self.play(
                a3.animate
                .move_to(pos_a3)
                .set_color(cor)
                .scale(0.55),

                b3.animate
                .move_to(pos_b3)
                .set_color(cor)
                .scale(0.55)
            )

            ponto_3 = MathTex(
                r'\cdot',
                color=cor
            ).scale(0.55).move_to(pos_p3)

            mais_2 = MathTex(
                r'+',
                color=cor
            ).scale(0.55).move_to(pos_mais2)

            self.play(
                FadeIn(ponto_3),
                FadeIn(mais_2)
            )

            self.wait(1)

            return VGroup(
                a1, ponto_1, b1,
                mais_1,
                a2, ponto_2, b2,
                mais_2,
                a3, ponto_3, b3
            )

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

        centro_c11 = C_generica.get_entries()[0].get_center()

        resultado_c11 = animar_resultado(
            centro_c11,
            a_11_1, b_11_1,
            a_12_1, b_21_1,
            a_13_1, b_31_1,
            PINK
        )

        self.wait(2)

        # ==========================================================
        # REMOVE DESTAQUES C11
        # ==========================================================

        self.play(
            FadeOut(destaque_A),
            FadeOut(destaque_B)
        )

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

        centro_c12 = C_generica.get_entries()[1].get_center()

        resultado_c12 = animar_resultado(
            centro_c12,
            a_11_2, b_12_1,
            a_12_2, b_22_1,
            a_13_2, b_32_1,
            BLUE
        )

        self.wait(2)

        self.play(
            FadeOut(destaque_A),
            FadeOut(destaque_B)
        )

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

        centro_c21 = C_generica.get_entries()[2].get_center()

        resultado_c21 = animar_resultado(
            centro_c21,
            a_21_1, b_11_2,
            a_22_1, b_21_2,
            a_23_1, b_31_2,
            GREEN
        )

        self.wait(2)

        self.play(
            FadeOut(destaque_A),
            FadeOut(destaque_B)
        )

        # ==========================================================
        # C22 - YELLOW
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
            color=YELLOW
        )

        destaque_B = SurroundingRectangle(
            elemento_c22_B,
            buff=0.08,
            color=YELLOW
        )

        self.play(
            Create(destaque_A),
            Create(destaque_B)
        )

        centro_c22 = C_generica.get_entries()[3].get_center()

        resultado_c22 = animar_resultado(
            centro_c22,
            a_21_2, b_12_2,
            a_22_2, b_22_2,
            a_23_2, b_32_2,
            YELLOW
        )

        self.wait(2)

        self.play(
            FadeOut(destaque_A),
            FadeOut(destaque_B)
        )

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

        centro_c31 = C_generica.get_entries()[4].get_center()

        resultado_c31 = animar_resultado(
            centro_c31,
            a_31_1, b_11_3,
            a_32_1, b_21_3,
            a_33_1, b_31_3,
            ORANGE
        )

        self.wait(2)

        self.play(
            FadeOut(destaque_A),
            FadeOut(destaque_B)
        )

        # ==========================================================
        # C32 - PURPLE
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
            color=PURPLE
        )

        destaque_B = SurroundingRectangle(
            elemento_c32_B,
            buff=0.08,
            color=PURPLE
        )

        self.play(
            Create(destaque_A),
            Create(destaque_B)
        )

        centro_c32 = C_generica.get_entries()[5].get_center()

        resultado_c32 = animar_resultado(
            centro_c32,
            a_31_2, b_12_3,
            a_32_2, b_22_3,
            a_33_2, b_32_3,
            PURPLE
        )

        self.wait(2)

        self.play(
            FadeOut(destaque_A),
            FadeOut(destaque_B)
        )

        self.wait(4)