from janela_login import *
from janela_principal import *

print("Executando janela de login.")
#Executa a função no modulo janela_login para realizar o login ou cadastro do usuario
if iniciarlogin():
    # Se o login for um sucesso, ele irá executar esta função do modulo janela_principal para executar o app
    iniciarjanela()