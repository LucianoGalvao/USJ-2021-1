"""
Exercício 3: Escreva um programa que peça por uma pontuação entre
0.0 e 1.0. Se a pontuação for fora do intervalo, mostre uma mensagem
de erro. Se a pontuação estiver entre 0.0 e 1.0, mostre a respectiva nota usando a seguinte tabela

Pontuação Nota
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F

Digite a Pontuação: 0.95
A

Digite a Pontuação: perfeito
Pontuação Inválida

Digite a Pontuação: 10.0
Pontuação Inválida

Digite a Pontuação: 0.75
C
Digite a Pontuação: 0.5
F

Rode o programa repetidamente como mostrado acima para testar diferentes valores de entrada.
"""
print("Digite 'fim' para acabar")
pontuacao = input("Informe a pontuação (Entre 0.0 e 1.0): ").lower()
while pontuacao != "fim":
    try:
        pontuacao = float(pontuacao)
        if 1.0 >= pontuacao >= 0.9:
            nota = "A"
            print(f'Pontuação: {pontuacao} | Nota: {nota}')
        elif 0.9 >= pontuacao >= 0.8:
            nota = "B"
            print(f'Pontuação: {pontuacao} | Nota: {nota}')
        elif 0.8 >= pontuacao >= 0.7:
            nota = "C"
            print(f'Pontuação: {pontuacao} | Nota: {nota}')
        elif 0.7 >= pontuacao >= 0.6:
            nota = "D"
            print(f'Pontuação: {pontuacao} | Nota: {nota}')
        elif 0.6 >= pontuacao >= 0.5:
            nota = "F"
            print(f'Pontuação: {pontuacao} | Nota: {nota}')
        else:
            print("Pontuação Inválida")
        pontuacao = input("Informe a pontuação (Entre 0.0 e 1.0): ")
    except ValueError:
        print("Pontuação Inválida")
        pontuacao = input("Informe a pontuação (Entre 0.0 e 1.0): ")
