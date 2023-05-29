from manim import *
import numpy as np

class WelcomeCard(Scene):
    def construct(self):
        title = Tex("Welcome to CVX", font_size= 64)

        self.play(Write(title), run_time= 2)
        self.wait(6)
        self.play(FadeOut(title), run_time= 1)

class DCPDetails(Scene):
    def construct(self):
        first = Tex("First things first:").scale(0.85)
        dcp = Tex("D", "isciplined ", "C", "onvex ", "P", "rogramming", " Rules.", color= ORANGE).next_to(first, DOWN)    

        text = VGroup(first, dcp).move_to((0,0,0))
        dcp2 = Tex("D", "C", "P", " Rules.", color= ORANGE).move_to(dcp)

        self.play(Write(first), run_time= 0.75)
        self.play(Write(dcp))
        self.wait(1)
        self.play(TransformMatchingTex(dcp, dcp2), run_func= smooth)
        self.wait(1)
        self.play(FadeOut(first, dcp2), run_func=smooth)

class OptimizationProblem(Scene):
    def construct(self):
        opt_obj = MathTex(r"\max_{p_1, p_2,...,p_M} R_{sum}")
        opt_obj_details = MathTex(r"\max_{p_1, p_2,...,p_M} \sum_{k=1}^{M}\log_2\left( 1 + \frac{p_k\left|{\hat{h}_k}\right|^2}{\left|{\hat{h}_k}\right|^2\sum_{j=1}^{k-1}p_j+P\sigma^2_{\epsilon} + \sigma^2} \right)")

        subject_to = MathTex(r"\text{s.t.}")
        first_constraint = MathTex(r"C1:\quad \sum_{k=1}^{M}p_k \leq P.").next_to(subject_to, RIGHT)
        second_constraint = MathTex(r"C2:\quad p_k\geq (w_k -1)\left( \sum_{j=1}^{k-1} p_j + \frac{P\sigma_{\epsilon}^2+\sigma^2}{\left|{\hat{h}_k}\right|^2} \right ) \quad \forall k = 1,2,...,M.").next_to(first_constraint, DOWN).align_to(first_constraint, LEFT)

        constraints_group = VGroup(subject_to, first_constraint, second_constraint).scale(0.6).move_to((0,0,0))

        opt_obj_details.scale(0.65).next_to(constraints_group, UP)
        opt_obj.scale(0.65).next_to(opt_obj_details, UP)

        opt_problem = VGroup(opt_obj, opt_obj_details, constraints_group).move_to((0,0,0)).arrange(DOWN, buff= 0.5)

        self.play(AnimationGroup(*[Write(t) for t in opt_problem], lag_ratio=0.75))
        self.wait(3)

        self.play(Indicate(opt_obj_details, scale_factor= 1.15, color=ORANGE))
        self.wait(1)

        self.play(FadeOut(opt_obj, constraints_group), rate_func=smooth)
        self.play(opt_obj_details.animate.scale(1.15).move_to((0,0,0)), rate_func= smooth)
        self.wait(2)

    
class DCPRules(Scene):
    def construct(self):
        problem = MathTex(r"\max_{p_1, p_2,...,p_M}", r"\sum_{k=1}^{M}", r"\log_2", r"\left( 1 + \frac{p_k\left|{\hat{h}_k}\right|^2}{\left|{\hat{h}_k}\right|^2\sum_{j=1}^{k-1}p_j+P\sigma^2_{\epsilon} + \sigma^2} \right)").scale(0.7475)
        without_max_str = MathTex(r"\sum_{k=1}^{M}", r"\log_2", r"\left( 1 + \frac{p_k\left|{\hat{h}_k}\right|^2}{\left|{\hat{h}_k}\right|^2\sum_{j=1}^{k-1}p_j+P\sigma^2_{\epsilon} + \sigma^2} \right)").scale(0.7475)
        without_sum_str = MathTex(r"\log_2", r"\left( 1 + \frac{p_k\left|{\hat{h}_k}\right|^2}{\left|{\hat{h}_k}\right|^2\sum_{j=1}^{k-1}p_j+P\sigma^2_{\epsilon} + \sigma^2} \right)").scale(0.7475)
        without_log_str = MathTex(r"\left( 1 + \frac{p_k\left|{\hat{h}_k}\right|^2}{\left|{\hat{h}_k}\right|^2\sum_{j=1}^{k-1}p_j+P\sigma^2_{\epsilon} + \sigma^2} \right)").scale(0.7475)
        without_braces_str = MathTex(r"1", r"+", r"\frac{p_k\left|{\hat{h}_k}\right|^2}{\left|{\hat{h}_k}\right|^2\sum_{j=1}^{k-1}p_j+P\sigma^2_{\epsilon} + \sigma^2}").scale(0.7475)

        self.add(problem)
        self.wait(1)
        self.play(TransformMatchingTex(problem, without_max_str, path_along_arc= LEFT), run_func= smooth)
        self.wait(1)
        self.play(TransformMatchingTex(without_max_str, without_sum_str), run_func= smooth)
        self.wait(1)
        self.play(TransformMatchingTex(without_sum_str, without_log_str), run_func= smooth)
        self.play(TransformMatchingTex(without_log_str, without_braces_str), run_func= smooth)
        self.wait(1)

        C = without_braces_str.get_parts_by_tex(r"\sigma^2_{\epsilon} + \sigma^2}")[0]
        C_group = VGroup(*C)

        brace = Brace(C_group[-7:], direction=DOWN)
        brace_text = brace.get_tex("C")

        self.play(AnimationGroup(GrowFromCenter(brace), Write(brace_text), lag_ratio= 0.55))
        self.wait(2)

        without_braces_str_with_C = MathTex(r"1", r"+", r"\frac{p_k\left|{\hat{h}_k}\right|^2}{\left|{\hat{h}_k}\right|^2\sum_{j=1}^{k-1}p_j+ C}").scale(0.7475)

        self.play(FadeOut(brace), run_time=0.5)
        self.play(AnimationGroup(FadeOut(brace_text, shift=UP),
                                TransformMatchingTex(without_braces_str, without_braces_str_with_C),
                                run_func= smooth,
                                lag_ratio= 0.28))
        self.wait(1)

        dec_one = MathTex(r"\frac{\left|{\hat{h}_k}\right|^2\sum_{i=1}^{k-1}p_i+ C}{\left|{\hat{h}_k}\right|^2\sum_{j=1}^{k-1}p_j+ C}",
                          r"+",
                          r"\frac{p_k\left|{\hat{h}_k}\right|^2}{\left|{\hat{h}_k}\right|^2\sum_{j=1}^{k-1}p_j+ C}").scale(0.7475)
        
        self.play(TransformMatchingTex(without_braces_str_with_C, dec_one), run_func= smooth)
        self.wait(1)

        whole = MathTex(r"\frac{\left|{\hat{h}_k}\right|^2\sum_{i=1}^{k-1}p_i+ C + p_k\left|{\hat{h}_k}\right|^2}{\left|{\hat{h}_k}\right|^2\sum_{j=1}^{k-1}p_j+ C}").scale(0.7475)

        # self.play(TransformMatchingTex(dec_one, whole), run_func= smooth)
        self.play(ReplacementTransform(dec_one, whole), run_func= smooth)
        self.wait(1)

        final_form = MathTex(r"\frac{\left|{\hat{h}_k}\right|^2\sum_{i=1}^{k}p_i+ C}{\left|{\hat{h}_k}\right|^2\sum_{j=1}^{k-1}p_j+ C}").scale(0.7475)

        # self.play(TransformMatchingTex(whole, final_form), run_func= smooth)
        self.play(ReplacementTransform(whole, final_form), run_func= smooth)
        self.wait(1)

        final_form_braces = MathTex(r"\left(\frac{\left|{\hat{h}_k}\right|^2\sum_{i=1}^{k}p_i+ C}{\left|{\hat{h}_k}\right|^2\sum_{j=1}^{k-1}p_j+ C}\right)").scale(0.7475)
        back_to_whole_equation = MathTex(r"\max_{p_1, p_2,...,p_M}", r"\sum_{k=1}^{M}", r"\log_2", r"\left(\frac{\left|{\hat{h}_k}\right|^2\sum_{i=1}^{k}p_i+ C}{\left|{\hat{h}_k}\right|^2\sum_{j=1}^{k-1}p_j+ C}\right)").scale(0.7475)

        self.play(TransformMatchingTex(final_form, final_form_braces), run_func= smooth, run_time=0.25)
        self.play(TransformMatchingTex(final_form_braces, back_to_whole_equation), run_func= smooth, run_time=0.75)
        self.wait(0.5)

        self.play(back_to_whole_equation.animate.shift(0.75*UP))

        warning = Tex("This doesn't follow DCP rules.", color= RED).shift(0.75*DOWN)
        details = Tex("linear / linear ratio.").scale(0.75).shift(1.25*DOWN)
        self.play(Write(warning), run_time= 0.55)
        self.play(Write(details), run_time= 0.4)
        self.wait(2)
        self.play(FadeOut(back_to_whole_equation, warning, details), run_func= smooth)

