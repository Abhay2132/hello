_range = 10

nums = input("Enter a number : ")

nums_dict = {
    "0":"zero",
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
}

if len(nums) >= _range :
    raise Exception("SANCHIT ka Error")
else:
    for num in nums:
        print(nums_dict[str(num)], end=" ")