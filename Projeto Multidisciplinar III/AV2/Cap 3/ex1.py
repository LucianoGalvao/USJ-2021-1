"""
Exercício 1: Reescreva seu programa de pagamento, para pagar ao funcionário 1.5
vezes o valor da taxa horária de pagamento pelo tempo trabalhado acima de 40 horas
Digite as Horas: 45
Digite a taxa: 10
Pagamento: 475.0
"""

horas = int(input("Informe as horas: "))
taxa = float(input("Informe a taxa: "))
if horas > 40:
    taxaExtra = taxa * 1.5
    horasExtra = horas - 40
    comissao = horasExtra * taxaExtra
    servico = (40 * taxa) + comissao
    print(f'Horas: {horas}, taxa: R${taxa}, horas extras: {horasExtra}, valor da comissão: R${comissao} valor do '
          f'serviço: R${servico}')
else:
    servico = horas * taxa
    print(f'Horas: {horas}, taxa: R${taxa}, valor do serviço: R${servico}')

