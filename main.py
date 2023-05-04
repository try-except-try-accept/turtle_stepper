from sys import argv




def get_pad(line):
    pad = (len(line) - len(line.strip()))
    pad_char, mul = " ", 4
    if line.startswith("\t"):
        pad_char = "\t"
        mul = 1
    
    first_tok = line.split(" ")[0]
    if first_tok in "if,else,elif,for,def,while,try".split(","):
        pad += (1 * mul)
    
    return pad_char * pad

def parse_turtle_code(fn):
    code = ""
    with open(fn, "r") as file:
        for line in file.read().splitlines():
            if line.strip():
                code += line + f"\n{get_pad(line)}input('Continue?: ')\n"

    print(code)
    return code





if __name__ == "__main__":
    fn = "turtle_demo.py"
    if len(argv) > 1:
        fn = argv[1]


    exec(parse_turtle_code(fn))

    
