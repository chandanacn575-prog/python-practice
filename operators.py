#operators
#addition
a=10
a=a+100 #a=a+100  shortform a+=100
print(a)
a+=100
print(a)

#2 multiplication
b=65
b=b*65
print(b)
b*=65
print(b)

#3 subtraction
sen=2
sen=sen-2
print(sen)
sen-=2
print(sen)

#4 division
div=100
div=div/100
print(div)
div/=100
print(div)

#5 modulus
m=100
m=m%100
print(m)
m%=100
print(m)

##COMPARISON OPERATORS
a=10
b=20
print(a==b) #equality operator
print(a!=b) #not equal operator
print(a>b) #greater than operator
print(a<b) #less than operator
print(a>=b) #greater than or equal to operator
print(a<=b) #less than or equal to operator

##LOGICAL OPERATORS
print(False or True) 
print(True or False) # OR operator
print(False and True)  # AND operator
print(not False) 
print(not(True)) # NOT operator
print(1>2 or 2>1)
print(1>2 and 2>1)
print(not(1>2))

##Membership operator
y="sumukha"
z="cista"
print(['s' in y])
print(['s' not in y])
print(['s' in y])
print('s' in y) and ('s' in z)
print('h' in y) and ('h' in z)
print((not'h' in y)) and ('h' in z)
