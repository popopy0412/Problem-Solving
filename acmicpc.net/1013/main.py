import re
for s in open(0).read().split()[1:]:print('YES'if re.match('(100+1+|01)+$',s)else'NO')