name = input("Enter the name ")

try:
    age = int(input("Enter the age "))
    gender = input("Enter the gender ")

    salary = int(input("Enter the salary "))

    state = input("Enter the state ")

    city = input("Enter the city ")


    class InvalidError(Exception):
        def _init__(self, message):
            self.message = message


    try:
        for i in range(len(name)):
            if (ord(name[i]) < 65):
                raise InvalidError("Only characters allowed")
        for i in range(len(name)):
            if (ord(gender[i]) < 65):
                raise InvalidError("Only characters allowed")
        for i in range(len(name)):
            if (ord(state[i]) < 65):
                raise InvalidError("Only characters allowed")
        for i in range(len(name)):
            if (ord(city[i]) < 65):
                raise InvalidError("Only characters allowed")
        print(
            "Name: " + name + "\n" +
            "Age: " + str(age) + "\n" +
            "Gender: " + gender + "\n" +
            "Salary: " + str(salary) + "\n" +
            "State: " + state + "\n" +
            "City: " + city + "\n"
        )
    except InvalidError as e:
        print(e)





except:
    print("Only numbers")


