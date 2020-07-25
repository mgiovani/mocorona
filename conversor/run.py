from datetime import datetime
from time import sleep

from utils import api, ocr_api

def main():
    while True:
        print('Iniciando busca de imagens...')
        data = datetime.now().date()
        imagens = api.busca_imagens_data(data)
        for imagem in imagens:
            checksum = imagem['checksum']
            url = imagem['url']
            texto = ocr_api.converte_imagem(checksum, url)
            api.envia_texto(checksum, texto, data)
            print('Aguardando 1 minuto para nova busca...')
            sleep(60)

if __name__ == '__main__':
    main()
