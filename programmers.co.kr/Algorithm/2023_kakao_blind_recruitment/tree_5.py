from math import *
def div(l,r,d):
    if l==r: return 1
    m=(l+r)//2
    if d[m]=='0':
        if d[l:r+1]=='0'*(r-l+1): return 1
        return 0
    return div(l,m-1,d)&div(m+1,r,d)
def solution(numbers):
    answer = []
    n=len(numbers)
    d=[bin(i)[2:] for i in numbers]
    for i in range(n):
        k=len(d[i])
        t=int(log2(k))+1
        d[i]='0'*(2**t-1-k)+d[i]
        answer.append(div(0,len(d[i])-1,d[i]))
    return answer