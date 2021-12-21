from estrutura import cabecalho
from estrutura import escolha_operacao

parar = "S"

while parar == "S":
    cabecalho() # chama cabeçalho

    escolha_operacao() # chama estrutura

    parar = str(input("Deseja Calcular novamente (S) SIM ou (N) não: ")).upper()


'''git'''




