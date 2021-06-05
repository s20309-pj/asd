def head(array):
    return array[0]


def tail(array):
    return array[1:]


def is_empty(array):
    if len(array) != 0:
        return True
    else:
        return False


def common_elements(first_array, second_array):
    if not is_empty(first_array) or not is_empty(second_array):
        return
    if head(first_array) < head(second_array):
        return common_elements(tail(first_array), second_array)
    elif head(first_array) > head(second_array):
        return common_elements(first_array, tail(second_array))
    else:
        my_array.append(head(first_array))
        return common_elements(tail(first_array), tail(second_array))


def reverse(string):
    if not is_empty(string):
        return
    new_string = head(string)
    reverse(tail(string))
    print(new_string, end='')


first_array1 = [5, 6, 7, 8, 9, 10]
second_array2 = [1, 2, 4, 5, 6, 22, 69]
my_array = []
common_elements(first_array1, second_array2)
print(my_array)

print(reverse("Asia"))
