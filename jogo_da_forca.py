import tkinter as tk
import random

class JogoDaForca:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da forca")
        self.palavras = ["PYTHON", "FORCA", "JOGO", "DESENVOLVIMENTO", "INTERFACE"]
        self.palavra_atual = random.choice(self.palavras)
        self.palavra_oculta = ["_" for _ in self.palavra_atual]
        self.tentativas_max = 6
        self.tentativas = 0

        self.label_palavra = tk.Label(root, text=' '.join(self.palavra_oculta), font=('Arial', 16))
        self.label_palavra.pack(pady=10)

        self.label_tentativas = tk.Label(root, text=f'Tentativas restantes: {self.tentativas_max}', font=('Arial', 12))
        self.label_tentativas.pack()

        self.botoes_letras = [tk.Button(root, text=letra, width=4, height=2, font=('Arial', 12), command=lambda l=letra: self.tentar_letra(l)) for letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
        for botao in self.botoes_letras:
            botao.pack(side=tk.LEFT, padx=2, pady=2)

        self.canvas = tk.Canvas(root, width=150, height=200)
        self.canvas.pack()


    def tentar_letra(self, letra):
        if letra in self.palavra_atual:
            for i, letra_palavra in enumerate(self.palavra_atual):
                if letra_palavra == letra:
                    self.palavra_oculta[i] = letra

            if "_" not in self.palavra_oculta:
                self.label_palavra.config(text="Parabéns! Você venceu!")
                self.bloquear_botoes()
        else:
            self.tentativas += 1
            self.label_tentativas.config(text=f'Tentativas restantes: {self.tentativas_max - self.tentativas}')

            if self.tentativas == self.tentativas_max:
                self.label_palavra.config(text=f'Você perdeu! A palavra era {self.palavra_atual}')
                self.mostrar_palavra_correta()
                self.bloquear_botoes()

        self.label_palavra.config(text=' '.join(self.palavra_oculta))

    def bloquear_botoes(self):
        for botao in self.botoes_letras:
            botao.config(state=tk.DISABLED)

    def mostrar_palavra_correta(self):
        # Mostra a palavra correta que não foi descoberta
        for i, letra_palavra in enumerate(self.palavra_atual):
            if self.palavra_oculta[i] == "_":
                self.palavra_oculta[i] = letra_palavra

        self.label_palavra.config(text=' '.join(self.palavra_oculta))

root = tk.Tk()
jogo = JogoDaForca(root)
root.mainloop()
