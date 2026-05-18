for _ in range(int(input())):
    s=input()
    print('Yes' if not(('N' in s)^('S' in s)) and not(('E' in s)^('W' in s)) else 'No')