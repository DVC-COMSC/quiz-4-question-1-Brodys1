
# ******************************
# Make your Code
flag = 0
count = 0
for i in range(10):
    number = int(input("Enter a number: "))
    if number % 2 == 0: # Even
        flag += 1
        if i == 9:
            if flag >= 2:
                count += 1
    else: # Odd
        if flag >= 2:
            count += 1
        flag = 0
print(count)
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
