'''
Author: your name
Date: 2020-11-11 13:53:44
LastEditTime: 2020-11-11 13:53:59
LastEditors: your name
Description: In User Settings Edit
FilePath: /leetcode-python/leetcode-python/1115.print-foobar-alternately.py
'''
class FooBar:
    def __init__(self, n):
        self.n = n
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()
        self.lock2.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.lock1.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.lock2.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.lock2.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.lock1.release()