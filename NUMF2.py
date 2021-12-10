fi=open("NUMF2.INP","r")
a=int(fi.readline())
fi.close()
x=0
while a!=0:
    num=a%10
    x=(x*10)+num
    a=a//10
fo=open("NUMF2.OUT","w")
print(x,file=fo)
fo.close()