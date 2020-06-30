
def parse_args(string):
    '''Parser for the live demo of pgscript objects. this function parses the string from the text box and turns it into arguments for the pgscript object.'''
    open_curl = []
    close_curl = []

    open_square = []
    close_square = []
    for n,char in enumerate(string):
        if char == "(":
            open_curl.append(n)
        if char == ")":
            close_curl.append(n)
        
        if char == "[":
            open_square.append(n)
        if char == "]":
            close_square.append(n)
    
    curl = []
    for i in range(len(open_curl)):
        curl.append((open_curl[i], close_curl[i]))

    square = []
    for m in range(len(open_square)):
        square.append((open_square[m], close_square[m]))

    for n in curl:
        string = string[:n[0]] + string[n[0]:n[1]].replace(",", "%") + string[n[1]:]

    for n in square:
        string = string[:n[0]] + string[n[0]:n[1]].replace(",", "%") + string[n[1]:]

    args_list = string.split(",")

    for n in range(len(args_list)):
        args_list[n] = args_list[n].replace("%", ",").strip()
    for n in range(len(args_list)):
        if "(" in args_list[n] or "[" in args_list[n]:
            args_list[n] = args_list[n][1:-1].split(",")
            for c,l in enumerate(args_list[n]):
                args_list[n][c] = int(l)
        
        elif args_list[n].isdigit():
            args_list[n] = int(args_list[n])

        elif args_list[n].lower() == "true" or args_list[n].lower() == "false":
            args_list[n] = bool(args_list[n])

        elif args_list[n][0] == "'" or args_list[n][0] == '"':
            args_list[n] = args_list[n][1:-1]
     
    args_list.pop(0)
    return args_list


