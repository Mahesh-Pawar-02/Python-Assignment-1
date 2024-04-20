# Problem statement : Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers. 

def Add(No1, No2):
    Ans = 0
    Ans = No1 + No2
    return Ans    


def main():
    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    Ret = Add(Value1, Value2)

    print("Addition is : ",Ret)

# Starter    
if __name__ == "__main__":
    main()

# Test cases : 
# Input : Enter first number  : 11  
#         Enter second number : 5
# Output : Addition is : 16 