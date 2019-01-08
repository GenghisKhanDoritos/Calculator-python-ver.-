#Calculator Memory Type.py
"""2019-01-06
Made by 임해찬
본 프로그램은 먼저 2개의 수와 1개의 연산자를 받아 저장하고 그후부터 1개의 수와 연산자를 받는다.
2.0업데이트
int로 받던걸 float로 받습니다"""
import sys, time
print('='*50)
print('Calculator Memory type')
print('='*50)

Working_Memory = 0
Secondary_Memory = 0

def operation(FN,OP,SN,Default):
    if OP=='1':
        Default = Default+FN+SN
        print('='*50)
        print(Default)
    elif OP=='2':
        Default = Default+FN-SN
        print('='*50)
        print(Default)
    elif OP=='3':
        Default= FN*SN
        print('='*50)
        print(Default)
    elif OP=='4':
        Default = FN/SN
        print('='*50)
        print(Default)
    else:
        print('='*50)
        print('Please input operator number correctly')
        print('1.Add')
        print('2.Subtract')
        print('3.Multiply')
        print('4.Division')
        OP=input("Input Operator number correctly\n")

    return Default
def operation2(Default,SN,ME,OP):
    if SN==0:
        Default = 0
        print(Default)
        print('='*50)
    elif OP=='1':
        Default = Default+SN
        print(Default)
        print('='*50)
    elif OP=='2':
        Default = Default-SN
        print(Default)
        print('='*50)
    elif OP=='3':
        Default = Default*SN
        print(Default)
        print('='*50)
    elif OP=='4':
        Default = Default/SN
        print(Default)
        print('='*50)
    else:
        print('='*50)
        print('Please input operator number correctly')
        print('1.Add')
        print('2.Subtract')
        print('3.Multiply')
        print('4.Division')
        OP=input("Input Operator In Number(if you input 0,input any operator.)\n")

    return Default


print('='*50)
First_Number = float(input("Input First number\n"))
print('='*50)
print('1.Add')
print('2.Subtract')
print('3.Multiply')
print('4.Division')
Operator = input('Input Operator in Number\n')
print('='*50)
Second_Number = float(input('Input Second number\n'))
print('='*50)
Working_Memory = operation(First_Number,Operator,Second_Number,Working_Memory)
while True:
    Second_Number = float(input("Input Next number('input 0 to Reset')\n"))
    print('1.Add')
    print('2.Subtract')
    print('3.Multiply')
    print('4.Division')
    Operator = input('Input Operator in Number(if you input 0, input any Operator)\n')
    Working_Memory = operation2(Working_Memory,Second_Number,Secondary_Memory,Operator)