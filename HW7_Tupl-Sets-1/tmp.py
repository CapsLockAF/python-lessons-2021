def calc_sum(str_nums):
    list_nums = str_nums.split()
    s = 0
    for item in list_nums:
        s += int(item)
    return s


print("Please start to enter string of numbers separated by space. "
      "'#': stop input:")

ans = "o"
total = 0
while ans != "#":
    strNums = input()
    if "#" in strNums:
        ans = "#"
        i = strNums.index("#")
        strNums = strNums[:i]
    sum_str = calc_sum(strNums)
    print(sum_str)
    total += sum_str
print(total)
