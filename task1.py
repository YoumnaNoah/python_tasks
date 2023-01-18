#not using eval function since accord.to search its not safe though, dont know if it apply here
#using the result in the next operation (not done yet)
#mode
import time
mode=int(input("enter 1 if you want scientific mode enter 2 if you want programming mode: \n"))
#scientific mode
while mode == 1:
	print("\n")
	print("=====>To exit mode enter 0")
	time.sleep(2)
	print("\n")
	print("=====>To choose from this list")
	print("\n")
	print(" 1. addition\n 2. subtraction\n 3. multiplication\n 4. division ,\n")
	op=int(input("select the operation you want to perform from 1, 2, 3, 4 : \n"))
	
	if op == 0:
		break 
	print("to reuse your last ans enter x in any of your numbers \n")
	num_1=int(input("enter the first number\n"))
	num_2=int(input("enter the second number\n"))
	if op == 1:
		sum = num_1 + num_2
		print(num_1, "+", num_2, "=", sum)
		time.sleep(3)
		ans = sum
	elif op == 2:
		sub = num_1 - num_2
		print(num_1, "-", num_2, "=", sub)
		time.sleep(3)
		
	elif op == 3:
		mult = num_1 * num_2
		print(num_1, "x", num_2, "=", mult)
		time.sleep(3)
		
	elif op == 4:
		div = num_1 / num_2
		print(num_1, "÷", num_2, "=", div)
		time.sleep(3)
		

#prigramming mode
while mode == 2:
	print("\n")
	print("=====>To exit mode enter 0")
	time.sleep(2)
	print("\n")
	print("=====>To choose from this list")
	print("\n")
	time.sleep(1)
	print(" 1.And, 2. OR, 3.XOR, 4. NOT, 5. shift left, 6. shift right \n")
	btop = int(input("select the operation you want to perform form 1, 2, 3, 4, 5, 6,\n"))
	if btop == 0:
		break
	
	if btop ==1:
		num1 = int(input("enter your first number \n"))
		num2 = int(input("enter your second number \n"))
		Andr = num1 & num2
		print(num1,"AND",num2,"=",Andr,)
		time.sleep(3)
		
	if btop == 2:
		num1 = int(input("enter your first number \n"))
		num2 = int(input("enter your second number \n"))
		ORr = num1 | num2
		print(num1,"OR",num2,"=",ORr)
		time.sleep(3)
	
	if btop == 3:
		num1 = int(input("enter your first number \n"))
		num2 = int(input("enter your second number \n"))
		XORr = num1 ^ num2	
		print(num1,"XOR",num2,"=",XORr)	
		time.sleep(3)	
			
	if btop == 4:
		num1 = int(input("enter your number \n"))
		NOTr = ~num1	
		print("NOT", num1, "=", NOTr)	
		time.sleep(3)	
		
	if btop == 5:
		num1 = int(input("enter your  number \n"))
		num2 = int(input("enter your shift value \n"))
		shiftleft = num1 << num2		
		print(num1,"<<",num2,"=",shiftleft)
		time.sleep(3)	
		
	if btop == 6:
		num1 = int(input("enter your  number \n"))
		num2 = int(input("enter your shift value \n"))
		shiftright = num1 >> num2		
		print(num1,">>",num2,"=",shiftright)	
		time.sleep(3)	 
   

