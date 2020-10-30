import logging
from time import sleep

import requests

from crawlers.status import CrawlerStatus
from crawlers.instagram import CrawlerInstagram


def main():
    logging.getLogger().setLevel(logging.INFO)

    crawler_status = CrawlerStatus()
    crawler_instagram = CrawlerInstagram()

    logging.info('Iniciando crawler de status...')
    crawler_status.inicia_busca()
    logging.info('Iniciando crawler do Instagram...')
    crawler_instagram.inicia_busca()

if __name__ == '__main__':
    main()
