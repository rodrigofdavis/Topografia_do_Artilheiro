from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.factory import Factory
from math import atan
from math import degrees

class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    def btn(self):
        show_popup()

    def btn2(self):
        show_popup2()

    def btn3(self):
        show_popup3()

class P(FloatLayout):
    pass

class Q(FloatLayout):
    pass

class R(FloatLayout):
    pass

def show_popup():
    show = P()

    popupWindow = Popup(title='Aviso!', content=show, size_hint=(None,None), size=(400,400), auto_dismiss=True)

    popupWindow.open()

def show_popup2():
    show = Q()

    popupWindow = Popup(title='Aviso!', content=show, size_hint=(None,None), size=(400,400), auto_dismiss=True)

    popupWindow.open()

def show_popup3():
    show = R()

    popupWindow = Popup(title='Aviso!', content=show, size_hint=(None,None), size=(400,400), auto_dismiss=True)

    popupWindow.open()

class Distancia(Screen):

    def soma(self):
        Ea = float(self.ids.Ea.text)
        Na = float(self.ids.Na.text)
        Eb = float(self.ids.Eb.text)
        Nb = float(self.ids.Nb.text)
        a = (Eb - Ea) ** 2
        b = (Nb - Na) ** 2
        c = a + b
        dist = int(c ** (1 / 2))
        self.ids.apertado.text = 'A distância na carta é de: {} metros'.format('%.2f' % dist)

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

