a,b,c,d,e,f=map(int,open(0).read().split())
t=(a-c)*(b-f)-(a-e)*(b-d)
print(t//abs(t) if t else 0)