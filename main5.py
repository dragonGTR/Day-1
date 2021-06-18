print("1. Binary")
print("2. Octal")
print("3. Hexa")

try:
    num = int(input("Enter the number "))
    choose = int(input("choose the conversion method "))

    if choose == 1:
        print("Converted into Binary \n", bin(num))

    elif choose == 2:
        print("Converted into Octal \n", oct(num))

    elif choose == 3:
        print("Converted into Hexadecimal \n", hex(num))

    else:
        print("Invalid Number")

except:
    print("Invalid number")