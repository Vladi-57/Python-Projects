while True:
    problem = str(input("what operator are you using today? "))
    x = int(input("what is your x value: "))
    y = int(input("what is your y value: "))

    if(problem == 'Add' or problem == "+"):
        print(x + y)
    elif (problem == 'Subtract' or problem == "-"):
        print(x - y)
    elif (problem == 'Multiply' or problem == "*"):
        print(x * y)
    elif (problem == 'Divide' or problem == "/"):
        if y == 0:
            print("y value can't be zero")
        else:
            print(x/y)
    elif problem != "Add" or "Subtract" or "Multiply" or "Divide":
        print("You have to pick, Add, Subtract, Multiply or Divide")
        
    break