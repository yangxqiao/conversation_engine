tags = {
    "greeting": "Hi, {name}. You are {age}.",
    "age": "18",
    "name": "Yang-{nickname}",
    "nickname": "smarty-pants",
}


def is_curly_braces_pair(str):
    start_idx = str.find("{")
    end_idx = str.find("}")
    if start_idx != -1 and end_idx != -1:
        return True
    else:
        return False


def find_curly_braces(str):
    if is_curly_braces_pair(str):
        for i in range(len(str)):
            if str[i] == '{':
                start_idx = i
        for i in range(start_idx, len(str)):
            if str[i] == '}':
                end_idx = i
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


def display(str):
    while is_curly_braces_pair(str):
        s, e = find_curly_braces(str)
        str = replace_in_braces(str, s, e)
    print(str)


display("{greeting} How are you?")

