''' Tentativa de criar uma Calculadora de raiz quadrada baseada em python
    1-utilizando o método de Newton-Raphson
        A(n+1)=[A(n)+n/A(n)]*1/2
    2-O método de Newton-Raphson usa a seguinte formula para se aproximar do resultado

Obs: porque não testar com numeros grandes como os dos cartões de credito:
    1-4984011032943903
    2-5234219170632858-794
'''
#TODO: Melhorar a interface com usuário para organizar as funções.
#TODO:tratar números negativos

#####################################define as funções necessárias ao processamento####################################
import Calculator

#################################Entrada de dados######################################################################
'''     Nessa parte fazemos testes para tratar excessões numéricas tais quais números negativos

'''
print("Ola o que voce deseja fazer\n(1)Calcular uma raiz quadrada\n(2)Calcular uma raiz generica\n(3)Calcular o mdc de dois numeros.\n")
opcao=int(input("Digite a opção desejada"))

numero = 3#só pra não perder
#Tratamentos antes do calculo
###############################processamento############################################################################

    ##Resultado=Calculator.raiz_quadrada(numero)
    #Resultado=Calculator.calcula_raiz_limite(numero)
    grau=int(input("Digite o grau da raiz que deseja calcular\n(Apenas valores inteiros são aceitos)\n"))
    #Resultado=Calculator.calcula_raiz_generica(numero,grau)
    mdc=Calculator.mdc(numero,grau)

################################ Saída #################################################################################
#print("A raiz é ",Resultado)
print("E o mdc deles é {}".format(mdc))