from calculaor_function import  add,sub,mul,div


while True:
    print("1:add")
    print("2:sub")
    print("3:mul")
    print("4:div")
    print("5:exit")

    choice=int(input("enter your choice"))

    if choice==1:
        number1=int(input("enter your first number"))
        number2=int(input("enter your second number"))
        answer=add(number1,number2)
        print(f"{number1}+{number2}={answer}")
    elif choice==2:
        number1=int(input("enter your first number"))
        number2=int(input("enter your second number"))
        answer=sub(number1,number2)
        print(f"{number1}-{number2}={answer}")
    elif choice==3:
        number1=int(input("enter your first number"))
        number2=int(input("enter your second number"))
        answer=mul(number1,number2)
        print(f"{number1}*{number2}={answer}")
    elif choice==4:
        number1=int(input("enter your first number"))
        number2=int(input("enter your second number"))
        if number2==0:
            print( "cannote be divided by 0")
        else:
            answer=div(number1,number2)
            print(f"{number1}/{number2}={answer}")
    elif choice==5:
        break
