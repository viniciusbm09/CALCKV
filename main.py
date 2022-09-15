from itertools import count
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout


class CustomLayout1(MDBoxLayout):
    #Função para zerar o display
    def clear_display(self):
        self.ids.display.text = '0'

    #Função que recebe os valores dos botões
    def buttom_number(self, number):
        #Restringe o número de caracteres no display
        if len(self.ids.display.text) != 12:
            if self.ids.display.text == '0' or self.ids.display.text == 'error':
                self.ids.display.text = ''
                self.ids.display.text = f'{number}'
            else:
                self.ids.display.text += f'{number}'
        
    #Função que recebe a operação
    def buttom_operation(self, operation):
        if len(self.ids.display.text) != 12:
            x = self.ids.display.text
            self.ids.display.text = f'{x}{operation}'

    #Função para incluir o percentual
    def percent(self):
        x = self.ids.display.text
        if "*" in x:
            if "%" in x:
                pass
            else:
                x = f'{x}%'
                self.ids.display.text = x
    #Função para ajustar a expressão de cálculo de percentual
    def calculate_percentual(self, x):
        #x = self.ids.display.text
        if "%" in x:
            x = eval(x.replace("%","/100"))
            return x
      
    #Função para a tecla ponto
    def ponto(self):
        x = self.ids.display.text
        if "." in x:
            pass
        else:
            x = f'{x}.'
            self.ids.display.text = x

    #Função para obter o resultado da expressão no display
    def result(self):  
        try:
            #x = eval(self.ids.display.text)
            x = self.ids.display.text
            if "%" in x:
                self.ids.display.text = f'{round(self.calculate_percentual(x),4)}'
            else:                
                self.ids.display.text = f'{round(eval(x),4)}'
        except:
            self.ids.display.text = 'error'

    #Função que altera o sinal do valor no display
    def posneg(self):
        x = self.ids.display.text
        if x == '0':
            pass
        else:
                
            if "-" in x:
                self.ids.display.text = f'{x}'.replace('-','')
            else:
                self.ids.display.text = f'-{x}'
    #Função de backspace
    def backspace(self):
        x = self.ids.display.text
        if len(x) == 1:
            self.ids.display.text = '0'
        else:
            x = x[:-1]
            self.ids.display.text = x



class CustomLayout2(MDGridLayout):
    pass

class MyApp(MDApp):
    #Função que retorna a string formada no arquivo .kv
    def build(self):
        self.title = "Calculadora"
        return  Builder.load_file('main.kv')

if __name__=="__main__":
    MyApp().run()

#Para rodar simulando size da janela como smartphone
#python main.py -m screen:note2,portrait,scale=.5