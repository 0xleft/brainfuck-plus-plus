import argparse

args = argparse.ArgumentParser(description='Transpile a file')
args.add_argument('file', metavar='file', type=str, nargs=1, help='file to transpile')
args = args.parse_args()

def extract_code(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        bfpp_code = ""
        for line in lines:
            bfpp_code += line

    return bfpp_code

bfpp_code = extract_code(args.file[0])
