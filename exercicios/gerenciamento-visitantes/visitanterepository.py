import json

from constants import NOME_ARQUIVO, ENCODING_ARQUIVO

def carregar_visitantes():
    with open(NOME_ARQUIVO, "r", encoding=ENCODING_ARQUIVO) as arquivo:
        return json.load(arquivo)

def salvar_visitantes(visitantes):
    with open(NOME_ARQUIVO, "w", encoding=ENCODING_ARQUIVO) as arquivo:
        json.dump(visitantes, arquivo, indent=2)