n=input()
arr=[]
c=0
for i in n:
    arr.append(i)
for i in arr:
    c=c+(int(i)**3)
if str(c)==n:
    print("armstrong")
else:
    print("no")
    
