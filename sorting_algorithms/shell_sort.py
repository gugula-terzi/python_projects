def shell_sort(arr):
    """
    :param arr: массив чисел
    """
    gap = len(arr) // 2
    
    while gap > 0:
        for value in range(gap, len(arr)):
            current_value = arr[value]
            position = value

            while position >= gap and arr[position - gap] > current_value:
                arr[position] = arr[position - gap]
                position -= gap
                arr[position] = current_value

        gap //= 2
        print(gap)

    return arr

array = [58, 46, 18, 40, 75, 28, 90, 13, 63, 84]

print("Unsorted array: ", array)
shell_sort(array)
print("Sorted array: ", array)