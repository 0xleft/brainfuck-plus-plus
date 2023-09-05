import argparse

args = argparse.ArgumentParser(description='Interpret a file')
args.add_argument('file', metavar='file', type=str, nargs=1, help='file to interpret')
args.add_argument('--max-memory', metavar='max-memory', type=int, nargs=1, default=[30000], help='maximum memory')
args = args.parse_args()

COMP_CHARS = "+ - > < [ ] . ,".split(" ")

def extract_code(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        bf_code = ""
        for line in lines:
            for char in line:
                if char in COMP_CHARS:
                    bf_code += char

    return bf_code

bf_code = extract_code(args.file[0])

def interpret(code, max_memory):
    memory = [0] * max_memory
    pointer = 0
    code_pointer = 0
    while code_pointer < len(code):
        char = code[code_pointer]
        if char == '+':
            memory[pointer] += 1
        elif char == '-':
            memory[pointer] -= 1
        elif char == '>':
            pointer += 1
        elif char == '<':
            pointer -= 1
        elif char == '[':
            if memory[pointer] == 0:
                while code[code_pointer] != ']':
                    code_pointer += 1
        elif char == ']':
            if memory[pointer] != 0:
                while code[code_pointer] != '[':
                    code_pointer -= 1
        elif char == '.':
            print(chr(memory[pointer]), end="")
        elif char == ',':
            memory[pointer] = ord(input()[0])
        code_pointer += 1

interpret(bf_code, args.max_memory[0])