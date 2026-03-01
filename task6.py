def merge_lists(*lists):
    result = []
    for lst in lists:
        result.extend(lst)
    return result

list1 = [1,2,3,4]
list2 = [5,6,7]
list3 = [8,9,10]

big_list = merge_lists(list1, list2, list3)
print(big_list)
