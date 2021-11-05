from datetime import datetime

import logging
import requests
from bs4 import BeautifulSoup

from utils import api

class CrawlerStatus:
    URL_BASE = 'https://saude.montesclaros.mg.gov.br/'

    def inicia_busca(self):
        logging.info('Iniciando busca de status...')
        html = requests.get(self.URL_BASE)
        soup = BeautifulSoup(html.content, 'html.parser')
        notificacoes = self._encontra_notificacoes(soup)
        negativos = self._encontra_negativos(soup)
        confirmados = self._encontra_confirmados(soup)
        recuperados = self._encontra_recuperados(soup)
        obitos = self._encontra_obitos(soup)
        data = self._encontra_ultima_atualizacao(soup)
        api.envia_resumo(
            notificacoes, negativos, confirmados, recuperados, obitos, data
        )

        reforco = self._encontra_contador(soup, 'Dose de reforço')
        unica = self._encontra_contador(soup, 'Dose Única')
        primeira = self._encontra_contador(soup, '1ª Dose')
        segunda = self._encontra_contador(soup, '2ª Dose')
        target = self._encontra_target(soup)
        api.envia_resumo_vacinas(
            reforco, unica, primeira, segunda, data, target
        )

    def _encontra_notificacoes(self, soup):
        notificacoes = self._encontra_contador(soup, 'Notificações')
        logging.info(f'Foram encontradas {notificacoes} notificações.')
        return notificacoes

    def _encontra_negativos(self, soup):
        negativos = self._encontra_contador(soup, 'Negativos')
        logging.info(f'Foram encontrados {negativos} negativos.')
        return negativos

    def _encontra_confirmados(self, soup):
        confirmados = self._encontra_contador(soup, 'Confirmados')
        logging.info(f'Foram encontrados {confirmados} confirmados.')
        return confirmados

    def _encontra_recuperados(self, soup):
        recuperados = self._encontra_contador(soup, 'Recuperados')
        logging.info(f'Foram encontrados {recuperados} recuperados.')
        return recuperados

    def _encontra_obitos(self, soup):
        obitos = self._encontra_contador(soup, 'Óbitos')
        logging.info(f'Foram encontrados {obitos} óbitos.')
        return obitos

    def _encontra_ultima_atualizacao(self, soup):
        ultima_atualizacao = soup.select('.badge-light')[0]
        data = ultima_atualizacao.text
        data = datetime.strptime(data, '%d/%m/%Y %H:%M').isoformat()
        data = f'{data}-03:00'
        logging.info(f'Atualizado pela última vez em: {data}')
        return data

    def _encontra_contador(self, soup, nome_contador):
        contadores = soup.select('.timer')
        for contador in contadores:
            if contador.next.next.text == nome_contador:
                return int(contador.attrs.get('data-to'))

    def _encontra_target(self, soup):
        target = soup.select('h1')[-1].text
        return target.strip()
