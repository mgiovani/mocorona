import io
import os

import requests

URL_BASE = os.getenv('API_URL', 'http://localhost:1337/')
OCR_URL_BASE = os.getenv('OCR_API_URL', '')
OCR_API_TOKEN = os.getenv('OCR_API_TOKEN', '')

def converte_imagem(checksum, url):
    print(f'Convertendo imagem {checksum}...')
    url_textos = f'{URL_BASE}textos'
    imagem_ja_convertida = requests.get(f'{url_textos}?checksum_img={checksum}').json()
    if imagem_ja_convertida:
        return imagem_ja_convertida[0]['texto']
    
    corpo = {
        'url': f'{URL_BASE}{url.strip("/")}',
        'language': 'por',
        'scale': True,
        'isTable': True,
        'apikey': OCR_API_TOKEN,
    }
    res = requests.post(OCR_URL_BASE, data=corpo)
    texto = res.json()['ParsedResults'][0]['ParsedText']
    return texto
