# OPCODE:
# 1 = Add
# 2 = Mul
# 99 = Terminate

infile = open("Day2/input.txt", "r")
opcodes = [int(i) for i in infile.readline().split(',')]
# print(opcodes)
opit = iter(opcodes)

for x in range(len(opcodes)):
    terminate = False
    pos1 = opcodes[x+1]
    pos2 = opcodes[x+2]
    insert = opcodes[x+3]
    if x%4 == 0:
        if opcodes[x] == 1:
            opcodes[insert] = opcodes[pos1] + opcodes[pos2]
            print("Pos: ", x, " Add: ", opcodes[pos1], " and ", opcodes[pos2], " is ", opcodes[insert])
            continue
        if opcodes[x] == 2:
            opcodes[insert] = opcodes[pos1] * opcodes[pos2]
            print("Pos: ", x, " Mul: ", opcodes[pos1], " and ", opcodes[pos2], " is ", opcodes[insert])
            continue
        if opcodes[x] == 99:
            # for a in range(opcodes[x], len(opcodes)):
            print(opcodes)
            print (x, " : ",opcodes[x])
            print("Final Opcode: ", opcodes[0])
            terminate = True
            break
    if terminate:
        break
    continue


#     print(x)
#     if opcodes[x] == 1:
#         opcodes[insert] = opcodes[pos1] + opcodes[pos2]
#
#         print("Pos: ", x, " Add: ", opcodes[pos1], " and ", opcodes[pos2], " is ", opcodes[insert])
#         continue
#     if opcodes[x] == 2:
#         opcodes[insert] = opcodes[pos1] * opcodes[pos2]
#         print("Pos: ", x, " Mul: ", opcodes[pos1], " and ", opcodes[pos2], " is ", opcodes[insert])
#         continue
#     if opcodes[x] == 99:
#         print("Final Opcode: ", opcodes[0])
#         break
#
# print(opcodes)
#

# fix array positions to read values from the correct places
