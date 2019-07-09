#Transpose Matrix
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        r = len(A[0])
        c = len(A)
        ans = []
        for i in range(r):
            a = []
            for j in range(c):
                a.append(A[j][i]) #�@���s�@����m��C
            ans.append(a)
            
        return ans