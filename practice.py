#problem 1 
# first_name = input("enter your first name:")
# print("length of your first name is:", len(first_name))
# first_name = first_name.capitalize()
# print(first_name)

#problem..2
#ask a user to give interger number and find if postive negative or 0
# a = int(input("enter and integer"))
# if(a>0):
#  print("this number is positive")
# elif(a<0):
#  print("this number is negative")
# elif(a==0):
#  print("this number is eqaul to zero")

#problem..3
#ask user to give a no find odd or even or also find number is greater than 5

# a = int(input("enter a number:"))
# if(a % 2 == 0):
#  print(a,"this an even number")
# elif(a % 2 != 0):
#  print(a,"this is an odd number")
# if(a>50):
#  print(a,"is greater than 50")
# elif(a<50):
#  print(a,"is less than 50")

#problem..4
# a = int(input("enter your marks:"))
# if a>100 or a<0:
#  print("is invalid marks")
# elif(a>=90):
#  print("A")
# elif(a>=80):
#  print("B")
# elif(a>=70):
#  print("c")
# elif(a>=60):
#  print("D")
# elif(a<60):
#  print("f")

#problem..5
# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
# c=  int(input("enter third number:"))

# if(a>b and a>c):
#     print( a," is greatest")
# elif(b>a and b>c):
#     print( b," is greatest")
# elif(c>b and c>a):
#     print(c," is greatest")
# else:
#     print("all are equal")

# #problem..6
# a = input("Enter a password: ")

# if len(a) < 8:
#     print("Password is too short")

# else:
#     print("Password length is acceptable")

#problem..7 real world problem
#ask customer for total bill apply discoutn according to the bill range and then count the total bill

# amount = float(input("enter the amount:"))

# discount1 = (amount*20)/100
# final_amount1 = amount-discount1
# discount2 = (amount*10)/100
# final_amount2 = amount-discount2
# discount3 = (amount*5)/100
# final_amount3 = amount-discount3

# if(amount>=20000):
#     print("total amount:", amount)
#     print("final amount after discount is:", final_amount1)
#     print("discount amount:", discount1)
# elif(amount>=10000):
#     print("total amount:", amount)
#     print("final amount after discout is: ", final_amount2)
#     print("discount amount:", discount2)
# elif(amount>=5000):
#     print("total amount:", amount)
#     print("final amount after discount is:", final_amount3)
#     print("discount amount:", discount3)
# else:
#     print("you are not eligible for discount")

#problem..8
#ask the user to enter a amount to withdrawl from it's account if balnce is not equal or graeater than the balance show

# balance = int(input("enter the total blance in your account:"))
# amount = int(input("enter the amount to withdraw:"))
# rem = balance-amount
# if amount % 500 != 0:
#     print("Please enter a valid amount")
#     exit()
#     print("Valid amount")
# elif (amount>balance):
#     print("insuficient balance")
# elif(amount<=balance):
#     print("your withdrawl successful")
#     print("your remaining balance is;", rem)


#problem..9
#ask user to enter his age and salary if both satidfies than he will be eligible for the company premium package

age = int(input("enter your age:"))
salary = int(input("please enter your salary:"))

if(age>18 and salary>50000):
    print("your are eligible for premuium package")
elif(age<18):
    print("your age is less then adult so you are not eligible ")
elif(salary<50000):
    print("your salary is too low so you are not eligible ")