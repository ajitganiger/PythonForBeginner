__author__ = 'aganiger'

data = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6]


def find_max_element(array):
    myMap = {}

    for i in array:
        if i in myMap:
            myMap[i] += 1
        else:
            myMap[i] = 1

    return myMap


print(find_max_element(data))


def majority_element(num_list):
    maxCount = 0
    index = -1

    for i in range(1, len(num_list)):
        cnt = 0
        for j in range(1, len((num_list))):
            if num_list[i] == num_list[j]:
                cnt += 1
        if cnt > maxCount:
            maxCount = cnt
            index = i

    if maxCount > len(num_list) / 2:
        return num_list[index]
    else:
        return -1


print(majority_element([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6]))