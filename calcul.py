#/bin/python3

def combinaison(n, k):
    if (n == 0 and k == 0):
        return (1)
    tmp = (combinaison(n-1, k-1) + combinaison(n-1, k))
    return tmp

def iterative_calc(n, k):
    i = 0
    res = 1

    if (k > n - k):
        k = n - k
    while (i <= k - 1):
        res *= (n - i) / (k - i) 
        i += 1
    return res

def combi_of_a_set(n, k):
    c = 0
    c = iterative_calc(n, k)
    print(k, "-combination of a ", n, " set:", sep='')
    print("%.f" % c)
    return

def bino_and_poisson(d):
    p_succes = d / (8 * 3600) #a day is 8h
    print(p_succes)

    return