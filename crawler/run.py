from time import sleep

import requests

from crawlers.status import CrawlerStatus

def main():
    crawler_status = CrawlerStatus()
    while True:
        print('Iniciando crawler de status...')
        crawler_status.inicia_busca()
        print('Aguardando 1 minuto para nova busca...')
        sleep(60)

if __name__ == '__main__':
    main()
