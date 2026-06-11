x = int(input())
num = x
for i in range(0,12):
    if i != 0:
        num +=1

    if num % 2 != 0:
        print(num)
        