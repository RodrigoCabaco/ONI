
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

def part_2():
	P = input().split(' ')
	N = int(P[0])
	X = int(P[1] )
	A = list(map(int,input().split(' ')))
	B = list(map(int,input().split(' ')))
	final = A
	for i in A:
		for l in B:
			if i==l:
				final.append(i)
			elif i<l:
				while i<l:
					g = final[A.index(i)]
					g+=X
					if g == i:
						final[A.index(i)]
					elif g > i:
						return [-1]
						break
	return(final)


t = input()
if t=="1":part_1()
if t=="2":print(part_2())