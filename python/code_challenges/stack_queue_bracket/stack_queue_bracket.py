from stack import Stack

def validate_brackets(str):
    brack_Stack = Stack()

    str_list = str.split(''

    for char in str_list:
        if char == '{' or char == '(' or char == '[':
            brack_Stack.push(char)

        match char:
            case '}':
                if brack_Stack.peek() != False:
                    comparison = brack_Stack.pop()
                    if comparison != '{':
                        return False
            case ')':
                if brack_Stack.peek() != False:
                    comparison = brack_Stack.pop()
                    if comparison != '(':
                        return False
            case ']':
                if brack_Stack.peek() != False:
                    comparison = brack_Stack.pop()
                    if comparison != '[':
                        return False

    if brack_Stack.is_empty() == True
        return True
    else:
        return False

test1 = '{}(){}';
test2 = '()[[Extra Characters]]';
test3 = '{}{Code}[Fellows](())';
test4 = '[({}]';
test5 = '(](';
test6 = '{(})';
test7 = '{';
test8 = ')';
test9 = '[}';

print(f'test1:  '{validate_brackets(test1)});
print(f'test2:  ', validate_brackets(test2));
print(f'test3:  ', validate_brackets(test3));
print(f'test4:  ', validate_brackets(test4));
print(f'test5:  ', validate_brackets(test5));
print(f'test6:  ', validate_brackets(test6));
print(f'test7:  ', validate_brackets(test7));
print(f'test8:  ', validate_brackets(test8));
print(f'test9:  ', validate_brackets(test9));
