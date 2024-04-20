#Problem statement :  Write a program which contains one function named as ChkNum() which accept one parameter as number. 
# If number is even then it should display “Even number” otherwise display “Odd number” on console. 

def ChkNum(iNo):
    if(iNo % 2 == 0):
        print("Even number")
    else:
        print("Odd number")


def main():
    print("Enter number : ")
    ivalue = int(input())
    ChkNum(ivalue)

# Starter    
if __name__ == "__main__":
    main()

# Test Cases: 
# Input : 11    Output : Odd Number 
# Input : 8     Output : Even Number