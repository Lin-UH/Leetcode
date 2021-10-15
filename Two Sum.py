'''
list.index
list.copy()
enumerate()
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_copy = nums.copy()
        answer = []
        for index, each in enumerate(nums_copy):
            temp = nums[index]
            nums[index] = "i"
            if -1 * (each - target) in nums:
                if nums.index(-1 * (each - target)) != index:
                    answer.append(nums.index(-1 * (each - target)))
            nums[index] = temp
        return answer
