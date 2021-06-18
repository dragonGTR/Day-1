print("1. HCF")
print("2. GCD")

try:
    num = int(input("Enter the number "))

    if (num == 1):
        num1 = int(input("Enter the number 1 "))
        num2 = int(input("Enter the number 2 "))

        while num1 % num2 != 0:
            rem = num1 % num2
            num1 = num2
            num2 = rem

        print("HCF is ", num2)

    else:
        def gcd(num1, num2):
            if (num2 == 0):
                return num1
            else:
                return (gcd(num2, num1 % num2))


        num1 = int(input("Enter the number 1 "))
        num2 = int(input("Enter the number 2 "))
        result = gcd(num1, num2)
        print("GCD is " + str(result))




except:
    print("Enter the number")