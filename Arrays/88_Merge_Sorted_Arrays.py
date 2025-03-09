class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for j in range(n):
            nums1[m+j] = nums2[j]
        nums1.sort()
        
'''
Runtime : 0 ms
Memory : 18.01 MB

Approach : adding the elements of nums2 from the index 'm' from nums1

Complexity :
Space : O(1) -> We're not using any extra space
Time : O((m+n)log(m+n)) because of the sort() method
'''


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i < 0 or nums1[i] < nums2[j]:  # On prend nums2[j] si i < 0 ou si nums2[j] est plus grand
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1

# Approach : using two pointers, i for nums1, j for nums2, and k to keep track of the poistion in nums1 where we'll be placing the larger element

'''
Runtime : 4 ms
Memory : 17.9 MB

Time Complexity : O(m+n) because we're interating through both arrays once.
Space Complexity : O(1), we don't use any extra space.
'''
