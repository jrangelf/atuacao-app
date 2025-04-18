import logging

from logging import CRITICAL, ERROR, WARNING, INFO, DEBUG
from logging import critical, error, warning, info, debug
from logging import basicConfig



# Configuração básica do logging com FileHandler e codificação UTF-8
logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.FileHandler(filename='atuacao.log', mode='a', encoding='utf-8')
    ],
    format='%(levelname)s:%(asctime)s:%(message)s'
)
