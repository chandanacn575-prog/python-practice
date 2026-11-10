print("Loves")

boy_name=(input("Boy name>>"))
girl_name=(input("Girl name>>"))
print(boy_name)
print(girl_name)
print(boy_name,girl_name)
boy_age=int(input("Boy age"))
girl_age=int(input("Girl age"))
age_diff=(boy_age-girl_age)

#using abs because sometimes boy might be younger
age_diff=abs(boy_age-girl_age)

'''
this is a 
multiline
comment
'''
print(girl_name + "Loves"+boy_name )
print(girl_name + " loves "+ boy_name)
print(boy_name + " loves " + girl_name + ".Age Difference is"+ str(age_diff)) #need to add str
print(f"{boy_name} loves {girl_name}.Age Differnce is{age_diff}")

print(girl_name+ " loves " +boy_name +"Age Differnce is"+str(age_diff))
print(f"{girl_name}loves {boy_name}Age Difference is{age_diff}")



#square nd cube
num=int(input("enter a number"))
square=num*num
cube=num*num*num
print("Square is",square)
print("Cube is",cube)