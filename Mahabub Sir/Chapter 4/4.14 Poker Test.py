import math
import random

n = int(input())

p_four_different_digit = (10 / 10) * (9 / 10) * (8 / 10) * (7 / 10) * n
p_three_equal_digit = (10 / 10) * (1 / 10) * (1 / 10) * (9 / 10) * n
p_all_digit_equal = (10 / 10) * (1 / 10) * (1 / 10) * (1 / 10) * n
p_one_pair = math.comb(4, 2) * (10 / 10) * (1 / 10) * (9 / 10) * (8 / 10) * n
p_two_pair = math.comb(4, 2) * (10 / 10) * (1 / 10) * (9 / 10) * (1 / 10) * n

four_different_digit = 0
three_equal_digit = 0
all_digit_equal = 0
one_pair = 0
two_pair = 0
for i in range(n):
    rn = random.randint(1000, 9999)
    lst = list(str(rn))
    lst.sort()
    count = 1

    for i in range(4 - 1):
        if lst[i] == lst[i + 1]:
            count += 1

    if count == 4:
        all_digit_equal += 1
    elif count == 2:
        one_pair += 1
    elif count == 1:
        four_different_digit += 1
    else:
        if lst[1] == lst[2]:
            three_equal_digit += 1
        else:
            two_pair += 1

print(all_digit_equal,three_equal_digit,four_different_digit,one_pair,two_pair)

res1 = abs(four_different_digit - p_four_different_digit) ** 2 / p_four_different_digit
res2 = abs(three_equal_digit - p_three_equal_digit) ** 2 / p_three_equal_digit
res3 = abs(all_digit_equal - p_all_digit_equal) ** 2 / p_all_digit_equal
res4 = abs(one_pair - p_one_pair) ** 2 / p_one_pair
res5 = abs(two_pair - p_two_pair) ** 2 / p_two_pair

print(res1 + res2 + res3 + res4 + res5)