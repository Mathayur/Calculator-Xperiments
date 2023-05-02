#Functions that define the operations and other functionalities inside the calculator
def soma(x,y):
    return x + y

def subtracao(x,y):
    return x - y

def multiplicacao(x,y):
    return x * y

def divisao(x,y):
    return x / y

def potencia(x,y):
    return x ** y

def raiz(x,y):
    return x ** (1/y)
    
def end_program():
    print('Closing Program.')
    exit()

#Dictionary Internal Menu, this makes easier for the program to access the functions that may be increased if needed.
basic = {
    "+":soma,
    "-":subtracao,
    "*":multiplicacao,
    "/":divisao,
    "**":potencia,
    "//":raiz
}

#The menu displayed to the user, choosing the operation access the internal menu in the dictionary
while True:
    print('''-----OPERATIONS-----\n
  + - ADDITION
  - - SUBTRACTION
  * - MULTIPLICATION
  / - DIVISION
  ** - EXPONENTIATION
  // - ROOTS
          ''')
#This is the initial input that is required from the user, which are the first number the operation and the second number    
    x = float(input('First Value: '))
    operation = input('Operation:')
    y = float(input('Second Value: '))
#This is the loop that is actually the calculator, it uses the first 3 inputs and does the choosen operation and then keeps asking the user if they want to continue
#If Yes is choosen then the program ask the new operand and new value
    if operation in basic:
        result = basic[operation](x,y)
        print(result)
        new_result = result
        while True:
            following = input('Continue? Y/N: ').upper()
            if following == 'Y':
                operation = input('Operation:')
                if operation in basic:
                    z = float(input('Next Value: '))
                    new_result = basic[operation](new_result,z)
                    print(new_result)
                else:
                    print('Operation not found!\n Try again.') 
            elif following == 'N':
                end_program()
            else:
                print('Invalid input! Please enter Y or N.')
    else:
        print('Operation not found!\n Try again.')
    