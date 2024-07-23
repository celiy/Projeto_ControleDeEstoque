from tkinter import *
from janela_principal_funcoes import *

def janelacadastros():

    def cadastrar():
        nome = insnome.get()
        rua = insrua.get()
        num = insnumcasa.get()
        cidade = inscidade.get()
        endereco = str(rua+", "+num+" / "+cidade)
        registrarcliente(nome,endereco)

    janela = Tk()
    janela.title("Cadastros")

    framecadastro = Frame(janela)
    framecadastro.pack(pady=30,padx=50)

    descricao = Label(framecadastro, text="Insira os dados do cliente:", font=("Helvetica", 10),height=4).pack(side=TOP)
    nomecliente = Label(framecadastro, text="Nome:", font=("Helvetica", 10)).pack(side=TOP)
    insnome = (Entry(framecadastro))
    insnome.pack(side=TOP, pady=4)
    enderecocliente = Label(framecadastro, text="Endereço: (Rua, Numero da casa / Cidade)", font=("Helvetica", 10)).pack(side=TOP)
    insrua = Entry(framecadastro,width=15)
    insrua.pack(side=LEFT)
    insnumcasa = Entry(framecadastro,width=10)
    insnumcasa.pack(side=LEFT)
    inscidade = Entry(framecadastro,width=15)
    inscidade.pack(side=LEFT)
    butsubmit = Button(framecadastro, text="Cadastrar", font=("Helvetica", 10), command=cadastrar)
    butsubmit.pack(side=RIGHT)

    janela.mainloop()

def janelaestoque():

    def drawlist():
        filepath = "estoqueinfo.txt"

        if os.path.isfile(filepath):
            with open(filepath, "r") as file:
                produtosinfo = file.readlines()

            produtos = []
            produto = ""
            for linha in produtosinfo:
                if linha.strip() == "/":
                    if produto:
                        produtos.append(produto)
                    produto = ""
                else:
                    produto += linha.strip() + " "

            listbox = Listbox(janela, width=120, height=20)
            listbox.grid(row=0, column=1)

            for n, produto in enumerate(produtos):
                listbox.insert(n, produto)

    def cadastrar():
        #nomep
        #descp
        #tipop
        #marcap

        drawlist()

    janela = Tk()
    janela.title("Estoque")

    framecadastro = Frame(janela,bd=3, relief='groove')
    framecadastro.grid(row=0,column=0)

    descricao = Label(framecadastro, text="Registrar estoque:", font=("Helvetica", 10), height=4,width=20).pack(side=TOP)
    descricaoitens = Label(framecadastro, text="Nome",font=("Helvetica", 10)).pack(side=TOP)
    insnome = Entry(framecadastro, width=15)
    insnome.pack(side=TOP,pady=3)
    descricaoitens = Label(framecadastro, text="Descrição", font=("Helvetica", 10)).pack(side=TOP)
    insdesc = Entry(framecadastro, width=15)
    insdesc.pack(side=TOP,pady=3)
    descricaoitens = Label(framecadastro, text="Tipo", font=("Helvetica", 10)).pack(side=TOP)
    instipo = Entry(framecadastro, width=15)
    instipo.pack(side=TOP,pady=3)
    descricaoitens = Label(framecadastro, text="Marca", font=("Helvetica", 10)).pack(side=TOP)
    insmarca = Entry(framecadastro, width=15)
    insmarca.pack(side=TOP,pady=3)
    descricaoitens = Label(framecadastro, text="Quantidade", font=("Helvetica", 10)).pack(side=TOP)
    insquant = Entry(framecadastro, width=15)
    insquant.pack(side=TOP,pady=3)
    butsubmit = Button(framecadastro, text="Cadastrar", font=("Helvetica", 10), command=cadastrar)
    butsubmit.pack(side=TOP,pady=3)

    drawlist()

    janela.mainloop()

def janelavendas():
    janela = Tk()
    janela.title("Vendas")

    janela.mainloop()

def janelaclientes():
    janela = Tk()
    janela.title("Clientes")

    janela.mainloop()
def iniciarjanela(userid):
    janela = Tk()
    janela.title("Controle de estoque")
    print("Na janela principal com o ID: "+userid)

    #vars para atributos widgets
    framecebuttonw = 15
    framecebuttonh = 3

    #Widgets

    #Botões do lado esquerdo
    dashboard = Button(janela,text="Dashboard",width=framecebuttonw,height=framecebuttonh,state=DISABLED)
    dashboard.grid(row=0)
    cadastros = Button(janela,text="Cadastrar",width=framecebuttonw,height=framecebuttonh,command=janelacadastros)
    cadastros.grid(row=1)
    estoque = Button(janela,text="Estoque",width=framecebuttonw,height=framecebuttonh,command=janelaestoque)
    estoque.grid(row=2)
    vendas = Button(janela,text="Vendas",width=framecebuttonw,height=framecebuttonh)
    vendas.grid(row=3)
    clientes = Button(janela,text="Clientes",width=framecebuttonw,height=framecebuttonh)
    clientes.grid(row=4)

    #Labels do centro
    h1dashboard = Label(janela,text="Dashboard")
    h1dashboard.grid(row=0,column=1)

    vendashoje = Label(janela,text="Vendas de hoje:",width=20)
    vendashoje.grid(row=1,column=1,sticky='n')
    varvenhj = IntVar()
    venhj = Label(janela,textvariable=varvenhj)
    venhj.grid(row=1, column=1, sticky='s')

    faturamentomes = Label(janela,text="Faturamento do mês:",width=20)
    faturamentomes.grid(row=1,column=2,sticky='n')
    varfames = IntVar()
    fames = Label(janela,textvariable=varfames)
    fames.grid(row=1, column=2, sticky='s')

    pagarhoje = Label(janela,text="A pagar hoje:",width=20)
    pagarhoje.grid(row=1,column=3,sticky='n')
    varpahj = IntVar()
    pahj = Label(janela,textvariable=varpahj)
    pahj.grid(row=1, column=3, sticky='s')

    janela.mainloop()

iniciarjanela("1")