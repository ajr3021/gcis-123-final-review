"""
Create a function that, given a string of opening and closing parenthesis (),
will return weather or not the parenthesis are valid.

For parenthesis to be balanced every opening parenthesis should be closed
and every closing parenthesis should should actual close something.

Examples:

() => valid
)( => invalid 
((())) => valid
(())) => invalid

Note: If you practice with testing, feel free to write unit tests for this. 
"""

from Stack import Stack
"""
Implement the above function using a stack
"""

def valid_parenthesis_stack(string):
    stack = Stack()

    for ch in string:
        if ch == '(':
            stack.push(ch) # push when see an open
        else:
            if stack.is_empty(): # is there is nothing to close
                return False # invalid
            stack.pop() # pop when you see a close
    return stack.is_empty() # if there are more opens left, it is invalid, otherwise it is valid

"""
Implement the above function using recursion
"""
def valid_parenthesis_rec(string):
    if len(string) == 0:
        return True
    elif len(string) == 1:
        return False
    elif string[0] != '(' or string[-1] != ')':
        return False
    else:
        return valid_parenthesis_rec(string[1:-1])


print(valid_parenthesis_stack('()'))
print(valid_parenthesis_stack(')('))
print(valid_parenthesis_stack('((((()))))'))
print(valid_parenthesis_stack('((((())))))))'))
print(valid_parenthesis_stack('(((((((()))))))'))

print(valid_parenthesis_rec('()'))
print(valid_parenthesis_rec(')('))
print(valid_parenthesis_rec('((((()))))'))
print(valid_parenthesis_rec('((((())))))))'))
print(valid_parenthesis_rec('(((((((()))))))'))