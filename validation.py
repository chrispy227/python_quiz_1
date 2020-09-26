def get_in_range_str_input(prompt):
    while True:
        value = input(prompt)
        if value.lower().strip() not in ('a', 'b', 'c', 'd'):
            print("Sorry, your response must be A, B, C, or D. Please Try Again.")
            continue
        else:
            break
    return value


# def is_input_int_or_str(promptValue):
#     while True:
#         try:
#             testValue = int(promptValue)
#             if testValue:
#                 pass


def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


yes = "Duh yesssssssshhhh"
answer = get_in_range_str_input(yes)
