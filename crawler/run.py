from time import sleep

import requests

from crawlers.status import CrawlerStatus
from crawlers.instagram import CrawlerInstagram

def main():
    crawler_status = CrawlerStatus()
    crawler_instagram = CrawlerInstagram()
    while True:
        print('Iniciando crawler de status...')
        crawler_status.inicia_busca()
        print('Iniciando crawler do Instagram...')
        crawler_instagram.inicia_busca()
        print('Aguardando 1 minuto para nova busca...')
        sleep(60)

if __name__ == '__main__':
    main()
