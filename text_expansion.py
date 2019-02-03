class Foo:
    def __init__(self):
        self.name = "foo"

    def __repr__(self):
        return self.name


tags = {
    "greeting": "Hi, {name}, who's {age} years old.",
    "name": "Yang-{nickname}}",
    "nickname": "smarty-pants",
    "age": 18,
}


def expand(string):
    while is_curly_braces_pair(string):
        s, e = find_curly_braces(string)
        string = replace_in_braces(string, s, e)
        print string
    return string


def is_curly_braces_pair(string):
    start_idx = string.find("{")
    end_idx = string.find("}")
    print start_idx, end_idx
    if start_idx != -1 and end_idx != -1:
        if start_idx < end_idx:
            return True
        else:
            raise IOError
    elif start_idx != -1 or end_idx != -1:
        raise IOError
    else:
        return False


def find_curly_braces(string):
    start_idx = string.find("{")
    end_idx = string.find("}")
    if is_curly_braces_pair(string):
        return start_idx, end_idx
    else:
        raise IOError


"""
def find_curly_braces(str):
    if is_curly_braces_pair(str):
        start_idx = str.find('{')
        imd = str[start_idx + 1:].find('{')
        end_idx = 0
        for i in range(start_idx, imd + start_idx):
            if str[i] == '}':
                end_idx = i
        return start_idx, end_idx
    else:
        raise IOError
"""


def replace_in_braces(string, start_idx, end_idx):
    substring = string[start_idx+1:end_idx]
    try:
        replacement = str(tags[substring])
    except KeyError:
        return None

    new_string = string[0:start_idx] + replacement + string[end_idx+1:]
    return new_string

try:
    print expand("{greeting} How are you?")
except IOError, e:
    print e

