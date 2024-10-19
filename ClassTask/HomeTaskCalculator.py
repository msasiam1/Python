print("-----Calculator Home Task----\n")
a=int(input("Enter 1st Number:"))
b=int(input("Enter 2nd Number:"))
sign=str(input("Operation (+,-,*,/,%) :"))

if sign == "+" :
    print(f"{a} + {b} = {a + b}")
elif sign == "-" :
    print(f"{a} - {b} = {a - b}")
elif sign == "*" :
    print(f"{a} * {b} = {a * b}")
elif sign == "/" :
    print(f"{a} / {b} = {a / b}")
elif sign == "%" :
    print(f"{a} % {b} = {a % b}")
else:
    print("Invalid Operator")