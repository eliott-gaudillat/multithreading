import time

import numpy as np


class Task:
    def __init__(self, id: int, size: int):
        self.identifier = id
        self.size = size
        self.a = None
        self.b = None
        self.x = None
        self.time = None

    def work(self):
        # create a and b as vector of size ( 1, self.size)
        self.a = np.random.rand(self.size, self.size)
        self.b = np.random.rand(self.size)

        # solve problem ax=b
        start_time = time.time()
        self.x = np.linalg.solve(self.a, self.b)
        end_time = time.time()

        self.time = end_time - start_time

        print("Task" + str(self.identifier) + " finish after " + str(self.time) + "s")


# if __name__ == "__main__":
#  task1 = Task(1, 10000)
# task1.work()
