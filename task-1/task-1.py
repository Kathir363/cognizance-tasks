x=int(input("Enter a coordinate of friend's house:")) #input of x
y=x
for i in range(1,y):
    if x>=5:
        x-=5  #Unless the x value is more than five it keeps subtracting
    else:
        break  #I've abstracted if x<5 then loop is breaked
print("The minimum no. of steps to reach his friend:",i)            
