b = 0
a = int(input())
while a > 1:
    if a < 0:
        print('Wrong one')
    if a % 2 == 0:
        a//=2
        b+=1
    elif a % 2 == 1:
        a = 3*a + 1
        b+=1
print(b)