class Angulo(Screen):
    def calc_qm_sim(self):
        Ea = float(self.ids.Ea.text)
        Na = float(self.ids.Na.text)
        Eb = float(self.ids.Eb.text)
        Nb = float(self.ids.Nb.text)
        a_carta = int(self.ids.input0.text)
        a_atual = int(self.ids.input1.text)
        dmg = float(self.ids.input2.text)
        dmm = float(self.ids.input3.text)/60
        dms = float(self.ids.input4.text)/3600
        dmag = abs(float(self.ids.input5.text))
        dmam = abs(float(self.ids.input6.text)/60)
        dmas = abs(float(self.ids.input7.text)/3600)
        conv_g = abs(float(self.ids.input8.text))
        conv_m = abs(float(self.ids.input9.text)/60)
        conv_s = abs(float(self.ids.input10.text)/3600)

        dif_ano = a_atual - a_carta

        # graus total da declinação magnética anual:
        dmi = dmg + dmm + dms

        # graus total da declinação magnética no ano de confecção da carta
        dma = dmag + dmam + dmas

        # dm0 é a variação da declinação anual desde a confecção da carta
        dm0 = dmi * dif_ano
        # soma da declinação magnética da carta com a declinação anual
        decl_mag = dm0 + dma

        # convergência de meridianos

        conv_mer = conv_g + conv_m + conv_s


        qm_sim = decl_mag - conv_mer


        dE = Eb - Ea
        dN = Nb - Na
        if Nb == Na:
            self.ids.resultado.text = 'Divisão por zero não existe'
        else:
            tang = dE / dN
            a_grau = degrees(atan(tang))
            a_grau_2e3Q = a_grau + 180
            a_grau_4Q = a_grau + 360
            if dN == 0:
                self.ids.resultado.text = '1º Quadrante \n dE =  {} e dN = {} \n Ângulo QM = {} \n O Lançamento de AB é em graus {}º \n O lançamento de AB em milésimos é {} milésimos'.format(
                    dE, dN, '%.2f' % qm_sim, '%.2f' % a_grau, '%.2f' % ((a_grau * 160) / 9))
            if dE >= 0 and dN >= 0:
                self.ids.resultado.text = '1º Quadrante \n dE =  {} e dN = {} \n Ângulo QM = {} \n O Lançamento de AB é em graus {}º \n O lançamento de AB em milésimos é {} milésimos'.format(
                    dE, dN, '%.2f' % qm_sim,  '%.2f' % a_grau, '%.2f' % ((a_grau * 160) / 9))
            if dE > 0 and dN < 0:
                self.ids.resultado.text = '2º Quadrante \n dE =  {} e dN = {} \n Ângulo QM = {} \n O Lançamento de AB é em graus {}º \n O lançamento de AB em milésimos é {} milésimos'.format(
                    dE, dN, '%.2f' % qm_sim, '%.2f' % a_grau_2e3Q, '%.2f' % (((a_grau_2e3Q) * 160) / 9))
            if dE < 0 and dN < 0:
                self.ids.resultado.text = '3º Quadrante \n dE =  {} e dN = {} \n Ângulo QM = {} \n O Lançamento de AB é em graus {}º \n O lançamento de AB em milésimos é {} milésimos'.format(
                    dE, dN, '%.2f' % qm_sim, '%.2f' % a_grau_2e3Q, '%.2f' % (((a_grau_2e3Q) * 160) / 9))
            if dE < 0 and dN > 0:
                self.ids.resultado.text = '4º Quadrante \n dE =  {} e dN = {} \n Ângulo QM = {} \n O Lançamento de AB é em graus {}º \n O lançamento de AB em milésimos é {} milésimos'.format(
                    dE, dN, '%.2f' % qm_sim, '%.2f' % a_grau_4Q, '%.2f' % (((a_grau_4Q) * 160) / 9))



    def calc_qm_nao(self):
        Ea = float(self.ids.Ea.text)
        Na = float(self.ids.Na.text)
        Eb = float(self.ids.Eb.text)
        Nb = float(self.ids.Nb.text)
        a_carta = int(self.ids.input0.text)
        a_atual = int(self.ids.input1.text)
        dmg = float(self.ids.input2.text)
        dmm = float(self.ids.input3.text) / 60
        dms = float(self.ids.input4.text) / 3600
        dmag = abs(float(self.ids.input5.text))
        dmam = abs(float(self.ids.input6.text) / 60)
        dmas = abs(float(self.ids.input7.text) / 3600)
        conv_g = abs(float(self.ids.input8.text))
        conv_m = abs(float(self.ids.input9.text) / 60)
        conv_s = abs(float(self.ids.input10.text) / 3600)

        dif_ano = a_atual - a_carta

        # graus total da declinação magnética anual:
        dmi = dmg + dmm + dms

        # graus total da declinação magnética no ano de confecção da carta
        dma = dmag + dmam + dmas

        # dm0 é a variação da declinação anual desde a confecção da carta
        dm0 = dmi * dif_ano
        # soma da declinação magnética da carta com a declinação anual
        decl_mag = dm0 + dma

        # convergência de meridianos

        conv_mer = conv_g + conv_m + conv_s

        qm_nao = decl_mag + conv_mer

        dE = Eb - Ea
        dN = Nb - Na
        if Nb == Na:
            self.ids.resultado.text = 'Divisão por zero não existe'
        else:
            tang = dE / dN
            a_grau = degrees(atan(tang))
            a_grau_2e3Q = a_grau + 180
            a_grau_4Q = a_grau + 360
            if dN == 0:
                self.ids.resultado.text = '1º Quadrante \n dE =  {} e dN = {} \n Ângulo QM = {} \n O Lançamento de AB é em graus {}º \n O lançamento de AB em milésimos é {} milésimos'.format(
                    dE, dN, '%.2f' % qm_nao, '%.2f' % a_grau, '%.2f' % ((a_grau * 160) / 9))
            if dE >= 0 and dN >= 0:
                self.ids.resultado.text = '1º Quadrante \n dE =  {} e dN = {} \n Ângulo QM = {} \n O Lançamento de AB é em graus {}º \n O lançamento de AB em milésimos é {} milésimos'.format(
                    dE, dN, '%.2f' % qm_nao, '%.2f' % a_grau, '%.2f' % ((a_grau * 160) / 9))
            if dE > 0 and dN < 0:
                self.ids.resultado.text = '2º Quadrante \n dE =  {} e dN = {} \n Ângulo QM = {} \n O Lançamento de AB é em graus {}º \n O lançamento de AB em milésimos é {} milésimos'.format(
                    dE, dN, '%.2f' % qm_nao, '%.2f' % a_grau_2e3Q, '%.2f' % (((a_grau_2e3Q) * 160) / 9))
            if dE < 0 and dN < 0:
                self.ids.resultado.text = '3º Quadrante \n dE =  {} e dN = {} \n Ângulo QM = {} \n O Lançamento de AB é em graus {}º \n O lançamento de AB em milésimos é {} milésimos'.format(
                    dE, dN, '%.2f' % qm_nao, '%.2f' % a_grau_2e3Q, '%.2f' % (((a_grau_2e3Q) * 160) / 9))
            if dE < 0 and dN > 0:
                self.ids.resultado.text = '4º Quadrante \n dE =  {} e dN = {} \n Ângulo QM = {} \n O Lançamento de AB é em graus {}º \n O lançamento de AB em milésimos é {} milésimos'.format(
                    dE, dN, '%.2f' % qm_nao, '%.2f' % a_grau_4Q, '%.2f' % (((a_grau_4Q) * 160) / 9))


    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

