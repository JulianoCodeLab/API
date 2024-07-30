#---------------------------------Decoradores-----------------------------
import functools

#Tem a capacidade de transformar "embrulhar" uma função
#--- pode ser usado para autenticação de usuario 

def meu_decorador(funcao):

    #embrulhe minha função
    @functools.wraps(funcao) 
    def func_que_roda_funcao():
        print("******** Embrulhando funcao no decorador! ************")

        #depois de rodar algum codigo, você roda a função
        funcao()

        #depois de rodar a função podemos rodar algum outro codigo
        print("***** fechando embrulho ******* ")

    #função principal
    return func_que_roda_funcao



#---------------------------Como usar a funcao ----------------------------

#crio uma funcao
def minha_funcao():
    print('Eu sou uma funcao!')

minha_funcao()

#Se eu tiver um decorador
@meu_decorador
    def minha_funcao():
        print('Eu sou uma funcao!')

    minha_funcao()