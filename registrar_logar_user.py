import os

def checar_existencia(nome, senha, texto):
    linhas = texto.split('\n')
    for i in range(len(linhas)):
        if linhas[i].strip().startswith("Nome:") and linhas[i].strip().endswith(nome):
            if i + 1 < len(linhas) and linhas[i + 1].strip().startswith("Senha:") and linhas[i + 1].strip().endswith(
                    senha):
                for j in range(i, -1, -1):
                    if linhas[j].strip().startswith("ID:"):
                        print("ID do checar existencia: " + str(linhas[j].strip().split("ID: ")[-1]))
                        return linhas[j].strip().split("ID: ")[-1]
    return None


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
    return True

#Esta função executa o processo de verificar se o login do usuário é válido
def logaruser(lognome, logsenha):
    #Checa se o arquivo com as informações do login existem
    filepath = "userinfo.txt"
    if os.path.isfile(filepath):
        with open(filepath, "r") as file:
            userinfo = file.read()
        #Mostra as informações do arquivo
        print("L - Elementos do arquivo:")
        print(userinfo)

        #Checa se o login é válido e retorna o id do usuário logado
        useridrlu = str(checar_existencia(lognome, logsenha, userinfo))
        useridrlu.replace("ID:", "")
        print("UserID retornado do login: " + useridrlu)
        if "ID:" in useridrlu:
            return False
        else:
            return str(useridrlu)
    return False
