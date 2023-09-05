import argparse
import re

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
            if line.startswith("#"):
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
            # var variable_name variable_type = variable_init_value
            variable_name = line.split(" ")[1]
            variable_type = line.split(" ")[2]
            variable_init_value = line.split(" = ")[1]

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
                # remove the quotes from the string
                if variable_init_value[0] != "\"" or variable_init_value[-1] != "\"":
                    Exception(f"Invalid string {variable_init_value}")
                variable_init_value = variable_init_value[1:-1]
                variables[variable_name] = {
                    "type": "str",
                    "pointer": variable_length,
                    "length": len(variable_init_value),
                }
                variable_length += len(variable_init_value)
                for char in variable_init_value:
                    bf_code += "+" * ord(char)
                    bf_code += ">"
                    code_pointer += 1
            else:
                Exception(f"Invalid variable type {variable_type}")

        # expression instruction
        elif line.startswith("set"):
            # set fizzbuzz str = fizz + buzz
            expression_return_variable = line.split(" ")[1]
            expression_return_type = line.split(" ")[2]
            expression = line.split(" = ")[1]
            expression = expression.split(" ")

            if expression_return_variable in variables:
                Exception(f"Variable {expression_return_variable} already defined")

            Exception("Not implemented")

        # print variable instruction
        elif line.startswith("print"):
            # print fizzbuzz
            variable_name = line.split(" ")[1]
            if variable_name not in variables:
                Exception(f"Variable {variable_name} not defined")
            variable = variables[variable_name]
            if variable["type"] == "int":
                # if variable is behind the pointer, move the pointer to the variable
                if variable["pointer"] > code_pointer:
                    bf_code += ">" * (variable["pointer"] - code_pointer)
                    code_pointer = variable["pointer"]
                # if variable is in front of the pointer, move the pointer to the variable
                elif variable["pointer"] < code_pointer:
                    bf_code += "<" * (code_pointer - variable["pointer"])
                    code_pointer = variable["pointer"]
                bf_code += "."
            elif variable["type"] == "str":
                # if variable is behind the pointer, move the pointer to the variable
                if variable["pointer"] > code_pointer:
                    bf_code += ">" * (variable["pointer"] - code_pointer)
                    code_pointer = variable["pointer"]
                # if variable is in front of the pointer, move the pointer to the variable
                elif variable["pointer"] < code_pointer:
                    bf_code += "<" * (code_pointer - variable["pointer"])
                    code_pointer = variable["pointer"]
                bf_code += "["
                bf_code += "<" * variable["length"]
                bf_code += ">"
                bf_code += "."
                bf_code += ">" * variable["length"]
                bf_code += "]"

                print(f"printing pointer {code_pointer} {variable}")
                # adjust the pointer to the end of the string
            else:
                Exception(f"Invalid variable type {variable['type']}")
        elif line.startswith("if"):
            pass
            # execute the stuff inside the if statemend if the condition is true
        else:
            Exception("Invalid instruction")
    
    print(variables)
    return bf_code + "bfpp"

bf_code = transpile(bfpp_code)
print(bf_code)