a, b, c = map(float, input().split())
temp = 0

if a >= b and a >= c and c >= b:
    temp = b
    b = c
    c = temp
elif b >= a and b >= c and a >= c:
    temp = a
    a = b
    b = temp
elif b >= a and b >= c and c >= a:
    temp = a
    a = b
    b = c
    c = temp
elif c >= a and c >= b and a >= b:
    temp = a
    a = c
    c = b
    b = temp
elif c >= b and c >= a and b >= a:
    temp = a
    a = c
    c = temp

if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
    if(a ** 2 == (b ** 2 + c ** 2)):
        print('TRIANGULO RETANGULO')
    elif a * a > (b * b + c * c):
        print('TRIANGULO OBTUSANGULO')
    elif a * a < (b * b + c * c):
        print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or a == c or b == c:
        print('TRIANGULO ISOSCELES')
else:
    print('NAO FORMA TRIANGULO')