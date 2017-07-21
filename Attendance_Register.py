from tkinter import Tk, StringVar, ttk, messagebox, PhotoImage
from tkinter import *
import time
import datetime

#-------------------------GUI----------------------------
"""Start by setting up a GUI"""
root = Tk()                        
root.title("Attendance Register")  # title of GUI    
root.geometry("1350x650+0+0")      # dimensions of GUI
root.configure(background='black') # background color


#------------------------Frames--------------------------
"""Make frames (Left and Right)"""
 
leftMayFrame = Frame(root, width = 1000, height = 650, bd = 8, relief = "raise")
leftMayFrame.pack(side = LEFT)    #left frame
rightMayFrame = Frame(root, width = 350, height = 650, bd = 8, relief = "raise")
rightMayFrame.pack(side = RIGHT)  #right frame

"""Divide left frame into two"""
leftMayFrame_1 = Frame(leftMayFrame, width = 1000, height = 100, bd = 8, relief = "raise")
leftMayFrame_1.pack(side = TOP) #top frame
leftMayFrame_2 = Frame(leftMayFrame, width = 1000, height = 550, bd = 8, relief = "raise")
leftMayFrame_2.pack(side = TOP) #bottom frame

"""Divide right frame into two"""
rightMayFrame_1 = Frame(rightMayFrame, width = 350, height = 215, bd = 8, relief = "raise")
rightMayFrame_1.pack(side = TOP) #top frame
rightMayFrame_2 = Frame(rightMayFrame, width = 350, height = 415, bd = 8, relief = "raise")
rightMayFrame_2.pack(side = TOP) #bottom frame

"""Image of school on bottom-right"""
cont1 = Canvas(rightMayFrame_2, width = 350, height = 425, bg = "black")
cont1.grid(row = 0, column = 0)
image5 = PhotoImage(file = "Images/school.gif")
cont1.create_image(175, 175, image = image5)

"""Pictures of students"""

#------------------------Variables-----------------------
DateofOrder = StringVar() #stores date
"""value0 would be used to store letter
that can be applied to all others when fill button is pressed"""
value0 = StringVar()
"""Value for each box would be stored in variables below"""
value1 = StringVar()
value2 = StringVar()
value3 = StringVar()
value4 = StringVar()
value5 = StringVar()
value6 = StringVar()
value7 = StringVar()
value8 = StringVar()
value9 = StringVar()
value10 = StringVar()
value11= StringVar()
#----------------------Functions of exit and reset--------

def fill_all_box():
    """When fill is pressed, all box would fill with value0"""
    store = value0.get()
    value0.set(store)
    value1.set(store)
    value2.set(store)
    value3.set(store)
    value4.set(store)
    value5.set(store)
    value6.set(store)
    value7.set(store)
    value8.set(store)
    value9.set(store)
    value10.set(store)
    value11.set(store)

