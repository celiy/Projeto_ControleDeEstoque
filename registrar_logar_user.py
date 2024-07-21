import os

def checar_existencia(nome, senha, texto):
    linhas = texto.split('\n')
    for i in range(len(linhas)):
        if linhas[i].strip().startswith("Nome:") and linhas[i].strip().endswith(nome):
            if i + 1 < len(linhas) and linhas[i + 1].strip().startswith("Senha:") and linhas[i + 1].strip().endswith(
                    senha):
                return True
    return False

def registraruser(regnome, regsenha):
    filepath = "userinfo.txt"
    while True:
        if os.path.isfile(filepath):
            with open(filepath, "r") as file:
                userinfo = file.read()
            print("R - Elementos do arquivo:")
            print(userinfo)

            if checar_existencia(regnome, regsenha, userinfo):
                return False
            else:
                newid = str(userinfo.count("ID: "))
                with open(filepath, "a") as file:
                    file.write(
                        f"/\n {{\n  ID: {newid}\n  Nome: {regnome}\n  Senha: {regsenha}\n }}\n/\n")
                print("R - Informações adicionadas ao arquivo com sucesso.")

            with open(filepath, "r") as file:
                userinfo = file.read()
            print("R - Elementos do arquivo adicionado:")
            print(userinfo)
            break
        else:
            with open(filepath, "w") as file:
                file.write("/\n {\n  ID: \n  Nome: \n  Senha: \n }\n/\n")
            print("Arquivo criado com sucesso")

def logaruser(lognome, logsenha):
    filepath = "userinfo.txt"
    if os.path.isfile(filepath):
        with open(filepath, "r") as file:
            userinfo = file.read()
        print("L - Elementos do arquivo:")
        print(userinfo)

        if checar_existencia(lognome, logsenha, userinfo):
            print("Login valido")
            return True
        else:
            print("Login invalido")
            return False
    return False