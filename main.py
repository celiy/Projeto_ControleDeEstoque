from janela_login import *
from janela_principal import *

print("Executando janela de login.")
#Executa a função no modulo janela_login para realizar o login ou cadastro do usuario
userid = iniciarlogin()

#Se o id for retornado do login for valido, ele ira iniciar o programa normalmente
if len(userid) >= 1:
    print("ID do usuario logado: "+userid)
    iniciarjanela(userid)