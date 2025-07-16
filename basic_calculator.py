#A simple Calculator
print('''$*$*$*$*$*$*$**$*$*$*$*$*$*$
1.	Addition
2	Subtraction
3.	Multiplication
4.	Division
$*$*$*$*$*$*$*$*$*$*$*$*$*$''')

print ("Enter two numbers to addd")
#accepts first number and store it
firstNumber=(input("First Number:"))
#accepts second number and store it
secondNumber=(input("Second Number:"))
sum = float(firstNumber) + float(secondNumber) 
print (f"{firstNumber} + {secondNumber} = {sum:.2f}")
print("****************")
print("Subtraction")
print("****************")
print ("Enter two numbers to Subtrac")
#accepts first number and store it
firstNumber=(input("First Number:"))
#accepts second number and store it
secondNumber=(input("Second Number:"))
sub = float(firstNumber) - float(secondNumber)
print (f"{firstNumber} - {secondNumber} = {sub:.2f}")





print("****************")
print("Multiplication")
print("****************")
print ("Enter two numbers to Multiply")
#accepts first number and store it
firstNumber=(input("First Number:"))
#accepts second number and store it
secondNumber=(input("Second Number:"))
mul = float(firstNumber) * float(secondNumber)
print (f"{firstNumber} * {secondNumber} = {mul:.2f}") 





print("****************")
print("Division")
print("****************")
print ("Enter two numbers to Divide")
#accepts first number and store it
firstNumber=(input("First Number:"))
#accepts second number and store it
secondNumber=(input("Second Number:"))
div = float(firstNumber) / float(secondNumber)
print (f"{firstNumber} / {secondNumber} = {div:.2f}")
 


print("****************")
print("Exponential")
print("****************")
print ("Enter two numbers to find the exponential")
#accepts first number and store it
firstNumber=(input("First Number:"))
#accepts second number and store it
secondNumber=(input("Second Number:"))
exp = float(firstNumber) ** float(secondNumber)
print (f"{firstNumber} ** {secondNumber} = {exp:.2f}") 


print("****************")
print("Floor Division")
print("****************")
print ("Enter two numbers to perform floor divition")
#accepts first number and store it
firstNumber=(input("First Number:"))
#accepts second number and store it
secondNumber=(input("Second Number:"))
floor_div = float(firstNumber) // float(secondNumber)
print (f"{firstNumber} // {secondNumber} = {floor_div:.2f}")

