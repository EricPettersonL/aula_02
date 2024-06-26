# Exercício 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
# O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, 
# garantir que a entrada seja numérica, tratando qualquer ValueError. 
# Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

temperatura_celsius = input("Digite a temperatura em graus celsius: ")

try:
    temperatura_celsius = float(temperatura_celsius)
    temperatura_fahrenheit = (1.8 * temperatura_celsius) + 32
    print(f"A temperatura em Fahrenheit é: {temperatura_fahrenheit}")
except ValueError:
    print("Entrada inválida. Por favor, digite um número.")
    
    
# Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo 
# (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
# Utilize try-except para garantir que a entrada seja uma string. 
# Dica: Utilize a função isinstance() para verificar o tipo da entrada.

palavra = input("Digite uma palavra ou frase: ")

try:
    if isinstance(palavra, str):
        formatada = palavra.lower().replace(" ", "").replace(".", "")
        if formatada == formatada[::-1]:
            print("A palavra ou frase é um palíndromo.")
        else:
            print("A palavra ou frase não é um palíndromo.")
    else:
        print("Entrada inválida. Por favor, digite uma string.")
except ValueError:
    print("Entrada inválida. Por favor, digite uma string.")


# Exercício 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
# Use try-except para lidar com divisões por zero e entradas não numéricas. 
# Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
# Imprima o resultado ou uma mensagem de erro apropriada.

numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")
operador = input("Digite o operador (+, -, *, /): ")

try:
    numero1 = float(numero1)
    numero2 = float(numero2)
    if operador == "+":
        resultado = numero1 + numero2
    elif operador == "-":
        resultado = numero1 - numero2
    elif operador == "*":
        resultado = numero1 * numero2
    elif operador == "/":
        if numero2 == 0:
            print("Erro: divisão por zero.")
            exit()
        else:
            resultado = numero1 / numero2
    else:
        print("Operador inválido.")
        exit()
    print(f"O resultado da operação {numero1} {operador} {numero2} = {resultado}")
except ValueError:
    print("Entrada inválida. Por favor, digite um número.")

# Exercício 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. 
# Utilize try-except para assegurar que a entrada seja numérica e utilize 
# if-elif-else para classificar o número como "positivo", "negativo" ou "zero". 
# Adicionalmente, identifique se o número é "par" ou "ímpar".

numero = input("Digite um número: ")

try:
    numero = float(numero)
    if numero > 0:
        print("O número é positivo.")
    elif numero < 0:
        print("O número é negativo.")
    else:
        print("O número é zero.")
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
except ValueError:
    print("Entrada inválida. Por favor, digite um número.")

# Exercício 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
# O programa deve converter a string de entrada em uma lista de números inteiros. 
# Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. 
# Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. 
# Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

lista_usuario = input("Digite uma lista de números separados por virgulas: ")

try:
    lista = [int(num) for num in lista_usuario.split(",")]
    print("Lista de inteiros:", lista)
except ValueError:
    print("Entrada inválida. Por favor, digite uma lista de números separados por virgulas.")


