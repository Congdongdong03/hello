def next_number(num):
    if num % 2 == 0:
        return 3*num + 1
    else:
        return 2*num + 2
num = [6,7]
for re_num in num:
    print(next_number(re_num))