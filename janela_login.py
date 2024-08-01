from tkinter import *
from tkinter import messagebox
from appinfo import *
from registrar_logar_user import *

useridjl = ""

#Esta é a primeira janela que aparece quando o programa é iniciado
#Esta janela é a qual o usuário faz login
def iniciarlogin():
    print("Na janela de login.")

    #Esta função executa uma outra função do modulo "registrar_logar_user" para fazer o login
    def logar():
        lognome = insnome.get()
        logsenha = inssenha.get()

        #Aqui a função pega o id do usuário logado retornado do modulo "registrar_logar_user"
        print("Nome logado: " + lognome)
        print("Senha logado: " + logsenha)
        global useridjl
        useridjl = str(logaruser(lognome, logsenha))
        print("UserID no modulo login: "+str(useridjl))
        #Aqui a função retorna um id para o modulo "main" caso válido ou retorna um id vazio caso inválido
        if not useridjl == "False":
            print("Login completo.")
            janelalo.destroy()
        else:
            useridjl = ""
            messagebox.showerror(title='Incorreto!', message='As informações de login estão incorretas.')

    #Esta função fecha a janela de login e executa a função de registrar no modulo "registrar_logar_user"
    def registrar():
        janelalo.destroy()
        registrarusuario()

    #Pega a versão do app do modulo "appinfo"
    def getversao():
        vers = SetAppinfo()
        versao.set(vers.versaoatual)

    #Abre uma janela com as informações do app a partir do modulo "appinfo"
    def getsobre():
        getappinfo()

    janelalo = Tk()
    janelalo.geometry("400x500")
    janelalo.title("Login")
    janelalo.resizable(False,False)

    versao = StringVar()
    getversao()

    frame = Frame(janelalo)
    frame.place(relx=0.5,rely=0.4,anchor=CENTER)

    #Menu bar de cima que permite que o usuário veja as informações do app
    menubar = Menu(janelalo)
    janelalo.config(menu=menubar)
    file_menu = Menu(menubar,tearoff=0)
    file_menu.add_command(label='Sobre',command=getsobre)
    menubar.add_cascade(label="Mais",menu=file_menu)

    txtlogin = Label(frame,text="Login:",font=("Helvetica",10)).pack(side=TOP)
    insnome = (Entry(frame))
    insnome.pack(side=TOP,pady=4)
    inssenha = Entry(frame,show="*")
    inssenha.pack(side=TOP)
    butentrar = Button(frame,text="Entrar",font=("Helvetica",10),command=logar).pack(side=TOP,pady=(4, 10))

    txtregistrar = Label(frame,text="Não tem login?",font=("Helvetica",10)).pack(side=TOP, pady=(20, 4))
    butregistrar = Button(frame,text="Registrar",font=("Helvetica",10),command=registrar).pack(side=TOP)

    txtfooter = Label(janelalo,textvariable=versao,fg='gray').pack(side=BOTTOM)

    janelalo.mainloop()

    global useridjl
    return str(useridjl)

#Esta função é iniciada a partir da janela de login que permite que o usuário se registre no sistema
def registrarusuario():
    print("Na janela de registrar.")

    #Pega a versão do app do modulo "appinfo"
    def getversao():
        vers = SetAppinfo()
        versao.set(vers.versaoatual)

    #Esta função faz o registro do usuário
    def registrar():
        regnome = insnome.get()
        regsenha = inssenha.get()
        print("Nome registrado: "+regnome)
        print("Senha registrado: "+regsenha)
        #Após coletar as informações do registro a cima, o programa executa a função de registrar usuário
        #do módulo "registrar_logar_user" e volta para a janela de login caso o registro é válido
        if not registraruser(regnome, regsenha):
            messagebox.showerror(title='Já existe!', message='O usuário que você informou já existe.')
        else:
            messagebox.showinfo(title='Sucesso!', message='Usuário criado com sucesso!')
            janelare.destroy()
            iniciarlogin()

    janelare = Tk()
    janelare.geometry("400x500")
    janelare.title("Registrar")
    janelare.resizable(False,False)

    versao = StringVar()
    getversao()

    frame = Frame(janelare)
    frame.place(relx=0.5,rely=0.4,anchor=CENTER)

    txtnome = Label(frame,text="Nome e senha:",font=("Helvetica",10)).pack(side=TOP)
    insnome = (Entry(frame))
    insnome.pack(side=TOP,pady=4)
    inssenha = (Entry(frame,show="*"))
    inssenha.pack(side=TOP)
    butregistrar = Button(frame,text="Registrar",font=("Helvetica",10),command=registrar).pack(side=TOP,pady=(4, 10))

    txtfooter = Label(janelare,textvariable=versao,fg='gray').pack(side=BOTTOM)

    janelare.mainloop()