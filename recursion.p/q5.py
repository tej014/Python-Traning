# Write a recursive function to calculate the power of a number.
  

def power_num(num,power):
    if power == 0:
        return 1
    return power_num(num,power-1)*num

print(power_num(2,4)) 