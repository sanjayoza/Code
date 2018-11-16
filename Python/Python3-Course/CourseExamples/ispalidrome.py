import string

def ispalidrome(string1):
    p = (string1.replace(" ", "")).lower()
    print(p)
    r = p[::-1]
    print(r)
    if p == r:
        return True
    return False


print(ispalidrome("This is a string"))
