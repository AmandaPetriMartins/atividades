def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """Retorna o valor da gorjeta baseado no total da conta e na porcentagem desejada."""
    return valor_conta * (porcentagem_gorjeta / 100)


# Exemplo de uso:
conta = 120.00
porc = 10
print("Gorjeta: R$", round(calcular_gorjeta(conta, porc), 2))



def eh_palindromo(texto: str) -> bool:
    # Mantém apenas letras e números, e coloca tudo em minúsculo
    filtrado = "".join(c.lower() for c in texto if c.isalnum())
    return filtrado == filtrado[::-1]


# Exemplo de uso:
frase = input("Digite uma palavra ou frase: ")
resultado = eh_palindromo(frase)

if resultado:
    print("Sim")
else:
    print("Não")



nome_produto = input("Nome do produto: ")
preco_original = float(input("Preço original (R$): "))
desconto_percentual = float(input("Desconto (%): "))

valor_desconto = preco_original * (desconto_percentual / 100)
preco_final = preco_original - valor_desconto

print("\n--- RESUMO ---")
print("Produto:", nome_produto)
print("Preço original: R$", round(preco_original, 2))
print("Desconto:", desconto_percentual, "%")
print("Valor do desconto: R$", round(valor_desconto, 2))
print("Preço final: R$", round(preco_final, 2))




from datetime import date

ano = int(input("Ano de nascimento (ex: 1990): "))
mes = int(input("Mês de nascimento (1-12): "))
dia = int(input("Dia de nascimento (1-31): "))

data_nascimento = date(ano, mes, dia)
hoje = date.today()

dias_vivo = (hoje - data_nascimento).days

print("Você está vivo(a) há", dias_vivo, "dias.")




