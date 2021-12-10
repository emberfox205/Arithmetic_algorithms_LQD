fi=open("NUMF1.INP","r")
a=int(fi.readline())
fi.close()
x=a%10
fo=open("NUMF1.OUT","w")
print(x,file=fo)
fo.close()
