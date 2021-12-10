fi=open("MUL.INP","r")
a=int(fi.readline())
b=int(fi.readline())
fi.close()
x=a*b
fo=open("MUL.OUT","w")
print(x,file=fo)
fo.close()