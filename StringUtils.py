def format_filename(s):
    not_allowed = '\\:"/*?<>|'
    for char in not_allowed:
        if char in "\\/|":
            s = s.replace(char, "-")
        elif char == '"':
            s = s.replace(char, "'")
        elif char == "<":
            s = s.replace(char, "(")
        elif char == ">":
            s = s.replace(char, ")")
        else:
            s = s.replace(char, "")
    return s