# name="diya"
# age=22
# if name:
#     print("iam in if body")
#     if age>25:
#         print("age is greater than 25")
#     else:
#         print("age is < 25")
# else:
#     print("if else body")



#if_elif_else

# day=int(input("enter a number : "))
# if day==1:
#     print("sunday")
# elif day==2:
#     print("monday")
# elif day==3:
#     print("tuesday")
# elif day==4:
#     print("wednesday")
# elif day==5:
#     print("thursday")
# elif day==6:
#     print("friday")
# elif day==7:
#     print("saturday")
# else:
#     print("entered number have no day") 


#qst 1

# number=int(input("enter the number : "))
# if number>0:
#     print("positive number")


#qst 2

# mark=int(input("enter the mark : "))
# if mark>=50:
#     print("pass")

#qst 3

# age=int(input("enter  age : "))
# if age>=18:
#     print("enable to vote ")

#qst 4


# num = int(input("enter a number"))
# if num % 5==0:
#     print("divisible by 5")


#qst5


# number = int(input("enter the number"))
# if number>100:
#     print("number is greater than 100")

#if elseqst 1

# num = int(input("enter the number"))
# if num % 2==0:
#     print("even")
# else:
#     print("odd")

#qst 2


# mark=int(input("enter the mark : "))
# if mark>=40:
#      print("pass")
# else:
#      print("fail")



#qst3

# age = int(input("enter the number"))
# if age >=18:
#     print("eligible to vote")
# else:
#     print("not eligible to vote")

#qst 4

# number=int(input("enter the number : "))
# if number>0:
#      print("positive number")
# else:
#     print("negavite number")


#qst 5

# amount=int(input("enter the number : "))
# if amount>=5000:
#     print("eligible for dis")
# else:
#     print("not eligible for dis")


#nested if qst 1


# age=int(input("enter the number : "))
# test=(input("passed driving test ? "))

# if age>=18:
#     if test =="yes":
#         print("eligible for driving licence")
#     else:
#         print("driiving test not completed")
# else:
#     print("not eligible")


#qst2


# attendance=int(input("enter the number : "))
# fee=(input("exam fee paid ? "))

# if attendance>=75:
#     if fee =="yes":
#         print("eligible for exam")
#     else:
#         print("pay exam fee")
# else:
#     print("not eligible due to attendance")

#qst3
# age=int(input("enter the age : "))
# salary=int(input("enter monthly salary "))

# if age>=21:
#     if salary >=25000:
#         print("eligible for loan")
#     else:
#         print("salary is too low")
# else:
#     print("age is below 21")


#qst4


# login = input("Are You Logged In ?")
# balance = int(input("enter balance"))
# if login=="yes":
#     if balance>0:
#         print("you can purchase the product")
#     else:
#         print("insufficient balance")
# else:
#     print("please login")

#qst5

# marks=int(input("enter marks: "))
# exam=input("entrance exam completed?")
# if marks>=50:
#     if exam =="yes":
#         print("eligible for admission")
#     else:
#         print("complete entrence exam")
# else:
#     print("not eligible")

#if elif else

# marks=int(input("enter mmarks:"))
# if marks>=90:
#     print("A")
# elif marks>=75:
#     print("B")
# elif marks>=60:
#     print("c")
# elif marks>=40:
#     print("D")
# else:
#     print("F")


#qqst2

# days=int(input("enter dy number:"))
# if days==1:
#     print("monday")
# elif days==2:
#     print("tuesday")
# elif days==3:
#     print("wednesday")
# elif days==4:
#     print("thrusday")
# elif days==5:
#     print("friday")
# elif days==6:
#     print("saturday")
# elif days==7:
#     print("sunday")
# else:
#     print("invalid dayy")

#qst3

# num= int(input("enter a number"))
# if num>0:
#     print("positive")
# elif num<0:
#     print("negative")
# else:
#     print("zero")

#qst 4


# amount=int(input("enter amount:"))
# if amount>=10000:
#     print("20% dis")
# elif amount>=5000:
#     print("10% dis")
# elif amount>=2000:
#     print("5% dis")

# else:
#     print("no dis")

#qst 5

# age=int(input("enter age:"))
# if age<=12:
#     print("child")
# elif age<=19:
#     print("teenager")
# elif age<=59:
#     print("adult")

# else:
#     print("senoir citzen")

#list comperhension


# number=[1,2,3,4,5,6]
# a=[x for x in number]
# print(a)


# l=[i for i in range(11) if i %2==0]
# print(l)

# def add():
#     print(5+3)


# def name():
#     print("diya")


# add()
# name()

#1.with argument with return

#2.with argument without return

#3.without argument with return

#4.without argument without return

n=int(input("enter a number"))
if n==0:
    print("n is 0")
else:
    print("n is not 0")

