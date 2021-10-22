da fare 
def algo(A, p, r):
    ret = 0
    if p <= r:
        if p == r:
            ret = A[p]
        else:
            q = (p + 2*r) // 3
            
            q1 = (2*p + r) // 3
