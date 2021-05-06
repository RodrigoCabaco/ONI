
def part_1():
	P = input().split(' ')
	N = int(P[0])
	X = int(P[1])
	A = [1,4,6,2]
	B = [1,5,6,5]
	#Output = multiplos de 3 (1,5)(1,5)(4,5)(6,6)(2,1)
	K = []
	for i in A:
		for l in B:
			if (i+l)%X==0:
				K.append((i+l))
	print(len(K))