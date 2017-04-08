import math

def nCr(n, r):
    return math.factorial(n) / math.factorial(r) / math.factorial(n-r)

def probability_distribution(prob, n):
    '''
    prob: probability
    n: length of vectors
    '''
    dist = {}
    for i in range(n + 1):
        dist[i] = ((prob ** i)* ((1-prob) ** (n-i)) * nCr(n, i))
    return dist

def interests_vector(interests):
    '''
    '''
    vector = [0]*len(interests)
    for i, interest in enumerate(interests):
        if interest:
            vector[i] = 1
    return vector


