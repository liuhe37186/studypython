# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。

# 示例 1:

# 输入: "()"
# 输出: true
# 示例 2:

# 输入: "()[]{}"
# 输出: true

def isVialid(s):
	stack = []
	paren_map = {')':'(',']':'[','}':'{'}
	for c in s:
		if c not in paren_map:
			stack.append(c)
		elif not stack or paren_map[c] != stack.pop():
			return False
	return not stack

def isVialid2(s):
	if len(s)%2 != 0:
		return False

	str = ' '
	paren_map = {'{':1,'}':9,'[':2,']':8,'(':3,')':7,' ':0}
	for c in range(0,len(s)):
		if paren_map[str[-1]] + paren_map[s[c]] != 10:
			str = str + s[c]
		else:
			str = str[:-1]
	if str == ' ':
		return True
	else:
		return False



str = input('输入括号字符串')
# print(isVialid(str))
print(isVialid2(str))




