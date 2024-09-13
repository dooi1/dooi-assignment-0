def adder(x,y):
    return x + y

def main():
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))

        result = adder (num1, num2)

        print(str(num1) + " + " + str(num2) + " is " + str(result))


    except ValueError:
        print("Please enter valid numbers.")


if __name__ == "__main__":
    main()
