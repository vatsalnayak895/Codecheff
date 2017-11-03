a=[]
i=0
while True:
	x=int(input())
	if x!=42:
		a.append(x)
		i+=1
		continue
	else:
		for l in range(len(a)):
			print(a[l])
		break