from QueueManager import QueueClient
from Task import Task


class Boss(QueueClient):
    def __init__(self, address, authkey):
        super().__init__(address, authkey)

    def put_task(self, id, size):
        task = Task(id, size)

        self.tasks.put(task)

    def get_result(self):
        result = self.result.pop()
        print(result)
