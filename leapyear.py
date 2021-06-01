def main():
    while True:
        try:
            year = int(input("Please enter a year. Positive integer values only: "))
            if(year < 0):
                raise ValueError
            break
        except ValueError:
            print("Invalid input!")
    
    print(isLeapYear(year))

def calcLeapYear(year):
    if (year%400 == 0):
        return ("% s is a Leap Year." % year)

if __name__ == '__main__':
    main()