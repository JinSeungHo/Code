def insertion_sorting(list):
    for i in range(1, len(list)):
        max_index = i

        for j in range(max_index):
            if list[max_index] < list[j]:
                temp = list[j]
                list[j] = list[max_index]
                list[max_index] = temp

    return list

print(insertion_sorting([4, 2, 7, 1, 9, 3]))
print(insertion_sorting([1, 5, 4, 10, 98, 77]))