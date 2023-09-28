for i in range(1,6):
    for j in range(1,6):
        if (i==1 and(j==2 or j==3 or j==4) or j==3 and(i!=5) or j==1 and(i==4 ) or j==2 and(i==5) ):
            print("0",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
            