from tkinter import *
from tkinter import messagebox
from janela_principal_funcoes import *

guserid = ""

def janelacadastros():

    def cadastrar():
        nome = insnome.get()
        rua = insrua.get()
        num = insnumcasa.get()
        cidade = inscidade.get()
        endereco = str(rua+", "+num+" / "+cidade)
        if registrarcliente(nome,endereco) == False:
            messagebox.showerror(title='Já existe!', message='O cliente que você informou já existe.')
        else:
            messagebox.showinfo(title='Sucesso!', message='Cliente registrado com sucesso!')
            insnome.delete(0, END)
            insrua.delete(0, END)
            insnumcasa.delete(0, END)
            inscidade.delete(0, END)

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
        nomep = insnome.get()
        descp = insdesc.get()
        tipop = instipo.get()
        marcap = insmarca.get()
        quantp = insquant.get()
        global guserid
        userid = guserid
        registrarproduto(nomep,descp,tipop,marcap,quantp,userid)
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

    textestoque = Label(janela,text="Estoque atual:")
    textestoque.grid(row=0, column=1)

    def drawestoque():
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
            listbox.grid(row=1, column=1)

            for n, produto in enumerate(produtos):
                listbox.insert(n, produto)

    textvendas = Label(janela, text="Vendas atual:")
    textvendas.grid(row=2, column=1)

    def drawvendas():
        filepath = "vendasinfo.txt"

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
            listbox.grid(row=3, column=1)

            for n, produto in enumerate(produtos):
                listbox.insert(n, produto)

    textclientes = Label(janela, text="Clientes atual:")
    textclientes.grid(row=0, column=2)

    def drawclientes():
        filepath = "clientesinfo.txt"

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

            listbox = Listbox(janela, width=60, height=40)
            listbox.grid(row=0, column=2, rowspan=4)

            for n, produto in enumerate(produtos):
                listbox.insert(n, produto)

    def cadastrar():
        nomep = insnome.get()
        nomec = insnomec.get()
        quantv = insquant.get()
        preco = inspre.get()
        registrarvenda(nomep, nomec, quantv, preco)
        drawestoque()
        drawvendas()

    framecadastro = Frame(janela,bd=3, relief='groove')
    framecadastro.grid(row=0,column=0, rowspan=3)

    descricao = Label(framecadastro, text="Registrar venda:", font=("Helvetica", 10), height=4,width=20).pack(side=TOP)
    descricaoitens = Label(framecadastro, text="Nome produto:",font=("Helvetica", 10)).pack(side=TOP)
    insnome = Entry(framecadastro, width=15)
    insnome.pack(side=TOP,pady=3)
    descricaoitens = Label(framecadastro, text="Nome cliente", font=("Helvetica", 10)).pack(side=TOP)
    insnomec = Entry(framecadastro, width=15)
    insnomec.pack(side=TOP,pady=3)
    descricaoitens = Label(framecadastro, text="Quantidade", font=("Helvetica", 10)).pack(side=TOP)
    insquant = Entry(framecadastro, width=15)
    insquant.pack(side=TOP,pady=3)
    descricaoitens = Label(framecadastro, text="Preço", font=("Helvetica", 10)).pack(side=TOP)
    inspre = Entry(framecadastro, width=15)
    inspre.pack(side=TOP, pady=3)
    butsubmit = Button(framecadastro, text="Cadastrar", font=("Helvetica", 10), command=cadastrar)
    butsubmit.pack(side=TOP,pady=3)

    drawestoque()
    drawvendas()
    drawclientes()

    janela.mainloop()

def janelaclientes():
    janela = Tk()
    janela.title("Clientes")

    def drawclientes():
        filepath = "clientesinfo.txt"

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

            listbox = Listbox(janela, width=80, height=40)
            listbox.grid(row=0, column=0)

            for n, produto in enumerate(produtos):
                listbox.insert(n, produto)

    drawclientes()

    janela.mainloop()

def iniciarjanela(userid):
    janela = Tk()
    janela.title("Controle de estoque")
    print("Na janela principal com o ID: "+userid)

    global guserid
    guserid = userid

    def vendastotal():
        filepath = "vendasinfo.txt"
        if os.path.isfile(filepath):
            with open(filepath, "r") as file:
                vendasinfo = file.read()
            vendast = vendasinfo.count("IDVenda")
            varvenhj.set(vendast-1)

    def faturamentos():
        fatura = somar_precos()
        varfames.set(fatura)

    def emestoque():
        filepath = "estoqueinfo.txt"
        if os.path.isfile(filepath):
            with open(filepath, "r") as file:
                vendasinfo = file.read()
            total = vendasinfo.count("Nome: ")
            varest.set(total-1)

    def refresh():
        vendastotal()
        faturamentos()
        emestoque()

    #vars para atributos widgets
    framecebuttonw = 15
    framecebuttonh = 3

    #Widgets

    #Botões do lado esquerdo
    dashboard = Button(janela,text="Dashboard",width=framecebuttonw,height=framecebuttonh,state=DISABLED)
    dashboard.grid(row=0)
    cadastros = Button(janela,text="Cadastrar\nClientes",width=framecebuttonw,height=framecebuttonh,command=janelacadastros)
    cadastros.grid(row=1)
    estoque = Button(janela,text="Estoque",width=framecebuttonw,height=framecebuttonh,command=janelaestoque)
    estoque.grid(row=2)
    vendas = Button(janela,text="Vendas",width=framecebuttonw,height=framecebuttonh,command=janelavendas)
    vendas.grid(row=3)
    clientes = Button(janela,text="Clientes",width=framecebuttonw,height=framecebuttonh,command=janelaclientes)
    clientes.grid(row=4)

    #Labels do centro
    h1dashboard = Label(janela,text="Dashboard")
    h1dashboard.grid(row=0,column=1)

    vendashoje = Label(janela,text="Vendas total:",width=20)
    vendashoje.grid(row=1,column=1,sticky='n')
    varvenhj = IntVar()
    venhj = Label(janela,textvariable=varvenhj)
    venhj.grid(row=1, column=1, sticky='s')

    faturamentomes = Label(janela,text="Faturamento do mês:",width=20)
    faturamentomes.grid(row=1,column=2,sticky='n')
    varfames = IntVar()
    fames = Label(janela,textvariable=varfames)
    fames.grid(row=1, column=2, sticky='s')

    pagarhoje = Label(janela,text="Produtos em estoque:",width=20)
    pagarhoje.grid(row=1,column=3,sticky='n')
    varest = IntVar()
    pahj = Label(janela,textvariable=varest)
    pahj.grid(row=1, column=3, sticky='s')

    atualizar = Button(janela, text="Atualizar", width=framecebuttonw, height=framecebuttonh, command=refresh)
    atualizar.grid(row=5,column=3)

    refresh()

    janela.mainloop()