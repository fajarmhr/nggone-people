value1 = input("Please enter first integer:\n")
value2 = input("Please enter second integer:\n")
 
v1 = int(value1)
v2 = int(value2)
 
choice = input("Enter 1 for addition.\nEnter 2 for subtraction.\nEnter 3 for Multiplication.:\n")
choice = int(choice)
 
if choice == 1:
    print(f'You entered {v1} and {v2} and their addition is {v1 + v2}')
elif choice == 2:
    print(f'You entered {v1} and {v2} and their subtraction is {v1 - v2}')
elif choice == 3:
    print(f'You entered {v1} and {v2} and their multiplication is {v1 * v2}')
else:
    print("Wrong Choice, terminating the program.")