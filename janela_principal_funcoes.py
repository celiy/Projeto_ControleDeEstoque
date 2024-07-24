import os

def registrarcliente(nomec,enderecoc):
    def checar_existencia(nome, endereco, texto):
        linhas = texto.split('\n')
        for i in range(len(linhas)):
            if linhas[i].strip().startswith("Nome:") and linhas[i].strip().endswith(nome):
                if i + 1 < len(linhas) and linhas[i + 1].strip().startswith("Endereco:") and linhas[i + 1].strip().endswith(endereco):
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
                            f"/\n {{\n  ID: {newid}\n  Nome: {regnome}\n  Endereco: {regendereco}\n }}\n/\n")
                    print("R - Informações adicionadas ao arquivo com sucesso.")

                with open(filepath, "r") as file:
                    clientesinfo = file.read()
                print("R - Elementos do arquivo adicionado:")
                print(clientesinfo)
                break
            else:
                with open(filepath, "w") as file:
                    file.write("/\n {\n  ID: \n  Nome: \n  Endereco: \n }\n/\n")
                print("Arquivo criado com sucesso")

    registrar(nomec,enderecoc)

def registrarproduto(nomep, descricaop, tipop, marcap, quantidadep, userid):
    def checar_existencia(nome, texto):
        linhas = texto.split('\n')
        for i in range(len(linhas)):
            if linhas[i].strip().startswith("Nome:") and linhas[i].strip().endswith(nome):
                for j in range(i, -1, -1):
                    if linhas[j].strip().startswith("ID:"):
                        print("ID do checar existencia: " + str(linhas[j].strip().split("ID: ")[-1]))
                        return linhas[j].strip().split("ID: ")[-1], i
        return None, None

    def registrarprod(regnome, regdescricao, regtipo, regmarca, regquantidade, reguserid):
        filepath = "estoqueinfo.txt"
        while True:
            if os.path.isfile(filepath):
                with open(filepath, "r") as file:
                    produtosinfo = file.read()
                print("R - Elementos do arquivo:")
                print(produtosinfo)

                id_existente, index = checar_existencia(regnome, produtosinfo)

                if id_existente:
                    # Produto já existe, adicionar a quantidade
                    linhas = produtosinfo.split('\n')
                    for k in range(index, len(linhas)):
                        if linhas[k].strip().startswith("Quantidade:"):
                            quantidade_atual = int(linhas[k].strip().split("Quantidade: ")[-1])
                            nova_quantidade = quantidade_atual + regquantidade
                            linhas[k] = f"  Quantidade: {nova_quantidade}"
                            break
                    produtosinfo = '\n'.join(linhas)
                    with open(filepath, "w") as file:
                        file.write(produtosinfo)
                    print("Quantidade atualizada com sucesso.")
                else:
                    newid = str(produtosinfo.count("ID: "))
                    with open(filepath, "a") as file:
                        file.write(
                            f"/\n{{\n  | ID: {newid}\n  | Nome: {regnome}\n  | Descricao: {regdescricao}\n  | Tipo: {regtipo}\n  | Marca: {regmarca}\n  | Quantidade: {regquantidade}\n  | UserID: {reguserid}\n}}\n/\n")
                    print("R - Informações adicionadas ao arquivo com sucesso.")

                with open(filepath, "r") as file:
                    produtosinfo = file.read()
                print("R - Elementos do arquivo adicionado:")
                print(produtosinfo)
                break
            else:
                with open(filepath, "w") as file:
                    file.write("/\n{\n  ID: \n  Nome: \n  Descricao: \n  Tipo: \n  Marca: \n  Quantidade: \n  UserID: \n}\n/\n")
                print("Arquivo criado com sucesso")

    registrarprod(nomep, descricaop, tipop, marcap, quantidadep, userid)