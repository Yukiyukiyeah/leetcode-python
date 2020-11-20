'''
Author: your name
Date: 2020-11-20 16:35:25
LastEditTime: 2020-11-20 17:06:32
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/204.count-primes.py
'''
class Solution:
  def countPrimes(self, n: int) -> int:
          if n<3:
              return 0
          isPrime = [1] * n
          isPrime[0] = isPrime[1] = 0
          for i in range(2, int(sqrt(n)+1)):
              if isPrime[i] == 0: continue
              for j in range(i*i, n, i):
                  isPrime[j] = 0
          return sum(isPrime)