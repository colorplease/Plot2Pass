current_input = ""
importing_grades = "CONTINUE"
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
while importing_grades == "CONTINUE":
    while input_valid == False:
        points_gotten = input("Enter the amount of points YOU EARNED for this assignment ")
        num_input_checker(points_gotten)
        print_spacer()
    input_valid = False
    while input_valid == False:
         points_out_of = input("Enter the amount of TOTAL POINTS that were avaliable for that assignment ")
         num_input_checker(points_out_of)
         print_spacer()
    input_valid = False
    date_assignment = input("Enter the date the assignment was due (MONTH/DAY/YEAR) ")
    current_input = current_input + ";" + points_gotten + ";" + points_out_of + ";" + date_assignment
    importing_grades = input("Type COMPLETE to plot your grade trend. Type CONTINUE to record another assignment ")

