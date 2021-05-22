def selection_sort(list):
    for i in range(len(list) - 1):
        min_index = i
        min = list[min_index]
        for j in range((i + 1), len(list)):
            if list[j] <= min:
                min_index = j
                min = list[min_index]
        list[i], list[min_index] = list[min_index], list[i]
    return list

list = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
print(selection_sort(list))