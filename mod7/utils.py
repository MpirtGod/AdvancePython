import logging
from configMethod import configure_logging
from config_JSON import config_by_levels
from logging import config
import logging_tree


def write_log_tree_to_file(file):
    with open(file, 'w') as book:
        book.write(logging_tree.format.build_description())


# logger = logging.getLogger('utilsLogger')
logger = logging.getLogger('unitsFileLogger')   #С фильтром ASCIII
# logging.basicConfig(level=logging.INFO)
# configure_logging()
logging.config.dictConfig(config_by_levels)
logger.debug('Тест')
logger.info("Test")


def get_number_input():
    while True:
        try:
            number = float(input("> "))
            return number
        except ValueError:
            logger.warning('Пожалуйста, введите число: ')


def get_operation():
    while True:
        try:
            choice = int(input("> "))
            if choice not in [1, 2, 3, 4]:
                raise ValueError
            return choice
        except ValueError:
            logger.warning("Пожалуйста, выберите номер операции (от 1 до 4).")


def add(x,y):
    return x + y


def subtract(x,y):
   return x - y


def multiply(x,y):
   return x * y


def divide(x,y):
   if y == 0:
       logger.error('На ноль делить нельзя!')
       raise ZeroDivisionError("На ноль делить нельзя!")
   else:
       return x / y

write_log_tree_to_file('logging_tree.txt')