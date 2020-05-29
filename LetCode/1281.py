class Solution:
	def subtractProductAndSum(self, n: int) -> int:
		prod = 1
		sum_data = 0
		for i in str(n):
			prod *= int(i)
			sum_data += int(i)
		return prod - sum_data


n = int(input())
obj = Solution()
print(obj.subtractProductAndSum(n))
