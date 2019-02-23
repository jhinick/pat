# input a list of students' info (including name, id, and score)
# this procedure is to find the highest and lowest scores of them and print them out

num = int(input())

high_name = None
high_id = None
high_score = -1
low_name = None
low_id = None
low_score = 101


for i in range(num):
    info = input()
    name, id, score = info.split()
    if int(score) > int(high_score):
        high_name = name
        high_id = id
        high_score = score
    if int(score) < int(low_score):
        low_name = name
        low_id = id
        low_score = score

print(high_name, high_id, sep=" ")
print(low_name, low_id, sep=" ")

