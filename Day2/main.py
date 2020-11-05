# OPCODE:
# 1 = Add
# 2 = Mul
# 99 = Terminate

infile = open("Day2/input.txt", "r")
opcodesIn = [int(i) for i in infile.readline().split(',')]


def update_codes(codes, verb, noun):
    copy = list(codes)
    copy[1] = verb
    copy[2] = noun
    return copy


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
# found_pair = ()
def find_pair_from_output(output):
    found_output = False
    for x in range(100):
        if found_output:
            break
        for y in range(100):
            mydict[x,y] = process_opcodes(x, y)
            if mydict[x, y] == output:
                found_output = True
                # found_pair = (x, y)
                break

print("Enter the value to obtain the verb/noun pair:")
user_input = int(input())
find_pair_from_output(user_input)
for key,value in mydict.items():
    if value == user_input:
        print("(Verb, Noun): ", key, "\nValue: ", value)
