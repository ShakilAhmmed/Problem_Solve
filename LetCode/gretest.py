class Solution:
    def kidsWithCandies(self, candies, extraCandies):
      max_candy = max(candies)
      output = []
      for i in candies:
          if i + extraCandies >= max_candy:
             output.append(True)
          else:
            output.append(False)
      return output
obj = Solution()
print(obj.kidsWithCandies([2,3,5,1,3],3))