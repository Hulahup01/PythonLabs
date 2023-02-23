from calculate import calculate_two_numbers


print("Hello World")

try:
    firstNumber = int(input("Enter the first number:"))
    operation = input("Choose the operation (add, sub, div, mult):")
    secondNumber  =int(input("Enter the second number:"))

    print(f"Result: {calculate_two_numbers(firstNumber, secondNumber, operation)}")

except Exception as exp:
    print(exp.args)   


listWithNumbers = [1, 2, 3 ,4, 5, 6]
print(f"List with all numbers: {listWithNumbers}")
listWithEvenNumber = [i for i in listWithNumbers if i % 2 == 0]
print(f"List contains even numbers: {listWithEvenNumber}")