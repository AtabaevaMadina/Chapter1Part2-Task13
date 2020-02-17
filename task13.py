num_N = int(input('Enter an integer '))
i = 1
for i in range(1, num_N+1):
    i *= i
    if i <= num_N:
        print(i)