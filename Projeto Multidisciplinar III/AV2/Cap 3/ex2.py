"""
Exercício 2: Reescreva seu programa de pagamento utilizando try e
except, de forma que o programa consiga lidar com entradas não numéricas graciosamente,
mostrando uma mensagem e saindo do programa. A seguir é mostrado duas execuções do programa

Digite as Horas: 20
Digite a taxa: nove
Erro, por favor utilize uma entrada numérica

Digite as Horas: quarenta
Erro, por favor utilize uma entrada numérica
"""

horas = input("Informe as horas: ")
taxa = input("Informe a taxa: ")
try:
    horas = int(horas)
    taxa = float(taxa)

    servico = horas * taxa
    print(f'Horas: {horas}, taxa: R${taxa}, valor do serviço: R${servico}')
except ValueError:
    print("Erro, por favor utilize uma entrada numérica")
