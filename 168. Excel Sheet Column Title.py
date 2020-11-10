class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n<1:
            return None
        res = []
        n-=1
        while n>=0:
            res.append(chr(n%26+65))
            n = n//26
            n-=1
        res = res[::-1]
        string = ''.join(res)
        return string