#Calculator Memory Type.py
print('='*50)
print('Calculator Memory type')
print('='*50)

Working_Memory = 0
Secondary_Memory = 0

def operation(FN,OP,SN,Default):
    if OP=='1':
        Working_Memory = Default+FN+SN
        print(Working_Memory)
    elif OP=='2':
        Working_Memory = Default+FN-SN
        print(Working_Memory)
    elif OP=='3':
        Working_Memory = FN*SN
        print(Working_Memory)
    elif OP=='4':
        Working_Memory = FN/SN
        print(Working_Memory)
    else:
        print('Please input operator number correctly')
        print('''1.Add
        2.Subtract
        3.Multiply
        4.Division''')
        OP=input("Input Operator number correctly\n")

    return Working_Memory
def operation2(Default,SN,ME,OP):
    if SN==0:
        Working_Memory = 0
        print(Working_Memory)
    elif OP=='1':
        Working_Memory = Default+SN
        print(Working_Memory)
    elif OP=='2':
        Working_Memory = Default-SN
        print(Working_Memory)
    elif OP=='3':
        Working_Memory = Default*SN
        print(Working_Memory)
    elif OP=='4':
        Working_Memory = Default/SN
        print(Working_Memory)
    else:
        print('Please input operator number correctly')
        print('''1.Add
        2.Subtract
        3.Multiply
        4.Division''')
        OP=input("Input Operator In Number(if you input 0,input any operator.)\n")

    return Working_Memory


First_Number = int(input("Input First number\n"))
print('''1.Add
2.Subtract
3.Multiply
4.Division''')
Operator = input('Input Operator in Number\n')
Second_Number = int(input('Input Second number\n'))
Working_Memory = operation(First_Number,Operator,Second_Number,Working_Memory)
while True:
    Second_Number = int(input("Input Next number('input 0 to Reset')\n"))
    print('''1.Add
2.Subtract
3.Multiply
4.Division''')
    Operator = input('Input Operator in Number(if you input 0, input any Operator)\n')
    Working_Memory = operation2(Working_Memory,Second_Number,Secondary_Memory,Operator)