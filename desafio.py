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
    
    
print(salario)
# Solicite ao usuario que digite o valor do bônus recebido

# bonus = float(input("Digite seu bonus: "))

# Calcule o valor do bônus final

# final_bonus = (salario*bonus)

# Imprima o cálculo do KPI para o usuário
# Imprima a mensagem personalizada incluindo o nome do usuário, e o valor do bônus
# kpi_2 = (bonus_2024 + final_bonus)
# kpi = str(bonus_2024 + final_bonus)
# print( "Olá "+ nome +" seu KPI do bônus de 2024 é de " + kpi + " Reais")
# print(f"Oi {nome} seu bônus ficou em {kpi_2} reais")
