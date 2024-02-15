
def merge_lists(list_1, list_2):
    list_3 = []
    for i in list_1:
        list_3.append(i)
    for i in list_2:
        list_3.append(i)
    list_3.sort()
    return list_3
