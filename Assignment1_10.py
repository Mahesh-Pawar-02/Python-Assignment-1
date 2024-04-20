# Problem statement : Write a program which accept name from user and display length of its name.

def CalculateLen(string):
    print(len(string))

def main():
    print("Enter string : ", end = " ")
    str = input()
    CalculateLen(str)

# Starter    
if __name__ == "__main__":
    main()

# Test Case :
# Input : Enter string : Marvellous
# Output : 10