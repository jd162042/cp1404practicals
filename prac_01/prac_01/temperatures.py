"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":                                    #Quit the code

    if choice == "C":                                   #Choose celsius to fahrenheit
        celsius = float(input("Celsius: "))             #Ask for user input (C)
        fahrenheit = celsius * 9.0 / 5 + 32             #Do the conversion
        print(f"Result: {fahrenheit:.2f} F")            #Show the converted value (F)

    elif choice == "F":                                 #Choose F to C
        fahrenheit = float(input("Fahrenheit: "))       #Ask for user input (F)
        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        celsius = 5 / 9 * (fahrenheit - 32)             #Do the conversion
        # Remove the "pass" statement when you are done. It's a placeholder.
        print(f"Result: {celsius:.2f} C")               #Show the converted value (C)

    else:                                               #If the user selects a non-existent option
        print("Invalid option")
    print(MENU)                                         #Restart until user uses Quit option
    choice = input(">>> ").upper()
print("Thank you.")