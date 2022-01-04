def swap_case(s):
    new_str = ""
    for i in s:
        if i.isupper():
            new_str += i.lower()
        elif not i.isupper():
            new_str += i.upper()
        else:
            pass
    
    return new_str