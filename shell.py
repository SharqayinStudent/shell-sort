
def shell(array, n):

    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j>= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap

            array[j] = temp
        gap //= 2


arr = [9, 8, 3, 7,10, 5, 6, 4, 1]
size = len(arr)
shell(arr, size)

print(arr)
