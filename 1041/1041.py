num1, num2 = map(float, input().split())

if num1 > 0.0 and num2 > 0.0:
    print('Q1')
elif num1 < 0.0 and num2 > 0.0:
    print('Q2')
elif num1 < 0.0 and num2 < 0.0:
    print('Q3')
elif num1 > 0.0 and num2 < 0.0:
    print('Q4')
elif num1 == 0.0 and (num2 > 0.0 or num2 < 0.0):
    print('Eixo Y')
elif num2 == 0.0 and (num1 > 0.0 or num1 < 0.0):
    print('Eixo X')
else:
    print('Origem')