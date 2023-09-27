def filter_string(string):
    num_str = ''
    for char in string:
        if '0' <= char <= '9':
            num_str += char
    return int(num_str) if num_str else None


string = ' '
print(filter_string(string))

