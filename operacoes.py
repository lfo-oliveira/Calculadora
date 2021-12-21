def adicao():
    try:
        n1 = float(input("Entre com o primeiro número da soma: "))
        n2 = float(input("Entre com o segundo número da soma: "))
        soma = n1 + n2
        print(f"Soma entre {n1} + {n2} é {soma}")
    except:
        print("Favor digitar um número valdio:")

def subtracao():
    try:
        n1 = float(input("Entre com o primeiro número da subtração: "))
        n2 = float(input("Entre com o segundo número da subtração: "))
        diferenca = n1 - n2
        print(f"A subtração entre {n1} - {n2} é {diferenca}")
    except:
        print("Favor digitar um número valdio:")
        subtracao()

def divisao():
    try:
        dividento = float(input("Entre com o primeiro número da divisão: "))
        divisor = float(input("Entre com o segundo número da divisão"))
        if(divisor == 0):
            print("Não existe divisão por ZERO. Favor digitar um número valido!")
            divisao()
        else:
            quociente = dividento / divisor
            print(F"O Cociente de {divisor} dividido por {divisor} é {quociente}")
    except:
        print("Favor digitar um número valdio:")
        divisao()

def multiplicacao():
    try:
        fator1 = float(input("Entre com o primeiro numero a ser multiplicado: "))
        fator2 = float(input("Entre com o segundo numero a ser multiplicado: "))
        produto = fator1 * fator2
        print(f"O resultado da multiplicação de {fator1} por {fator2} é {produto}!")
    except:
        print("Favor digitar um número valdio:")
        multiplicacao()

'''testes de comit'''