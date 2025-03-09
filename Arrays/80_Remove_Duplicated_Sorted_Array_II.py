class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for element in nums:
            if i == 0 or i == 1 or nums[i-2] != element:
                nums[i] = element
                i += 1
        return i
        
'''
Approach : The function removes duplicates from a sorted array while keeping at most two occurrences of each element. It uses two pointers: i tracks the position where the next valid element should be placed, and ele iterates through the array. The first two elements are always kept, and for the rest, if nums[i-2] is different from ele, it is stored at nums[i]. Finally, i is returned as the new array length.

Runtime : 78 ms
Memory : 20.48 MB

Time Complexity : O(n), The function loops through the array once, processing each element in constant time.
Space Complexity : O(1), we didn't use any extra space in our code, because we remove the duplicates in-place, in the same array.

'''  