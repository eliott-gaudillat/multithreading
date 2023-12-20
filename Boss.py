from QueueManager import QueueClient
from Task import Task


class Boss(QueueClient):
    def __init__(self):
        super().__init__()

    def put_tasks(self, size, nb_task):
        for i in range(nb_task):
            task = Task(i, size)
            self.tasks.put(task)

    def get_res(self):
        result = self.results.get()
        print(result)

    # def working(self):


if __name__ == "__main__":
    # creation du boss
    b = Boss()
    # creation de 10 taches mis dans la queue
    b.put_tasks(1000, 10)
