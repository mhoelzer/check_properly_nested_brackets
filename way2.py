import sys


def check_nested_brackets(filename):
    with open(filename) as f:
        exp_list = f.read().split("\n")
    with open("output2.txt", "w") as o:
        for expressions in exp_list:
            result = check_brackets(expressions)
            print(result)
            o.write(result + "\n")


def check_brackets(expressions):
    # print(expressions)
    stack = []
    open_brackets = ["(", "[", "{", "<", "(*"]
    closed_brackets = [")", "]", "}", ">", "*)"]
    count = 0

    while expressions:
        token = expressions[0]
        # ^^^ just token, but if special case, see below
        if expressions.startswith("(*"):
            token = "(*"
        if expressions.startswith("*)"):
            token = "*)"
        count += 1

        if token in open_brackets:
            stack.append(token)
        elif token in closed_brackets:
            closed_index = closed_brackets.index(token)
            # ^^^ idnex of token in the c_b list; match at same index; everything has to line up
            expected_opener = open_brackets[closed_index]
            # gets the symbol based on the index of the item in the o_b based on c_i
            if expected_opener != stack.pop():
                # s.p take off last string and compare to expected string
                return "NO " + str(count)
        expressions = expressions[len(token)]
        # ^^^ slicing; replace expression w/ what has been sliced

    if len(stack) > 0:
        return "NO " + str(count + 1)
    return "YES"


def main(args):
    # first is always there; 2nd is optional/thing you want to do stuff on
    if len(sys.argv) != 2:
        print("hey! give an input file, dumbdumb")
        sys.exit(1)
        # if not, bail out
    check_nested_brackets(sys.argv[1])


if __name__ == "__main__":
    main(sys.argv)
    # ^^^ name of argv will always be in there
    # sys.argv is list of strings w/ a few things in elemnt 0
