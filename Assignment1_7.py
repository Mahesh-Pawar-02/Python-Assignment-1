# Problem stetment : Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false. 

def Display(No):
    if No % 5 == 0:
        return "True"
    else:
        return "False"

def main():
    print("Enter number : ")
    num = int(input())
    Display(num)


# Starter    
if __name__ == "__main__":
    main()

# Test case : 
# Input : 8    Output : False 
# Input : 25   Output : True 