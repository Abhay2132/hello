s = input("enter random input : ")

numbers = []
special_chars = []
upper = []
lower = []

for c in s:
    # checking for int
    if str(c).isnumeric():
        numbers.append(c)
    else:
        if c == " ":
            continue
        elif c.isalpha():
            if c.islower():
                lower.append(c)
            else:
                upper.append(c)
        else:
            special_chars.append(c)

print("numbers : ", set(numbers))
print("special : ", set(special_chars))
print("Small   : ", set(lower))
print("Capital : ", set(upper))