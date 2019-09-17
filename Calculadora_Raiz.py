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

#define função para chue inicial
def calc_ini(Numero)
#TODO:Otimizar a procura, talvez procura binaria, para reduzir os numeros buscados
    n=1
    quadrado=n*n

    while(quadrado<Numero):
        n=n+1
        quadrado=n*n
    return n

##Entrada de dados

'''
    Função calculadora de raízes quadradasbaseada no método de Newton-Raphson
    Antes de ser ativada é necessário alguns processamentos para evitar exceçoes
        1-Não tratar numeros negativos
        2-deifinir um bom chute inicial
    
'''
numero=int(input("Digite o valor de n\n"))
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
    inicial=calc_ini(numero)
    chute_n=inicial
    print("meu chute inicial será ",str(inicial))

##processamento
'''Declaração modular da função de calcula raiz quadrada'''
def raiz_quadrada(incognita):
    chute=calc_ini(incognita)
    teto_superior=100
    for n in range(0,teto_superior):
        chute=(chute+(numero/chute))*(1/2)
    return chute
chute_n=raiz_quadrada(numero)
##Saída
print("A raiz é ",chute_n)
