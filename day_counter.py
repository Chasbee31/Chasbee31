# This code counts the number of a specific day in a chosen month and year 
# i.e. The number of Mondays in January 2022
# The code can detect if information was passed in incorrectly and/or outside of the accepted range

import calendar
def main():
    #While loop for continuous code running
    while 0<1:
        #Asks the user which day in the week they would like to count the quntity of
        print("Which day of the week do you want to count?")
        #Prints to the user which number to enter for each day e.g. "0 : Monday"
        for index, names in enumerate(calendar.day_name,start=0):
            print(index, ":", names)
        #Informs the user that typing "exit" will quit the code
        print("Or 'exit to quit'")

        #Saves user's response within exception handeling for correct input
        try:
            d = input()
            if d == "exit":
                break
            #Check user input was a number
            d = int(d)
        except ValueError as e:
            print("You didn't give me a valid number!")
            continue
        #Checks user's input was within range
        try:
            if d > 6 or d < 0:
                ze = 1/0
        except ZeroDivisionError as e:
            print("You didn't give me a number between 0 and 6!")
            continue

        #Asks the user which year they wish to count in, and informs the user that typing "exit" will quit the code
        try:
            y = input("Enter year e.g. 2022\nOr 'exit to quit'\n")
            if y == "exit":
                break
            #Check user input was a number
            y = int(y)
        except ValueError as e:
            print("You didn't give me a valid number!")
            continue
        try:
            #Checks user's input was within range
            if y < 0 :
                ze = 1/0
        except ZeroDivisionError as e:
            print("You didn't give me a number greater than 0!")
            continue

        #Asks the user which month in their chosen year they wish to count in
        print("Which month in", str(y) + "?")
        #Prints to the user which number to enter for each month e.g. "1 : January"
        for index, names in enumerate(calendar.month_name,start=0):
            if index != 0:
                print(index, ":", names)
        #Informs the user that typing "exit" will quit the code
        print("Or 'exit to quit'")
        try:
            m = input()
            if m == "exit":
                break
            #Check user input was a number
            m = int(m)
        except ValueError as e:
            print("You didn't give me a valid number!")
            continue
        #Checks user's input was within range
        try:
            if m > 12 or m < 1:
                ze = 1/0
        except ZeroDivisionError as e:
            print("You didn't give me a number between 12 and 1!")
            continue

        #Generates a calendar for the supplied year and month
        cal = calendar.monthcalendar(int(y), int(m))
        #Converts numerical day selected into text
        ds = (calendar.day_name[int(d)])
        #Converts day string into all upper case
        ds = ds.upper()
        #Initialises a counter
        count = 0
        #For loop iterates through each week in calender checking if the day specified is contained within it
        for i in range(0,5):
            if cal[i][getattr(calendar, str(ds))] != 0:
                 count += 1

        #Informs the user on the number of their chosen days within the month and year they selected
        print("There are", count, ds.capitalize() + "s in", calendar.month_name[int(m)], y)

#Main function runs on start up if this script is main script i.e. not called by another script
if __name__ == "__main__":
    main()