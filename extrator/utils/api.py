import io
import os

import requests

URL_BASE = os.getenv("API_URL", "http://localhost:1337/")
API_TOKEN = os.getenv("API_TOKEN", "")

def envia_casos_bairros(data, dados):
    print('Enviando casos de bairros para a API...')
    url_bairros = f'{URL_BASE}bairros?token={API_TOKEN}'
    for bairro in dados.keys():
        corpo = {
            'nome': bairro,
            'casos': int(dados[bairro]),
            'data_atualizacao': data.strftime('%Y-%m-%d'),
        }
        res = requests.post(url_bairros, json=corpo)
