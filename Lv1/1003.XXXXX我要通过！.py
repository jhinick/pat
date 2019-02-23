
################################# 1.0
# expr {A}P{A+}T{A}
# time = input()      # indict how many strings will be tested

# for i in range(int(time)):
#     string = input()
#     state = 0
#     for j in string:
#         if state == 0:              # state 0: {A}
#             if j == "P":
#                 state = 1
#                 continue
#             elif j == "A":
#                 continue
#             else:
#                 break               # state remains 0
#         if state == 1:              # state 1: {A}P
#             if j == "A":
#                 state = 2
#                 continue
#             else:
#                 break
#         if state == 2:              # state 2: {A}PA
#             if j == "A":
#                 continue
#             elif j == "T":
#                 state = 3
#                 continue
#             else:
#                 break
#         if state == 3:             # state 3: {A}P{A+}T
#             if j == "A":
#                 continue
#             else:
#                 state = -1
#     if state == 3:
#         print("YES")
#     else:
#         print("NO")


# leftA P midA T rightA

count = input()

for i in range(int(count)):
    string = input()
    phase = 0
    left_A = mid_A = right_A = 0
    for c in string:
        if phase == 0:          # "A"
            if c == "A":
                left_A += 1
                continue
            elif c == "P":
                phase = 1           # phase 1: {A}P
                continue
            else:
                break               # exit with phase == 0
        if phase == 1:              # phase 1: {A}P
            if c == "A":
                mid_A += 1
                continue
            elif c == "T":
                phase = 2
                continue            # phase 2: {A}P{A}T
            else:
                break               # exit with phase == 1
        if phase == 2:              # phase 2: {A}P{A}T
            if c == "A":
                right_A += 1
                continue
            else:
                phase = -1
                break               # exit with phase == -1

    if phase == 2:                  #
        if mid_A == 1:
            print("YES")            # xPATx
        else:
            if right_A >= (mid_A - 1) * left_A:
                print("YES")
            else:
                print("NO")
    else:
        print("NO")
















