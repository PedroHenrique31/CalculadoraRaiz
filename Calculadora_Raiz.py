''' Tentativa de criar uma Calculadora de raiz quadrada baseada em python
    1-utilizando o método de Newton-Raphson
        A(n+1)=[A(n)+n/A(n)]*1/2
Obs: porque não testar com numeros grandes como os dos cartões de credito:
    1-4984011032943903
    2-5234219170632858-794
'''
#TODO: tentar definir o mdc dos numeros pelo algoritmo de euclides
#TODO: Usar objeto para a classe calculadora
#TODO:tratar números negativos
#define função para chue inicial
def calc_ini(Numero):
    n=1
    quadrado=n*n

    while(quadrado<Numero):
        n=n+1
        quadrado=n*n
    return n

##Entrada de dados
numero=int(input("Digite o valor de n\n"))
if(numero<0):
    print("numero negativo não pode ser tratado")
else:
    #inicial=int(input("Digite o menor inteiro cujo quadrado perfeito seja maior que o seu\n"))
    inicial=calc_ini(numero)
    chute_n=inicial
    print("meu chute inicial será ",str(inicial))

##processamento
    teto_superior=100
    for n in range(0,teto_superior):
        chute_n=(chute_n+(numero/chute_n))*(1/2)
##Saída
    print("A raiz é ",chute_n)