class Lancamento(Screen):
    def calc_ang(self):
        Ea = float(self.ids.Ea.text)
        Na = float(self.ids.Na.text)
        Eb = float(self.ids.Eb.text)
        Nb = float(self.ids.Nb.text)
        dE = Eb - Ea
        dN = Nb - Na
        if Nb == Na:
            self.ids.resultado.text = 'Divisão por zero não existe'
        else:
            tang = dE / dN
            a_grau = degrees(atan(tang))
            a_grau_2e3Q = a_grau + 180
            a_grau_4Q = a_grau + 360
            if dN == 0:
                self.ids.resultado.text = '1º Quadrante \n dE =  {} e dN = {} \n O Lançamento de AB é em graus {}º \n O lançamento de AB em milésimos é {} milésimos'.format(dE, dN, '%.2f' % a_grau, '%.2f' % ((a_grau * 160) / 9))
            if dE >= 0 and dN >= 0:
                self.ids.resultado.text = '1º Quadrante \n dE =  {} e dN = {} \n O Lançamento de AB é em graus {}º \n O lançamento de AB em milésimos é {} milésimos'.format(dE, dN, '%.2f' % a_grau, '%.2f' % ((a_grau * 160) / 9))
            if dE > 0 and dN < 0:
                self.ids.resultado.text = '2º Quadrante \n dE =  {} e dN = {} \n O Lançamento de AB é em graus {}º \n O lançamento de AB em milésimos é {} milésimos'.format(dE, dN, '%.2f' % a_grau_2e3Q, '%.2f' % (((a_grau_2e3Q) * 160) / 9))
            if dE < 0 and dN < 0:
                self.ids.resultado.text = '3º Quadrante \n dE =  {} e dN = {} \n O Lançamento de AB é em graus {}º \n O lançamento de AB em milésimos é {} milésimos'.format(dE, dN,'%.2f' %  a_grau_2e3Q, '%.2f' % (((a_grau_2e3Q) * 160) / 9))
            if dE < 0 and dN > 0:
                self.ids.resultado.text = '4º Quadrante \n dE =  {} e dN = {} \n O Lançamento de AB é em graus {}º \n O lançamento de AB em milésimos é {} milésimos'.format(dE, dN, '%.2f' % a_grau_4Q, '%.2f' % (((a_grau_4Q)*160)/9))

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)




class MyApp(App):
    def build(self):
        Builder.load_string(open('Test.kv', encoding='utf-8').read(), rulesonly=True)
        return Gerenciador()



if __name__ == '__main__':
    MyApp().run()