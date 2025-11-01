def count_inversions(arr):
    def merge_sort(nums):
        if len(nums) <= 1:
            return nums, 0

        mid = len(nums) // 2
        left, inv_left = merge_sort(nums[:mid])
        right, inv_right = merge_sort(nums[mid:])
        merged, inv_split = merge(left, right)

    
        return merged, inv_left + inv_right + inv_split

    def merge(left, right):
        merged = []
        i = j = inv_count = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                
                inv_count += len(left) - i

       
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv_count

   
    _, total_inversions = merge_sort(arr)
    return total_inversions


arr = [2, 4, 1, 3, 5]
print("Number of Inversions:", count_inversions(arr))
