import unittest
import datetime
from freezegun import freeze_time

import mod2.task8
from mod2.task4to7 import app
from mod2.task3 import decode
from mod2.task8 import app as financeapp

weekdays_tuple = ('Понедельника', 'Вторника', 'Среды', 'Четверга', 'Пятницы', 'Субботы', 'Воскресения')


class TestHelloWorldApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_can_get_correct_weekday(self):
        week_day = weekdays_tuple[datetime.datetime.today().weekday()]
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        self.assertTrue(week_day in response_text)

    def test_can_get_correct_weekday_if_name_is_weekday(self):
        week_day = weekdays_tuple[datetime.datetime.today().weekday()]
        response = self.app.get(self.base_url + 'Хорошей среды')
        response_text = response.data.decode()
        self.assertTrue(week_day in response_text)

    @freeze_time("2023-03-06")
    def test_can_get_correct_monday(self):
        week_day = weekdays_tuple[datetime.datetime.today().weekday()]
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        self.assertTrue(week_day in response_text)

    @freeze_time("2023-03-07")
    def test_can_get_correct_tuesday(self):
        week_day = weekdays_tuple[datetime.datetime.today().weekday()]
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        self.assertTrue(week_day in response_text)

    @freeze_time("2023-03-08")
    def test_can_get_correct_wednesday(self):
        week_day = weekdays_tuple[datetime.datetime.today().weekday()]
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        self.assertTrue(week_day in response_text)

    @freeze_time("2023-03-09")
    def test_can_get_correct_thursday(self):
        week_day = weekdays_tuple[datetime.datetime.today().weekday()]
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        self.assertTrue(week_day in response_text)

    @freeze_time("2023-03-10")
    def test_can_get_correct_friday(self):
        week_day = weekdays_tuple[datetime.datetime.today().weekday()]
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        self.assertTrue(week_day in response_text)

    @freeze_time("2023-03-11")
    def test_can_get_correct_saturday(self):
        week_day = weekdays_tuple[datetime.datetime.today().weekday()]
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        self.assertTrue(week_day in response_text)

    @freeze_time("2023-03-12")
    def test_can_get_correct_sunday(self):
        week_day = weekdays_tuple[datetime.datetime.today().weekday()]
        response = self.app.get(self.base_url + 'username')
        response_text = response.data.decode()
        self.assertTrue(week_day in response_text)

class TestDecode(unittest.TestCase):
    def test_with_one_dot(self):
        tests = ['абра-кадабра.', '.']
        answers = ['абра-кадабра', '']
        for i in (0, len(tests)-1):
            with self.subTest(i=i):
                self.assertEqual(decode(tests[i]), answers[i])
    def test_with_two_dots(self):
        tests = ['абраа..-кадабра', 'абра--..кадабра']
        answers = ['абра-кадабра', 'абра-кадабра']
        for i in (0, len(tests)-1):
            with self.subTest(i=i):
                self.assertEqual(decode(tests[i]), answers[i])

    def test_with_three_dots(self):
        tests = ['абраа..-.кадабра', 'абрау...-кадабра', '1..2.3']
        answers = ['абра-кадабра', 'абра-кадабра', '23']
        for i in (0, len(tests)-1):
            with self.subTest(i=i):
                self.assertEqual(decode(tests[i]), answers[i])

    def test_with_more_than_three_dots(self):
        tests = ['абра........', 'абр......a.', '1.......................']
        answers = ['', 'a', '']
        for i in (0, len(tests)-1):
            with self.subTest(i=i):
                self.assertEqual(decode(tests[i]), answers[i])

    def test_with_empty_string(self):
        self.assertEqual(decode(''), '')


class TestFinanceApp(unittest.TestCase):
    def setUp(self):
        financeapp.config['TESTING'] = True
        financeapp.config['DEBUG'] = False
        self.financeapp = financeapp.test_client()
        self.base_url = '/'
        mod2.task8.storage = {'2023': {'01': 11000, '02': 5200, '03': 7200, '04': 75400, '05': 11000, '06': 5200, '07': 7200, '08': 75400, '09': 11000, '10': 5200, '11': 7200, '12': 75400},
                           '2022': {'01': 31000, '02': 52400, '03': 72200, '04': 754300, '05': 1000, '06': 7200, '07': 1200, '08': 7500, '09': 1100, '10': 54500, '11': 71100, '12': 7500}}

    def test_add_works_correctly(self):
        response = self.financeapp.get(self.base_url + 'add/20231101/1000')
        self.assertEqual(mod2.task8.storage['2023']['11'], 8200)

    def test_add_throws_date_error_correctly(self):
        response = self.financeapp.get(self.base_url + 'add/202a1101/1000')
        self.assertRaises(TypeError)

    def test_add_throws_money_error_correctly(self):
        response = self.financeapp.get(self.base_url + 'add/20231101/10a00')
        self.assertRaises(TypeError)

    def test_calculate_by_year_works_correctly(self):
        response = self.financeapp.get(self.base_url + 'calculate/2023')
        response_text = response.data.decode()
        self.assertTrue('296400' in response_text)

    def test_calculate_throws_year_error_correctly(self):
        with self.assertRaises(KeyError) as raises:
            response = self.financeapp.get(self.base_url + 'calculate/1111')

    def test_calculate_throws_year_error_correctly_with_empty_storage(self):
        mod2.task8.storage = {}
        with self.assertRaises(KeyError) as raises:
            response = self.financeapp.get(self.base_url + 'calculate/1111')

    def test_calculate_by_month_works_correctly(self):
        response = self.financeapp.get(self.base_url + 'calculate/2022/11')
        response_text = response.data.decode()
        self.assertTrue('71100' in response_text)

    def test_calculate_by_month_throws_type_error_correctly(self):
        response = self.financeapp.get(self.base_url + 'calculate/2022/aa')
        self.assertRaises(TypeError)

    def test_calculate_by_month_throws_month_error_correctly(self):
        with self.assertRaises(KeyError) as raises:
            response = self.financeapp.get(self.base_url + 'calculate/2022/22')