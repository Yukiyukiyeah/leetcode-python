'''
Author: your name
Date: 2020-11-11 14:17:59
LastEditTime: 2020-11-11 14:18:12
LastEditors: your name
Description: In User Settings Edit
FilePath: /leetcode-python/leetcode-python/1116.print-zero-even-odd.py
'''
import threading
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.lock_zero = threading.Lock()
        self.lock_even = threading.Lock()
        self.lock_odd = threading.Lock()
        self.lock_even.acquire()
        self.lock_odd.acquire()
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(0,self.n):
            self.lock_zero.acquire()
            printNumber(0)
            if i%2 == 0:
                self.lock_odd.release()
            else:
                self.lock_even.release()
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n+1, 2):
            self.lock_even.acquire()
            printNumber(i)
            self.lock_zero.release()
        
        
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1, 2):
            self.lock_odd.acquire()
            printNumber(i)
            self.lock_zero.release()
        
        
