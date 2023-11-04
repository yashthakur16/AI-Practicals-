# printing statement

print("Artificial Intelligence Practicals")

# variables

Name="Yash"
Roll=40

print("Name : "+Name)
print("Roll : "+str(Roll))

# Taking Inputs :

Name2=input("What is your Name ? ")
print("His name is : "+Name2)

Roll2=(input("What is your Roll no:"))
print("Roll : "+Roll2)

# strings :

Course="Artificial Intelligence and Data Science "

print(Course.upper())
print(Course.find('D'))
print("and" in Course)

# Arithematic operators

print(5+3)
print(5-3)
print(5*3)
print(5/3)
print(5//3)
print(5%3)


# Comparison Operators

print(5>3)
print(5>=3)
print(5<3)
print(5<=3)
print(5==3)
print(5!=3)

# Logical operator

print((5>3) and (5<=3))
print((5>3) or (5<=3))
print(not(5<=3))

# if Statements 

temp=26

if(temp>25):
    print("It is a hot day ")
else:
    print("It is not a hot day ")

# while loop

# printing 1 to 5

i=1

while(i<6):
    print(i)
    i=i+1

# Lists

names=["Krutik","Shrikunj","Aditya","Smith"]
print(names)
print(names[0])
print(names[-1])
print(names [0:2])

# List Methods

Roll =[1,2,3,4,5]
Roll.append(6)
Roll.insert(0,0)
print(Roll)
print(len(Roll))

for i in Roll:
    print(Roll[i])

for i in range(7):
    print(Roll[i])

