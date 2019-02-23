# 读入一个正整数 n，计算其各位数字之和，用汉语拼音写出和的每一位数字

# n is guaranteed not exceeding 10 ** 100

# the array of every number
pinyin = ["ling", "yi", "er", "san", "si", "wu", "liu", "qi", "ba", "jiu"]

n = input()         # we take n as a string rather than integer
sum = 0
for i in n:
    sum += int(i)
sum = str(sum)
for i in sum[0:-1]:
    print(pinyin[int(i)], end=" ")
print(pinyin[int(sum[-1])])



