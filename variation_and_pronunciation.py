def expand(string, dictionary):
    while is_brackets_pair(string, "{", "}"):
        s, e = find_brackets(string, "{", "}")
        string = replace_in_braces(dictionary, string, s, e)
    return string


def interpret_display(string):
    while is_brackets_pair(string, "[", "]") and string.find("#") != -1:
        s, e = find_brackets(string, "[", "]")
        before_string, after_string = get_string_before_and_after_substring(string, s, e)
        string = update_string_for_display(string, before_string, s, e)
    return string


def interpret_pronunciation(string):
    while is_brackets_pair(string, "[", "]") and string.find("#") != -1:
        s, e = find_brackets(string, "[", "]")
        before_string, after_string = get_string_before_and_after_substring(string, s, e)
        string = update_string_for_display(string, after_string, s, e)
    return string


def is_brackets_pair(string, start_bracket, end_bracket):
    start_idx = string.find(start_bracket)
    end_idx = string.find(end_bracket)
    if start_idx != -1 and end_idx != -1:
        if start_idx < end_idx:
            return True
        else:
            raise IOError("Found a closed parentheses before and open one => check your input")
    elif start_idx != -1 or end_idx != -1:
        raise IOError("Only found one parenthesis")
    else:
        return False


def find_brackets(string, start_bracket, end_bracket):
    start_idx = string.find(start_bracket)
    end_idx = string.find(end_bracket)
    if is_brackets_pair(string, start_bracket, end_bracket):
        return start_idx, end_idx
    else:
        raise IOError


def replace_in_braces(dictionary, string, start_idx, end_idx):
    substring = string[start_idx+1:end_idx]
    try:
        replacement = str(dictionary[substring])
    except KeyError:
        raise KeyError("No match for key \'%s\'" % substring)

    new_string = string[0:start_idx] + replacement + string[end_idx+1:]
    return new_string


def get_string_before_and_after_substring(string, s, e, substring='#'):
    substring_idx = string.find(substring)
    before_string = string[s+1:substring_idx]
    after_string = string[substring_idx+1:e]
    return before_string.strip(), after_string.strip()


def update_string_for_display(string_for_display, before_string, s, e):
    string_for_display = string_for_display[:s] + before_string + string_for_display[e+1:]
    return string_for_display


def update_string_for_pronounce(string_for_pronounce, after_string, s, e):
    string_for_pronounce = string_for_pronounce[:s] + after_string + string_for_pronounce[e + 1:]
    return string_for_pronounce


if __name__ == '__main__':

    tags = {
        "greeting": "Hi, {name}.",
        "name": "[Audrow# Aw drow] -{nickname}",
        "nickname": "smarty-pants",
    }

    string = "{greeting} How are you? He knows [Yang #Young]."


    try:
        string = expand(string, tags)
    except Exception as e:
        print("EXCEPTION:", e)

    print(string)

    string_for_display = interpret_display(string)

    string_for_pronounce = interpret_pronunciation(string)

    print(string_for_display)

    print(string_for_pronounce)