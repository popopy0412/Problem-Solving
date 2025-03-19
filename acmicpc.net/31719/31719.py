import sys
ip=sys.stdin.readline
for _ in range(int(ip())):
    n,*l=int(ip()),*map(int,ip().split())
    s=[];c=1;f=1
    for i in l:
        j=0
        while j<len(s):
            if s[j][0]==c:
                c=s[j][1]+1
                s.pop(j)
                break
            j+=1
        if i==c and len(s)<3:c+=1;continue
        if not s:s.append([i,i])
        elif len(s)<4:
            for j in range(len(s)):
                if s[j][1]+1==i:s[j][1]+=1;break
            else:
                if len(s)<3:s.append([i,i])
                else:print('NO');f=0;break
    if f:print('YES')