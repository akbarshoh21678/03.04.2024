n=input()
listt=[6,2,5,5,4,5,6,3,7,6]
yig=0
x=""
for i in range(len(n)):
    x=int(n[i])
    yig+=listt[x]
print(yig)