import re
from time import sleep

from extratores.bairros import ExtratorBairros

def main():
    extrator_bairros = ExtratorBairros()

    while True:
        print('Iniciando extrator de bairros...')
        extrator_bairros.inicia_extracao()
        print('Aguardando 1 minuto para nova busca...')
        sleep(60)

if __name__ == '__main__':
    main()
