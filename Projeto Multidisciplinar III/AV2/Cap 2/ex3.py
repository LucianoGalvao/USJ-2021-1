"""
Exercício 3: Escreva um programa que solicite ao usuário as horas e o
valor da taxa por horas para calcular o valor a ser pago por horas de
serviço.
Digite as horas: 35
Digite a taxa: 2.75
Valor a ser pago: 96.25
"""

horas = int(input("Informe as horas: "))
taxa = float(input("Informe a taxa: "))
servico = horas * taxa
print(f'Horas: {horas}, taxa: R${taxa}, valor do serviço: R${servico}')
