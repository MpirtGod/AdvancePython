import logging
from configMethod import configure_logging
from utils import *
from config_JSON import config_by_levels
from logging import config

logger = logging.getLogger('appLogger')


def calculate():
    logger.info("Введите два числа:")
    num1 = get_number_input()
    num2 = get_number_input()
    logger.debug("Введены два цисла")

    logger.info("Выберите операцию:1. Сложение 2. Вычитание 3. Умножение 4. Деление")
    operation = get_operation()

    if operation == 1:
        result = add(num1, num2)
    elif operation == 2:
        result = subtract(num1, num2)
    elif operation == 3:
        result = multiply(num1, num2)
    else:
        result = divide(num1, num2)
    logger.debug('Конец операции')

    logger.info(f'Результат: {result}')


if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO)
    # configure_logging()
    logging.config.dictConfig(config_by_levels)
    calculate()
