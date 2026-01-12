def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    arr.append(val)

print("Unsorted Array:", arr)
selection_sort(arr)
print("Sorted Array:", arr)