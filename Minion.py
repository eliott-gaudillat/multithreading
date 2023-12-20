import time

from QueueManager import QueueClient


class Minion(QueueClient):
    def __init__(self):
        super().__init__()
        self.current_task = None
        self.res = None

    def receive_task(self):
        self.current_task = self.tasks.get()

    def working(self):
        while True:
            self.receive_task()
            res = self.current_task.work()
            self.results.put(res)
            time.sleep(0.01)


if __name__ == "__main__":
    # creation des queues
    m = Minion()
    m.working()
