tags = {
    "greeting": "Hi, {name}.",
    "name": "Yang-{nickname}",
    "nickname": "smarty-pants",
}

def display(str):
    s, e = find_curly_braces(str)
    new_string = replace_in_braces(str, s, e)
    print(new_string)

    s, e = find_curly_braces(new_string)
    new_string = replace_in_braces(new_string, s, e)
    print(new_string)

    s, e = find_curly_braces(new_string)
    new_string = replace_in_braces(new_string, s, e)
    print(new_string)

def find_curly_braces(str):
    start_idx = str.find("{")
    end_idx = str.find("}")
    return start_idx, end_idx

def replace_in_braces(str, start_idx, end_idx):
    substring = str[start_idx+1:end_idx]
    try:
        replacement = tags[substring]
    except KeyError:
        return None

    new_string = str[0:start_idx] + replacement + str[end_idx+1:]
    return new_string

display("{greeting} How are you?")