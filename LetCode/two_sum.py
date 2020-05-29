class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    solution.append(i)
                    solution.append(j)
                    break
        return solution
    
obj = Solution()
print(obj.twoSum([2, 7, 11, 15],9))