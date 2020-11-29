# OPCODE:
# 1 = Add
# 2 = Mul
# 99 = Terminate

infile = open("Day2/input.txt", "r")
opcodesIn = [int(i) for i in infile.readline().split(',')]

# Generate list with verb and noun pair
def update_codes(codes, verb, noun):
    copy = list(codes)
    copy[1] = verb
    copy[2] = noun
    return copy


# execute opcodes in list and return result at list[0]
def process_opcodes(verb, noun):
    new_opcodes = update_codes(opcodesIn, verb, noun)

    for x in range(len(new_opcodes)):
        terminate = False
        pos1 = new_opcodes[x+1]
        pos2 = new_opcodes[x+2]
        insert = new_opcodes[x+3]
        if x % 4 == 0:
            if new_opcodes[x] == 1:
                new_opcodes[insert] = new_opcodes[pos1] + new_opcodes[pos2]
                continue
            if new_opcodes[x] == 2:
                new_opcodes[insert] = new_opcodes[pos1] * new_opcodes[pos2]
                continue
            if new_opcodes[x] == 99:
                terminate = True
                break
        if terminate:
            break
        continue
    return new_opcodes[0]

# dictionary to hold verb noun value
mydict = {}

# Brute force finds the (verb, noun) input pair that generate the provided output(param)
def find_pair_from_output(output):
    found_output = False
    for x in range(100):
        if found_output:
            break
        for y in range(100):
            mydict[x,y] = process_opcodes(x, y)
            if mydict[x, y] == output:
                found_output = True
                break
def test():
    for x in range(100):
        for y in range(100):
            mydict[x,y] = process_opcodes(x, y)
#
# test()
# print(mydict)
#
print("Enter the value to obtain the verb/noun pair:")
user_input = int(input())
find_pair_from_output(user_input)
for key,value in mydict.items():
    if value == user_input:
        print("(Verb, Noun): ", key, "\nValue: ", value)
