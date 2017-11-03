def accept():
	array=list(map(int, input("enter list").split())) #accept list
	return array

def test_case():
	lis = []
	N=int(input("enter the number of array elements (N):"))
	if 7<=N<=100:
		lis=accept()
		for i in range(0,len(lis)):
			x=lis[i]
			if x > 7:
				print("entered values incorrect")
				break
		else:
			q=check(lis)
			if q==True:
				print("rainbow")
			else:
				print("no rainbow")
				
	else:
		print("N entered out of bounds")

def check(list):
	a=len(list)%2
	b=len(list)
	if a==0: 						#evenlist
		fhalf=list[0:a]
		print("fhalf:",fhalf)
		shalf=list[a:b]
		print("shalf:",shalf)
		shalf.reverse()
		print("rev shalf",shalf)
		x=check_order(fhalf)
		if x==True:
			for i in  range(0,len(fhalf)):
				if fhalf[i]==shalf[i]:
					return True
				else:
					return False
	else:									#odd  list
		u=list.pop(a)
		v=len(list)//2
		fhalf=list[0:v]
		shalf=list[v:len(list)]
		shalf.reverse()
		x=check_order(fhalf)
		if x==True:
			for i in range(0,len(fhalf)):
				if fhalf[i]==shalf[i]:
					return True
				else:
					return False





def check_order(l):
	for i in range(0,len(l)):
		print(l[i])
		print(l[i+1])
		if l[i] > l[i+1]:
			print("entered list not in order")
			return False
			break
		else:
			return True




T=int(input("enter number of arrays (T):"))
if 1<=T<=100:
	for i in range(0,T):
		test_case()
		#if res==True:
else:
	print("T entered out of bounds")

