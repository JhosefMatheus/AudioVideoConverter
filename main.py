from tkinter import *
import AudioConverter

conversor_de_audio = AudioConverter.audioConverter()

aplicativo = Tk()

largura_aplicativo = 250
altura_aplicativo = 250

largura_tela = aplicativo.winfo_screenwidth()
altura_tela = aplicativo.winfo_screenheight()

x = int(largura_tela/2) - int(largura_aplicativo/2)
y = int(altura_tela/2) - int(altura_aplicativo/2)

aplicativo.geometry(f'{largura_aplicativo}x{altura_aplicativo}+{x}+{y}')
aplicativo.resizable(False, False)

botao_escolher_arquivo = Button(
    aplicativo,
    text='Escolher arquivo',
    command=lambda:conversor_de_audio.salvar_audio()
).place(x=80, y=100)

aplicativo.mainloop()