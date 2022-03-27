Touched by ihobbang250
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

#예외처리
try:
    a / b
    b / a
    a / c
    c / a
    b / c
    c / b
except ZeroDivisionError: #0을 입력받은 경우 에러처리
    print('0으로 나눌 수 없습니다') 
except TypeError: #문자를 입력받은 경우 에러처리
    print('모든 인자는 숫자여야 합니다')
else:
    GCD = gcd(gcd(a,b), c)
    LCM = lcm(lcm(a,b), c)
    print("최대공약수: {0}, 최소공배수: {1}".format(GCD, LCM))
