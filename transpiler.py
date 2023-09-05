import argparse

args = argparse.ArgumentParser(description='Transpile a file')
args.add_argument('file', metavar='file', type=str, nargs=1, help='file to transpile')
args = args.parse_args()

def extract_code(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        bfpp_code = []
        for line in lines:
            if line == "\n":
                continue
            bfpp_code.append(line.strip())

    return bfpp_code

bfpp_code = extract_code(args.file[0])
print(bfpp_code)

def transpile(code):
    bf_code = ""
    variables = {}
    code_pointer = 0
    for line in code:
        # define variable instruction
        if line.startswith("var"):
            variables[line.split(" ")[1]] = 0
        # set variable instruction
        elif line.startswith("set"):
            equation = line.split(" ")[2:]
            equation = " ".join(equation)
            for var in variables:
                equation = equation.replace(var, str(variables[var]))
            variables[line.split(" ")[1]] = eval(equation)
        # print variable instruction
        elif line.startswith("print"):
            pass
            # get the variable length and print it acordingly
        elif line.startswith("if"):
            pass
            # execute the stuff inside the if statemend if the condition is true
        else:
            Exception("Invalid instruction")

    print(variables)
    return bf_code

bf_code = transpile(bfpp_code)
print(bf_code)