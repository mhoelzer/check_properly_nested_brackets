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
                return "NO {}hey".format(str(position - 1))
        index += 1
    if len(storage) != 0:
        return "NO {}".format(str(index + 1))
    else:
        return "YES"


print(proper_brackets("(*a++(*)"))
print(proper_brackets("(*a{+}*)"))
print(proper_brackets("    <************)>"))
print(proper_brackets("    ()(***)(**)"))
print(proper_brackets("   ()(***)(*)"))
print(proper_brackets("({{}{}}[{(){}[]}"))
print(proper_brackets("   ([))"))
print(proper_brackets(" ()(**)"))
print(proper_brackets("    ()*"))
print(proper_brackets(" aaaaaaa"))
print(proper_brackets("    aaa(aaaa"))
print(proper_brackets(" *******"))
