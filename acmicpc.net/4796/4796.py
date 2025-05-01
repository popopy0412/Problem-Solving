t=1
while 1:
    l,p,v=map(int,input().split())
    if l==0: break
    print(f'Case {t}: {v//p*l+min(v%p,l)}')
    t+=1