class MEquations(Scene):
    def construct(self):
        E1 = MathTex(r"L(p, w, \mu, \nu, \lambda, \alpha) = R_{sum}(p,w) + \sum_{k=1}^{M} \mu_k g_k(p,w) + \nu f(w) + \lambda h(p) + \sum_{k=1}^{M} {\alpha_k y_k(p)}")
        E2 = MathTex(r"R_{\mathrm{sum}} = \sum_{k=1}^{M} w_B \log_2 \left[1 + \frac{P_k \left|\hat{h_k}\right|^2}{\left|\hat{h_k}\right|^2 \sum_{j=1}^{K-1} {p_j} + P \sigma_{\epsilon}^2 + w_B \sigma^2}\right]")
        E3 = MathTex(r"g_k(p,w) = R_k = w_B \log_2 \left[1 + \frac{P_k \left|\hat{h_k}\right|^2}{\left|\hat{h_k}\right|^2 \sum_{j=1}^{K-1} {p_j} + P \sigma_{\epsilon}^2 + w_B \sigma^2}\right] - r_k")
        E4 = MathTex(r"f (w) = W_{\mathrm{tot}} - w_B")
        E5 = MathTex(r"h(p) = P - \sum_{k=1}^{M} p_k")
        E6 = MathTex(r"y_k(p) = p_k")

        for e in [E1, E2, E3, E4, E5, E6]:
            self.play(Write(e.scale(0.75)))
            self.wait(1)
            self.play(FadeOut(e), run_func= smooth, run_time= 0.8)
            self.wait(1)

class MV1(Scene):
    def construct(self):
        r= r"R_{\mathrm{sum}} = "
        summation = r"\sum_{k=1}^{M}"
        w_B = r"w_B"
        log_2 = r"\log_2"

        first_term = r"\left[1 + \frac{P_1 \left|\hat{h_1}\right|^2}{P \sigma_{\epsilon}^2 + w_B \sigma^2}\right]"
        second_term = r"\left[1 + \frac{P_2 \left|\hat{h_2}\right|^2}{\left|\hat{h_2}\right|^2 p_1 + P \sigma_{\epsilon}^2 + w_B \sigma^2}\right]"
        third_term = r"\left[1 + \frac{P_3 \left|\hat{h_3}\right|^2}{\left|\hat{h_3}\right|^2 (p_1 + p_2) + P \sigma_{\epsilon}^2 + w_B \sigma^2}\right]"

        R_sum_whole_equation = MathTex(r, summation, w_B, log_2, r"\left[1 + \frac{P_k \left|\hat{h_k}\right|^2}{\left|\hat{h_k}\right|^2 \sum_{j=1}^{K-1} {p_j} + P \sigma_{\epsilon}^2 + w_B \sigma^2}\right]").scale(0.75)
        R_sum = MathTex(r).scale(0.8)
        R_first = MathTex(r, w_B, log_2, first_term).scale(0.8)
        R_second = MathTex(r, w_B, log_2, first_term, r"+", w_B, log_2, second_term).scale(0.8)
        R_third = MathTex(r, w_B, log_2, first_term, r"+", w_B, log_2, second_term, r"\\ \\", r"+",  w_B, log_2, third_term).scale(0.8)

        self.play(TransformMatchingTex(R_sum_whole_equation, R_sum), run_func=smooth)
        self.wait(0.2)
        self.play(TransformMatchingTex(R_sum, R_first), run_func=smooth)
        self.wait(0.1)
        self.play(TransformMatchingTex(R_first, R_second), run_func=smooth)
        self.wait(0.1)
        self.play(TransformMatchingTex(R_second, R_third), run_func=smooth)
        self.wait(1)
        self.play(FadeOut(R_third), run_func= smooth)

