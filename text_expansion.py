tags = {
    "greeting": "Hi, {name}.",
    "name": "Yang-{nickname}",
    "nickname": "smarty-pants",
}


def display(str):
    running = True
    while(is_curly_braces_pair(str)):
        s, e = find_curly_braces(str)
        str = replace_in_braces(str, s, e)
        if(str.find('{') == -1):
            running = False
            print(str)

def is_curly_braces_pair(str):
    start_idx = str.find("{")
    end_idx = str.find("}")
    if start_idx != -1 and end_idx != -1:
        return True
    else:
        return False

def find_curly_braces(str):
    start_idx = str.find("{")
    end_idx = str.find("}")
    if is_curly_braces_pair(str):
        return start_idx, end_idx
    else:
        raise IOError


def replace_in_braces(str, start_idx, end_idx):
    substring = str[start_idx+1:end_idx]
    try:
        replacement = tags[substring]
    except KeyError:
        return None

    new_string = str[0:start_idx] + replacement + str[end_idx+1:]
    return new_string

display("{greeting} How are you?")

