from tkinter import *

def janelacadastros():
    janela = Tk()
    janela.title("Cadastros")

    janela.mainloop()

def janelaestoque():
    janela = Tk()
    janela.title("Estoque")

    janela.mainloop()

def janelavendas():
    janela = Tk()
    janela.title("Vendas")

    janela.mainloop()

def janelaclientes():
    janela = Tk()
    janela.title("Clientes")

    janela.mainloop()
def iniciarjanela():
    janela = Tk()
    janela.title("Controle de estoque")

    framees = Frame(janela)
    framees.grid(row=2,column=0)

    framedi = Frame(janela)
    framedi.place(anchor=E)

    frameci = Frame(janela)
    frameci.place(anchor=N)

    frameba = Frame(janela)
    frameba.place(anchor=S)

    framece = Frame(janela)
    framece.place(anchor=CENTER)

    framecebuttonw = 15
    framecebuttonh = 3

    dashboard = Button(framees,text="Dashboard",width=framecebuttonw,height=framecebuttonh,state=DISABLED)
    dashboard.pack(side=TOP)
    cadastros = Button(framees,text="Cadastros",width=framecebuttonw,height=framecebuttonh,command=janelacadastros)
    cadastros.pack(side=TOP)
    estoque = Button(framees,text="Estoque",width=framecebuttonw,height=framecebuttonh)
    estoque.pack(side=TOP)
    vendas = Button(framees,text="Vendas",width=framecebuttonw,height=framecebuttonh)
    vendas.pack(side=TOP)
    clientes = Button(framees,text="Clientes",width=framecebuttonw,height=framecebuttonh)
    clientes.pack(side=TOP)

    janela.mainloop()