import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('example.txt', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s, %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

# logger.debug('Сообщение Debug')
# logger.info('Сообщение Info')
# logger.warning('Сообщение Warning')
# logger.error('Сообщение Error')
# logger.critical('Сообщение Critical')

def abc(a, b):
    if a > b:
        c = a + b
        logger.debug('Условие пройдено.')
    else:
        c = a - b
        logger.debug('Условие не пройдено')
    return c

print(abc(3,2))
print(abc(6,12))
print(abc(7,32))
print(abc(8,5))
print(abc(35,1))
print(abc(8,0))