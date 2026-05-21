I=input
for t in range(int(I())):
 I();m=a=0
 for x in map(int,I().split()[::-1]):m=max(m,x);a+=m-x
 print(f'#{t+1}',a)