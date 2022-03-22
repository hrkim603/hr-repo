# user2
def gcd(a, b):
    while(a % b != 0):
        temp = a % b
        a = b
        b = temp
    return int(b)

def lcm(a, b):
    return int(a * b // gcd(a, b))

a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

GCD = gcd(gcd(a,b), c)

LCM = lcm(lcm(a, b), c)

print(GCD, LCM)
