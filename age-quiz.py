'''create Variable age, add integer as we asking of age. 
use input - question enter your age?
if the user < 13 output message "You quality for the kiddie discount" 
the user is == 21 output message "Congrats on your 21st!"
order condition top to bottom, once condition true it execute the process. 
start with the user is > 100 output message "Sorry you are dead" 
user > = 65 output message "Enjoy your retirement"
user > 40 , output message "You are over the hill"
finish statement - else for anythig esle output "Age is but a number -
numbers executed 13 - 20 / 21 - 39"''' 


age = int(input("Enter your age: "))

if age < 13:
    print("You quality for the kiddie discount")
elif age == 21:
    print("Congrats on your 21st!")
elif age >100:
    print ("Sorry you are dead") 
elif age >=65:
        print("Enjoy your retirement")  
elif age >=40: 
    print ("You are over the hill") 
else:
    print("Age is but a number")
