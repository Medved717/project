import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('example.txt')
file_formatter = logging.Formater('%(asctime)s, %(linename)s: %(message)s')
file_handler.setFormater(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

logger.debug('Сообщение DEBUG')