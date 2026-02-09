from calculator import add_numbers

def main():
    print("Calculator App")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("Result:", add_numbers(x, y))

if __name__ == "__main__":
    main()
