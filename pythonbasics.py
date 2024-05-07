# Question One
def sum_of_even_numbers(digits):
    sum = 0
    for num in digits:
        if num % 2 == 0:
            sum += num
    return sum
digits = [1, 9, 67, 18, 90, 5, 153, 736, 893, 7]
print(sum_of_even_numbers(digits))

# Question Two
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged
arr = [70, 70, 8, 6, 230, 8, 56]
sorted_arr = merge_sort(arr)
print(sorted_arr)
