class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[index] = nums[i]
                index += 1
        return index

'''
Approach : The Intuition is to use two pointers, i and j (which is index in our case), to iterate through the array. The variable j is used to keep track of the current index where a unique element should be placed. The initial value of j is 1 since the first element in the array is always unique and doesn't need to be changed.

Runtime : 0 ms
Memory : 19.12 MB

Time Complexity : O(n), we have a loop
Space Complexity : O(1), we didn't use any extra space.
'''