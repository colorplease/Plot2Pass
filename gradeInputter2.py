from datetime import date

current_input = ""
importing_grades = "c"
input_valid = False

def write_input_to_file():
    pass
def num_input_checker(input_text):
    global input_valid
    if input_text.isnumeric() == False:
        input_valid = False
    elif input_text.isnumeric() == True:
        input_valid = True
def get_max_days_from_month(monthNum, isLeapYear):
    if monthNum == 1:
        return 31
    if monthNum == 2:
        if isLeapYear == True:
            return 29
        if isLeapYear == False:
            return 28
    if monthNum == 3:
        return 31
    if monthNum == 4:
        return 30
    if monthNum == 5:
        return 31
    if monthNum == 6:
        return 30
    if monthNum == 7:
        return 31
    if monthNum == 8:
        return 31
    if monthNum == 9:
        return 30
    if monthNum == 10:
        return 31
    if monthNum == 11:
        return 30
    if monthNum == 12:
        return 31
def check_if_leap_year(yearInputted):
    difference = abs(2024 - yearInputted)
    if difference % 4 == 0:
        return True
    else:
        return False

def print_spacer():
    spacer = """












    """
    print(spacer)

def getDayCount(date):
    dateElements = date.split('/')


#MAIN CODE AT EXECUTION
print_spacer()
current_input = input("Enter the CLASS NAME ")
print_spacer()
f = open(current_input + ".txt", "w")
#DATE CURRENT
today = date.today().strftime('%m/%d/%Y').split("/")
day_current = today[0][1]
month_current = today[1][1]
year_current = today[2]
print(year_current)
print(month_current)
print(day_current)
while importing_grades.lower() == "c":
    #POINTS OUT OF
    while input_valid == False:
         points_out_of = input("Enter the amount of TOTAL POINTS that were avaliable for that assignment ")
         num_input_checker(points_out_of)
         print_spacer()
    input_valid = False
    #POINTS EARNED
    while input_valid == False:
        points_gotten = input("Enter the amount of points YOU EARNED for this assignment ")
        if int(points_out_of) - int(points_gotten) > 0:
            num_input_checker(points_gotten)
        print_spacer()
    input_valid = False
    #YEAR ASSIGNMENT
    #exception: past the current day
    year = ""
    flag_isCurrentYear = False
    while input_valid == False:
        year = input("Enter the YEAR the assignment was due WITH 4 DIGITS (####) ")
        if len(year) == 4:
            if int(year_current) - int(year) >= 0:
                num_input_checker(year)
        print_spacer()
    input_valid = False
    if int(year) == int(year_current):
        flag_isCurrentYear = True
    #MONTH ASSIGNMENT
    #exception: past current month
    #exception: less than or equal to zero input_valid == False:
    month = ""
    flag_isCurrentMonth = False
    current_month_days = 0
    while input_valid == False:
        month = input("Enter the MONTH the assignment was due WITH NO LEADING ZEROES (#) or (##) ")
        if month[0] != "0":
            if ((int(month) < 13) and (int(month) > 0)):
                if flag_isCurrentYear == True:
                    if int(month_current) >= int(month):
                        num_input_checker(month)
                if flag_isCurrentYear == False:
                    num_input_checker(month)
        print_spacer()
    if int(month) == int(month_current):
        flag_isCurrentMonth = True
    current_month_days = get_max_days_from_month(int(month), check_if_leap_year(int(year)))
    input_valid = False
    #DAY ASSIGNMENT
    #exception: past the current day
    day = ""
    while input_valid == False:
        day = input("Enter the DAY the assignment was due WITH NO LEADING ZEROES (#) or (##) ")
        if ((int(day) > 0) and (int(day) <= current_month_days)):
            if flag_isCurrentMonth and flag_isCurrentYear:
                if int(day_current) >= int(day):
                    num_input_checker(day)
            if ((flag_isCurrentMonth == False) and (flag_isCurrentYear == False)):
                num_input_checker(day)
        print_spacer()
    input_valid = False
    #CONTINUE OR PLOT
    while input_valid == False:
        importing_grades = input("Type F to plot your grade trend. Type C to record another assignment ")
        print_spacer()
        if importing_grades.lower() != "f" and importing_grades.lower() != "c":
            input_valid = False
        else:
            input_valid = True
    input_valid = False
    f.write(points_gotten + ";" + points_out_of + ";" + month + ";" + day + ";" + year + '\n')
    f.close()

