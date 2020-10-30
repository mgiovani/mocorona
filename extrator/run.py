import logging
from time import sleep

from extratores.bairros import ExtratorBairros

def main():
    logging.getLogger().setLevel(logging.INFO)
    extrator_bairros = ExtratorBairros()

    logging.info('Iniciando extrator de bairros...')
    extrator_bairros.inicia_extracao()

if __name__ == '__main__':
    main()
