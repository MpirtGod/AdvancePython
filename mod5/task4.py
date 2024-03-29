import sys
from traceback import format_exc


class Redirect:
    def __init__(self, stdout=None, stderr=None):
        self.stdout = stdout
        self.stderr = stderr
        self.temp_stdout = sys.stdout
        self.temp_stderr = sys.stderr

    def __enter__(self):
        if self.stdout is not None:
            sys.stdout = self.stdout
        if self.stderr is not None:
            sys.stderr = self.stderr

    def __exit__(self, type, value, traceback):
        if self.stderr is not None:
            self.stderr.write(format_exc())
            self.stderr.close()
        if self.stdout is not None:
            self.stdout.close()

        sys.stdout = self.temp_stdout
        sys.stderr = self.temp_stderr
        return True


if __name__ == '__main__':
    print('Hello stdout')
    stdout_file = open('stdout.txt', 'w')
    stderr_file = open('stderr.txt', 'w')

    with Redirect(stdout=stdout_file, stderr=stderr_file):
        print('Hello stdout.txt')
        raise Exception('Hello stderr.txt')

    print('Hello stdout again')
    raise Exception('Hello stderr')