<p align="center">
  <img src=logo.jpg/>
</p>

# Kenzie Academy: Checking for Properly Nested Brackets
In this assessment, we had to check in different brackets were properly nested, hence the title.

## Nesting a bunch of Brackets
In this problem we consider expressions containing brackets that are properly nested. These expressions are obtained by juxtaposition of properly nested expressions in a pair of matching brackets, the left one an opening and the right one a closing bracket.

`( a + \$ ( b = ) ( a ) )` is properly nested

`( a + \$ ) b = ) ( a ( )` is not

In this problem we have several pairs of brackets, so we have to impose a second condition on the expression: the matching brackets should be of the same kind. Consequently ‘(())’ is OK, but ‘([))’ is not. The pairs of brackets are:

- ( )
- [ ]
- { }
- < >
- (\* \*)

The two characters ‘(\*’ should be interpreted as one symbol, not as an opening bracket ‘(’ followed immediately by an asterisk, and similarly for ‘\*)’. The combination ‘(\*)’ should be interpreted as ‘(\*’ followed by ‘)’.

Write a program that checks whether expressions are properly nested. If the expression is not properly nested your program should determine the position of the offending bracket, that is the length of the shortest prefix of the expression that can not be extended to a properly nested expression. Don’t forget ‘(\*’ counts as one, as does ‘\*)’. The characters that are not brackets also count as one.


### Input
The input is a text-file. Each line contains an expression to be checked followed by and end-of-line marker. No line contains more than 3000 characters. The input ends with a standard end-of-file marker.

### Input to Use
```
(*a++(*)
(*a{+}*)
    <************)>
    ()(***)(**)
   ()(***)(*)
({{}{}}[{(){}[]}
   ([))
 ()(**)
    ()*
 aaaaaaa
    aaa(aaaa
 *******
```


### Output
The output is a textfile. Each line contains the result of the check of the corresponding inputline, that is ‘YES’ (in upper case), if the expression is OK, and (if it is not OK) ‘NO’ followed by a space and the position of the error.

### Output to Use
```
NO 6
YES
NO 17
YES
NO 10
NO 17
NO 6
YES
YES
YES
NO 13
YES
```

# How to Make the Magic Happen:
1. Enter `python main.py` in the terminal along with whatever text file you want the function to read.
2. Look for the `output.txt` file.
3. Celebrate! :)