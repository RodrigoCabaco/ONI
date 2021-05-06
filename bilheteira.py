p = input() # 7
k = input().split(' ')
_max = []
for g in k:
	if len(_max)!=0:
		if int(g)>max(_max):
			_max.append(int(g))
	else:
		_max.append(int(g))

print(len(_max))
