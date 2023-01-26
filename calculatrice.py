from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Calculatrice(App):
    def build(self):
        self.operador = ['+', '-', '*', '/']  #Define os operadores aritmeticos
        self.ultoperador = None  #Memoria do ultimo operador
        self.ultbotao = None  #Memoria do ultimo botao
        main_layout = BoxLayout(orientation='vertical')  #Cria o layout
        self.resultado = TextInput(text = '', multiline = False, readonly = True, halign = 'right', font_size = 55)   #Cria a tela pra mostrar o resultado
        main_layout.add_widget(self.resultado)
        teclas = [
            ['7','8','9','/'],     #teclado da calculatrice
            ['4','5','6','*'],
            ['1','2','3','-'],
            ['.','0','C','+'],
        ]
        for coluna in teclas:     #loop para adicionar as teclas ao teclado
            horlayout = BoxLayout()
            for label in coluna:
                botao = Button(text = label, pos_hint = {'center_x':.5, 'center_y':.5})
                botao.bind(on_press = self.apertar)
                horlayout.add_widget(botao)   #adiciona o botao no layout do teclado
            main_layout.add_widget(horlayout)   #adiciona o teclado no layout principal

        botaoigual = Button(text ='=', pos_hint = {'center_x':0.5, 'center_y':0.5})
        botaoigual.bind(on_press = self.clicaresultado)
        main_layout.add_widget(botaoigual)
        return main_layout

    def apertar(self, instance):
        atual = self.resultado.text  #extrai o resultado mostrado na tela
        textobotao = instance.text  #extrai o valor do botao apertado

        if textobotao == 'C':  #limpar tudo
            self.resultado.text = ''
        else:
            if atual and (self.ultoperador and textobotao in self.operador):  #verif se o botao apertado eh um operador
                return
            elif atual == '' and textobotao in self.operador:  #verif se o primeiro botao eh um operador
                return
            else:
                novotexto = atual + textobotao
                self.resultado.text = novotexto  #mostra na tela os botoes apertados
            self.ultbotao = textobotao #guarda o ultimo numero clicado
            self.ultoperador = self.ultbotao in self.operador  #se o ultimo botao for operador entao guarda um TRUE



    def clicaresultado(self, instance):
        texto = self.resultado.text
        if texto:
            resultado = str(eval(self.resultado.text))
            self.resultado.text = resultado

if __name__ == '__main__':
    app = Calculatrice()
    app.run()