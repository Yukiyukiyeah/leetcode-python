'''
@Author: your name
@Date: 2020-05-21 19:01:11
@LastEditTime: 2020-05-21 19:22:23
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode-python/146.lru-cache.py
'''
#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
import collections
# @lc code=start
class LRUCache:

    def __init__(self, capacity: int):
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)
        self.dic[key] = v
        return v

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dic.popitem(last = False)
        self.dic[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

