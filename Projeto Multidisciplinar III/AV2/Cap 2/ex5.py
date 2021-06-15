"""
Exercício 5: Escreva um programa que solicite ao usuário uma temperatura
Celsius, converta para Fahrenheit, e mostre a temperatura convertida.

Fórmula Celsius -> Fahrenheit
(x(ºC) * 9/5) + 32 = y(ºF)
"""

celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = (celsius * (9/5)) + 32
print(f'Graus Celsius: {celsius}ºC | Graus Fahrenheit: {fahrenheit}ºF')
