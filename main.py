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
from kivy.properties import BooleanProperty
from kivy.properties import ObjectProperty
import locale
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

    def btn4(self):
        show_popup4()

class P(FloatLayout):
    pass

class Q(FloatLayout):
    pass

class R(FloatLayout):
    pass

class S(FloatLayout):
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

def show_popup4():
    show = S()
    popupWindow = Popup(title='Aviso!', content=show, size_hint=(None,None), size=(400,400), auto_dismiss=True)
    popupWindow.open()

class Distancia(Screen):

    def calcular_distancia(self):
        xa = float(self.ids.input1.text)
        ya = float(self.ids.input2.text)
        xb = float(self.ids.input3.text)
        yb = float(self.ids.input4.text)
        a = (xb - xa) ** 2
        b = (yb - ya) ** 2
        c = a + b
        dist = float(c ** (1 / 2))
        self.ids.apertado.text = 'A distância na carta é de: {} metros'.format('%.3f' % dist)

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

class Angulo(Screen):
    a_carta = ObjectProperty(None)
    a_atual = ObjectProperty(None)
    dmg = ObjectProperty(None)
    dmm = ObjectProperty(None)
    dms = ObjectProperty(None)
    dmag = ObjectProperty(None)
    dmam = ObjectProperty(None)
    dmas = ObjectProperty(None)
    conv_g = ObjectProperty(None)
    conv_m = ObjectProperty(None)
    conv_s = ObjectProperty(None)
    resultado = ObjectProperty(None)
    t_bold = BooleanProperty(False)
    t2_bold = BooleanProperty(False)

    def virgula_p_float(self, m):
        locale.setlocale(locale.LC_ALL, "")
        n = locale.atof(m)
        return n

    def dmi_func(self):
        if self.t2_bold == False:
            dmi = self.virgula_p_float(self.dmg.text) + self.virgula_p_float(self.dmm.text) / 60 + self.virgula_p_float(
                self.dms.text) / 3600
        if self.t2_bold == True:
            dmi = (-1) * (self.virgula_p_float(self.dmg.text) + self.virgula_p_float(
                self.dmm.text) / 60 + self.virgula_p_float(self.dms.text) / 3600)
        return dmi

    def decl_mag(self):
        dif_ano = int(self.a_atual.text) - int(self.a_carta.text)
        # graus total da declinação magnética no ano de confecção da carta
        dma = self.virgula_p_float(self.dmag.text) + self.virgula_p_float(self.dmam.text) / 60 + self.virgula_p_float(
            self.dmas.text) / 3600
        # dm0 é a variação da declinação anual desde a confecção da carta
        dm0 = self.dmi_func() * dif_ano
        # soma da declinação magnética da carta com a declinação anual
        decl_mag = dm0 + dma
        return decl_mag

    def conv_mer(self):
        # convergência de meridianos
        conv_mer = self.virgula_p_float(self.conv_g.text) + self.virgula_p_float(
            self.conv_m.text) / 60 + self.virgula_p_float(self.conv_s.text) / 3600
        return conv_mer

    def qm_sim(self):
        qm_sim = self.decl_mag() + self.conv_mer()
        return qm_sim

    def qm_nao(self):
        qm_nao = self.decl_mag() - self.conv_mer()
        return qm_nao

    def calc_qm_sim(self):
        if self.t_bold == False:
            self.resultado.text = 'Ângulo QM = {}'.format(self.qm_sim())

    def calc_qm_nao(self):
        if self.t_bold == True:
            self.resultado.text = 'Ângulo QM = {}'.format(self.qm_nao())

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

