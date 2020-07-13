import os
import re
import datetime

from utils import api


class ExtratorBairros:
    PATH_TEXTOS = os.path.join('..', 'conversor', 'textos')

    def inicia_extracao(self):
        print('Iniciando extracação de bairros...')
        data = datetime.datetime.now().date()
        textos = self._encontra_arquivos_data(data)
        for texto in textos:
            if self._texto_tipo_bairros(texto):
                dados = self._extrai_dados_arquivo(texto)
                api.envia_casos_bairros(data, dados)

    def _encontra_arquivos_data(self, data):
        data = data.strftime('%Y-%m-%d')
        print(f'Procurando arquivos para o dia {data}...')

        caminho_pasta = os.path.join(self.PATH_TEXTOS, data)
        nomes_arquivos = os.listdir(caminho_pasta)
        textos = []
        for nome in nomes_arquivos:
            caminho = os.path.join(caminho_pasta, nome)
            textos.append(open(caminho).read())
        return textos

    def _texto_tipo_bairros(self, texto):
        return 'CONFIRMADOS POR BAIRRO' in texto

    def _extrai_dados_arquivo(self, texto):
        dados_iniciais = re.findall(r'(?P<bairro>[\w\d .?-]+)\t(?P<casos>\d+)', texto)
        dados_corrigidos = self._corrige_nomes_bairros(dados_iniciais)
        return dados_corrigidos

    def _corrige_nomes_bairros(self, dados):
        dados_corrigidos = {}
        for dado in dados:
            bairro, casos = dado
            bairro_corrigido = self._substitui_erros_comuns(bairro)
            dados_corrigidos.update({bairro_corrigido: casos})
        return dados_corrigidos
    
    def _substitui_erros_comuns(self, texto):
        substituicoes = {
            '11': 'II',
            'SR?': 'SR.ª',
            'ANTÔNIO 1': 'ANTÔNIO I',
            'ANÂLIA': 'ANÁLIA',
            'SR3.': 'SR.ª',
            'SR*': 'SR.ª',
            'SR-': 'SR.ª',
            '1 BITU RU NA': 'IBITURUNA',
            'CARME LO': 'CARMELO',
        }
        for erro in substituicoes.keys():
            texto = texto.replace(erro, substituicoes[erro])
        return texto
