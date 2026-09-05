#string functions

# str = "hi its a string"
# str = (str.capitalize())
# print(str)

#practice questions
#1
# inpur user first name and display the length of the name

# first_name = input("enter you first name:")
# print("length of your first name is", len(first_name))
#2
# str1 = " wango nii naam mera $ chalda "
# print(str1.find("$"))

#3
# grade a student based on marks obtained

# a = 83
# if a >= 100:
#     print("A+")
# elif a >= 90:
#     print("A")
# elif a >= 80:
#     print("B")
# elif a >= 70:
#     print("C")
# elif a >= 60:
#     print("D")
# else:
#     print("F")

# a = int(input("Enter your marks:"))
# if a >= 100:
#     grade = "A+"
# elif a >= 90:
#     grade = "A"
# elif a >= 80:
#     grade = "B"
# elif a >= 70:
#     grade = "C"
# elif a >= 60:
#     grade = "D"
# else:
#     grade = "F"
# print("Your grade is:", grade)

# 0dd or even number

# num = int(input("enter a number:"))
# rem = num % 2
# if rem == 0:
#     print("even number")
# else:
#     print("odd number")

# find the largest number among three numbers
a = 10
b = 17
c = 30
if(a >b and a>c):
    print("a is largest")
elif(b > a and b>c):
    print("b is largest")
elif(c > a and c>b):
    print("c is largest")
else:
    print("all are equal")