
# find out which num is not examed in the procedure of examing the very first given num

key = int(input())

array = input().split()         # split(), with a list as return value

while key != 1:
    if key % 2 == 0:
        key /= 2
    else:
        key = (3 * key + 1) / 2
    if str(int(key)) in array:
        array.remove(str(int(key)))

for i in array:
    i = int(i)

array.sort(key=int, reverse=True)

print(*array, sep=" ")
