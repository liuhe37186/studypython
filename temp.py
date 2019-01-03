temp = input("输入带符号的温度值")
if temp[-1] in ['F','f']:
	C = (eval(temp[0:-1])-32)/1.8
	print("输出温度{:.2f}C".format(C))
elif temp[-1] in ['C','c']:
	F = eval(temp[0:-1])*1.8+32
	print("输出温度{:.2f}F".format(F))
else:
	print("输入错误")
