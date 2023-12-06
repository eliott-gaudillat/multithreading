import QueueClient


class Minion(QueueClient):
    def __init__(self, adress, authkey):
        super().__init__(adress, authkey)
