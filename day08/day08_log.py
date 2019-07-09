import logging.handlers
from time import sleep

fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] : %(message)s'
logging.basicConfig(level=logging.DEBUG, format=fmt, filename='./msg.log')


def test_log():
    logging.debug('debug 哈哈哈哈哈')
    logging.info('info')
    logging.warning('warning')
    logging.error('error')
    logging.critical('critical')


def test_log2():
    logger = logging.getLogger('rain')
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler('./msg1.log')

    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)

    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.debug('debug 哈哈哈哈哈')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')


def test_log3():
    logger = logging.getLogger('rain03')
    logger.setLevel(logging.DEBUG)
    trfh = logging.handlers.TimedRotatingFileHandler('./msg03', when='S',
                                                     interval=10, backupCount=5, encoding='utf-8')
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    trfh.setFormatter(logging.Formatter(fmt))
    # trfh.setLevel()

    logger.addHandler(trfh)

    while True:
        sleep(0.5)
        logger.debug('testtesttest')


if __name__ == '__main__':
    test_log3()
