import io
import logging
import os

import requests

URL_BASE = os.getenv("API_URL", "http://localhost:1337/")
API_TOKEN = os.getenv("API_TOKEN", "")

def envia_resumo(notificacoes, negativos, confirmados, recuperados, obitos, data):
    logging.info('Enviando resumo de casos para a API...')
    url_resumos = f'{URL_BASE}resumos?token={API_TOKEN}'
    data_convertida = '-'.join(data.split('/')[::-1])
    dados = {
        'notificacoes': notificacoes,
        'negativos': negativos,
        'confirmados': confirmados,
        'recuperados': recuperados,
        'obitos': obitos,
        'data_atualizacao': data_convertida,
    }
    res = requests.post(url_resumos, json=dados)
    logging.info(res)


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
