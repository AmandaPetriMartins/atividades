import string
import secrets

tamanho = int(input("Digite o tamanho da senha (mínimo 8): "))

if tamanho < 8:
    print("Senha fraca: escolha pelo menos 8 caracteres.")
else:
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(secrets.choice(caracteres) for _ in range(tamanho))
    print("Senha gerada:", senha)



import requests

url = "https://randomuser.me/api/"

try:
    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()

    dados = resposta.json()
    usuario = dados["results"][0]

    nome = f'{usuario["name"]["first"]} {usuario["name"]["last"]}'
    email = usuario["email"]
    pais = usuario["location"]["country"]

    print("Nome:", nome)
    print("E-mail:", email)
    print("País:", pais)

except requests.exceptions.RequestException:
    print("Falha na conexão ou na requisição da API.")
except (KeyError, ValueError):
    print("Falha ao processar os dados retornados pela API.")



import requests

cep = input("Digite o CEP (apenas números): ").strip()

if not cep.isdigit() or len(cep) != 8:
    print("CEP inválido. Digite 8 números.")
else:
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()

        dados = resposta.json()

        if dados.get("erro"):
            print("Falha: CEP não encontrado.")
        else:
            print("Logradouro:", dados.get("logradouro", ""))
            print("Bairro:", dados.get("bairro", ""))
            print("Cidade:", dados.get("localidade", ""))
            print("Estado:", dados.get("uf", ""))

    except requests.exceptions.RequestException:
        print("Falha na conexão ou na requisição da API.")
    except ValueError:
        print("Falha ao processar os dados retornados pela API.")



import requests
from datetime import datetime

moeda = input("Digite a moeda (ex: USD, EUR, CAD): ").strip().upper()

url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"

try:
    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()

    dados = resposta.json()

    chave = f"{moeda}BRL"
    if chave not in dados:
        print("Erro: moeda não encontrada.")
    else:
        info = dados[chave]

        valor_atual = float(info["bid"])
        maxima = float(info["high"])
        minima = float(info["low"])

        # AwesomeAPI retorna timestamp (segundos)
        timestamp = int(info["timestamp"])
        ultima_atualizacao = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M:%S")

        print(f"Moeda: {moeda}/BRL")
        print("Valor atual:", round(valor_atual, 4))
        print("Máxima:", round(maxima, 4))
        print("Mínima:", round(minima, 4))
        print("Última atualização:", ultima_atualizacao)

except requests.exceptions.RequestException:
    print("Erro: falha na conexão ou na requisição da API.")
except (KeyError, ValueError):
    print("Erro: falha ao processar os dados retornados pela API.")




