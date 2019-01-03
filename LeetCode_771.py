class Solution:
	def numJewelsInStones(self, J, S):
		sum = 0
		for j in J:
			for s in S:
				if(s==j):
					sum = sum + 1
		return sum
