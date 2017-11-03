def accept():
	N=int(input()) #"enter the number of elements in the array (N):"
	array=list(map(int,input().split()))
	if 1<=N<=100:
		if len(array)>N:
			print("array out of bounds max no of elements should be less then",N)
			return False
		else:
			return array

def prefixSum(array,a):
	res=sum(array[:a+1])
	return res

def suffixSum(array,a):
	res=sum(array[a:])
	return res

def Tsum(l):
	x=[]
	for i in range(0,len(l)):
		res=prefixSum(l,i)+suffixSum(l,i)
		x.append(res)
	return x



T=int(input())
s=[]
a=[]
if 1<=T<=10:
	for i in range(0,T):
		lis=accept()
		s=Tsum(lis)
		a.append(s.index(min(s))+1)
	for i in range(0,len(a)):	
		print(a[i])
