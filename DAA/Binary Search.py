arr = []
num_elements = int(input("Enter the number of elements for the array: "))

for i in range(num_elements):
    value = int(input(f"Enter element {i+1}: "))
    arr.append(value)

print("Given Array:", arr)

target = int(input("Enter the number to search: "))

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        print(f"Element found at index {mid}")
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")