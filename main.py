__author__ = "mhoelzer"

import sys


def proper_brackets(string):
    storage = []
    index = 0
    position = 0
    # for loop doesnt help with indexing
    while index < len(string):
        position += 1
        item = string[index]
        if item == "(" and index < (len(string) - 1) and string[index + 1] == "*":
            storage.append("(*")
            item += string[index + 1]
            index += 1
        elif item in ["[", "{", "<", "("]:
            storage.append(item)

        if item == "*" and index < (len(string) - 1) and string[index + 1] == ")":
            position -= 1
            if len(storage) == 0:
                return "NO {}".format(str(position))
            elif "(*" == storage[-1]:
                item += string[index + 1]
                index += 1
                storage.pop()
        elif item in ["]", "}", ">", ")"]:
            position += 1
            if len(storage) == 0:
                return "NO {}".format(str(position))
            elif (item == "]" and "[" == storage[-1]) or (item == "}" and "{" == storage[-1]) or (item == ">" and "<" == storage[-1]) or (item == ")" and "(" == storage[-1]):
                storage.pop()
            else:
                return "NO {}".format(str(position - 1))
        index += 1
    if len(storage) != 0:
        return "NO {}".format(str(index))
    else:
        return "YES"


def main(filename):
    with open(filename, "r") as read_opened_file:
        with open("output.txt", "w") as output_file:
            for input_line in read_opened_file:
                answer = proper_brackets(input_line)
                output_file.write("{}\n".format(answer))
    if len(sys.argv) != 2:
        print("usage: python main.py file-to-read")
        sys.exit(1)


if __name__ == "__main__":
    filename = sys.argv[1]
    # ^^^ this refers to what your terminal input is
    # first argument is this file, and 2nd/index 1 is to-read
    main(filename)
