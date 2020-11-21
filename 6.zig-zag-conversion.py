class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        numGroup = numRows * 2 - 2
        res =  [''] * numRows
        for i in range(len(s)):
            rem = i % numGroup
            row = rem if rem <= numRows - 1 else numGroup - rem
            res[row] += s[i]
        return ''.join(res)
            