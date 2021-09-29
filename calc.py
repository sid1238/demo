import math

def cosine(x):
    return (round(math.cos(x), 1))

def sine(x):
    return (round(math.sin(x), 1))

def power(x,y):
    return math.pow(x,y)

def logarithm(x):
    if x<0:
        raise ValueError("Cannot calculate")
    return (round(math.log(x),1))