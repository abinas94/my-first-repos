def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

def permutations(n, k):
    return factorial(n) // factorial(n-k)

def combinations(n, k):
    return permutations(n, k) // factorial(k)

#print((combinations(10,3))/(2**10))

p_atmost_2heads = (C.combinations(10, 0) / 2**10) +(C.combinations(10, 1) / 2**10) +(C.combinations(10, 2) / 2**10)
print(p_atmost_2heads)