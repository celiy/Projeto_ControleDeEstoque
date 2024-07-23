import os

def registrarcliente(nomec,enderecoc):
    def checar_existencia(nome, endereco, texto):
        linhas = texto.split('\n')
        for i in range(len(linhas)):
            if linhas[i].strip().startswith("Nome:") and linhas[i].strip().endswith(nome):
                if i + 1 < len(linhas) and linhas[i + 1].strip().startswith("Endereço:") and linhas[i + 1].strip().endswith(endereco):
                    for j in range(i, -1, -1):
                        if linhas[j].strip().startswith("ID:"):
                            print("ID do checar existencia: " + str(linhas[j].strip().split("ID: ")[-1]))
                            return linhas[j].strip().split("ID: ")[-1]
        return None

    def registrar(regnome, regendereco):
        filepath = "clientesinfo.txt"
        while True:
            if os.path.isfile(filepath):
                with open(filepath, "r") as file:
                    clientesinfo = file.read()
                print("R - Elementos do arquivo:")
                print(clientesinfo)

                if checar_existencia(regnome, regendereco, clientesinfo):
                    return False
                else:
                    newid = str(clientesinfo.count("ID: "))
                    with open(filepath, "a") as file:
                        file.write(
                            f"/\n {{\n  ID: {newid}\n  Nome: {regnome}\n  Endereço: {regendereco}\n }}\n/\n")
                    print("R - Informações adicionadas ao arquivo com sucesso.")

                with open(filepath, "r") as file:
                    clientesinfo = file.read()
                print("R - Elementos do arquivo adicionado:")
                print(clientesinfo)
                break
            else:
                with open(filepath, "w") as file:
                    file.write("/\n {\n  ID: \n  Nome: \n  Endereço: \n }\n/\n")
                print("Arquivo criado com sucesso")

    registrar(nomec,enderecoc)