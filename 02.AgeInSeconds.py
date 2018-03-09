import datetime

currentDay = datetime.datetime.now()
print("Today is: " + currentDay.strftime("%d/%m/%Y"))

def years_main(currentDay):
    your_date = str(input("\nEnter your birth date (keep the format shown above): "))

    try:
        your_date = datetime.datetime.strptime(your_date, "%d/%m/%Y")
        difference = (abs((your_date - currentDay).days))
        print("Passed " + str(difference) + " days.")
        seconds = difference * 86400
        print("In seconds: " + str(seconds))

    except ValueError:
        print("Wrong format ! Try again, please.")
        years_main(currentDay)

years_main(currentDay)
