bonus_2024 = 1000

# Solicite ao usuario que digite seu nome
# Verificar se o nome foi preenchido
# Verificar se o nome não contém apenas espacos em branco	
# Verificar se o nome não contem números

nome = input("Digite seu nome: ")

if nome == "":
    print("O nome deve ser preenchido")
elif nome.isspace():
    print("O nome não deve conter apenas espaços em branco")
elif any(char.isdigit() for char in nome):
    print("Seu nome deve conter apenas letras")
    exit()

# Solicite ao usuario que digite o valor do seu salário
# Verificar se o valor do salário foi preenchido
# Verificar se o valor do salário é um número
# Verificar se o valor do salário é maior que zero

salario = input("Digite seu salario: ")

try:
    if salario == "":
        print("O valor do salario deve ser preenchido")
        exit()
    salario = float(salario)
    if float(salario) <= 0:
        print("O valor do salario deve ser maior que zero")
        exit()
except ValueError:
    print("O valor do salario deve ser um numero")
    
# Solicite ao usuario que digite o valor do bônus recebido
# Verificar se o valor do salário foi preenchido
# Verificar se o valor do salário é um número
# Verificar se o valor do salário é maior que zero

bonus = input("Digite seu bonus: ")

try:
    if bonus == "":
        print("O valor do bonus deve ser preenchido")
        exit()
    bonus = float(bonus)
    if float(bonus) <= 0:
        print("O valor do bonus deve ser maior que zero")
        exit()
except ValueError:
    print("O valor do bonus deve ser um número")

# Calcule o valor do bônus final

final_bonus = (salario*bonus)

# Imprima o cálculo do KPI para o usuário
# Imprima a mensagem personalizada incluindo o nome do usuário, e o valor do bônus

kpi_2 = (bonus_2024 + final_bonus)
print(f"Oi {nome} seu bônus final ficou em {kpi_2:.2f} reais")
