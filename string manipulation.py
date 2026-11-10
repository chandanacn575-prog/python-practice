# ex for concatenation
first="Chandana" 
second="CN"
full_name=first + " " + second 
print(full_name )

#Repetition ex
message="Warning!" *9
print(message)

message="Hello World!"
print(message)

#string methods
print(message.upper()) #method call
print(message.lower())
print(message.strip() *2) #space
print(message.replace ( "World","baby" )) #replacing old,new

name = 'chandana says"bye"'
name1 = "chandana says" 'I LOVE U'
print(name)
print(name1)

char = '''the place where it ends"IT BEGINS"
so be "CALM"'''
print(char )

#string length(len())
a= "hai this is user"
print(len(a)) #length

#accessing string characters(zero based indexing)
type="CHANDANA"
print(type[5])  #index=position-1
print(type[4])

#slicing the strings
print(type[2:4])
print(type[3:5]) #python extracts from index 3 to 5
print(type[:5]) #python same as above
print(type[7:])#programming from index 7 to end
print(type[:7])
print(type[0:-4])
print(type[-2])  #negative indexing last character
print(type[-3])  #second last character 
print(type[::2]) #step size 2
print(type[1:2:3]) #step size 3
print(type[::3]) #step size 3