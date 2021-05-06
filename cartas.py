
def part_1():
	P = input().split(' ')
	N = int(P[0])
	X = int(P[1])
	A = list(map(int,input().split(' ')))
	B = list(map(int,input().split (' ')))
	#Output = multiplos de 3 (1,5)(1,5)(4,5)(6,6)(2,1)
	K = 0
	_A = []
	_B = []
	for f in A:
		_A.append(f%X)
	for g in B:
		_B.append(f%X)

	for l in _A:
		for j in _B:
			if j==l:
				K+=(X/2)
	print(int(K))

t = input()
if t=="1":part_1()
