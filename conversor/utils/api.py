import io
import os

import requests

URL_BASE = os.getenv('API_URL', 'http://localhost:1337/')
API_TOKEN = os.getenv('API_TOKEN', '')

def busca_imagens_data(data):
    print(f'Buscando imagens de {data}...')
    url_imagens = f'{URL_BASE}imagens?data={data.strftime("%Y-%m-%d")}'
    res = requests.get(url_imagens)
    return res.json()


def envia_texto(checksum, texto, data):
    print(f'Enviando texto {checksum}...')
    url_textos = f'{URL_BASE}textos?token={API_TOKEN}'
    corpo = {
        'checksum_img': checksum,
        'texto': texto,
        'data': data.strftime("%Y-%m-%d"),
    }
    res = requests.post(url_textos, json=corpo)
    return res.json()
