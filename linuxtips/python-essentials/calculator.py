import sys
import os
from datetime import datetime

args = sys.argv[1:]

if not args:
    operator = input("Choose the operation to be calculated -> ")
    value_one = input("Type number 1 -> ")
    value_two = input("Type number 2 -> ")
    arguments = (operator, value_one, value_two)
elif len(args) != 3:
    print("Invalid arguments")
    print("ex: sum 2 2")
    sys.exit(1)
else:
    operator = args[0]
    value_one = args[1]
    value_two = args[2]
    arguments = (operator, value_one, value_two)

operator, *nums = arguments
print(f"Operator: {operator}")
print(f"Nums: {nums}")

operations = ["sum", "sub", "mul", "div"]
if operator not in operations:
    print("Operator not supported")
    sys.exit(1)

validated_nums = []
for num in nums:
    if not num.replace('.', "").isdigit():
        print(f"Number {num} is not digit")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

n1, n2 = validated_nums

result = None
if(operator == 'sum'):
    result = n1 + n2
elif(operator == 'sub'):
    result = n1 - n2
elif(operator == 'mul'):
    result = n1 * n2
elif(operator == 'div'):
    result = n1 / n2

print(f"Resultado: {result}")

path = os.curdir
filepath = os.path.join(path, 'calculator-log.log')
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymous')


with open(filepath, "a") as file:
    file.write(f"{timestamp} - {user}: {operator}, {n1}, {n2} = {result}\n")