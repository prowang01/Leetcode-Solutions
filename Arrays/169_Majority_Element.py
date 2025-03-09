class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]
        
'''
Approach: The function first sorts the array, which groups identical elements together. Since the majority element appears more than n/2 times, it is guaranteed to be at index n//2 in the sorted array. The function simply returns the element at this position.

Runtime : 0 ms
Memory : 19.30 MB

Time Complexity : O(n log n), The sorting step dominates the complexity, as sorting an array of size n takes O(n log n) time. The lookup at n//2 is O(1), so it does not affect the complexity.

Space Complexity : O(1) (or O(n) depending on the sorting algorithm), If the sorting is done in place, no extra space is needed. But some sorting methods, like merge sort, may require extra space O(n).
'''


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        n = len(nums)

        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        
        n = n//2
        for key, value in dict.items():
            if value > n:
                return key
        
'''
Approach : The function uses a dictionary (dict) to count the occurrences of each number in nums. It then checks which element appears more than n // 2 times and returns it as the majority element. Since the problem guarantees a majority element, the function will always find and return one.

Runtime : 11 ms
Memory : 19.29 MB

Time Complexity : O(n) → We iterate through nums once to build the dictionary (O(n)) and once more to find the majority element (O(n)). This results in an overall complexity of O(n) + O(n) = O(n).

Space Complexity : O(n) → The dictionary stores up to n unique elements in the worst case (when all elements are distinct), leading to O(n) extra space
'''


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        return candidate

'''
Approach : 

The algorithm uses the Boyer-Moore Voting Algorithm to find the majority element in a single pass (O(n)). 
It maintains a candidate variable and a count to track the dominant element.

1.Traverse the array and adjust count:

- If count == 0, pick the current element as the new candidate.
- If the current element is the same as candidate, increase count.
- Otherwise, decrease count.

2. At the end, the candidate is guaranteed to be the majority element.

Runtime : 3 ms
Memory : 19.30 MB

Time Complexity : O(n) → The algorithm iterates through the array once (single pass).
Space Complexity : O(1) → Only two variables (candidate, count) are used, making it constant space.

'''
