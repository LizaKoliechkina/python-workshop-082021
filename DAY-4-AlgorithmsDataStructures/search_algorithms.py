def linear_search(input_list, search_element):
    for idx, elem in enumerate(input_list):
        if elem == search_element:
            return idx

    return -1


result = linear_search([1, 4, 6, 2], 4)
print('Linear search: ', result)


def sort_search(sorted_list, search_element, start=0, end=None):
    end = end if end is not None else len(sorted_list)
    # end if end else ... - bad, because if end = 0 condition will succeed
    if start == end:
        return -1

    mid_index = (start + end) // 2
    if search_element == sorted_list[mid_index]:
        return mid_index
    elif search_element < sorted_list[mid_index]:
        return sort_search(sorted_list, search_element, start, mid_index)
    else:
        return sort_search(sorted_list, search_element, mid_index + 1, end)


print('Sort search: ', sort_search([2, 3, 6, 7, 8], 7))
print('Sort search: ', sort_search([2, 3, 6, 7, 8], 3))
print('Sort search: ', sort_search([2, 3, 6, 7, 8], 6))

