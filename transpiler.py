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
    variable_length = 0
    for line in code:
        # define variable instruction
        if line.startswith("var"):
            variable_name = line.split(" ")[1]
            variable_type = line.split(" ")[2]
            variable_init_value = line.split(" = ")[1]

            # check if variable init value is a

            if line.split(" ")[1] in variables:
                Exception(f"Variable {variable_name} already defined")
            if variable_type == "int":
                variables[variable_name] = {
                    "type": "int",
                    "pointer": variable_length,
                    "length": 1
                }
                variable_length += 1
                bf_code += "+" * int(variable_init_value)
                bf_code += ">"
                code_pointer += 1
            elif variable_type == "str":
                variables[variable_name] = {
                    "type": "str",
                    "pointer": variable_length,
                    "length": len(variable_init_value)
                }
                variable_length += len(variable_init_value)
                for char in variable_init_value:
                    bf_code += "+" * ord(char)
                    bf_code += ">"
                    code_pointer += 1
            else:
                Exception(f"Invalid variable type {variable_type}")

        # set variable instruction
        elif line.startswith("set"):
            equation = line.split(" ")[2:]
            equation = " ".join(equation)
            print(equation)

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
    return bf_code + "bfpp"

bf_code = transpile(bfpp_code)
print(bf_code)