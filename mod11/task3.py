import logging
import random
import threading
import time

TICKETS_COUNT = 10
TICKETS_LEFT = 100

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Director(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        self.max_tickets = TICKETS_LEFT
        self.tickets_added = 0
        logger.info('Director started work')

    def run(self):
        global TICKETS_COUNT
        global TICKETS_LEFT
        is_running = True
        while is_running:
            if TICKETS_COUNT == 4:
                with self.sem:
                    tickets_to_print = min(TICKETS_LEFT, 10 - TICKETS_COUNT)
                    TICKETS_COUNT += tickets_to_print
                    TICKETS_LEFT -= tickets_to_print
                    self.tickets_added += tickets_to_print
                    logger.info(f'Director added {tickets_to_print} tickets; {TICKETS_LEFT} left')
                    if TICKETS_LEFT == 0:
                        is_running = False
        logger.info(f'Director printed {self.tickets_added} tickets')


class Seller(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        self.tickets_sold = 0
        logger.info('Seller started work')

    def run(self):
        global TICKETS_COUNT
        global TICKETS_LEFT
        while True:
            self.random_sleep()
            if TICKETS_LEFT != 0 and TICKETS_COUNT <= 4:
                continue
            else:
                if TICKETS_COUNT == 0:
                    break
                with self.sem:
                    self.tickets_sold += 1
                    TICKETS_COUNT -= 1
                    logger.info(f'{self.name} sold one;  {TICKETS_COUNT} left')
        logger.info(f'Seller {self.name} sold {self.tickets_sold} tickets')

    def random_sleep(self):
        time.sleep(random.randint(0, 1))


def main():
    semaphore = threading.Semaphore()
    workers = []

    director = Director(semaphore)
    director.start()


    for _ in range(4):
        seller = Seller(semaphore)
        seller.start()
        workers.append(seller)

    workers.append(director)

    for worker in workers:
        worker.join()



if __name__ == '__main__':
    main()