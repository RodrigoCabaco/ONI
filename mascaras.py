
def part_1():
	P = input()
	N = int(P.split(' ')[0])
	M = int(P.split(' ')[1])
	A = list(map(int,input().split(' ')))
	f = 0
	for i in range(M):
		u = min(A)
		A.remove(u)
		f +=u

	print(f)
	
def part_2():
	N = 4
	M = 5
	f = 0
	A = [1,2,1,3]
	for x in range(M):
		u = min(A)
		A[A.index(u)] = u+1
		f+=u
	print(f)
t = input()
if t=="1":	part_1()
if t=="2": part_2()