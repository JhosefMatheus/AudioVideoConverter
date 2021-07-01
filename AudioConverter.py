from tkinter import messagebox, filedialog as fd
import moviepy.editor as mp

class audioConverter:
    def __init__(self):
        self.video_name = None

    def escolher_arquivo(self):
        return fd.askopenfilename()

    def converter_arquivo_selecionado(self):
        arquivo = self.escolher_arquivo()

        video = mp.VideoFileClip(arquivo)

        self.video_name = arquivo.split('/')[-1]

        return video.audio

    def salvar_audio(self):
        try:
            audio = self.converter_arquivo_selecionado()

            diretorio = fd.askdirectory()

            audio.write_audiofile(f'{diretorio}/{self.video_name}.mp3')

            messagebox.showinfo('Conversão conluída!', f'Parabéns, arquivo {self.video_name} convertido com sucesso\n Por padrão nós salvamos o áudio com o nome do vídeo, caso queira, basta alterar o nome! =D')

        
        except Exception as e:
            messagebox.showerror('Erro!', 'Infelizmente a conversão não deu certo, por favor, verifique se você forneceu um arquivo de vídeo válido')

