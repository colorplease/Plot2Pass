import tkinter as tk
from datetime import date

input_valid = False

def num_input_checker(input_text):
    global input_valid
    if input_text.isnumeric() == False:
        input_valid = False
    elif input_text.isnumeric() == True:
        input_valid = True

today = date.today().strftime('%m/%d/%Y').split("/")
day_current = today[0][1]
month_current = today[1][1]
year_current = today[2]

def check_out_of(points_out_of):
    #POINTS OUT OF
    num_input_checker(points_out_of)
    if input_valid == False:
         Error_lbl.config(text="ERROR: TYPE VALID NUMBER")
         From_entry.delete(0, "end")
    else:
        Error_lbl.config(text="")
        Score_lbl.config(text=str(points_out_of))
        From_entry.delete(0, "end")
        #sets up window to input POINTS GOTTEN
        windowInputGrade.title('how many points did you EARN for this assignment?')
        Title_lbl.config(text="how many points did you EARN for this assignment?")
        step_num = 1
        input_valid = False

def check_got(points_gotten):
    if int(TOTAL_POINTS) - int(points_gotten) > 0:
        num_input_checker(points_gotten)
    else:
        Error_lbl.config(text="ERROR: POINTS GOTTEN IS HIGHER THAN POINTS AVALIABLE")
        From_entry.delete(0, "end")
    if input_valid == False:
        Error_lbl.config(text="ERROR: TYPE VALID NUMBER")
        From_entry.delete(0, "end")
    else:
        Error_lbl.config(text="")
        Score_lbl.config(text=str(points_gotten + " / " + TOTAL_POINTS))
        From_entry.delete(0, "end")
        input_valid = False

#all window stuff
TOTAL_POINTS = 0
GOT_POINTS = 0
step_num = 0
def inputGrades():
    if(step_num == 0):
        TOTAL_POINTS = From_entry.get()
        check_out_of(TOTAL_POINTS)
    elif(step_num == 1):
        GOT_POINTS = From_entry.get()
        check_got(GOT_POINTS)
#demo:
#create window and set window size
#sets up window to input TOTAL AVALIABLE
windowInputGrade = tk.Tk()
frame_InputGrades = tk.Frame(windowInputGrade)
frame_InputGrades.grid(column=0, row=0, sticky="N", pady=100)
frame_InputGrades.pack(fill="both", expand=True)
windowInputGrade.wm_geometry("800x600")
windowInputGrade.resizable(False, False)
windowInputGrade.title('how many points were AVALIABLE for this assignment?')
#textbox
From_entry = tk.Entry(frame_InputGrades,font=('font name',45), justify="center")
#label
Title_lbl = tk.Label(frame_InputGrades,text="how many points were AVALIABLE for this assignment?",font=('font name',19))
Title_lbl.pack()
From_entry.pack()
Submit_btn = tk.Button(frame_InputGrades, text="CONFIRM", command=inputGrades, font=('font name',19))
Submit_btn.pack()
Score_lbl = tk.Label(frame_InputGrades,text="",font=('font name',45))
Score_lbl.pack()
Error_lbl = tk.Label(frame_InputGrades,text="",font=('font name',30), fg='red')
Error_lbl.pack()
windowInputGrade.mainloop()