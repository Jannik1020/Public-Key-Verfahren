import math


def is_prime(x):
    prime = True
    if x > 1:
        for i in range(2, x // 2):
            if(x % i) == 0:
                prime = False
                break
    else:
        prime = False
    return prime


def calc_d (e, z):
    # es gilt: d * e % z = 1
    for d in range(z):
        if d*e % z == 1:
            return d


p = 0
while not is_prime(p):
    p = int(input("Geben sie eine Primzahl ein: "))

q = 0
while not is_prime(q):
    q = int(input("Geben sie eine weitere Primzahl ein: "))

n = p * q
z = (q-1)*(p-1)

e = int(input("Geben sie eine Zahl e ein, für die gilt: ggT(e, "+str(z)+") = 1 und 1 < e < " + str(z) + ": "))
while math.gcd(z, e) != 1 and z > e > 1:
    e = int(input("Geben sie eine Zahl e ein, für die gilt: ggT(e, "+str(z)+") = 1 und 1 < e < " + str(z) + ": "))

d = calc_d(e, z)
print("Public key: (" + str(n) + ", " + str(e) + ")")
print("Private key: (" + str(n) + ", " + str(d) + ")")
