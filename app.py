def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap Year")
            else:
                print("Not leap year")
        else:
            print("leap year")
    else:
        print("Not leap year")

Year = int(input("Enter the year to check leap year or not: "))

is_leap_year(Year)