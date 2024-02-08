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
def print_spacer():
    spacer = """












    """
    print(spacer)

def getDayCount(date):
    dateElements = date.split('/')


#MAIN CODE AT EXECUTION

current_input = input("Enter the CLASS NAME ")
f = open(current_input + ".txt", "w")
#DATE CURRENT
today = date.today().strftime('%m/%d/%Y').split("/")
day_current = today[0][1]
month_current = today[1][1]
year_current = today[2]
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
    year = ""
    while input_valid == False:
        year = input("Enter the YEAR the assignment was due WITH 4 DIGITS (####) ")
        if len(year) == 4:
            if int(year_current) - int(year) >= 0:
                num_input_checker(year)
        print_spacer()
    input_valid = False
    #MONTH ASSIGNMENT
    month = ""
    while input_valid == False:
        month = input("Enter the MONTH the assignment was due WITH NO LEADING ZEROES (#) or (##) ")
        if month[0] != "0":
            if int(month) < 13:
                num_input_checker(month)
        print_spacer()
    input_valid = False
    #DAY ASSIGNMENT
    day = ""
    while input_valid == False:
        day = input("Enter the DAY the assignment was due WITH NO LEADING ZEROES (#) or (##) ")
        if day[0] != "0":
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

