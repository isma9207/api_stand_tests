n = int(input('Type a number -> '))
i = 0

if 1<=n<=20:
    while i < n:
        print(i**2)
        i += 1
else:
    print('The nummer n is out of range, 1<=n<=100 ')

