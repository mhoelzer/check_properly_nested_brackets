def proper_brackets(string):
    storage = []
    index = 0
    while index < len(string):
        # # if (string[0] == "(") and (string[1] == "*"):
        # if "(*" in string:
        #     # string = string.replace("(", "~").replace("*", "~")
        #     string = string.replace("(*", "&~")
        #     print(string),
        # elif "*)" in string:
        #     string = string.replace("*)", "~&")
        #     print(string),
        item = string[index]
        if item == "(" and index < len(string)-1 and string[index + 1] == "*":
            storage.append("(*")
            index += 1
        elif item in ["[", "{", "<", "("]:
            storage.append(item)

        # print storage
        if item == "*" and index < len(string)-1 and string[index + 1] == ")":
            if len(storage) == 0:
                return False, index
            elif "(*" == storage[-1]:
                index += 1
                storage.pop()
        elif item in ["]", "}", ">", ")"]:
            if len(storage) == 0:
                return False, index
            elif (item == "]" and "[" == storage[-1]) or (item == "}" and "{" == storage[-1]) or (item == ">" and "<" == storage[-1]) or (item == ")" and "(" == storage[-1]):
                storage.pop()
            else:
                return False
        index += 1
    if len(storage) != 0:
        return False, index
    else:
        return True

    # storage = []
    # dict1 = {"[": "sym1", "{": "sym2", "(": "sym3", "<": "sym4", "(*": "sym5"}
    # dict2 = {"]": "sym1", "}": "sym2", ")": "sym3", ">": "sym4", "*)": "sym5"}
    # for item in string:
    #     if item in dict1:
    #         storage.append(item)
    #     if item in dict2:
    #         if len(storage) == 0:
    #             return False, index
    #         elif (item in dict2 and item in storage):
    #             storage.pop()
    #         else:
    #             return False, index
    # if len(storage) != 0:
    #     return False, index
    # else:
    #     return True

    # parens = 0
    # curls = 0
    # squares = 0
    # arrows = 0
    # stars = 0
    # for element in string:
    #     if element == "(":
    #         parens += 1
    #     elif element == ")":
    #         parens -= 1
    #     if element == "{":
    #         curls += 1
    #     elif element == "}":
    #         curls -= 1
    #     if element == "[":
    #         squares += 1
    #     elif element == "]":
    #         squares -= 1
    #     if element == "<":
    #         arrows += 1
    #     elif element == ">":
    #         arrows -= 1
    #     if element == "(*":
    #         stars += 1
    #     elif element == "*)":
    #         stars -= 1
    #     if parens < 0 or curls < 0 or squares < 0 or arrows < 0 or stars < 0:
    #         return False, string.index(element)
    # return parens == 0 and curls == 0 and squares == 0 and arrows == 0 and stars == 0


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
