def proper_brackets(string):
    for element in string:
        if "(" in element:
            return True


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