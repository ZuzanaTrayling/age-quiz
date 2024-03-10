def evaluate_age(age):
    if age < 13:
        print("You qualify for the kiddie discount (under 13 years old).")
    elif age == 21:
        print("Congratulations on your 21st birthday!")
    elif age > 100:
        print("Sorry, you are considered to have reached the end of life expectancy.")
    elif age >= 65:
        print("Enjoy your retirement!")
    elif age >= 40:
        print("You are over the hill, but life is just beginning!")
    else:
        print("Age is but a number - you are in the prime of your life!")


def main():
       try:
        age = int(input("Enter your age: "))
        evaluate_age(age)
    except ValueError:
        print("Invalid input! Please enter a valid age.")

if __name__ == "__main__":
    main()
