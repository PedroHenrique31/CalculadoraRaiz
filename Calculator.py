"""                             Calculadora de raízes Python
            Repositório de funções para calcular raízes genéricas em Python, usando principalemnte
o método de Newton-Raphson, que consiste da seguinte fórmula:
        X(n+1)=X(n)-[f(X(n)/f'(X(n)]
    Onde,
    n pertence aos naturais;
    f(x) é a função X**n-q=0, cuja a raiz é a raiz enesima de q;
    X(n) é o enésimo valor de x;
"""
#TODO:criar função para raiz generica aqui
#Calcula a raiz
def raiz_quadrada(incognita):
    chute=calc_ini(incognita)
    teto_superior=100
    for n in range(0,teto_superior):
        chute=(chute+(incognita/chute))*(1/2)
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

    chute_n=calc_ini(entrada)
    teste=False #Definição de variavel teste para ser iterado
    while(teste==False):
        tmp=chute_n #armazena o valor atual de chute_n para posterior calculo
        chute_n=(chute_n+(entrada/chute_n))*(1/2) #calcula chute_n
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
#Calcula uma raiz de grau n qualquer
#TODO:Melhorar a busca por um chute inicial ao invés de um chute fixo.
#TODO:Solucionar o problema da parada ela precisão e não por iterações fixas.
def calcula_raiz_generica(numero,grau):
    teto_superior=100
    palpite=100
    def funcao(enesimo):
        f=0
        f=(enesimo**grau)-numero
        return f
    def derivada_funcao(enesimo):
        f=0
        f=grau*(enesimo**(grau-1))
        return f
    for n in range(0,teto_superior):
        func=funcao(palpite)
        dervfunc=derivada_funcao(palpite)
        print("func={} dervfunc={} Raiz={} \n".format(func,dervfunc,palpite))
        palpite=(palpite-(func/dervfunc))
    return palpite

'''
def calcula_raiz_generica(numero,grau):#grau é a n raiz, se grau=2 a raiz é quadrada
    teto_superior=1000
    palpite=1
    def funcao(enesimo):
        f=0
        f=(enesimo**grau)-numero
        return f

    def funcao_derivada(enesimo):
        f=grau*(enesimo**(grau-1))
        return f

    for n in range(0,teto_superior):
        func=funcao(palpite)
        dervfunc=funcao_derivada(palpite)
        palpite=(palpite+(func/dervfunc)

    return palpite
'''