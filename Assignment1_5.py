# Problem stetment : Write a program which display 10 to 1 on screen. 

def Display():
    for num in range(10, 0, -1):
        print(num, end = " ") 

def main():
    Display()

# Starter    
if __name__ == "__main__":
    main()

# Test Case: 
# Output : 10 9 8 7 6 5 4 3 2 1