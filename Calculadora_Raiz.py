''' Tentativa de criar uma Calculadora de raiz quadrada baseada em python
    1-utilizando o método de Newton-Raphson
        A(n+1)=[A(n)+n/A(n)]*1/2
    2-O método de Newton-Raphson usa a seguinte formula para se aproximar do resultado

Obs: porque não testar com numeros grandes como os dos cartões de credito:
    1-5234213942469343
    2-5234219170632858-794
    3-4984236077624809
    4-5502096247409121-025
'''
#TODO: Melhorar a interface com usuário para organizar as funções.
#TODO:tratar números negativos

#####################################define as funções necessárias ao processamento####################################
import Calculator

#################################Entrada de dados######################################################################
'''     Nessa parte fazemos testes para tratar excessões numéricas tais quais números negativos, para as raízes pares

'''
print("Ola o que voce deseja fazer\n(1)Calcular uma raiz quadrada\n(2)Calcular uma raiz generica\n(3)Calcular o mdc de dois numeros.\n")
opcao=int(input("Digite a opção desejada: "))

numero = 3#só pra não perder
#Tratamentos antes do calculo
###############################processamento############################################################################
    #TODO: melhorar essa interface
    ##Resultado=Calculator.raiz_quadrada(numero)
if(opcao==1):
        numero=int(input("Qual o número  desejas saber a raiz?\n"))
        Resultado=Calculator.calcula_raiz_limite(numero)
        mdc='Não calculado!'
elif(opcao==2):
        numero=int(input("Digite o valor que quer calcular\n"))
        grau=int(input("Digite o grau da raiz que deseja calcular\n(Apenas valores inteiros são aceitos)\n"))
        Resultado=Calculator.calcula_raiz_generica(numero,grau)
        mdc = 'Não calculado!'
elif(opcao==3):
        numero=int(input("Digite os valores que quer calcular\n"))
        grau=int(input("Agora o segundo numero:"))
        mdc=Calculator.mdc(numero,grau)
        Resultado=mdc
else:
        mdc='NÃO SELECIONADO!'
        Resultado='NÃO SELECIONADO!'

################################ Saída #################################################################################
print("A raiz é ",Resultado)
print("E o mdc deles é {}".format(mdc))
print("Obrigado por tudo,tchau!!:) :* bjão\n")