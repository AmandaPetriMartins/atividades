import pandas as pd

arquivo = input("Digite o caminho do arquivo CSV: ").strip()

try:
    df = pd.read_csv(arquivo)

    if "tempo_execucao" not in df.columns:
        print("Erro: a coluna 'tempo_execucao' não existe no arquivo.")
    else:
        media = df["tempo_execucao"].mean()
        maximo = df["tempo_execucao"].max()

        print("Média de tempo_execucao:", round(float(media), 2))
        print("Máximo de tempo_execucao:", round(float(maximo), 2))

except FileNotFoundError:
    print("Erro: arquivo CSV não encontrado.")
except pd.errors.EmptyDataError:
    print("Erro: o arquivo CSV está vazio.")
except pd.errors.ParserError:
    print("Erro: falha ao ler o CSV (formato inválido).")
except Exception:
    print("Erro: ocorreu um problema na leitura do arquivo.")



import csv

pessoas = [
    {"nome": "Ana", "idade": 25, "cidade": "Londrina"},
    {"nome": "Bruno", "idade": 31, "cidade": "Curitiba"},
    {"nome": "Carla", "idade": 28, "cidade": "São Paulo"},
]

arquivo_saida = input("Digite o nome do arquivo CSV para salvar (ex: pessoas.csv): ").strip()

try:
    with open(arquivo_saida, "w", newline="", encoding="utf-8") as arquivo:
        campos = ["nome", "idade", "cidade"]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        escritor.writeheader()
        escritor.writerows(pessoas)

    print("Arquivo salvo com sucesso:", arquivo_saida)

except Exception:
    print("Falha: não foi possível salvar o arquivo.")



arquivo_txt = input("Digite o nome/caminho do arquivo TXT: ").strip()

try:
    with open(arquivo_txt, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            print(linha.rstrip())  # remove o \n do final

except FileNotFoundError:
    print("Erro: arquivo não encontrado.")
except Exception:
    print("Erro: ocorreu um problema ao ler o arquivo.")




import json

arquivo_json = input("Digite o nome do arquivo JSON (ex: pessoa.json): ").strip()

dados = {
    "nome": "Amanda",
    "idade": 32,
    "cidade": "Vancouver"
}

# Salvar
try:
    with open(arquivo_json, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    print("Dados salvos no arquivo:", arquivo_json)

except Exception:
    print("Falha: erro ao salvar o arquivo JSON.")
    raise SystemExit

# Ler
try:
    with open(arquivo_json, "r", encoding="utf-8") as arquivo:
        dados_lidos = json.load(arquivo)

    print("\n--- Dados lidos do JSON ---")
    print("Nome:", dados_lidos.get("nome"))
    print("Idade:", dados_lidos.get("idade"))
    print("Cidade:", dados_lidos.get("cidade"))

except FileNotFoundError:
    print("Falha: o arquivo JSON não existe.")
except Exception:
    print("Falha: erro ao ler o arquivo JSON.")



