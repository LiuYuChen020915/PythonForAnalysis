a=[]
for i in range(1,10):
    a.append(i)
    i+=1
print("a:",a)
b=0
for b in range(0,9):
    b+=1
    for index in range(0,9):
        message = str(b) + "*" + str(a[index]) + '=' + str(b * a[index])
        print(message)
        index+=1
        if index==9 or a[index]-1==b:
            break