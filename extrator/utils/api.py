import io
import logging
import os

import requests

URL_BASE = os.getenv("API_URL", "http://localhost:1337/")
API_TOKEN = os.getenv("API_TOKEN", "")

def envia_casos_bairros(data, dados):
    logging.info('Enviando casos de bairros para a API...')
    url_bairros = f'{URL_BASE}bairros?token={API_TOKEN}'
    for bairro in dados.keys():
        corpo = {
            'nome': bairro,
            'casos': int(dados[bairro]),
            'data_atualizacao': data.strftime('%Y-%m-%d'),
        }
        res = requests.post(url_bairros, json=corpo)
        logging.info(res)

def encontra_textos(data):
    logging.info(f'Buscando textos de {data}...')
    url_textos = f'{URL_BASE}textos?data={data.strftime("%Y-%m-%d")}'
    res = requests.get(url_textos)
    logging.info(res)
    return [texto['texto'] for texto in res.json()]