class MV2(Scene):
    def construct(self):
        g_k =  MathTex(r"g_k", r"(p,w)", r"= R_k = w_B \log_2 \left[1 + \frac{P_k \left|\hat{h_k}\right|^2}{\left|\hat{h_k}\right|^2 \sum_{j=1}^{K-1} {p_j} + P \sigma_{\epsilon}^2 + w_B \sigma^2}\right] - r_k").scale(0.7)
        g_k_raw = MathTex(r"g_k").scale(0.7)
        g_k1 = MathTex(r"g_1").scale(0.7)
        g_k2 = MathTex(r"g_2").scale(0.7)
        g_k3 = MathTex(r"g_3").scale(0.7)

        self.play(Write(g_k))
        self.wait(0.5)

        self.play(TransformMatchingTex(g_k, g_k_raw), run_func= smooth)
        self.wait(0.5)
        self.play(AnimationGroup(
            FadeOut(g_k_raw),
            FadeIn(g_k1),
            g_k1.animate.shift(1.5*UP),
            FadeIn(g_k2),
            FadeIn(g_k3),
            g_k3.animate.shift(1.5*DOWN)
        ))
        self.wait(1)

        g_1 = r"R_1 = w_B \log_2 \left[p_1 \left|\hat{h_1}\right|^2 + P \sigma_{\epsilon}^2 + w_B \sigma^2\right] - w_B \log_2 \left[P \sigma_{\epsilon}^2 + w_B \sigma^2\right] - r_1"
        g_2 = r"R_2 = w_B \log_2 \left[(p_1 + p_2) \left|\hat{h_2}\right|^2 + P \sigma_{\epsilon}^2 + w_B \sigma^2\right] - w_B \log_2 \left[p_1 \left|\hat{h_2}\right|^2 + P \sigma_{\epsilon}^2 + w_B \sigma^2\right] - r_2"
        g_3 = r"R_3 = w_B \log_2 \left[(p_1 + p_2 + p_3) \left|\hat{h_3}\right|^2 + P \sigma_{\epsilon}^2 + w_B \sigma^2\right] \\ - w_B \log_2 \left[(p_1 + p_2) \left|\hat{h_3}\right|^2 + P \sigma_{\epsilon}^2 + w_B \sigma^2\right] - r_3"

        g_1_tex = MathTex(r"g_1", r"=", g_1).scale(0.7).shift(1.5*UP)
        g_2_tex = MathTex(r"g_2", r"=", g_2).scale(0.7)
        g_3_tex = MathTex(r"g_3", r"=", g_3).scale(0.7).shift(1.5*DOWN)

        self.play(TransformMatchingTex(g_k1, g_1_tex), run_func=smooth)
        self.wait(0.5)
        self.play(TransformMatchingTex(g_k2, g_2_tex), run_func=smooth)
        self.wait(0.5)
        self.play(TransformMatchingTex(g_k3, g_3_tex), run_func=smooth)
        self.wait(2)
        self.play(FadeOut(g_1_tex, g_2_tex, g_3_tex), run_func= smooth)

class MV3(Scene):
    def construct(self):
        h_sum = MathTex(r"h(p)", r"=", r"P-" r"\sum_{k=1}^{M}", r"p_k").scale(0.8)
        h_p = MathTex(r"h(p)").scale(0.8)
        h_new = MathTex(r"h(p)", r"=", r"P-", r"p_1", r"-", r"p_2", r"-", r"p_3").scale(0.8)

        self.play(Write(h_sum), run_func=smooth)
        self.wait(0.5)
        self.play(TransformMatchingTex(h_sum, h_new), run_func = smooth)
        self.wait(1)
        self.play(FadeOut(h_new), run_func= smooth)

class MV4(Scene):
    def construct(self):
        y_k = MathTex(r"y_k(p)=",  r"p_k").scale(0.8)
        y_1 = MathTex(r"y_1(p)=",  r"p_1").scale(0.8)
        y_2 = MathTex(r"y_2(p)=",  r"p_2").scale(0.8)
        y_3 = MathTex(r"y_3(p)=",  r"p_3").scale(0.8)

        self.play(Write(y_k), run_func=smooth)
        self.wait(0.5)
        self.play(AnimationGroup(
            FadeOut(y_k),
            FadeIn(y_1),
            y_1.animate.shift(1.5*UP),
            FadeIn(y_2),
            FadeIn(y_3),
            y_3.animate.shift(1.5*DOWN)
        ))
        self.wait(1)

        self.play(FadeOut(y_1, y_2, y_3), run_func= smooth)

class MV5(Scene):
    def construct(self):
        L_original = MathTex(r"L(p, w, \mu, \nu, \lambda, \alpha) =",
                             r"R_{sum}(p,w)",
                             r"+",
                             r"\sum_{k=1}^{M}\mu_k g_k(p,w)",
                             r"+",
                             r"\nu(w)",
                             r"+",
                             r"\lambda h(p)",
                             r"+",
                             r"\sum_{k=1}^{M} {\alpha_k y_k(p)}").scale(0.8)
        
        L_temp = MathTex(r"L(p, w, \mu, \nu, \lambda, \alpha) =",
                        r"R_{sum}(p,w)",
                        r"\\",
                        r"+ \mu_1 R_1 + \mu_2 R_2 + \mu_3 R_3 - \mu_1 r_1 - \mu_2 r_2 - \mu_3 r_3 + \nu W_{tot} - \nu w_B",
                        r"\\",
                        r"+ \lambda P - \lambda p_1 - \lambda p_2 - \lambda p_3 + \alpha_1 p_1 + \alpha_2 p_2 + \alpha_3 p_3").scale(0.8)

        L_new = MathTex(r"L(p, w, \mu, \nu, \lambda, \alpha) =",
                        r"w_B \log_2 \left[1 + \frac{P_1 \left|\hat{h_1}\right|^2}{P \sigma_{\epsilon}^2 + w_B \sigma^2}\right]",
                        r"\\",
                        r"+",
                        r"w_B \log_2 \left[1 + \frac{P_2 \left|\hat{h_2}\right|^2}{\left|\hat{h_2}\right|^2 p_1 + P \sigma_{\epsilon}^2 + w_B \sigma^2}\right]",
                        r"\\",
                        r"+",
                        r"w_B \log_2 \left[1 + \frac{P_3 \left|\hat{h_3}\right|^2}{\left|\hat{h_3}\right|^2 (p_1 + p_2) + P \sigma_{\epsilon}^2 + w_B \sigma^2}\right]",
                        r"\\",
                        r"+ \mu_1 R_1 + \mu_2 R_2 + \mu_3 R_3 - \mu_1 r_1 - \mu_2 r_2 - \mu_3 r_3 + \nu W_{tot} - \nu w_B",
                        r"\\",
                        r"+ \lambda P - \lambda p_1 - \lambda p_2 - \lambda p_3 + \alpha_1 p_1 + \alpha_2 p_2 + \alpha_3 p_3").scale(0.8)
        
        self.play(Write(L_original), run_func=smooth)
        self.wait(0.5)
        self.play(TransformMatchingTex(L_original, L_temp), run_func= smooth)
        self.wait(0.5)
        self.play(TransformMatchingTex(L_temp, L_new), run_func= smooth)
        self.wait(0.5)
        self.play(FadeOut(L_new), run_func= smooth)

