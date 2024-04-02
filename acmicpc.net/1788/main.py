l=[0,1]
n,M=int(input()),10**9
for _ in range(abs(n)-1):l.append((l[-1]+l[-2])%M)
if n:print(f'{-1 if n<0 and~n%2 else 1}\n{l[-1]}')
else:print('0\n0')