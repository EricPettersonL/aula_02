# Import Library
import statistics
import math

# # Exercícios

# # Inteiros (int)
# # 1.Escreva um programa que soma dois números inteiros inseridos pelo usuário.

numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite outro número inteiro: "))
soma = numero1 + numero2
print(f"A soma de {numero1} + {numero2} = {soma}")

# # 2.Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

numero3 = int(input("Digite um número inteiro: "))
resto = numero3 % 5
print(f"O resto da divisão de {numero3} por 5 = {resto}")

# # 3.Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

numero4 = int(input("Digite um número inteiro: "))
numero5 = int(input("Digite outro número inteiro: "))
multiplicacao = numero4 * numero5
print(f"A multiplicação de {numero4} * {numero5} = {multiplicacao}")

# # 4.Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

numero6 = int(input("Digite um número inteiro: "))
numero7 = int(input("Digite um outro número inteiro: "))
divisao_inteira = numero6 // numero7
print(f"O número {numero6} dividido pelo número {numero7} é igual a: {divisao_inteira} inteiros")

# # 5.Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

numero8 = int(input("Digite um número inteiro: "))
quadrado_de_um_numero = numero8 ** 2
print(f"O quadrado do {numero8} é: {quadrado_de_um_numero}")

# #Números de Ponto Flutuante (float)

# # 6.Escreva um programa que receba dois números flutuantes e realize sua adição.

numero9 = float(input("Digite um número: "))
numero10 = float(input("Digite outro número: "))
soma_float = numero10 + numero9
print(f"A soma do {numero9} e o {numero10} é = {soma_float}") 

# # 7.Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

numero11 = float(input("Digite um número: "))
numero12 = float(input("Digite outro número: "))
media = statistics.median([numero11, numero12])
print(f"A media do {numero11} e do {numero12} é: {media}")

# # 8.Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

numero_13 = float(input("Digite um número pra ser a base: "))
numero_14 = float(input("Digite um número pra ser o expoente: "))
potencia = numero_13 ** numero_14
print(f"O número {numero_13} elevado ao expoente {numero_14} é: {potencia}")

# # 9.Faça um programa que converta a temperatura de Celsius para Fahrenheit.

temperatura_celsius = float(input("Digite a temperatura em graus celsius: "))
temperatura_fahrenheit = (1.8 * temperatura_celsius) + 32
print(f"A temperatura de {temperatura_celsius}° celsius é {temperatura_fahrenheit}° em Fahrenheit")

# # 10.Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

raio = float(input("Digite o raio da sua circunferencia: "))
area_circulo = (math.pi * (raio**2))
print(f"A área da sua circunferencia é: {area_circulo}")

# Strings (str)

# 11.Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

string_maiuscula = input("Digite uma palavra: ")
resultado = string_maiuscula.upper()
print(f"A palavra {string_maiuscula} convertida para maiúsculas é: {resultado}")

# 12.Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

nome_completo = input("Digite seu nome completo: ")
nome_minusculo = nome_completo.lower()
print(f"Seu nome em letras minúsculas é: {nome_minusculo}")

# 13.Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

frase = input("Digite uma frase: ")
frase_sem_espacos = frase.strip()
print(f"A frase sem espaços em branco é: {frase_sem_espacos}")


# 14.Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data_usuario = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data_usuario.split("/")
print(f"Data: o dia é {dia}, o mês é {mes} e o ano é {ano}")

# 15.Escreva um programa que concatene duas strings fornecidas pelo usuário.

palavra1 = input("Digite uma palavra: ")
palavra2 = input("Digite mais uma palavra: ")
conctenacao = palavra1 + palavra2
print(f"A concatenação de {palavra1} e {palavra2} é: {conctenacao}")

# Booleanos (bool)

# 16.Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

exp_bool = input("Digite uma expressão booleana: ").title().endswith("True",0)
exp_bool2 = input("Digite mais uma expressão booleana: ").title().endswith("True",0)
resultado = exp_bool and exp_bool2
print(f"A expressão {exp_bool} e {exp_bool2} retornam o valor {resultado} de operação AND")

# 17.Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

exp_bool3 = input("Digite uma expressão booleana: ").title().endswith("True",0)
exp_bool4 = input("Digite mais uma expressão booleana: ").title().endswith("True",0)
resultado_2 = exp_bool3 or exp_bool4
print(f"A expressão {exp_bool3} e {exp_bool4} retornam o valor {resultado_2} de operação OR")

# 18.Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

exp_bool5 = input("Digite uma expressão booleana: ").title().endswith("True",0)
resultado_3 = not exp_bool5
print(f"A expressão {exp_bool5} retornou o valor {resultado_3} de operação NOT")

# 19.Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

numero_15 = int(input("Digite um número: "))
numero_16 = int(input("Digite outro número: "))
igual = numero_15 == numero_16
print(f"Os números {numero_15} e {numero_16} sao iguais? {igual}")

# 20.Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

numero_17 = int(input("Digite um número: "))
numero_18 = int(input("Digite outro número: "))
diferentes = numero_17 != numero_18
print(f"Os números {numero_17} e {numero_18} sao diferentes? {diferentes}")