class MV6(Scene):
    def construct(self):
        L_p1 = MathTex(r"\frac{\partial}{\partial p_1} L(p, w, \mu, \nu, \lambda, \alpha)").scale(0.8).shift(1.5*UP)
        L_p2 = MathTex(r"\frac{\partial}{\partial p_2} L(p, w, \mu, \nu, \lambda, \alpha)").scale(0.8)
        L_p3 = MathTex(r"\frac{\partial}{\partial p_3} L(p, w, \mu, \nu, \lambda, \alpha)").scale(0.8).shift(1.5*DOWN)

        self.play(Write(L_p1))
        self.play(Write(L_p2))
        self.play(Write(L_p3))

        L_p1_new = MathTex(r"\frac{\partial {R_{sum}}}{\partial {p_1}} - \lambda^\ast + \mu_1^\ast \frac{\partial {R_1}}{\partial {p_1}} + \mu_2^\ast \frac{\partial {R_2}}{\partial {p_1}} + \mu_3^\ast \frac{\partial {R_3}}{\partial {p_1}}", r"+ \alpha_1^\ast", r"= 0").scale(0.8).shift(1.5*UP)
        L_p2_new = MathTex(r"\frac{\partial {R_{sum}}}{\partial {p_2}} - \lambda^\ast + \mu_2^\ast \frac{\partial {R_2}}{\partial {p_2}} + \mu_3^\ast \frac{\partial {R_3}}{\partial {p_2}}", r"+ \alpha_2^\ast", r"= 0").scale(0.8)
        L_p3_new = MathTex(r"\frac{\partial {R_{sum}}}{\partial {p_3}} - \lambda^\ast + \mu_3^\ast \frac{\partial {R_3}}{\partial {p_3}}", r"+ \alpha_3^\ast", r"= 0").scale(0.8).shift(1.5*DOWN)

        L_p1_newest = MathTex(r"\frac{\partial {R_{sum}}}{\partial {p_1}} - \lambda^\ast + \mu_1^\ast \frac{\partial {R_1}}{\partial {p_1}} + \mu_2^\ast \frac{\partial {R_2}}{\partial {p_1}} + \mu_3^\ast \frac{\partial {R_3}}{\partial {p_1}}", r"= 0").scale(0.8).shift(1.5*UP)
        L_p2_newest = MathTex(r"\frac{\partial {R_{sum}}}{\partial {p_2}} - \lambda^\ast + \mu_2^\ast \frac{\partial {R_2}}{\partial {p_2}} + \mu_3^\ast \frac{\partial {R_3}}{\partial {p_2}}", r"= 0").scale(0.8)
        L_p3_newest = MathTex(r"\frac{\partial {R_{sum}}}{\partial {p_3}} - \lambda^\ast + \mu_3^\ast \frac{\partial {R_3}}{\partial {p_3}}", r"= 0").scale(0.8).shift(1.5*DOWN)

        self.play(ReplacementTransform(L_p1, L_p1_new), run_func= smooth)
        self.wait(0.5)
        self.play(ReplacementTransform(L_p2, L_p2_new), run_func= smooth)
        self.wait(0.5)
        self.play(ReplacementTransform(L_p3, L_p3_new), run_func= smooth)
        self.wait(0.5)

        self.play(TransformMatchingTex(L_p1_new, L_p1_newest), run_func=smooth, run_time= 0.75)
        self.wait(0.5)
        self.play(TransformMatchingTex(L_p2_new, L_p2_newest), run_func=smooth, run_time= 0.75)
        self.wait(0.5)
        self.play(TransformMatchingTex(L_p3_new, L_p3_newest), run_func=smooth, run_time= 0.75)
        self.wait(0.5)

        self.play(FadeOut(L_p1_newest, L_p2_newest, L_p3_newest), run_func= smooth)

class HV1(Scene):
    def construct(self):
        main_R = MathTex(r"R_k", r"=", r"w_B^\ast", r"\log_2", r"\left[1 + \frac{p_k^\ast \left|\hat{h_k}\right|^2}{\left|\hat{h_k}\right|^2 \sum_{j=1}^{K-1} {p_j^\ast} + P \sigma_{\epsilon}^2 + w_B^\ast \sigma^2}\right]", r"= r_k", r"\qquad \text{for} \ k = 2, 3").scale(0.8)
        P_sum = MathTex(r"p_1^\ast + p_2^\ast + p_3^\ast = P").scale(0.8).next_to(main_R, DOWN, buff= 0.5)
        W_cons = MathTex(r"w_B^\ast = W_{\mathrm{tot}}").scale(0.8).next_to(P_sum, DOWN, buff= 0.5)

        VGroup(main_R, P_sum, W_cons).move_to((0,0,0))

        for e in [main_R, P_sum, W_cons]:
            self.play(Write(e), run_func= smooth)
            self.wait(0.5)
        self.wait(0.5)

        self.play(AnimationGroup(
            FadeOut(P_sum, W_cons),
            main_R.animate.move_to((0,0,0))
        ))
        self.wait(0.5)
        
        r_k = MathTex(r"r_k", r"=", r"w_B^\ast", r"\log_2", r"\left[1 + \frac{p_k^\ast \left|\hat{h_k}\right|^2}{\left|\hat{h_k}\right|^2 \sum_{j=1}^{K-1} {p_j^\ast} + P \sigma_{\epsilon}^2 + w_B^\ast \sigma^2}\right]").scale(0.8)
        self.play(TransformMatchingTex(main_R, r_k), run_func= smooth)
        self.wait(0.5)

        r_w = MathTex(r"\frac{r_k}{w_B^\ast}", r"=", r"\log_2", r"\left[1 + \frac{p_k^\ast \left|\hat{h_k}\right|^2}{\left|\hat{h_k}\right|^2 \sum_{j=1}^{K-1} {p_j^\ast} + P \sigma_{\epsilon}^2 + w_B^\ast \sigma^2}\right]").scale(0.8)
        self.play(TransformMatchingTex(r_k, r_w), run_func= smooth)
        self.wait(0.5)

        e_r_w = MathTex(r"2^{\frac{r_k}{w_B^\ast}}", r"=", r"\left[1 + \frac{p_k^\ast \left|\hat{h_k}\right|^2}{\left|\hat{h_k}\right|^2 \sum_{j=1}^{K-1} {p_j^\ast} + P \sigma_{\epsilon}^2 + w_B^\ast \sigma^2}\right]").scale(0.8)
        self.play(TransformMatchingTex(r_w, e_r_w), run_func= smooth)
        self.wait(0.5)

        brace = Brace(e_r_w[0], direction=DOWN)
        brace_text = brace.get_tex("m_k").scale(0.8)
        self.play(AnimationGroup(GrowFromCenter(brace), Write(brace_text), lag_ratio= 0.55))
        self.wait(0.5)

        m_k = MathTex(r"m_k", r"=", r"\left[1 + \frac{p_k^\ast \left|\hat{h_k}\right|^2}{\left|\hat{h_k}\right|^2 \sum_{j=1}^{K-1} {p_j^\ast} + P \sigma_{\epsilon}^2 + w_B^\ast \sigma^2}\right]").scale(0.8)
        m_k_no_brackets = MathTex(r"m_k", r"=", r"1", r"+", r"\frac{p_k^\ast \left|\hat{h_k}\right|^2}{\left|\hat{h_k}\right|^2 \sum_{j=1}^{K-1} {p_j^\ast} + P \sigma_{\epsilon}^2 + w_B^\ast \sigma^2}").scale(0.8)

        self.play(FadeOut(brace), run_time=0.5)
        self.play(AnimationGroup(FadeOut(brace_text, shift=UP),
                                TransformMatchingTex(e_r_w, m_k),
                                run_func= smooth,
                                lag_ratio= 0.28))
        
        self.play(TransformMatchingTex(m_k, m_k_no_brackets))
        m_1 = MathTex(r"m_k", r"-", r"1", r"=", r"\frac{p_k^\ast \left|\hat{h_k}\right|^2}{\left|\hat{h_k}\right|^2 \sum_{j=1}^{K-1} {p_j^\ast} + P \sigma_{\epsilon}^2 + w_B^\ast \sigma^2}").scale(0.8)
        self.play(TransformMatchingTex(m_k_no_brackets, m_1))
        self.wait(0.5)

        p_k_prod = MathTex(r"\left(m_k-1\right)", r"\left(\left|\hat{h_k}\right|^2 \sum_{j=1}^{K-1} {p_j^\ast}\right) + P \sigma_{\epsilon}^2 + w_B^\ast \sigma^2", r"=", r"p_k^\ast", r"\left|\hat{h_k}\right|^2").scale(0.8)
        self.play(ReplacementTransform(m_1, p_k_prod), run_func= smooth)
        self.wait(0.5)

        p_k_h = MathTex(r"p_k^\ast", r"\left|\hat{h_k}\right|^2", r"=", r"\left(m_k-1\right)", r"\left(\left|\hat{h_k}\right|^2 \sum_{j=1}^{K-1} {p_j^\ast} + P \sigma_{\epsilon}^2 + w_B^\ast \sigma^2\right)").scale(0.8)
        self.play(TransformMatchingTex(p_k_prod, p_k_h), run_func= smooth)
        self.wait(0.5)

        p_k = MathTex(r"p_k^\ast", r"=", r"\left(m_k-1\right)", r"\left(\frac{\left|\hat{h_k}\right|^2 \sum_{j=1}^{K-1} {p_j^\ast} + P \sigma_{\epsilon}^2 + w_B^\ast \sigma^2}{\left|\hat{h_k}\right|^2}\right)").scale(0.8)
        self.play(TransformMatchingTex(p_k_h, p_k), run_func= smooth)
        self.wait(0.5)

        final_form = MathTex(r"p_k^\ast", r"=", r"\left(m_k-1\right)", r"\left(\sum_{j=1}^{K-1} {p_j^\ast} + \frac{P \sigma_{\epsilon}^2 + w_B^\ast \sigma^2}{\left|\hat{h_k}\right|^2}\right)").scale(0.8)
        self.play(TransformMatchingTex(p_k, final_form), run_func= smooth)
        self.wait(1)

        self.play(FadeOut(final_form), run_func= smooth)

