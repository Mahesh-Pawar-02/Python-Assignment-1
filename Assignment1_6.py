# Problem stetment : Write a program which accept number from user and check whether that number is positive or negative or zero. 

def Check(No):
    if(No > 0):
        print("Positive number")
    if(No < 0):
        print("negative number")
    elif(No == 0):
        print("Zero number")

def main():
    print("Enter number : ")
    num = int(input())
    Check(num)

# Starter    
if __name__ == "__main__":
    main()

# Test case : 
# Input : 11    Output : Positive Number 
# Input : -8    Output : Negative Number 
# Input : 0     Output : Zero 
