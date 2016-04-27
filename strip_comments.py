import sys

def strip_comments(str):
    # Tokenize input on each line
    tokens = str.split("\n")
    new_str = []
    # Go through each line to find C style comments and remove
    for line in tokens:
        # Check if quotes are used. If they are, only remove double slashes outside of quotes
        if "\"" in line:
            if line[0:line.rfind(" //")].rfind("\"") is not line[0:line.rfind(" //")].find("\""):
                new_str.append(line[0:line.rfind(" //")])
            else:
                new_str.append(line)
        elif "\'" in line:
            if line[0:line.rfind(" //")].rfind("\'") is not line[0:line.rfind(" //")].find("\'"):
                new_str.append(line[0:line.rfind(" //")])
            else:
                new_str.append(line)
        # If no quotes are used, grab everything before double slashes
        else:
            new_str.append(line.partition("//")[0])

    # Return new string created from list of stripped lines
    # Join on newline character to preserve original format
    return "\n".join(new_str)

def main():
    print sys.argv[1]
    file_name = sys.argv[1]
    f = open(file_name, 'r')
    f_data = f.read()

    stripped_str = strip_comments(f_data)
    print stripped_str

if __name__ == '__main__':
    main()
