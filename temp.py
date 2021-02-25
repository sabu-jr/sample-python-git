number=33
sums=0
while(number!=0):
    temp=number%10
    sums=sums+int(temp)
    number=int(number/10)
    
print("Sum of the digits = ",sums)
