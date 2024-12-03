def reverse_string_manual(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

print(reverse_string_manual("hello"))  # "olleh"

# def reverse_string_manual(s):
#     reversed = ""
#     for char in s:
#         reversed = char + reversed
#     return reversed
