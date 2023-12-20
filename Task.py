import json
import time

import numpy as np


class Task:
    def __init__(self, id: int, size: int, a=None, b=None):
        self.identifier = id
        self.size = size
        self.x = None
        self.time = None
        if a is None:
            self.a = np.random.rand(self.size, self.size)
        else:
            self.a = a

        if b is None:
            self.b = np.random.rand(self.size)
        else:
            self.b = b

    def work(self):
        # solve problem ax=b
        start_time = time.time()
        self.x = np.linalg.solve(self.a, self.b)
        end_time = time.time()

        self.time = end_time - start_time

        print("Task" + str(self.identifier) + " finish after " + str(self.time) + "s")
        return self.x

    def to_JSON(self):
        return json.dumps(
            {
                "a": self.a.tolist(),
                "b": self.b.tolist(),
                "s": self.size,
                "id": self.identifier,
            }
        )

    @classmethod
    def from_json(self, txt):
        dic = json.loads(txt)
        return Task(
            dic["id"], size=dic["s"], a=np.array(dic["a"]), b=np.array(dic["b"])
        )

    def __eq__(self, t):
        if isinstance(t, Task):
            if np.array_equal(self.a, t.a) and np.array_equal(self.b, t.b):
                return True
        return False

    # def __add__(self, other):
    #
    # def __eq__(self, other):


if __name__ == "__main__":
    task1 = Task(1, 10)
    task2 = Task(2, 15)
    # task1.work()
    txt = task1.to_JSON()
    print(txt)
    task3 = Task.from_json(txt)
    print(task1 == task2)
    print(task1 == task3)
