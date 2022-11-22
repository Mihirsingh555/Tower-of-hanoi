

def TowerOfHanoi(n , s, d, a):
	if n==1:
		print ("Move disk 1 from start",s,"to destination",d)
		return
	TowerOfHanoi(n-1, s, a, d)
	print ("Move disk",n,"from start",s,"to destination",d)
	TowerOfHanoi(n-1, a, d, s)
		

n = 4
TowerOfHanoi(n,'A','B','C')
