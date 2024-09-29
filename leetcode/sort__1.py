def count_sort(my_arrray):
    n = len(my_arrray)
    k = max(my_arrray)
    count = [0] * (k + 1)
    for i in range(n):
        count[my_arrray[i]] += 1
    for i in range(1, k + 1):
        count[i] += count[i - 1]
    result = [0] * n
    for i in range(n - 1, -1, -1):
        result[count[my_arrray[i]] - 1] = my_arrray[i]
        count[my_arrray[i]] -= 1
    return result


if __name__ == '__main__':
    my_array = [4, 2, 2, 8, 3, 3, 1]
    sorted_array = count_sort(my_array)
    print("Sorted Array:", sorted_array)



def isomorphic(str1, str2):
    if len(str1) != len(str2):
        return False

    dictionary = dict()

    for i in range(len(str1)):
        if str1[i] not in dictionary:
            if str2[i] not in dictionary.values():
                dictionary[str1[i]] = str2[i]
            else:
                return False

        dictionary[str1[i]] = str2[i]
    return True