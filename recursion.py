def fibonnaci(n):
    if n <= 1:
        return n 
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def compareTo(s1,s2):
    if not s1 or not s2:
        if s1:
            return 1
        elif s2:
            return -1
        else:
            return 0
    else:
        return compareTo(s1[:-1],s2[:-1])