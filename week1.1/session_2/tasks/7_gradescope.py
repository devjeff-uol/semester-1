# To test that you can successfully download a file and upload it to gradescope

# You are going to write a very simple program:

# Ask a user to enter two numbers (one per input)
try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    res = num1 * num2
    print(f"{num1} * {num2} = {res}")
except:
    print("That is not a number")