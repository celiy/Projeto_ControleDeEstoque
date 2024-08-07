from tkinter import *

#Esta classe é usada para retornar informações do app caso necessário
class SetAppinfo:
    def __init__(self):
        self.versaoatual = "Build 1.1"
        self.dataversao = "26/07/2024"
        self.criador = "Diogo Carvalho Viegas"

#Essa função inicia uma janela que mostra as informações do app
def getappinfo():

    janelaso = Tk()
    janelaso.geometry("300x200")
    janelaso.title("Sobre")
    janelaso.resizable(False, False)

    Label(janelaso, text="Versão:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
    Label(janelaso, text="Build 1.1").grid(row=0, column=1, padx=10, pady=10, sticky='e')

    Label(janelaso, text="Data da Versão:").grid(row=1, column=0, padx=10, pady=10, sticky='w')
    Label(janelaso, text="26/07/2024").grid(row=1, column=1, padx=10, pady=10, sticky='e')

    Label(janelaso, text="Criador:").grid(row=2, column=0, padx=10, pady=10, sticky='w')
    Label(janelaso, text="Diogo Carvalho Viegas").grid(row=2, column=1, padx=10, pady=10, sticky='e')

    janelaso.mainloop()
