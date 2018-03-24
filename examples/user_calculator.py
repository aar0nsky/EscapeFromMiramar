import calculator
user_input = input("Which numbers do you want to add?").split(" ")
print("The sum is: " + calculator.add(user_input[0], user_input[1]))