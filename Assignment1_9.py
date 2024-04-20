# Problem statement : Write a program which display first 10 even numbers on screen. 

def DisplayEven(No):
    count = 0
    num = 0
    while count < No:
        if num % 2 == 0:
            print(num, end=" ")
            count += 1
        num += 1

def main():
    print("Enter number : ", end = " ")
    No = int(input())

    DisplayEven(No)

# Starter    
if __name__ == "__main__":
    main()

# Test Case : 
# Input : Enter number : 10
# Output : 2 4 6 8 10 12 14 16 18 20