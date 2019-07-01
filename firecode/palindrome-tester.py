def is_palindrome(input_string):
    result = True
    ls = len(input_string)
    
    for i in range(0, int(ls/2)):
        if input_string[i] != input_string[ls-i-1]:
            return False
            break
        
    return result
        