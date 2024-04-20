# Problem statement : Write a program which accept number from user and print that number of “*” on screen.

def Display(No):
    for i in range(No):
        print("*", end = " ") 

def main():
    print("Enter number : ")
    num = int(input())
    Display(num)

# Starter    
if __name__ == "__main__":
    main()

# Test Case : 
# Input : 5
# Output : *    *   *   *   *   