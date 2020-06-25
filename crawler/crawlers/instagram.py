import json
import os
from datetime import datetime

import requests
from bs4 import BeautifulSoup

class CrawlerInstagram:
    URL_BASE = 'https://www.instagram.com/sec_saude_moc/'

    def inicia_busca(self):
        print('Iniciando busca de imagens...')
        html = requests.get(self.URL_BASE)
        soup = BeautifulSoup(html.content, 'html.parser')
        json_pagina = self._extrai_json_pagina(soup)
        imagens = self._encontra_imagens(json_pagina)

    def _extrai_json_pagina(self, soup):
        body = soup.find('body')
        tag_script = body.find('script').string
        string_js = tag_script.strip().replace('window._sharedData =', '').replace(';', '')
        try:
            return json.loads(string_js)
        except json.JSONDecodeError:
            return {}

    def _encontra_imagens(self, json_pagina):
        try:
            imagens = json_pagina['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']
        except:
            imagens = []
        data_atual = datetime.now().date()
        imagens_data = self._filtra_imagens_por_data(imagens, data_atual)
        urls = self._extrai_urls_imagens(imagens_data)
        self._salva_imagens(data_atual, urls)

    def _filtra_imagens_por_data(self, imagens, data):
        imagens_data = []
        for imagem in imagens:
            data_imagem = datetime.fromtimestamp(imagem['node']['taken_at_timestamp']).date()
            if data == data_imagem:
                imagens_data.append(imagem)
        return imagens_data


    def _extrai_urls_imagens(self, imagens):
        urls = []
        for imagem in imagens:
            try:
                imagens_multiplas = imagem['node']['edge_sidecar_to_children']['edges']
                urls.extend([img['node']['display_url'] for img in imagens_multiplas])
            except KeyError:
                urls.append(imagem['node']['display_url'])
        return urls

    def _salva_imagens(self, data, urls):
        data_str = data.strftime('%Y-%m-%d')
        diretorio_imagens = os.path.join('crawlers', 'imagens', data_str)
        os.makedirs(diretorio_imagens, exist_ok=True)
        for url in urls:
            imagem = requests.get(url)
            checksum = imagem.headers.get('x-needle-checksum')
            caminho_arquivo = f'{os.path.join(diretorio_imagens, checksum)}.jpg'
            if os.path.exists(caminho_arquivo):
                print(f'Arquivo {caminho_arquivo} ignorado, baixado anteriormente.')
                continue

            print(f'Criando arquivo {caminho_arquivo}...')
            with open(caminho_arquivo, 'wb') as f:
                f.write(imagem.content)
