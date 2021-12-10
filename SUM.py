fi=open("SUM.INP","r")
a=int(fi.readline())
b=int(fi.readline())
fi.close()
x=a+b
fo=open("SUM.OUT","w")
print(x,file=fo)
fo.close()