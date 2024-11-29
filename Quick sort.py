# Hanan Fijananto 24/538946/SV/24555
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

data = [67, 89, 23, 21, 90, 45, 4, 12, 10, 5]
sorted_data = quick_sort(data)
print("Data setelah diurutkan:", sorted_data)
