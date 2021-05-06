
def part_1():
	P = input().split(' ')
	N = int(P[0])
	X = int(P[1])
	A = list(map(int,input().split(' ')))
	B = list(map(int,input().split (' ')))
	#Output = multiplos de 3 (1,5)(1,5)(4,5)(6,6)(2,1)
	K = 0
	for i in A:
		for l in B:
			if (i+l)%X==0:
				K+=1
	print(K)

t = input()
if t=="1":part_1()
