from typing import List


class Solution:
	def findNumbers(self, numbers: List[int]) -> int:
		count = 0
		for i in numbers:
			if len(str(i)) % 2 == 0:
				count += 1
		return count


numbers = list(map(int, input().split()))
obj = Solution()
print(obj.findNumbers(numbers))
