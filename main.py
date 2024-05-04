from Lab4 import *
from Lab6 import *
from Task import *

class Perform_The_Task(object):
    def Perform_The_lab_4_1(self):
        result = Lab4()
        result.task_1()

    def Perform_The_lab_4_2(self):
        result = Lab4()
        result.task_2()

    def Perform_The_lab_6_1(self):
        result = Lab6()
        result.task_1()

    def Perform_The_lab_6_2(self):
        result = Lab6()
        result.task_2()

    def Perform_tasks(self):
        result = Task()
        result.Task1()
        result.Task2()
        result.Task3()
        result.Task4()

if __name__ == '__main__':
    Perform_The_Task().Perform_tasks()