class HV2(Scene):
    def construct(self):
        p_2 = MathTex(r"\text{for} \quad k=2: \qquad", r"p_2^\ast", r"=", r"\left(m_2 - 1\right)", r"\left(p_1^\ast + \frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2}{\left|\hat{h_2}\right|^2}\right)").scale(0.8)
        p_3 = MathTex(r"\text{for} \quad k=3: \qquad", r"p_3^\ast", r"=", r"\left(m_3 - 1\right)", r"\Bigg(", r"p_1^\ast", r"+", r"p_2^\ast", r"+", r"\frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2}{\left|\hat{h_3}\right|^2}", r"\Bigg)").scale(0.8).next_to(p_2, DOWN, buff=0.5)

        VGroup(p_2, p_3).move_to((0,0,0))

        self.play(Write(p_2), run_func=smooth)
        self.play(Write(p_3), run_func=smooth)
        self.wait(0.5)
        
        self.play(AnimationGroup(
            FadeOut(p_2),
            p_3.animate.move_to((0,0,0))
        ))
        self.wait(0.5)

        p_3_clear = MathTex(r"p_3^\ast", r"=", r"\left(m_3 - 1\right)", r"\Bigg(", r"p_1^\ast", r"+", r"p_2^\ast", r"+", r"\frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2}{\left|\hat{h_3}\right|^2}", r"\Bigg)").scale(0.8)
        self.play(TransformMatchingTex(p_3, p_3_clear), run_func= smooth)
        self.wait(0.5)

        brace = Brace(p_3_clear[6], direction=DOWN)
        brace_text = brace.get_tex(r"P - p_1^\ast - p_3^\ast").scale(0.8)
        self.play(AnimationGroup(GrowFromCenter(brace), Write(brace_text), lag_ratio= 0.55))
        self.wait(0.5)

        p_3_with_sum = MathTex(r"p_3^\ast", r"=", r"\left(m_3 - 1\right)", r"\Bigg(", r"p_1^\ast", r"+", r"P", r"-", r"p_1^\ast", r"-", r"p_3^\ast", r"+", r"\frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2}{\left|\hat{h_3}\right|^2}", r"\Bigg)").scale(0.8)

        self.play(FadeOut(brace), run_time=0.5)
        self.play(AnimationGroup(FadeOut(brace_text, shift=UP),
                                TransformMatchingTex(p_3_clear, p_3_with_sum),
                                run_func= smooth,
                                lag_ratio= 0.15))
        self.wait(0.5)

        p_3_ff = MathTex(r"p_3^\ast", r"=", r"\left(m_3 - 1\right)", r"\Bigg(", r"P", r"-", r"p_3^\ast", r"+", r"\frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2}{\left|\hat{h_3}\right|^2}", r"\Bigg)").scale(0.8)
        self.play(TransformMatchingTex(p_3_with_sum, p_3_ff), run_func= smooth)
        self.wait(0.5)

        p_3_prod = MathTex(r"p_3^\ast", r"=", r"\left(m_3 - 1\right)", r"P", r"-", r"\left(m_3 - 1\right)", r"p_3^\ast", r"+", r"\left(m_3 - 1\right)", r"\Bigg(", r"\frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2 }{ \left| \hat{h_3} \right| ^2 }", r"\Bigg)").scale(0.8)
        self.play(TransformMatchingTex(p_3_ff, p_3_prod), run_func= smooth)
        self.wait(0.5)
        
        p_3_in_one_term = MathTex(r"p_3^\ast", r"+", r"\left(m_3 - 1\right)", r"p_3^\ast", r"=", r"\left(m_3 - 1\right)", r"P", r"+", r"\left(m_3 - 1\right)", r"\Bigg(", r"\frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2 }{ \left| \hat{h_3} \right| ^2 }", r"\Bigg)").scale(0.8)
        self.play(TransformMatchingTex(p_3_prod, p_3_in_one_term), run_func= smooth)
        self.wait(0.5)

        m_3_p_3 = MathTex(r"m_3", r"p_3^\ast" r"=", r"\left(m_3 - 1\right)", r"P", r"+", r"\left(m_3 - 1\right)", r"\Bigg(", r"\frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2 }{ \left| \hat{h_3} \right| ^2 }", r"\Bigg)").scale(0.8)
        self.play(TransformMatchingTex(p_3_in_one_term, m_3_p_3), run_func= smooth)
        self.wait(0.5)

        p_3_final_form = MathTex(r"p_3^\ast" r"=", r"\frac{\left(m_3 - 1\right)}{m_3}", r"P", r"+", r"\frac{\left(m_3 - 1\right)}{m_3}", r"\Bigg(", r"\frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2 }{ \left| \hat{h_3} \right| ^2 }", r"\Bigg)").scale(0.8)
        self.play(TransformMatchingTex(m_3_p_3, p_3_final_form), run_func= smooth)
        self.wait(0.5)

        p_2 = MathTex(r"p_2^\ast", r"=", r"\left(m_2 - 1\right)", r"\Bigg(", r"p_1^\ast", r"+", r"\frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2}{\left|\hat{h_2}\right|^2}", r"\Bigg)").scale(0.8)
        
        self.play(AnimationGroup(
            FadeIn(p_2),
            p_2.animate.shift(1.2*UP),
            p_3_final_form.animate.shift(1.2*DOWN)
        ), run_func= smooth)
        self.wait(1)

        self.play(AnimationGroup(
            FadeOut(p_3_final_form),
            p_2.animate.move_to((0,0,0))
        ))
        self.wait(0.5)

        brace = Brace(p_3_clear[5], direction=DOWN)
        brace_text = brace.get_tex(r"P - p_2^\ast - p_3^\ast").scale(0.8)
        self.play(AnimationGroup(GrowFromCenter(brace), Write(brace_text), lag_ratio= 0.55))
        self.wait(0.5)

        p_2_with_sum = MathTex(r"p_2^\ast", r"=", r"\left(m_2 - 1\right)", r"\Bigg(", r"P", r"-", r"p_2^\ast", r"-", r"p_3^\ast", r"+", r"\frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2}{\left|\hat{h_2}\right|^2}", r"\Bigg)").scale(0.8)
        
        self.play(FadeOut(brace), run_time=0.5)
        self.play(AnimationGroup(FadeOut(brace_text, shift=UP),
                                TransformMatchingTex(p_2, p_2_with_sum),
                                run_func= smooth,
                                lag_ratio= 0.15))
        self.wait(0.5)

        p_2_prod = MathTex(r"p_2^\ast", r"=", r"\left(m_2 - 1\right)", r"P", r"-", r"\left(m_2 - 1\right)", r"p_2^\ast", r"-", r"\left(m_2 - 1\right)", r"p_3^\ast", r"+", r"\left(m_2 - 1\right)", r"\Bigg(", r"\frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2}{\left|\hat{h_2}\right|^2}", r"\Bigg)").scale(0.8)
        self.play(TransformMatchingTex(p_2_with_sum, p_2_prod), run_func= smooth)
        self.wait(0.5)

        p_2_in_one_term = MathTex(r"p_2^\ast", r"+", r"\left(m_2 - 1\right)", r"p_2^\ast", r"=", r"\left(m_2 - 1\right)", r"P", r"-", r"\left(m_2 - 1\right)", r"p_3^\ast", r"+", r"\left(m_2 - 1\right)", r"\Bigg(", r"\frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2}{\left|\hat{h_2}\right|^2}", r"\Bigg)").scale(0.8)
        self.play(TransformMatchingTex(p_2_prod, p_2_in_one_term), run_func= smooth)
        self.wait(0.5)

        p_2_temp_ff = MathTex(r"m_2", r"p_2^\ast", r"=", r"\left(m_2 - 1\right)", r"P", r"-", r"\left(m_2 - 1\right)", r"p_3^\ast", r"+", r"\left(m_2 - 1\right)", r"\Bigg(", r"\frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2}{\left|\hat{h_2}\right|^2}", r"\Bigg)").scale(0.8)
        self.play(TransformMatchingTex(p_2_in_one_term, p_2_temp_ff), run_func= smooth)
        self.wait(0.5)

        p_2_ff = MathTex(r"p_2^\ast", r"=", r"\left(\frac{m_2 - 1}{m_2}\right)", r"P", r"-", r"\left(\frac{m_2 - 1}{m_2}\right)", r"p_3^\ast", r"+", r"\left(\frac{m_2 - 1}{m_2}\right)", r"\Bigg(", r"\frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2}{\left|\hat{h_2}\right|^2}", r"\Bigg)").scale(0.8)
        self.play(TransformMatchingTex(p_2_temp_ff, p_2_ff), run_func= smooth)
        self.wait(0.5)

        p_2_sub_for_p3 = MathTex(r"p_2^\ast", r"=", r"\left(\frac{m_2 - 1}{m_2}\right)", r"P", r"\\", r"-", r"\left(\frac{m_2 - 1}{m_2}\right)",  r"\Bigg[", r"\frac{\left(m_3 - 1\right)}{m_3}", r"P", r"+", r"\frac{\left(m_3 - 1\right)}{m_3}", r"\Bigg(", r"\frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2 }{ \left| \hat{h_3} \right| ^2 }", r"\Bigg)", r"\Bigg]", r"\\", r"+", r"\left(\frac{m_2 - 1}{m_2}\right)", r"\Bigg(", r"\frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2}{\left|\hat{h_2}\right|^2}", r"\Bigg)").scale(0.8)
        self.play(TransformMatchingTex(p_2_ff, p_2_sub_for_p3), run_func= smooth)
        self.wait(0.5)

        p_2_before_clean_up = MathTex(r"p_2^\ast",
                               r"=",
                               r"\left(\frac{m_2 - 1}{m_2}\right)",
                               r"P", 
                               r"+",
                               r"\left(\frac{(m_2 - 1)(m_3 - 1)}{m_2 m_3}\right)",
                               r"P",
                               r"\\",
                               r"-",
                               r"\left(\frac{(m_2 - 1)(m_3 - 1)}{m_2 m_3}\right)",
                               r"\Bigg(",
                               r"\frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2 }{ \left| \hat{h_3} \right| ^2 }",
                               r"\Bigg)",
                               r"\\",
                               r"+",
                               r"\left(\frac{m_2 - 1}{m_2}\right)",
                               r"\Bigg(",
                               r"\frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2}{\left|\hat{h_2}\right|^2}",
                               r"\Bigg)").scale(0.8)
        
        self.play(TransformMatchingTex(p_2_sub_for_p3, p_2_before_clean_up), run_func= smooth)
        self.wait(0.5)

        p_2_after_clean_up = MathTex(r"p_2^\ast",
                               r"=",
                               r"\left(\frac{m_2 m_3( m_2 -1 ) - m_2 (m_2 -1) (m_3 - 1)}{m_2^2 m_3}\right)",
                               r"P",
                               r"\\",
                               r"-",
                               r"\left(\frac{(m_2 - 1)(m_3 - 1)}{m_2 m_3}\right)",
                               r"\Bigg(",
                               r"\frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2 }{ \left| \hat{h_3} \right| ^2 }",
                               r"\Bigg)",
                               r"\\",
                               r"+",
                               r"\left(\frac{m_2 - 1}{m_2}\right)",
                               r"\Bigg(",
                               r"\frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2}{\left|\hat{h_2}\right|^2}",
                               r"\Bigg)").scale(0.8)
        
        self.play(TransformMatchingTex(p_2_before_clean_up, p_2_after_clean_up), run_func= smooth)
        self.wait(0.5)

        p_2_temp_final_form = MathTex(r"p_2^\ast",
                               r"=",
                               r"\left(\frac{m_2^2 - m_2}{m_2^2 m_3}\right)",
                               r"P",
                               r"\\",
                               r"-",
                               r"\left(\frac{(m_2 - 1)(m_3 - 1)}{m_2 m_3}\right)",
                               r"\Bigg(",
                               r"\frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2 }{ \left| \hat{h_3} \right| ^2 }",
                               r"\Bigg)",
                               r"\\",
                               r"+",
                               r"\left(\frac{m_2 - 1}{m_2}\right)",
                               r"\Bigg(",
                               r"\frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2}{\left|\hat{h_2}\right|^2}",
                               r"\Bigg)").scale(0.8)
        
        self.play(TransformMatchingTex(p_2_after_clean_up, p_2_temp_final_form), run_func= smooth)
        self.wait(0.5)

        p_2_temp_f_final_form = MathTex(r"p_2^\ast",
                               r"=",
                               r"\left(\frac{m_2(m_2 - 1)}{m_2^2 m_3}\right)",
                               r"P",
                               r"\\",
                               r"-",
                               r"\left(\frac{(m_2 - 1)(m_3 - 1)}{m_2 m_3}\right)",
                               r"\Bigg(",
                               r"\frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2 }{ \left| \hat{h_3} \right| ^2 }",
                               r"\Bigg)",
                               r"\\",
                               r"+",
                               r"\left(\frac{m_2 - 1}{m_2}\right)",
                               r"\Bigg(",
                               r"\frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2}{\left|\hat{h_2}\right|^2}",
                               r"\Bigg)").scale(0.8)
        
        self.play(TransformMatchingTex(p_2_temp_final_form, p_2_temp_f_final_form), run_func= smooth)
        self.wait(0.5)

        p_2_final_form = MathTex(r"p_2^\ast",
                               r"=",
                               r"\left(\frac{m_2 - 1}{m_2 m_3}\right)",
                               r"P",
                               r"\\",
                               r"-",
                               r"\left(\frac{(m_2 - 1)(m_3 - 1)}{m_2 m_3}\right)",
                               r"\Bigg(",
                               r"\frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2 }{ \left| \hat{h_3} \right| ^2 }",
                               r"\Bigg)",
                               r"\\",
                               r"+",
                               r"\left(\frac{m_2 - 1}{m_2}\right)",
                               r"\Bigg(",
                               r"\frac{P \sigma_\epsilon^2 + W_{tot} \sigma^2}{\left|\hat{h_2}\right|^2}",
                               r"\Bigg)").scale(0.8)
        
        self.play(TransformMatchingTex(p_2_temp_f_final_form, p_2_final_form), run_func= smooth)
        self.wait(0.5)

        p_1_final_form = MathTex(r"p_1^\ast = P - p_2^\ast - p_3^\ast")

        self.play(AnimationGroup(
            FadeIn(p_3_final_form),
            p_3_final_form.animate.shift(1.7*DOWN),
            FadeIn(p_1_final_form),
            p_1_final_form.scale(0.8).animate.shift(2.7*UP)
        ), run_func= smooth)
        self.wait(1)

        self.play(FadeOut(p_3_final_form, p_2_final_form, p_1_final_form), run_func= smooth)

