import unittest

from Task import Task


class TestTask(unittest.TestCase):
    def test_eq(self):
        task1 = Task(1, 10)
        task2 = Task(2, 15)
        txt = task1.to_JSON()
        task3 = Task.from_json(txt)
        self.assertEqual(task1, task3)
        self.assertNotEqual(task1, task2)


if __name__ == "__main__":
    unittest.main()
