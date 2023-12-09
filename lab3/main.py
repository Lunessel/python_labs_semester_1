
def MyUpper(initial_char: chr):
    ascii_code = ord(initial_char)
    if ascii_code >=65 and ascii_code <=90:
        return initial_char
    return chr(ascii_code - 32)


def capitalize(initial_string: str, array_of_indexes: []) ->str:

    initial_list = list(initial_string)
    lenth = len(initial_list)

    for i in array_of_indexes:
        if i < lenth:
            initial_list[i] = MyUpper(initial_list[i])

    return ''.join(initial_list)



print("\"abcdef\", [1,2,5] =>  ", capitalize("abcdef", [1,2,5]) )
print("\"abcdef\", [1,2,5,100] =>  ", capitalize("abcdef",[1,2,5,100]) )
print("\"abcdef\", [1,2,5,100] =>  ", capitalize("abcd",[0,2,5]) )
