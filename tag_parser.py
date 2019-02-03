def parse_start_tag(tag_body):

    tag_body = tag_body.split()
    tag = tag_body[0]
    attribs = {}
    tag_body_len = len(tag_body)

    idx = 1
    while idx < tag_body_len:

        # Add entries to the tag_body to make sure that we don't attempt to access an undefined index
        if idx+2 > tag_body_len:
            tag_body += [None, None]
        elif idx+1 > tag_body_len:
            tag_body.append(None)

        key_value_pair = ""
        if tag_body[idx + 1] == "=":
            key_value_pair += tag_body[idx] + tag_body[idx + 1] + tag_body[idx + 2]
            idx += 3
        elif tag_body[idx][-1] == "=" or tag_body[idx + 1][0] == "=":
            key_value_pair += tag_body[idx] + tag_body[idx + 1]
            idx += 2
        elif tag_body[idx].find("=") != -1 and tag_body[idx][-1] != "=":
            key_value_pair = tag_body[idx]
            idx += 1
        else:
            raise IOError("Invalid tag attribute in tag %s" % tag)

        key, value = get_string_before_and_after_substring(key_value_pair, "=")

        attribs[key] = value

    return tag, attribs


def find_parenthesis(string, open_paren="<", closed_paren=">"):
    start_idx = string.find(open_paren)
    end_idx = string.find(closed_paren)
    if is_parenthesis_pair(string):
        return start_idx, end_idx
    else:
        raise IOError


def is_parenthesis_pair(string, open_paren="<", closed_paren=">"):
    start_idx = string.find(open_paren)
    end_idx = string.find(closed_paren)
    if start_idx != -1 and end_idx != -1:
        if start_idx < end_idx:
            return True
        else:
            raise IOError("Found a closed parentheses before and open one => check your input")
    elif start_idx != -1 or end_idx != -1:
        raise IOError("Only found one parenthesist")
    else:
        return False


def get_substring(string, start_idx, end_idx):
    return string[start_idx+1:end_idx]


def get_string_before_and_after_substring(string, substring, is_strip_quotatations=True):
    start_idx = string.find(substring)
    end_idx = start_idx + len(substring)
    before_string = string[:start_idx].strip()
    after_string = string[end_idx:].strip()
    if is_strip_quotatations:
        before_string = strip_quotations(before_string)
        after_string = strip_quotations(after_string)
    return before_string, after_string


def strip_quotations(string):
    return string.strip().strip("\"")




def print_visit(visit_list):
    num_visits = len(visit_list)
    if num_visits == 0:
        string = "first"
    else:
        string = "not first"
    return string

visit_list = ["today", "yesterday", "day before that"]

node_text = """
{hi}, <voice speed="faster" pitch= "raise_pitch"  volume ="loud" tone = "funny">{Audrow##Aw drow}<anim ="winkHeadTurn">
</voice>! This is your <code>print_visit(visit_times)
</code> visit.
"""

s, e = find_parenthesis(node_text)
tag = get_substring(node_text, s, e)
print(tag)

print("start tag: " + str(parse_start_tag(tag)))

