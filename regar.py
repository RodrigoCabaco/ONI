def part_1():
	P = input()
	N = int(P.split(' ')[0])
	K = int(P.split(' ')[1])
	A = list(map(int, input().split(' ')))
	B = list(map(int, input().split(' ')))
	for G in range(K):
		for i in range(len(A)):
			A[i] = A[i]+(G*B[i]) 
	for p in A:
		if A.index(p)!= len(A)-1:
			print(p, end=" ")
		else:
			print(p, end="\n")


def part_2():
	P = input()
	N = int(P.split(' ')[0])
	K = int(P.split(' ')[1])
	A = list(map(int, input().split(' ')))	
	final_sum = 0
	for x in range(3):
		g = max(A)
		final_sum+=g
		f = A.index(g)
		A.remove(A[f])
		for l in range(K-1):
			f+=1
			if f <= len(A)-1:
				final_sum+=A[f]
				A.remove(A[f])
	print(final_sum)
t = input() 
if t=="1":part_1()
elif t=="2":part_2()
