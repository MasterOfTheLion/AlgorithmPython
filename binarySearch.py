def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (int)((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9, 10, 12, 16, 18, 19, 20, 22, 24, 26, 28, 29, 30, 31]


print(binary_search(my_list, 29))
