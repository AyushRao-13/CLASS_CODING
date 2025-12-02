arr = [5, 8, 2, 9, 1, 7]
target = int(input("Enter the number to search: "))

for i in range(len(arr)):
    if arr[i] == target:
        print(f"Element found at index {i}")
        break
else:
    print("Element not found")