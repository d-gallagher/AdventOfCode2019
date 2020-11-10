# puzzle range 125730-579381
# 6 digit num
# must not decrease left to right
# must be within range
# must contain double digit eg '11','22' etc

import re

low = 125730
high = 579381

# find repeating pair in pw
def repeating(pw):
    accept = False
    d = dict()
    for x in pw:
        if x in d:
            d[x] = d[x]+1
        else:
            d[x] = 1

    for value in d.values():
        if value == 2:
            accept = True

    return accept

# check pw digits increase
def check_increasing(pw):
    digits = [int(x) for x in pw]
    increasing = True
    running = True

    while running:
        for idx, elem in enumerate(digits):
            # break from loops after checking last index
            if idx == 5:
                running = False
                break
            thiselem = elem
            nextelem = digits[(idx + 1) % len(digits)]

            # break from loops after finding decrease
            if nextelem < thiselem:
                increasing = False
                running = False
                break

    return increasing

valid_pw_list = []

# process range of numbers and find valid passwords
def run():
    for i in range(low, high):
        # string representation of pw
        pw_str = str(i)
        pw_len = len(pw_str)
        # pw_isvalidlen = True if pw_len == 6 else False

        if repeating(pw_str) and check_increasing(pw_str):
            valid_pw_list.append(i)

    print(len(valid_pw_list))


# run program
run()
