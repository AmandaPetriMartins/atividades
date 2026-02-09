num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero"
else:
    resultado = "Operação inválida"

print("Resultado:", resultado)



quantidade = int(input("Quantos alunos há na turma? "))
soma = 0

for i in range(quantidade):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    soma += nota

media = soma / quantidade

print("Média da turma:", round(media, 2))




senha = input("Digite sua senha: ")

tem_numero = False

for caractere in senha:
    if caractere.isdigit():
        tem_numero = True

if len(senha) >= 8 and tem_numero:
    print("Senha válida")
else:
    print("Senha inválida")
    print("A senha deve ter pelo menos 8 caracteres e conter ao menos um número.")



pares = 0
impares = 0

while True:
    numero = int(input("Digite um número (0 para sair): "))

    if numero == 0:
        break

    if numero % 2 == 0:
        print("Número par")
        pares += 1
    else:
        print("Número ímpar")
        impares += 1

print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)




