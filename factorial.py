
#factorial by loop method

def fact(n):
    prd = 1
    for i  in range(1,n+1):
        prd = prd * i
    
    return prd

x = fact(5)
print(x)


# factorial by recursive method


def fac_rec(n):
    prd = 1
    if n == 1:
        return 1
    else:
        prd = prd * n *fac_rec(n-1)
    
    return prd
        
y = fac_rec(5)
print(y)