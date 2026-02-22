m1 = 'I love coffee' #this is a string variale
print(m1)
m2= 'bobby\'s coffee'#if we use \ then it will not show syntax error
print(m2)

print(len(m1))#len helps to count the text(length)
print(len(m2))

print(m1[0])# it will determine index number in accending order starts from 0
print(m2[8])
# Coffee = length(6)
# cofee = index(5)
#total index= total length -1 (always it be less than 1)
print(m1[-1]) #this will print last character of the string
print(m1[0:4])#this will print the first 4 characters of the string m1 (counts space as well)
print(m1[0:])#this will print all the characters 
print(m1[:3])#this will print 2 characters only before 3

#.lower()
print(m1.lower()) # .lower() will make string variable or all the characters in small letters.
print(m2.lower())

#.upper
print(m1.upper()) # .upper() capital letters
print(m2.upper())

#.count
print(m1.count("e")) # this will count number of times of the character 'e'

#.find
print(m1.find("e")) #this will count index num of the character of'e'

# .replace
new_m1= m1.replace("coffee","Juice")#this will replace the string 'coffee' with 'juice' and store it in a new variable m1
print(new_m1) 

#string concatenation 
Food = "Cake"
Like = "Yes"
Favourite = Food + ' ' +  Like
print(Favourite)
message = '{}, {}!'.format(Food,Like)#this will format the string by replacing the placeholders{} with the values of the variables 'Food' and 'Like' and it store in a new variable.


