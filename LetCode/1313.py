from typing import List


class Solution:
	def decompressRLElist(self, number: List[int]) -> List[int]:
		result = []
		for i in range(0, len(number), 2):
			freq, value = number[i], number[i + 1]
			decompresses = [value for x in range(freq)]
			result.extend(decompresses)
		return result


obj = Solution()
print(obj.decompressRLElist(number = [1, 2, 3, 4]))
