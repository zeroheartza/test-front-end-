n = 13
for i in range(n):
    if(i==0):
        print(" "*(int(n-1-i))+"x"+" "*i)
    elif(i==(n-1)):
        print("x "*n)
    else:
        print(" "*(int(n-1-i))+"x"+" "*((i*2)-1) +"x")
    
