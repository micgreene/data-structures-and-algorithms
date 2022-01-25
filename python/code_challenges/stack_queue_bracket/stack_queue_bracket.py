from stack import Stack

def validate_brackets(brack_str):
    brack_Stack = Stack()
    str_list = list(brack_str)

    for char in str_list:
        if char == '{':
            brack_Stack.push(char)
        elif char == '(':
            brack_Stack.push(char)
        elif char == '[':
            brack_Stack.push(char)
        elif char == '}':
            if brack_Stack.is_empty() != True:
                comparison = brack_Stack.pop()
                if comparison != '{':
                    return False
            else:
                return False
        elif char ==  ')':
            if brack_Stack.is_empty() != True:
                comparison = brack_Stack.pop()
                if comparison != '(':
                    return False
            else:
                return False
        elif char ==  ']':
            if brack_Stack.is_empty() != True:
                comparison = brack_Stack.pop()
                if comparison != '[':
                    return False
            else:
                return False
    if brack_Stack.is_empty() == True:
        return True
    else:
        return False
