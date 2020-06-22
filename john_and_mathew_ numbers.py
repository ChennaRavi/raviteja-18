l,u,w=map(int,input().split())
J=[]
t=[]
#jf=i*(2*i-1)
#mf=(i*(i+1))/2
for i in range(1,l+1):
    J.append(i*(2*i-1))
#[t.append(i) for i in J if i in range(l,u+1)]

for i in J:
    if(i in range(l,u+1)):
        t.append(i)
print('wanted:',t[w-1])