def qExit():
    """Ask the user whether he/she wants to exit the GUI"""
    qExit = messagebox.askyesno("Exit System", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return
    
def Reset():
    """When reset is pressed, all values are reset"""
    value0.set("")
    value1.set("")
    value2.set("")
    value3.set("")
    value4.set("")
    value5.set("")
    value6.set("")
    value7.set("")
    value8.set("")
    value9.set("")
    value10.set("")
    value11.set("")



"""Shows photo of student when button is pressed"""
cont = Canvas(rightMayFrame_1, width = 250, height = 215, bg = "black")
cont.grid(row = 0, column = 0)
imagePhoto = PhotoImage(file = "Images/Aaryan Patel.gif")
cont.create_image(20, 320, image = imagePhoto)

def Pick(photo):
    """This function displays photo on top right frame"""
    imagePhoto = cont.create_image(20, 320, image = photo)


#=========================Components=========================

DateofOrder.set(time.strftime("%d/%m/%y"))  # set date

#------------------------leftMayFrame_1 (top frame)----------------------

 # Label Number
lblNo = Label(leftMayFrame_1, font = ('arial', 10, 'bold'), text = "No.", bd = 16)
lblNo.grid(row = 0, column = 0, sticky = W)
 # Student Number
lblStudentNo = Label(leftMayFrame_1, font = ('arial', 10, 'bold'), text = "Student No.", bd = 16)
lblStudentNo.grid(row = 0, column = 1, sticky = W)
 # Student Name
lblStudentName = Label(leftMayFrame_1, font = ('arial', 10, 'bold'), text = "Student Name.", bd = 16)
lblStudentName.grid(row = 0, column = 2, sticky = W)
 # Course No.
lblCourseCode = Label(leftMayFrame_1, font = ('arial', 10, 'bold'), text = "Course Code", bd = 16)
lblCourseCode.grid(row = 0, column = 3, sticky = W)

"""create box with various attendance options. If the user selects attendence
option, all students will be marked with that option."""
box = ttk.Combobox(leftMayFrame_1, textvariable = value0, state = 'readonly')
box["values"] = [' ', '/', 'L', '0', 'A', 'B'] #attendance options
box.current(0)
box.grid(row = 0, column = 4)

#add buttons: fill, reset, exit
btnArrow = Button(leftMayFrame_1, text = "Fill", padx = 2, pady = 2, bd = 2, fg = "black",
                  font=('arial', 10, 'bold'), width = 12, height = 1, command = fill_all_box).grid(row = 0, column = 5)
btnReset = Button(leftMayFrame_1, text = "Reset", padx = 2, pady = 2, bd = 2, fg = "black",
                  font=('arial', 10, 'bold'), width = 12, height = 1, command = Reset).grid(row = 0, column = 6)
btnExit = Button(leftMayFrame_1, text = "Exit", padx = 2, pady = 2, bd = 2, fg = "black",
                  font=('arial', 10, 'bold'), width = 12, height = 1, command = qExit).grid(row = 0, column = 7)

#date of attendance
lblDateofOrder = Label(leftMayFrame_1, font = ('ariel', 10, 'bold'), textvariable = DateofOrder,
                       padx = 2, pady = 2, fg = "black", bg = "white", relief = "sunken")
lblDateofOrder.grid(row = 0, column = 8, sticky = W)


    #------------------------leftMayFrame_2 rows---------------------
def add_student_to_register(name, number, email, mobile, i, var, photo):
    """Ths functions add student to the registe at row i. Parameters:
    name, number, email, mobile, row, box-variable, photo of student"""
     # Label Numbers
    lblNo = Label(leftMayFrame_2, font = ('arial', 10, 'bold'), text = str(i), bd = 16)
    lblNo.grid(row = i, column = 0, sticky = W)
     # Student Numbers
    lblStudent_No_1 = Label(leftMayFrame_2, font = ('arial', 10, 'bold'), text = str(number), padx = 2,
                            pady = 2, bd = 2, fg = "Black", width = 16)
    lblStudent_No_1.grid(row = i, column = 1, sticky = W)
     # Student Names
    lblStudent_Name = Label(leftMayFrame_2, font = ('arial', 10, 'bold'), text = name, padx = 2,
                            pady = 2, bd = 2, fg = "Black", width = 12)
    lblStudent_Name.grid(row = i, column = 2, sticky = W)
     # Course No.
    lblCourse_Code = Label(leftMayFrame_2, font = ('arial', 10, 'bold'), text = "100S", padx = 2,
                            pady = 2, bd = 2, fg = "Black", width = 12)
    lblCourse_Code.grid(row = i, column = 3, sticky = W)

    #create box with various attendance options. If the user selects attendence option, all students will be marked with that option.
    box = ttk.Combobox(leftMayFrame_2, textvariable = var, state = 'readonly')
    box["values"] = [' ', '/', 'L', '0', 'A', 'B']
    box.current(0)
    box.grid(row = i, column = 4)

    #add buttons
    btnSpace = Button(leftMayFrame_2, text = email, padx = 2, pady = 2, bd = 2, fg = "black",
                      font=('arial', 10, 'bold'), width = 23, height = 1).grid(row = i, column = 5)
    btnSpace = Button(leftMayFrame_2, text = mobile, padx = 2, pady = 2, bd = 2, fg = "black",
                      font=('arial', 10, 'bold'), width = 11, height = 1).grid(row = i, column = 6)
    btnSpace = Button(leftMayFrame_2, text = "photo", padx = 2, pady = 2, bd = 2, fg = "black",
                      font=('arial', 10, 'bold'), width = 11, height = 1, command = lambda: Pick(photo)).grid(row = i, column = 7)

#variables stored in array to process them with ease 
values = [value1, value2, value3, value4, value5, value6, value7, value8, value9,
          value10, value11]

names = open('names.txt', 'r').readlines() #read name, number, and email

photo_of_student = [None]*11 #access photo by name and store it in array for simplicity and order

for i in range(11):    #11 rows
    """Add image references in an array (so that there is some order)"""
    x = names[i].split(", ") # get name
    string = "Images/" + x[0] + ".gif"  #access photo stored in Images as Name.gif
    try:
        photo_of_student[i] = PhotoImage(file = string) #if photo in Images
    except:
        photo_of_student[i] = PhotoImage(file = "Images/Default.gif")  #else use default
    
for i in range(11):
    name, number, email, mobile = names[i].split(", ")  #get name, number, email
    add_student_to_register(name, number, email, mobile, i, values[i], photo_of_student[i])


    












root.mainloop()
