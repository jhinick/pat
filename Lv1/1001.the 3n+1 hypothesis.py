# for every integer n, if it's odd, then half it, otherwise half 3n + 1, finally we will get 1

# now you should determine how many step it needs to get the "1" for any integer from 0 and not exceeding 1000

n = int(input())
step = 0
while n != 1:
    step += 1
    if n % 2 == 0:
        n /= 2
    else:
        n = (3*n + 1) / 2


print(step)
