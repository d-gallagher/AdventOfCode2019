# OPCODE:
# 1 = Add
# 2 = Mul
# 3 = Save input value to position(param)
# 4 = Output value at position(param)
# 99 = Terminate

from itertools import islice
from rich.traceback import install
from rich import print
install()

infile = open("Day5/input.txt", "r")
opcodes = [int(i) for i in infile.readline().split(',')]

infile_test = open("Day5/test.txt", "r")
opcodes_test = [int(i) for i in infile_test.readline().split(',')]
opcodes_list = [3,0,4,0,99]
# iterator parses instructions
def execute_opcode_instructions(instructions):
    instructions_iterator = iter(enumerate(instructions))
    for idx, elem in instructions_iterator:

        # print(idx, elem)
        opcode, arg1, arg2, arg3 = parse_opcode(elem, idx, instructions)
        if opcode == 1:
            # print(idx, " Instruction 1: \n add value at position", instructions[idx+1], "with", instructions[idx+2], "and store result at position ", instructions[idx+3])
            opcodes[arg3] = opcodes[arg1] + opcodes[arg2]
            print("idx", idx, "opcode", opcode, "opcodes[idx]",elem)
            print("arg1", arg1, ": arg2", arg2,": arg3", arg3)
            idx += 4
        if opcode == 2:
            # print(idx, " Instruction 2: \n mul value at position", instructions[idx+1], "with", instructions[idx+2], "and store result at position ", instructions[idx+3])
            opcodes[arg3] = opcodes[arg1] * opcodes[arg2]
            print("idx", idx, "opcode", opcode,"opcodes[idx]",elem)
            print("arg1", arg1, ": arg2", arg2,": arg3", arg3)
            idx += 4
        if opcode == 3:
            # print(idx, " Instruction 3: \n insert input (1) at position", instructions[idx+1])
            opcodes[arg1] = 1
            print("idx", idx, "opcode", opcode, "opcodes[idx]",elem)
            print("arg1", arg1, ": arg2", arg2,": arg3", arg3)
            idx += 2
        if opcode == 4:
            print(opcodes[arg1])
            # print(idx, " Instruction 4: \n output value at position", instructions[idx+1])
            print("idx", idx, "opcode", opcode, "opcodes[idx]",elem)
            print("arg1", arg1, ": arg2", arg2,": arg3", arg3)
            # if opcode == 4 or opcode == 99:
            #     if opcodes[arg1] != 0 and opcodes[idx + 2] == 99:
            #         print(f"Diagnostic tests succeed, final output = {opcodes[arg1]}")
            idx += 2
        # if opcode == 99:
        #     idx += 1
# read opcode instruction and pad zeroes
# return params to input into opcode add, mult, etc
def parse_opcode(code, idx, instructions):
    # opcode is at position zero
    opcode_value = code % 100
    # param modes
    p1_mode = code // 100 % 10
    p2_mode = code // 1000 % 10
    p3_mode = code // 10000 % 10

    # if mode is zero, use position mode, (same as day 2, use the value at the index of valPos*)
    # if mode is one, use immediate mode, (treat value at valPos* as the value)
    arg1 = instructions[idx + 1] if int(p1_mode) == 0 else (idx + 1)
    arg2 = instructions[idx + 2] if int(p2_mode) == 0 else (idx + 2)
    arg3 = instructions[idx + 3] if int(p3_mode) == 0 else (idx + 3)


    # print debug info
    # print(index)
    # try:
    #     print("opcode", opcode_value,": p1Mode", p1_mode, ": p2Mode", p2_mode,": p3Mode", p3_mode)
    #     print(idx, "opcode", opcode_value, "arg1", arg1, ": arg2", arg2,": arg3", arg3)
    # except UnboundLocalError as e:
    #     None

    # return the values for processing the instructions
    return opcode_value, arg1, arg2, arg3

execute_opcode_instructions(opcodes)
