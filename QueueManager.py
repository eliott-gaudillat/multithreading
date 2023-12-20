import os
import queue
from multiprocessing.managers import BaseManager

PORT = 7331
IP = "localhost"
KEY = b"daerhtitlum"


class QueueManager(BaseManager):
    """base class for manager of the queue"""

    pass


class QueueClient:
    """Base class for users of the Queue."""

    def __init__(self):
        # register
        QueueManager.register("get_tasks")
        QueueManager.register("get_results")
        # creation de l'instance du manager et connection au manager process distant
        manager = QueueManager(
            address=(os.environ.get("MANAGER_HOST", "localhost"), PORT), authkey=KEY
        )
        manager.connect()
        # recuperation des queues
        self.tasks = manager.get_tasks()
        self.results = manager.get_results()

        # def getTask(self):
        #     return self.tasks
        #
        # def getResult(self):
        #     return self.results


if __name__ == "__main__":
    # creation des queues
    task_queue = queue.Queue()
    result_queue = queue.Queue()
    # register
    QueueManager.register("get_tasks", callable=lambda: task_queue)
    QueueManager.register("get_results", callable=lambda: result_queue)
    QueueManager(address=("", PORT), authkey=KEY).get_server().serve_forever()
