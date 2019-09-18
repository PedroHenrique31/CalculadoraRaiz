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

#####################################define as funções necessárias ao processamento####################################
import Calculator

#################################Entrada de dados######################################################################
'''     Nessa parte fazemos testes para tratar excessões numéricas tais quais números negativos

'''
numero = int(input("Digite o valor de n\n"))
#Tratamentos antes do calculo
procedencia=False
procedencia=Calculator.pre_calc(numero)
if(procedencia==False):
    print("Não faço!!")
    Resultado='Não existe!!'
else:#Só avança para o processamento se estiver tudo certo
    print("OK,Eu faço pra você")

###############################processamento############################################################################

    ##Resultado=Calculator.raiz_quadrada(numero)
    #Resultado=Calculator.calcula_raiz_limite(numero)
    Resultado=Calculator.calcula_raiz_generica(numero,2)
################################ Saída #################################################################################
print("A raiz é ",Resultado)
