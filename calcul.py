#/bin/python3

from math import exp, factorial
import time

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
    b_values, b_time = build_b_values(p_succes)
    print_values(b_values, "Binomial", b_time)
    print() #empty line for code
    p_values, p_time = build_p_values(p_succes)
    print_values(p_values, "Poisson", p_time)
    return

def build_b_values(p_succes):
    i = 0
    values = []
    tmp = 0.0
    
    start = time.time()
    while (i <= 50):
        tmp = iterative_calc(3500, i) * pow(p_succes, i) * pow((1 - p_succes), 3500 - i) 
        values.append([i, tmp])
        i += 1
    end = time.time() #time for loop is in second
    return values, ((end - start) * 1000)

def build_p_values(p_succes):
    i = 0
    lamdba = 3500 * p_succes
    values = []
    tmp = 0.0
    
    start = time.time()
    while (i <= 50):
        tmp = (exp(-lamdba) * pow(lamdba, i)) / factorial(i)
        values.append([i, tmp])
        i += 1
    end = time.time() #time for loop is in second
    return values, ((end - start) * 1000)

def print_values(values, method, time):
    i = 0

    print(method, "distribution:")
    for pair in values:
        print(pair[0], "->", "%.3f" % pair[1], end='')
        if (i == 5 or pair[0] == 50):
            print()
            i = 0
        else:
            print(end='\t')
            i += 1
    print("overload: ", overload_calc(), "%", sep='')
    print("computation time:", "%.2f" % time, "ms")

def overload_calc():
    return 0