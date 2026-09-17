from manim import *

class ProdutoPorEscalar(MovingCameraScene):
    def construct(self):
        self.play(self.camera.frame.animate.scale(1.5))
        
        titulo = Text('Multiplicação de uma matriz por um escalar', font_size=32).shift(3*UP)

        self.play(FadeIn(titulo))

        legenda_1 =  Tex(
            r" A multiplicação de uma matriz por um escalar consiste em multiplicar",
            r" cada elemento da matriz por esse escalar, que necessariamente é um número real.").shift(3*DOWN).scale(0.8)
        
        n_generico = MathTex(r'n').shift(6*LEFT)

        n1 = MathTex(r'n').shift(6*LEFT)
        n2 = MathTex(r'n').shift(6*LEFT)
        n3 = MathTex(r'n').shift(6*LEFT)
        n4 = MathTex(r'n').shift(6*LEFT)
        n5 = MathTex(r'n').shift(6*LEFT)
        n6 = MathTex(r'n').shift(6*LEFT)
        n7 = MathTex(r'n').shift(6*LEFT)
        n8 = MathTex(r'n').shift(6*LEFT)
        n9 = MathTex(r'n').shift(6*LEFT)

        lista_n = [n1, n2, n3, n4, n5, n6, n7, n8, n9]

        multiplicacao = MathTex(r'\dot').shift(5.6*LEFT)

        def termo_matriz(p, m, n):
            termo = MathTex(f"{p}_{{{m}{n}}}")
            return termo

        A_generica = MobjectMatrix([
            [termo_matriz('a', 1, 1), termo_matriz('a', 1, 2), termo_matriz('a', 1, 3)],
            [termo_matriz('a', 2, 1), termo_matriz('a', 2, 2), termo_matriz('a', 2, 3)],
            [termo_matriz('a', 3, 1), termo_matriz('a', 3, 2), termo_matriz('a', 3, 3)]]).shift(3.3*LEFT)
        
        igual = MathTex(r'=').next_to(A_generica, RIGHT, buff=0.4)

        C_generica = MobjectMatrix([
            [MathTex(r"c_{11} + b_{11}"), MathTex(r"c_{12} + b_{12}"), MathTex(r"c_{13} + b_{13} + a_{13} + b_{11} + b_{11}")],
            [MathTex(r"c_{21} + b_{11}"), MathTex(r"c_{22} + b_{11}"), MathTex(r"c_{23} + b_{11} + a_{13} + b_{11} + b_{11}")],
            [MathTex(r"c_{31} + b_{11}"), MathTex(r"c_{32} + b_{11}"), MathTex(r"c_{33} + b_{11} + a_{13} + b_{11} + b_{11}")]
        ], v_buff=0.75).shift(3.2*RIGHT)

        for entrada in C_generica.get_entries():
            entrada.set_opacity(0)

        a_11 = MathTex("a_{11}").move_to(A_generica.get_entries()[0])
        a_12 = MathTex("a_{12}").move_to(A_generica.get_entries()[1])
        a_13 = MathTex("a_{13}").move_to(A_generica.get_entries()[2])
        a_21 = MathTex("a_{21}").move_to(A_generica.get_entries()[3])
        a_22 = MathTex("a_{22}").move_to(A_generica.get_entries()[4])
        a_23 = MathTex("a_{23}").move_to(A_generica.get_entries()[5])
        a_31 = MathTex("a_{31}").move_to(A_generica.get_entries()[6])
        a_32 = MathTex("a_{32}").move_to(A_generica.get_entries()[7])
        a_33 = MathTex("a_{33}").move_to(A_generica.get_entries()[8])

        elementos_a = [a_12, a_13, a_22, a_23, a_31, a_32, a_33, a_11, a_21]
        
        self.play(FadeIn(A_generica), FadeIn(n_generico), FadeIn(multiplicacao), FadeIn(igual), FadeIn(C_generica))

        for elemento in elementos_a:
            self.add(elemento)

        for elemento in lista_n:
            self.add(elemento)

        self.wait(1)
        
        self.play(FadeIn(legenda_1))

        m3 = MathTex(r'\dot').shift(0.8*UP + 1.2*RIGHT)
        m4 = MathTex(r'\dot').shift(0.8*UP + 3.3*RIGHT)
        m5 = MathTex(r'\dot').shift(0.8*UP + 5.4*RIGHT)

        m6 = MathTex(r'\dot').shift(0*DOWN + 1.2*RIGHT)
        m7 = MathTex(r'\dot').shift(0*DOWN + 3.3*RIGHT)
        m8 = MathTex(r'\dot').shift(0*DOWN + 5.4*RIGHT)

        m9 = MathTex(r'\dot').shift(0.8*DOWN + 1.2*RIGHT)
        m10 = MathTex(r'\dot').shift(0.8*DOWN + 3.3*RIGHT)
        m11 = MathTex(r'\dot').shift(0.8*DOWN + 5.4*RIGHT)

        m = [m3, m4, m5, m6, m7, m8, m9, m10, m11]

        self.wait(1)

        self.play(a_11.animate.move_to(C_generica.get_entries()[0]).shift(1.9*LEFT), n1.animate.move_to(C_generica.get_entries()[0]).shift(0.9*LEFT), FadeIn(m3))

        self.wait(1)

        self.play(n2.animate.move_to(C_generica.get_entries()[1]).shift(0.1*LEFT), a_12.animate.move_to(C_generica.get_entries()[1]).shift(1.1*LEFT), FadeIn(m4))

        self.wait(1)

        self.play(n3.animate.move_to(C_generica.get_entries()[2]).shift(2.6*RIGHT), a_13.animate.move_to(C_generica.get_entries()[2]).shift(1.6*RIGHT), FadeIn(m5))

        self.wait(1)

        self.play(a_21.animate.move_to(C_generica.get_entries()[3]).shift(1.9*LEFT), n4.animate.move_to(C_generica.get_entries()[3]).shift(0.9*LEFT), FadeIn(m6))

        self.wait(1)

        self.play(n5.animate.move_to(C_generica.get_entries()[4]).shift(0.1*LEFT), a_22.animate.move_to(C_generica.get_entries()[4]).shift(1.1*LEFT), FadeIn(m7))

        self.wait(1)

        self.play(n6.animate.move_to(C_generica.get_entries()[5]).shift(2.6*RIGHT), a_23.animate.move_to(C_generica.get_entries()[5]).shift(1.6*RIGHT), FadeIn(m8))

        self.wait(1)

        self.play(a_31.animate.move_to(C_generica.get_entries()[6]).shift(1.9*LEFT), n7.animate.move_to(C_generica.get_entries()[6]).shift(0.9*LEFT), FadeIn(m9))

        self.wait(1)

        self.play(n8.animate.move_to(C_generica.get_entries()[7]).shift(0.1*LEFT), a_32.animate.move_to(C_generica.get_entries()[7]).shift(1.1*LEFT), FadeIn(m10))

        self.wait(1)

        self.play(n9.animate.move_to(C_generica.get_entries()[8]).shift(2.6*RIGHT), a_33.animate.move_to(C_generica.get_entries()[8]).shift(1.6*RIGHT), FadeIn(m11))

        self.wait(3)

        for elemento in m:
            self.remove(elemento)

        for elemento in elementos_a:
            self.remove(elemento)
        
        for elemento in lista_n:
            self.remove(elemento)

        self.wait(1)

        tres = MathTex(r'3').shift(6*LEFT)

        tres1 = MathTex(r'3').shift(6*LEFT)
        tres2 = MathTex(r'3').shift(6*LEFT)
        tres3 = MathTex(r'3').shift(6*LEFT)
        tres4 = MathTex(r'3').shift(6*LEFT)
        tres5 = MathTex(r'3').shift(6*LEFT)
        tres6 = MathTex(r'3').shift(6*LEFT)
        tres7 = MathTex(r'3').shift(6*LEFT)
        tres8 = MathTex(r'3').shift(6*LEFT)
        tres9 = MathTex(r'3').shift(6*LEFT)


        e1 = MathTex(r'4').move_to(A_generica.get_entries()[0])
        e2 = MathTex(r'3').move_to(A_generica.get_entries()[1])
        e3 = MathTex(r'7').move_to(A_generica.get_entries()[2])
        e4 = MathTex(r'2').move_to(A_generica.get_entries()[3])
        e5 = MathTex(r'1').move_to(A_generica.get_entries()[4])
        e6 = MathTex(r'4').move_to(A_generica.get_entries()[5])
        e7 = MathTex(r'6').move_to(A_generica.get_entries()[6])
        e8 = MathTex(r'9').move_to(A_generica.get_entries()[7])
        e9 = MathTex(r'5').move_to(A_generica.get_entries()[8])

        e1_1 = MathTex(r'4').move_to(A_generica.get_entries()[0])
        e2_1 = MathTex(r'3').move_to(A_generica.get_entries()[1])
        e3_1 = MathTex(r'7').move_to(A_generica.get_entries()[2])
        e4_1 = MathTex(r'2').move_to(A_generica.get_entries()[3])
        e5_1 = MathTex(r'1').move_to(A_generica.get_entries()[4])
        e6_1 = MathTex(r'4').move_to(A_generica.get_entries()[5])
        e7_1 = MathTex(r'6').move_to(A_generica.get_entries()[6])
        e8_1 = MathTex(r'9').move_to(A_generica.get_entries()[7])
        e9_1 = MathTex(r'5').move_to(A_generica.get_entries()[8])

        lista_e = [e1_1, e2_1, e3_1, e4_1, e5_1, e6_1, e7_1,e8_1, e9_1 ]

        elemento_antigo1 = A_generica.get_entries()[0]
        elemento_antigo2 = A_generica.get_entries()[1]
        elemento_antigo3 = A_generica.get_entries()[2]
        elemento_antigo4 = A_generica.get_entries()[3]
        elemento_antigo5 = A_generica.get_entries()[4]
        elemento_antigo6 = A_generica.get_entries()[5]
        elemento_antigo7 = A_generica.get_entries()[6]
        elemento_antigo8 = A_generica.get_entries()[7]
        elemento_antigo9 = A_generica.get_entries()[8]

        self.play(Transform(n_generico, tres),ReplacementTransform(elemento_antigo1, e1),ReplacementTransform(elemento_antigo2, e2),ReplacementTransform(elemento_antigo3, e3),ReplacementTransform(elemento_antigo4, e4),ReplacementTransform(elemento_antigo5, e5),ReplacementTransform(elemento_antigo6, e6),ReplacementTransform(elemento_antigo7, e7),ReplacementTransform(elemento_antigo8, e8),ReplacementTransform(elemento_antigo9, e9))

        for elemento in lista_e:
            self.add(elemento)

        self.wait(2)

        self.play(tres1.animate.move_to(C_generica.get_entries()[0]).shift(1.9*LEFT), e1_1.animate.move_to(C_generica.get_entries()[0]).shift(0.9*LEFT), FadeIn(m3))

        self.wait(1)

        self.play(e2_1.animate.move_to(C_generica.get_entries()[1]).shift(0.1*LEFT), tres2.animate.move_to(C_generica.get_entries()[1]).shift(1.1*LEFT), FadeIn(m4))

        self.wait(1)

        self.play(e3_1.animate.move_to(C_generica.get_entries()[2]).shift(2.6*RIGHT), tres3.animate.move_to(C_generica.get_entries()[2]).shift(1.6*RIGHT), FadeIn(m5))

        self.wait(1)

        self.play(tres4.animate.move_to(C_generica.get_entries()[3]).shift(1.9*LEFT), e4_1.animate.move_to(C_generica.get_entries()[3]).shift(0.9*LEFT), FadeIn(m6))

        self.wait(1)

        self.play(e5_1.animate.move_to(C_generica.get_entries()[4]).shift(0.1*LEFT), tres5.animate.move_to(C_generica.get_entries()[4]).shift(1.1*LEFT), FadeIn(m7))

        self.wait(1)

        self.play(e6_1.animate.move_to(C_generica.get_entries()[5]).shift(2.6*RIGHT), tres6.animate.move_to(C_generica.get_entries()[5]).shift(1.6*RIGHT), FadeIn(m8))

        self.wait(1)

        self.play(tres7.animate.move_to(C_generica.get_entries()[6]).shift(1.9*LEFT), e7_1.animate.move_to(C_generica.get_entries()[6]).shift(0.9*LEFT), FadeIn(m9))

        self.wait(1)

        self.play(e8_1.animate.move_to(C_generica.get_entries()[7]).shift(0.1*LEFT), tres8.animate.move_to(C_generica.get_entries()[7]).shift(1.1*LEFT), FadeIn(m10))

        self.wait(1)

        self.play(e9_1.animate.move_to(C_generica.get_entries()[8]).shift(2.6*RIGHT), tres9.animate.move_to(C_generica.get_entries()[8]).shift(1.6*RIGHT), FadeIn(m11))

        self.wait(3)

        c_11_1 = MathTex("12").move_to(C_generica.get_entries()[0]).shift(1*LEFT)
        c_12_1 = MathTex("9").move_to(C_generica.get_entries()[1]).shift(0.5*LEFT)
        c_13_1 = MathTex("21").move_to(C_generica.get_entries()[2]).shift(1.8*RIGHT)
        c_21_1 = MathTex("6").move_to(C_generica.get_entries()[3]).shift(1*LEFT)
        c_22_1 = MathTex("3").move_to(C_generica.get_entries()[4]).shift(0.5*LEFT)
        c_23_1 = MathTex("12").move_to(C_generica.get_entries()[5]).shift(1.8*RIGHT)
        c_31_1 = MathTex("18").move_to(C_generica.get_entries()[6]).shift(1*LEFT)
        c_32_1 = MathTex("27").move_to(C_generica.get_entries()[7]).shift(0.5*LEFT)
        c_33_1 = MathTex("15").move_to(C_generica.get_entries()[8]).shift(1.8*RIGHT)

        grupo_11_1 = VGroup()
        grupo_11_1.add(m3, e1_1, tres1)

        self.play(Transform(grupo_11_1, c_11_1))

        self.wait(1)

        grupo_12_1 = VGroup()
        grupo_12_1.add(m4, e2_1, tres2)

        self.play(Transform(grupo_12_1, c_12_1))

        self.wait(1)

        grupo_13_1 = VGroup()
        grupo_13_1.add(m5, e3_1, tres3)

        self.play(Transform(grupo_13_1, c_13_1))

        self.wait(1)

        grupo_21_1 = VGroup()
        grupo_21_1.add(m6, e4_1, tres4)

        self.play(Transform(grupo_21_1, c_21_1))

        self.wait(1)

        grupo_22_1 = VGroup()
        grupo_22_1.add(m7, e5_1, tres5)

        self.play(Transform(grupo_22_1, c_22_1))

        self.wait(1)

        grupo_23_1 = VGroup()
        grupo_23_1.add(m8, e6_1, tres6)

        self.play(Transform(grupo_23_1, c_23_1))

        self.wait(1)

        grupo_31_1 = VGroup()
        grupo_31_1.add(m9, e7_1, tres7)

        self.play(Transform(grupo_31_1, c_31_1))

        self.wait(1)

        grupo_32_1 = VGroup()
        grupo_32_1.add(m10, e8_1, tres8)

        self.play(Transform(grupo_32_1, c_32_1))

        self.wait(1)

        grupo_33_1 = VGroup()
        grupo_33_1.add(m11, e9_1, tres9)

        self.play(Transform(grupo_33_1, c_33_1))

        self.wait(2)