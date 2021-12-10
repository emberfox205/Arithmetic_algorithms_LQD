fi=open("SUB.INP","r")
a=int(fi.readline())
b=int(fi.readline())
fi.close()
x=a-b
fo=open("SUB.OUT","w")
print(x,file=fo)
fo.close()