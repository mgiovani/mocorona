import logging
from time import sleep

import requests

from crawlers.status import CrawlerStatus
from crawlers.instagram import CrawlerInstagram


def main():
    while True:
        try:
            logging.getLogger().setLevel(logging.INFO)

            crawler_status = CrawlerStatus()
            crawler_instagram = CrawlerInstagram()

            logging.info('Iniciando crawler de status...')
            crawler_status.inicia_busca()
            logging.info('Iniciando crawler do Instagram...')
            crawler_instagram.inicia_busca()
            sleep(60)
        except Exception as ex:
            logging.error(ex)

if __name__ == '__main__':
    main()
