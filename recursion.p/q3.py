def sum_num(num):
    if num == 0:
        return 0
    return sum_num(num-1)+num

x = sum_num(5)
print(x)