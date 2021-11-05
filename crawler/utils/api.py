import io
import logging
import os

import requests

URL_BASE = os.getenv("API_URL", "http://localhost:8001/")
API_TOKEN = os.getenv("API_TOKEN", "")

def envia_request(url, dados):
    headers = {'authorization': API_TOKEN}
    res = requests.post(url, json=dados, headers=headers)
    logging.info(res)

def envia_resumo(notificacoes, negativos, confirmados, recuperados, obitos, data):
    logging.info('Enviando resumo de casos para a API...')
    url_resumos = f'{URL_BASE}covid-summaries'
    headers = {'authorization': API_TOKEN}
    dados = {
        'notification': notificacoes,
        'negative': negativos,
        'confirmed': confirmados,
        'recovered': recuperados,
        'dead': obitos,
        'release': data,
    }
    logging.info(dados)
    envia_request(url_resumos, dados)

def envia_resumo_vacinas(reforco, unica, primeira, segunda, data, target):
    logging.info('Enviando resumo de vacinas para a API...')
    url_resumos = f'{URL_BASE}vaccine-summaries'
    headers = {'authorization': API_TOKEN}
    dados = {
        "boosterdose": reforco,
        "uniquedose": unica,
        "firstdose": primeira,
        "seconddose": segunda,
        "release": data,
        "target": target,
    }
    logging.info(dados)
    envia_request(url_resumos, dados)

def envia_imagem(data, imagem, checksum):
    logging.info('Enviando imagem para a API...')
    url_imagens = f'{URL_BASE}imagens?token={API_TOKEN}'
    url_upload = f'{URL_BASE}upload?token={API_TOKEN}'
    res = requests.get(f'{url_imagens}&checksum={checksum}')
    if res.json():
        return

    imagem_io = io.BytesIO(imagem)
    files = {
        'files': (checksum, imagem_io, 'image/jpeg')
    }
    res = requests.post(url_upload, files=files)
    url_imagem = res.json()[0].get('url')
    dados = {
        'data': data.strftime('%Y-%m-%d'),
        'url': url_imagem,
        'checksum': checksum,
    }
    res = requests.post(url_imagens, json=dados)
    logging.info(res)