class Lancamento(Screen):
    ea = ObjectProperty(None)
    na = ObjectProperty(None)
    eb = ObjectProperty(None)
    nb = ObjectProperty(None)

    def dE(self):
        dE = float(self.eb.text) - float(self.ea.text)
        return dE

    def dN(self):
        dN = float(self.nb.text) - float(self.na.text)
        return dN

    def ang(self):
        tang = self.dE() / self.dN()
        a_grau = degrees(atan(tang))
        return a_grau

    def a_grau_2e3q(self):
        a_grau_2e3Q = self.ang() + 180
        return a_grau_2e3Q

    def a_grau_4q(self):
        a_grau_4Q = self.ang() + 360
        return a_grau_4Q

    def a_mil(self):
        a_mil = (self.ang() * 160) / 9
        return a_mil

    def a_mil_2e3q(self):
        a_mil_2e3q = (self.a_grau_2e3q() * 160) / 9
        return a_mil_2e3q

    def a_mil_4q(self):
        a_mil_4q = (self.a_grau_4q() * 160) / 9
        return a_mil_4q

    def calc_ang(self):
        if float(self.nb.text) == float(self.na.text):
            self.ids.apertado.text = 'Não existe divisão por zero'
        else:
            if self.dN() == 0:
                self.ids.apertado.text = '1º Quadrante \n dE =  {} e dN = {} \n O Lançamento de AB é em graus {}º \n O lançamento de AB em milésimos é {} milésimos'.format(
                    self.dE(), self.dN(), '%.2f' % self.ang(), '%.2f' % self.a_mil())
            if self.dE() >= 0 and self.dN() >= 0:
                self.ids.apertado.text = '1º Quadrante \n dE =  {} e dN = {} \n O Lançamento de AB é em graus {}º \n O lançamento de AB em milésimos é {} milésimos'.format(
                    self.dE(), self.dN(), '%.2f' % self.ang(), '%.2f' % self.a_mil())
            if self.dE() > 0 and self.dN() < 0:
                self.ids.apertado.text = '2º Quadrante \n dE =  {} e dN = {} \n O Lançamento de AB é em graus {}º \n O lançamento de AB em milésimos é {} milésimos'.format(
                    self.dE(), self.dN(), '%.2f' % self.a_grau_2e3q(), '%.2f' % self.a_mil_2e3q())
            if self.dE() < 0 and self.dN() < 0:
                self.ids.apertado.text = '3º Quadrante \n dE =  {} e dN = {} \n O Lançamento de AB é em graus {}º \n O lançamento de AB em milésimos é {} milésimos'.format(
                    self.dE(), self.dN(), '%.2f' % self.a_grau_2e3q(), '%.2f' % self.a_mil_2e3q())
            if self.dE() < 0 and self.dN() > 0:
                self.ids.apertado.text = '4º Quadrante \n dE =  {} e dN = {} \n O Lançamento de AB é em graus {}º \n O lançamento de AB em milésimos é {} milésimos'.format(
                    self.dE(), self.dN(), '%.2f' % self.a_grau_4q(), '%.2f' % self.a_mil_4q())

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True

