import queue
from multiprocessing.managers import BaseManager

PORT = 7331
IP = "localhost"
KEY = b"daerhtitlum"


class QueueManager(BaseManager):
    """base class for manager of the queue"""

    def __init__(self, address, authkey):
        # creation des queues
        self.task_queue = queue.Queue()
        self.result_queue = queue.Queue()
        # register
        QueueManager.register("get_task", callable=lambda: self.task_queue)
        QueueManager.register("get_result", callable=lambda: self.result_queue)

        # creation manager , server
        self.manager = super().__init__(address=address, authkey=authkey)
        self.server = self.manager.get_server()
        self.server.serve_forever()
        print("ok")
        # creation des queues


class QueueClient:
    """Base class for users of the Queue."""

    def __init__(self, address, authkey):
        # register
        QueueManager.register("get_task")
        QueueManager.register("get_result")
        # creation de l'instance du manager et connection au manager process distant
        manager = QueueManager(address=address, authkey=authkey)
        manager.connect()
        # recuperation des queues
        self.tasks = manager.get_task()
        self.result = manager.get_result()


if __name__ == "__main__":
    manager = QueueManager((IP, PORT), KEY)
    client = QueueClient((IP, PORT), KEY)
