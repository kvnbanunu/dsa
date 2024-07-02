def merge_sort(nums):
    if len(nums) < 2:
        return nums
    #slicing the array in half
    left = merge_sort(nums[:len(nums) // 2])
    right = merge_sort(nums[len(nums) // 2:])
    return merge(left, right)

def merge(left, right):
    final = []
    i = 0
    j = 0
    while i < len(left) and j < len(second):
        if left[i] <= right[j]:
            final.append(left[i])
            i += 1
        else:
            final.append(right[j])
            j += 1
    #appending any left over indexes
    while i < len(left):
        final.append(left[i])
        i += 1
    while j < len(second):
        final.append(second[j])
        j += 1
    return final
