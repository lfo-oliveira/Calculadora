from operacoes import adicao
from  operacoes import subtracao
from operacoes import  divisao
from operacoes import  multiplicacao


def cabecalho():
    print("-" * 42)
    print("-" * 6, " Minha primeira Calculadora ", "-" *6)
    print("-" * 42)

def escolha_operacao():
    print("Escolha qual a operação deseja executar")
    print("(1) Soma      (2) Subtração")
    print("(3) Divisão   (4) Multiplicação")
    operacao = int(input("Entre com o número da operação que deseja realizar: "))
    if (operacao == 1):
        adicao()

    elif (operacao == 2):
        subtracao()

    elif (operacao == 3):
        divisao()

    elif (operacao == 4):
        multiplicacao()

    else:
        print("Você não escolheu uma operação valida, Escolha novamente")
        print("*" * 42)
        escolha_operacao()

