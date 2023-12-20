# This is a sample Python script.
from Boss import Boss
from Minion import Minion

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    b = Boss()
    m1 = Minion()
    m2 = Minion()
    b.put_tasks(1000, 10)
    m1.working()
    m1.working()
