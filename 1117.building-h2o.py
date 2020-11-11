'''
Author: your name
Date: 2020-11-11 15:00:31
LastEditTime: 2020-11-11 15:00:52
LastEditors: your name
Description: In User Settings Edit
FilePath: /leetcode-python/leetcode-python/1117.building-h2o.py
'''
from threading import Semaphore, Barrier
class H2O:
    def __init__(self):
        self.sem_h = Semaphore(2)
        self.sem_o = Semaphore(1)
        self.bar_assembling = Barrier(3)


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        with self.sem_h:
            self.bar_assembling.wait()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
            releaseHydrogen()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.sem_o:
            self.bar_assembling.wait()
        # releaseOxygen() outputs "O". Do not change or remove this line.
            releaseOxygen()