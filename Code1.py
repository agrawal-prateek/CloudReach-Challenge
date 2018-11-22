# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)

def solution(T):
    def getdis(ans, d, cn, cd):
        ans[cd]+=1
        for i in d[cn]:
            getdis(ans, d, i, cd+1)
        
    n=len(T)
    k=0
    t=T
    d=defaultdict(list)
    for i in range(n):
        if not i==T[i]:
            d[t[i]].append(i)
        else:
            k=i
            
    ans=[0 for i in range(n)]
    # getdis(ans,d,k,0)
    # return ans[1:]
    
    queue=[]
    queue.append((k,0))
    cd=0
    tmp=0
    while queue:
        # print(queue)
        k = queue.pop(0)
        if k[1]!=tmp:
           cd+=1
        ans[cd]+=1
        for i in d[k[0]]: 
        	queue.append((i,cd+1))
        
        tmp=cd
        

    return ans[1:]
        
