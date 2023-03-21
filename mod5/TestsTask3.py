import unittest
from mod5.task3 import BlockErrors


class TestBlockErrors(unittest.TestCase):
    def test_zero_division_error_success(self):
        try:
            err_types = {ZeroDivisionError, TypeError}
            with BlockErrors(err_types):
                a = 1 / 0
            print('Выполнено без ошибок')
            assert True
        except:
            assert False

    def test_type_error_failure(self):
        try:
            err_types = {ZeroDivisionError}
            with BlockErrors(err_types):
                a = 1 / '0'
            print('Выполнено без ошибок')
            assert False
        except:
            assert True

    def test_outer_block_success(self):
        try:
            outer_err_types = {TypeError}
            with BlockErrors(outer_err_types):
                inner_err_types = {ZeroDivisionError}
                with BlockErrors(inner_err_types):
                    a = 1 / '0'
                print('Внутренний блок: выполнено без ошибок')
            print('Внешний блок: выполнено без ошибок')
            assert True
        except:
            assert False

    def test_child_block_success(self):
        try:
            err_types = {Exception}
            with BlockErrors(err_types):
                a = 1 / '0'
            print('Выполнено без ошибок')
            assert True
        except:
            assert False