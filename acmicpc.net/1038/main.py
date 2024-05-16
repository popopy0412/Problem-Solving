n,ans=int(input()),0
def bt(now,cnt,l):
    global ans
    if cnt==l:
        if ans==n:
            print(now)
            exit(0)
        ans+=1
        return
    for i in range(now%10 if cnt else 10): bt(now*10+i,cnt+1,l)
if n>1022: print(-1)
else:
    for i in range(10): bt(0,0,i+1)