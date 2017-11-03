def game():
    N=int(input("N:"))
    if 1<=N<=10**5:
        a=list(map(int,input("list:").split()))
        if len(a)<=N+1:
            m=0
            n=m+1
            oparr=[]
            #while True:
            

T=int(input("T:"))
final=[]
while T!=0:
    if 1<=T<=10:
        final.append(game())
        T-=1
    else:
        print("Tshould be 1<=T<=10")
        raise SystemExit