class Azimute(Screen):
    ea = ObjectProperty(None)
    na = ObjectProperty(None)
    eb = ObjectProperty(None)
    nb = ObjectProperty(None)
    a_carta = ObjectProperty(None)
    a_atual = ObjectProperty(None)
    dmg = ObjectProperty(None)
    dmm = ObjectProperty(None)
    dms = ObjectProperty(None)
    dmag = ObjectProperty(None)
    dmam = ObjectProperty(None)
    dmas = ObjectProperty(None)
    conv_g = ObjectProperty(None)
    conv_m = ObjectProperty(None)
    conv_s = ObjectProperty(None)
    resultado = ObjectProperty(None)
    t_bold = BooleanProperty(False)
    t2_bold = BooleanProperty(False)
    t3_bold = BooleanProperty(False)

    def virgula_p_float(self, m):
        locale.setlocale(locale.LC_ALL, "")
        n = locale.atof(m)
        return n

    def dE(self):
        dE = int(self.eb.text) - int(self.ea.text)
        return dE

    def dN(self):
        dN = int(self.nb.text) - int(self.na.text)
        return dN

    def ang(self):
        if self.dN() == 0:
            a_grau = 0
        else:
            tang = self.dE() / self.dN()
            a_grau = degrees(atan(tang))
        return a_grau

    def a_grau_2e3q(self):
        a_grau_2e3Q = self.ang() + 180
        return a_grau_2e3Q

    def a_grau_4q(self):
        a_grau_4Q = self.ang() + 360
        return a_grau_4Q

    def transf_grau_p_mil(self, ang_grau):
        a_mil = (ang_grau * 160) / 9
        return a_mil

    def lanc(self):
        if self.dN() == 0:
            lanc = self.ang()
        if self.dE() >= 0 and self.dN() >= 0:
            lanc = self.ang()
        if self.dE() > 0 and self.dN() < 0:
            lanc = self.a_grau_2e3q()
        if self.dE() < 0 and self.dN() < 0:
            lanc = self.a_grau_2e3q()
        if self.dE() < 0 and self.dN() > 0:
            lanc = self.a_grau_4q()
        return lanc

    def dmi_func(self):
        if self.t3_bold == False:
            dmi = self.virgula_p_float(self.dmg.text) + self.virgula_p_float(self.dmm.text) / 60 + self.virgula_p_float(
                self.dms.text) / 3600
        if self.t3_bold == True:
            dmi = (-1) * (self.virgula_p_float(self.dmg.text) + self.virgula_p_float(
                self.dmm.text) / 60 + self.virgula_p_float(self.dms.text) / 3600)
        return dmi

    def decl_mag(self):
        dif_ano = int(self.a_atual.text) - int(self.a_carta.text)
        # graus total da declinação magnética no ano de confecção da carta
        dma = self.virgula_p_float(self.dmag.text) + self.virgula_p_float(self.dmam.text) / 60 + self.virgula_p_float(
            self.dmas.text) / 3600
        # dm0 é a variação da declinação anual desde a confecção da carta
        dm0 = self.dmi_func() * dif_ano
        # soma da declinação magnética da carta com a declinação anual
        decl_mag = dm0 + dma
        return decl_mag

    def conv_mer(self):
        # convergência de meridianos
        conv_mer = self.virgula_p_float(self.conv_g.text) + self.virgula_p_float(
            self.conv_m.text) / 60 + self.virgula_p_float(self.conv_s.text) / 3600
        return conv_mer

    def qm_sim(self):
        qm_sim = self.decl_mag() + self.conv_mer()
        return qm_sim

    def qm_nao(self):
        qm_nao = self.decl_mag() - self.conv_mer()
        return qm_nao

    def calc_qm(self):
        if self.t_bold == False:
            qm = self.qm_sim()
            return qm
        if self.t_bold == True:
            qm = self.qm_nao()
            return qm
        return qm

    def az_sim(self):
        az_sim = self.lanc() - self.calc_qm()
        return az_sim

    def az_nao(self):
        az_nao = self.lanc() + self.calc_qm()
        return az_nao

    def qm_mil(self):
        qm_mil = self.transf_grau_p_mil(self.calc_qm())
        return qm_mil

    def az_mil_sim(self):
        az_mil = self.transf_grau_p_mil(self.az_sim())
        return az_mil

    def az_mil_nao(self):
        az_mil = self.transf_grau_p_mil(self.az_nao())
        return az_mil

    def lanc_mil(self):
        lanc_mil = self.transf_grau_p_mil(self.lanc())
        return lanc_mil

    def calc_az_sim(self):
        if self.t2_bold == False:
            self.resultado.text = 'Graus (QM = {}°; Az = {}º e Lc = {}º) / Milésimos (QM = {} mil''; Az = {} mil e Lc = {} mil)'.format(
                '%.2f' % self.calc_qm(), '%.2f' % self.az_sim(), '%.2f' % self.lanc(), '%.2f' % self.qm_mil(),
                '%.2f' % self.az_mil_sim(), '%.2f' % self.lanc_mil())

    def calc_az_nao(self):
        if self.t2_bold == True:
            self.resultado.text = 'Graus (QM = {}º; Az = {}º e Lc = {}º) / Milésimos (QM = {} mil; Az = {} mil e Lc = {} mil)'.format \
                ('%.2f' % self.calc_qm(), '%.2f' % self.az_nao(), '%.2f' % self.lanc(), '%.2f' % self.qm_mil(),
                 '%.2f' % self.az_mil_nao(), '%.2f' % self.lanc_mil())

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)




class MyApp(App):
    pass
    def build(self):
        Builder.load_string(open('Test.kv', encoding='utf-8').read(), rulesonly=True)
        return Gerenciador()



if __name__ == '__main__':
    MyApp().run()