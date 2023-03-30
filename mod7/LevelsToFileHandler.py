import logging

class LevelsToFileHandler(logging.Handler):
    def __init__(self, mode='w'):
        super().__init__()
        self.mode = mode
    def emit(self, record: logging.LogRecord) -> None:
        message = self.format(record)
        with open(f'logs/calc_{record.levelname.lower()}.log', mode=self.mode) as f:
            f.write(message + '\n')