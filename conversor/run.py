import logging
from datetime import datetime
from time import sleep

from utils import api, ocr_api

def main():
    logging.getLogger().setLevel(logging.INFO)
    data = datetime.now().date()
    logging.info('Iniciando busca de imagens...')
    imagens = api.busca_imagens_data(data)
    for imagem in imagens:
        checksum = imagem['checksum']
        url = imagem['url']
        texto = ocr_api.converte_imagem(checksum, url)
        api.envia_texto(checksum, texto, data)

if __name__ == '__main__':
    main()