class CVXTrials(Scene):
    def construct(self):
        title = Tex("Trial 1")
        trial1 = Tex("Charnes-Cooper Transformation", color= GOLD).next_to(title, DOWN)

        VGroup(title, trial1).move_to((0,0,0))

        self.play(AnimationGroup(
            FadeIn(title, run_func= smooth),
            title.animate.scale(1.5)
        ))

        self.play(Write(trial1), run_func= smooth)

        self.wait(0.5)
        self.play(FadeOut(title), run_func= smooth)

        self.play(trial1.animate.shift(3.3*UP))

        old_opt_problem = MathTex(r"\text{maximize}\quad \frac{c^Tx+\alpha}{d^Tx+\beta}").scale(0.8)
        old_constraints = MathTex(r"\text{s.t.}\quad Ax\leq b").next_to(old_opt_problem, DOWN).align_to(old_opt_problem, LEFT).scale(0.8)

        old_prob = VGroup(old_opt_problem, old_constraints).move_to((0,0,0))
        arrow = MathTex(r"\rightarrow")

        new_opt_problem = MathTex(r"\text{maximize}\quad c^Ty+\alpha t").scale(0.8)
        new_constraint = MathTex(r"\text{s.t.}", r"\quad Ay\leq bt").next_to(new_opt_problem, DOWN).align_to(new_opt_problem, LEFT).scale(0.8)
        new_constraint2 = MathTex(r"\quad d^T y + \beta t= 1").next_to(new_constraint, DOWN).scale(0.8).align_to(new_constraint[1], LEFT)
        new_constraint3 = MathTex(r"\quad t \geq 0").next_to(new_constraint2, DOWN).scale(0.8).align_to(new_constraint[1], LEFT)

        new_prob = VGroup(new_opt_problem, new_constraint, new_constraint2, new_constraint3).move_to((0,0,0))

        self.play(AnimationGroup(
            Write(old_opt_problem),
            Write(old_constraints)
        ))
        self.wait(0.5)

        self.play(AnimationGroup(
            old_prob.animate.shift(2.5*LEFT),
            FadeIn(arrow),
            FadeIn(new_prob),
            new_prob.animate.shift(2.5*RIGHT)
        ))

        self.wait(1)

        self.play(FadeOut(trial1, arrow, old_prob, new_prob))
        self.wait(0.5)

        title2 = Tex("Trial 2")
        trial2 = Tex("Introduce New Variable", color= GOLD).next_to(title, DOWN, buff=0.5)

        VGroup(title2, trial2).move_to((0,0,0))

        self.play(AnimationGroup(
            FadeIn(title2, run_func= smooth),
            title2.animate.scale(1.5)
        ))

        self.play(Write(trial2), run_func= smooth)

        self.wait(0.5)
        self.play(FadeOut(title2), run_func= smooth)

        self.play(trial2.animate.shift(3.3*UP))
        self.wait(0.5)

        problem = MathTex(r"\max_{p_1, p_2,...,p_M}",
                          r"\sum_{k=1}^{M}",
                          r"\log_2",
                          r"\Bigg(",
                          r"1",
                          r"+",
                          r"\frac{p_k\left|{\hat{h}_k}\right|^2}{\left|{\hat{h}_k}\right|^2\sum_{j=1}^{k-1}p_j + C}",
                          r"\Bigg)").scale(0.8)
        
        self.play(Write(problem), run_func= smooth)
        self.wait(0.5)
        
        brace = Brace(problem[6], direction=DOWN)
        brace_text = brace.get_tex(r"SINR_k")

        self.play(AnimationGroup(GrowFromCenter(brace), Write(brace_text), lag_ratio= 0.55))
        self.wait(0.5)

        problem_sinr = MathTex(r"\max_{SINR_1, ...,SINR_M}",
                          r"\sum_{k=1}^{M}",
                          r"\log_2",
                          r"\Bigg(",
                          r"1",
                          r"+",
                          r"SINR_k",
                          r"\Bigg)").scale(0.8)
        
        self.play(FadeOut(brace), run_time=0.5)
        self.play(AnimationGroup(FadeOut(brace_text, shift=UP),
                                TransformMatchingTex(problem, problem_sinr),
                                run_func= smooth,
                                lag_ratio= 0.28))
        self.wait(0.5)

        sinr_to_p = MathTex(r"SINR_k = \frac{p_k\left|{\hat{h}_k}\right|^2}{\left|{\hat{h}_k}\right|^2\sum_{j=1}^{k-1}p_j+ C}").scale(0.8)
        p_to_sinr = MathTex(r"p_k = SINR_k \left( \sum_{j=1}^{k-1} p_j + \frac{C}{\left|{\hat{h}_k}\right|^2} \right)").scale(0.8)

        self.play(problem_sinr.animate.shift(1.7*UP))
        self.wait(0.1)
        self.play(Write(sinr_to_p))
        self.wait(0.5)
        self.play(ReplacementTransform(sinr_to_p, p_to_sinr), run_func= smooth)
        self.wait(0.5)
        
        c1 = MathTex(r"C1:\quad \sum_{k=1}^{M}", r"p_k", r"\leq P.").scale(0.8).shift(2*DOWN)

        self.play(Write(c1))
        self.wait(0.5)

        c1_pk = MathTex(r"C1:\quad \sum_{k=1}^{M}",
                        r"SINR_k \left( \sum_{j=1}^{k-1} p_j + \frac{C}{\left|{\hat{h}_k}\right|^2} \right)",
                        r"\leq P.").scale(0.8).shift(2*DOWN)
        
        self.play(TransformMatchingTex(c1, c1_pk), run_func=smooth)

        self.play(AnimationGroup(
            problem_sinr.animate.shift(0.4*DOWN),
            c1_pk.animate.shift(0.7*UP),
            FadeOut(p_to_sinr)
        ))
        self.wait(0.5)

        c1_sinr = MathTex(r"\sum_{i=2}^{M} SINR_i \left( \frac{C}{\left|{\hat{h}_i}\right|^2} \right) + SINR_M \sum_{j=1}^{M-1} SINR_j \left( \frac{C}{\left|{\hat{h}_j}\right|^2} \right) + \left( \frac{C}{\left|{\hat{h}_1}\right|^2} \right) \sum_{k=1}^{M} \prod_{l=1}^{k-1} SINR_l",
                        r"\leq P.").scale(0.8).shift(1.3*DOWN)
        
        self.play(TransformMatchingTex(c1_pk, c1_sinr), run_func= smooth)
        self.play(c1_sinr.animate.scale(0.8))
        self.wait(0.5)

        self.play(FadeOut(trial2, problem_sinr, c1_sinr))
        self.wait(1)

        title21 = Tex("Trial 2.1")
        trial21 = Tex("Use Built-in Functions", color= GOLD).next_to(title, DOWN, buff=0.5)

        VGroup(title21, trial21).move_to((0,0,0))

        self.play(AnimationGroup(
            FadeIn(title21, run_func= smooth),
            title21.animate.scale(1.5)
        ))

        self.play(Write(trial21), run_func= smooth)

        self.wait(0.5)
        self.play(FadeOut(title21), run_func= smooth)

        self.play(trial21.animate.shift(3.3*UP))
        self.wait(0.5)

        constraint_prob = MathTex(r"\sum_{i=2}^{M} SINR_i \left( \frac{C}{\left|{\hat{h}_i}\right|^2} \right) + SINR_M \sum_{j=1}^{M-1} SINR_j \left( \frac{C}{\left|{\hat{h}_j}\right|^2} \right) + \left( \frac{C}{\left|{\hat{h}_1}\right|^2} \right) \sum_{k=1}^{M} \prod_{l=1}^{k-1} SINR_l",
                        r"\leq P.").scale(0.64)
        self.play(FadeIn(constraint_prob), run_time= 0.65)
        self.wait(0.5)

        hardcoded_cons = MathTex(r"SINR_1 \left( \frac{C}{\left|{\hat{h}_1}\right|^2} \right) + SINR_2 \left( \frac{C}{\left|{\hat{h}_2}\right|^2} \right) + SINR_3 \left( \frac{C}{\left|{\hat{h}_3}\right|^2} \right) \\ + SINR_3 SINR_2 \left( \frac{C}{\left|{\hat{h}_2}\right|^2} \right) + SINR_3 SINR_1 \left( \frac{C}{\left|{\hat{h}_1}\right|^2} \right) + SINR_2 SINR_1 \left( \frac{C}{\left|{\hat{h}_1}\right|^2} \right) \\ + SINR_3 SINR_2 SINR_1 \left( \frac{C}{\left|{\hat{h}_1}\right|^2} \right)",
                        r"\leq P.").scale(0.64)
        
        self.play(ReplacementTransform(constraint_prob, hardcoded_cons))
        self.wait(0.5)

        replaced_cons_with_y = MathTex(r"SINR_1 \left( \frac{C}{\left|{\hat{h}_1}\right|^2} \right) + SINR_2 \left( \frac{C}{\left|{\hat{h}_2}\right|^2} \right) + SINR_3 \left( \frac{C}{\left|{\hat{h}_3}\right|^2} \right) \\ + y_1 \left( \frac{C}{\left|{\hat{h}_2}\right|^2} \right) + y_2 \left( \frac{C}{\left|{\hat{h}_1}\right|^2} \right) + y_3 \left( \frac{C}{\left|{\hat{h}_1}\right|^2} \right) \\ + y_4 \left( \frac{C}{\left|{\hat{h}_1}\right|^2} \right)",
                        r"\leq P.").scale(0.64)
        
        self.play(TransformMatchingTex( hardcoded_cons, replaced_cons_with_y ))
        self.wait(0.5)

        self.play(FadeOut(replaced_cons_with_y))
        self.wait(0.5)

        y1 = MathTex(r"y_1")
        y2 = MathTex(r"y_2").next_to(y1, DOWN, buff=0.7)
        y3 = MathTex(r"y_3").next_to(y2, DOWN, buff=0.7)
        y4 = MathTex(r"y_4").next_to(y3, DOWN, buff=0.7)

        Y = VGroup(y1, y2, y3, y4).move_to((0,0,0))
        self.play(Write(Y), run_func= smooth)
        self.wait(0.5)

        y1_eq = MathTex(r"y_1", r"=", r"SINR_3 SINR_2")
        y2_eq = MathTex(r"y_2", r"=", r"SINR_3 SINR_1").next_to(y1_eq, DOWN, buff=0.7)
        y3_eq = MathTex(r"y_3", r"=", r"SINR_2 SINR_1").next_to(y2_eq, DOWN, buff=0.7)
        y4_eq = MathTex(r"y_4", r"=", r"SINR_3 SINR_2 SINR_1").next_to(y3_eq, DOWN, buff=0.7)

        Y_eq = Y = VGroup(y1_eq, y2_eq, y3_eq, y4_eq).move_to((0,0,0))

        self.play(AnimationGroup(
            TransformMatchingTex(y1, y1_eq, run_func= smooth),
            TransformMatchingTex(y2, y2_eq, run_func= smooth),
            TransformMatchingTex(y3, y3_eq, run_func= smooth),
            TransformMatchingTex(y4, y4_eq, run_func= smooth)
        ))
        self.wait(1)

        self.play(FadeOut(y1_eq, y2_eq, y3_eq, y4_eq))

        conc = Tex(r"So far, the problem has ", r"no solution", r" using CVX!").scale(0.8)
        conc.set_color_by_tex("no solution", RED)

        self.play(Write(conc))
        self.wait(0.5)
        self.play(FadeOut(conc, trial21))

class ThankYou(Scene):
    def construct(self):
        thank_you = Tex(r"Thank You!", color=GOLD_B).scale(1.5)

        self.play(Write(thank_you))
        self.wait(1)