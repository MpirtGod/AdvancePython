import unittest
from mod5.task4 import Redirect


class TestRedirect(unittest.TestCase):
    def test_stdout_file(self):
        stdout_file = open('stdout.txt', 'w')
        stderr_file = open('stderr.txt', 'w')
        with Redirect(stdout=stdout_file, stderr=stderr_file):
            print('Hello stdout.txt')
            raise Exception('Hello stderr.txt')

        with open('stdout.txt') as stdout:
            self.assertTrue('Hello stdout.txt' in stdout.read())

    def test_stderr_file(self):
        stdout_file = open('stdout.txt', 'w')
        stderr_file = open('stderr.txt', 'w')
        with Redirect(stdout=stdout_file, stderr=stderr_file):
            print('Hello stdout.txt')
            raise Exception('Hello stderr.txt')

        with open('stderr.txt') as stderr:
            self.assertTrue("Exception: Hello stderr.txt" in stderr.read())

    def test_no_stderr_argument(self):
        stderr_file = open('stderr.txt', 'w')
        stdout_file = open('stdout.txt', 'w')
        with Redirect(stdout=stdout_file):
            print('Hello stdout.txt')
            raise Exception('Hello stderr.txt')

        with open('stderr.txt') as stderr:
            self.assertTrue("Exception: Hello stderr.txt" not in stderr.read())


    def test_no_stdout_argument(self):
        stderr_file = open('stderr.txt', 'w')
        stdout_file = open('stdout.txt', 'w')
        with Redirect(stderr=stderr_file):
            print('Hello stdout.txt')
            raise Exception('Hello stderr.txt')

        with open('stdout.txt') as stdout:
            self.assertTrue('Hello stdout.txt' not in stdout.read())

    def test_no_arguments(self):
        stderr_file = open('stderr.txt', 'w')
        stdout_file = open('stdout.txt', 'w')
        with Redirect():
            print('Hello stdout.txt')
            raise Exception('Hello stderr.txt')

        with open('stdout.txt') as stdout, open('stderr.txt') as stderr:
            self.assertTrue('Hello stdout.txt' not in stdout.read() and "Exception: Hello stderr.txt" not in stderr.read())