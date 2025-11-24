

logo = """
.-----------------.
  |  21:20  100%    |
  |  ─────────────  |
  |  [7] [8] [9] ÷  |
  |  [4] [5] [6] ×  |
  |  [1] [2] [3] −  |
  |  [0] [.] [=] +  |
  '-----------------'
  
"""
print(logo)
print("Welcome to Zeney's Calculator")

def add(first,second):
    return first + second
def subtract(first,second):
    return first - second
def multiply(first,second):
    return first * second
def divide(first,second):
    if second==0:
        print("Error: Cannot divide by zero!")
        return None
    return first / second

def calculator():

    further_calculation= True
    first=float(input("Enter your first digit: "))
    while further_calculation:

        second= float(input("Enter you second digit: "))
        operations={
            "+":add,
            "-": subtract,
            "*": multiply,
            "/": divide
        }
        for symbols in operations:
            print (symbols)
        operation= input("Select from the above operations: ")
        answer= operations[operation](first,second)
        print(f"The answer is {answer}")
        more_game = input("Do you want to continue? Type y to continue or n to discontinue: ")

        if more_game=="y":
            first=answer
        elif more_game=="n":
            further_calculation= False
            print("\n"*20)
            calculator()

calculator()











