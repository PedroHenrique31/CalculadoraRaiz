''' Tentativa de criar uma Calculadora de raiz quadrada baseada em python
    1-utilizando o método de Newton-Raphson
        A(n+1)=[A(n)+n/A(n)]*1/2
    2-O método de Newton-Raphson usa a seguinte formula para se aproximar do resultado

Obs: porque não testar com numeros grandes como os dos cartões de credito:
    1-4984011032943903
    2-5234219170632858-794
'''
#TODO: tentar definir o mdc dos numeros pelo algoritmo de euclides
#TODO: Usar objeto para a classe calculadora
#TODO:tratar números negativos
#TODO:Calcular raízes genéricas

#####################################define as funções necessárias ao processamento#####################################
#Calcula a raiz
def raiz_quadrada(incognita):
    chute=calc_ini(incognita)
    teto_superior=100
    for n in range(0,teto_superior):
        chute=(chute+(numero/chute))*(1/2)
    return chute
#Calcula o chute inicial
def calc_ini(Numero):
#TODO:Otimizar a procura, talvez procura binaria, para reduzir os numeros buscados
    n=1
    quadrado=n*n
    while(quadrado<Numero):
        n=n+1
        quadrado=n*n
    return n
#Valor de precisão para parada
precisao=0.00001
#Calcula se o calculo já tá preciso
def defina_precisao(anterior, atual):
    resposta=False
    valor_teste=anterior-atual
    if(valor_teste<=precisao):
        resposta=True
    else:
        resposta=False
    return resposta

#calcula a raiz de outro jeito
def calcula_raiz_limite(entrada):

    teste=False #Definição de variavel teste para ser iterado
    while(teste==False):
        tmp=chute_n #armazena o valor atual de chute_n para posterior calculo
        chute_n=(chute_n+(numero/chute_n))*(1/2) #calcula chute_n
        teste=defina_precisao(tmp,chute_n) #valor bool que avalia se já ta preciso
    return chute_n
#Trata o numero antes do calculo
def pre_calc(numero):
    resposta=False
    if(numero<0):
        print("numero negativo não pode ser tratado")
        numero_positivo=numero*(-1)
        print("Você quis dizer {}".format(numero_positivo))
        condicao=input("(S/N): ")

        if(condicao=='S' or condicao== 's'):
            print("OK")
        else:
            print("então foda-se\n")
    else:
        resposta=True
    return resposta

#################################Entrada de dados######################################################################
numero = int(input("Digite o valor de n\n"))
#Tratamentos antes do calculo
procedencia=False
procedencia=pre_calc(numero)
if(procedencia==False):
    print("Não faço!!")
    Resultado='Não existe!!'
else:#Só avança para o processamento se estiver tudo certo
    print("OK,Eu faço pra você")

###############################processamento############################################################################

    Resultado=raiz_quadrada(numero)

################################ Saída #################################################################################
print("A raiz é ",Resultado)
