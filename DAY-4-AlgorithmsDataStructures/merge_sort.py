def merge(left, right):
    output = []
    r = l = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            output.append(left[l])
            l += 1
        else:
            output.append(right[r])
            r += 1

    output.extend(left[l:])
    output.extend(right[r:])
    return output


def merge_sort(list_to_sort):
    list_len = len(list_to_sort)

    if list_len == 1:
        return list_to_sort

    mid_index = list_len // 2
    left_part = merge_sort(list_to_sort[:mid_index])
    right_part = merge_sort(list_to_sort[mid_index:])

    return merge(left_part, right_part)


random_list = [1, 18, 5, 223, 49, 19, 8]
print(merge_sort(random_list))
