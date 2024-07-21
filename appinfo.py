from tkinter import *
class SetAppinfo:
    versaoatual = "Build 1.0"
    dataversao = "20/07/2024"
    criador = "Diogo Carvalho Viegas"

def getappinfo():

    def setfields():
        versaoapp.set(appinfo.versaoatual)
        dataversaoapp.set(appinfo.dataversao)
        criadorapp.set(appinfo.criador)

    janelaso = Tk()
    janelaso.geometry("300x300")
    janelaso.title("Sobre")
    janelaso.resizable(False,False)

    appinfo = SetAppinfo()
    versaoapp = StringVar()
    dataversaoapp = StringVar()
    criadorapp = StringVar()

    setfields()

    print(versaoapp)
    print(dataversaoapp)
    print(criadorapp)

    Label(janelaso,textvariable=versaoapp).pack()
    Label(janelaso,textvariable=dataversaoapp).pack()
    Label(janelaso,textvariable=criadorapp).pack()

    janelaso.mainloop()