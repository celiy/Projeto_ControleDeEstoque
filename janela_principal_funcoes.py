import os

def checar_existencia(nome, texto):
    linhas = texto.split('\n')
    for i in range(len(linhas)):
        if linhas[i].strip().startswith("Nome: ") and linhas[i].strip().endswith(nome):
            return True, i
    return None, None

def atualizarestoque(regnome, regquantidade):
    filepath = "estoqueinfo.txt"
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
                    nova_quantidade = quantidade_atual - int(regquantidade)
                    linhas[k] = f"  Quantidade: {nova_quantidade}"
                    break
            produtosinfo = '\n'.join(linhas)
            with open(filepath, "w") as file:
                file.write(produtosinfo)
            print("Quantidade atualizada com sucesso.")

def registrarcliente(nomec,enderecoc):
    def checar_existenciacli(nome, endereco, texto):
        linhas = texto.split('\n')
        for i in range(len(linhas)):
            if linhas[i].strip().startswith("Nome:") and linhas[i].strip().endswith(nome):
                if (i + 1 < len(linhas) and linhas[i + 1].strip().startswith("Endereco:")
                        and linhas[i + 1].strip().endswith(endereco)):
                    return True
        return False

    def registrar(regnome, regendereco):
        filepath = "clientesinfo.txt"
        while True:
            if os.path.isfile(filepath):
                with open(filepath, "r") as file:
                    clientesinfo = file.read()
                print("R - Elementos do arquivo:")
                print(clientesinfo)

                if checar_existenciacli(regnome, regendereco, clientesinfo):
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

    sucesso = registrar(nomec,enderecoc)
    if sucesso == False:
        return False

def registrarproduto(nomep, descricaop, tipop, marcap, quantidadep, userid):

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
                            nova_quantidade = quantidade_atual + int(regquantidade)
                            linhas[k] = f"  Quantidade: {nova_quantidade}"
                            break
                    produtosinfo = '\n'.join(linhas)
                    with open(filepath, "w") as file:
                        file.write(produtosinfo)
                    print("Quantidade atualizada com sucesso.")
                else:
                    # Novo produto, adicionar ao arquivo
                    newid = str(produtosinfo.count("ID: "))
                    with open(filepath, "a") as file:
                        file.write(
                            f"/\n{{\n  ID: {newid}\n  Nome: {regnome}\n  Descricao: {regdescricao}\n  Tipo: {regtipo}\n  Marca: {regmarca}\n  Quantidade: {regquantidade}\n  UserID: {reguserid}\n}}\n/\n")
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

def registrarvenda(nomep, nomec, quantv, preco):

    def registrar(nomepp, nomecc, quantvv, precoo):
        filepath = "vendasinfo.txt"
        while True:
            if os.path.isfile(filepath):
                with open(filepath, "r") as file:
                    produtosinfo = file.read()
                print("R - Elementos do arquivo:")
                print(produtosinfo)
                # Novo produto, adicionar ao arquivo
                newid = str(produtosinfo.count("ID: "))
                with open(filepath, "a") as file:
                    file.write(
                        f"/\n{{\n  IDVenda: {newid}\n  Nome Produto: {nomepp}\n  Nome Cliente: {nomecc}\n"
                        f"  Quantidade: {quantvv}\n  "
                        f"  Preço: {precoo}\n}}\n/\n")
                print("R - Informações adicionadas ao arquivo com sucesso.")

                with open(filepath, "r") as file:
                    produtosinfo = file.read()
                print("R - Elementos do arquivo adicionado:")
                print(produtosinfo)

                atualizarestoque(nomepp, quantvv)

                break
            else:
                with open(filepath, "w") as file:
                    file.write("/\n{\n  IDVenda: \n  Nome Produto: \n  Nome CLiente: \n  Quantidade: \n "
                               "Preço: \n}\n/\n")
                print("Arquivo criado com sucesso")

    registrar(nomep, nomec, quantv, preco)

def somar_precos():
    filepath = "vendasinfo.txt"
    soma_total = 0

    if os.path.isfile(filepath):
        with open(filepath, "r") as file:
            vendasinfo = file.read()

        linhas = vendasinfo.split('\n')
        for linha in linhas:
            if linha.strip().startswith("Preço:"):
                preco_venda = linha.split("Preço: ")[-1].strip()
                try:
                    preco_venda = float(preco_venda)
                    soma_total += preco_venda
                except ValueError:
                    print(f"Valor inválido encontrado: {preco_venda}")

        print(f"O valor total de todos os preços somados é: {soma_total}")
    else:
        print("Arquivo de vendas não encontrado.")

    return soma_total
