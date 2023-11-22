from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    def __init__(self):
        self.x = 1
