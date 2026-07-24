import customtkinter as ctk
import json


#---------------------------DISPLAY-------------------------------
def DISPLAY(): 
    Display = ctk.CTkToplevel(app)
    Display.title("Display students")
    Display.geometry("800x700")
    Display.focus()
    Display.lift()
    Display.attributes("-topmost", True)

    def display():
        with open("Data.json" , "r") as f:
            students = json.load(f)
        TB.delete("0.0","end")
        for student in students:
            name = student["name"]
            usn = student["usn"]
            branch = student["branch"]
            TB.insert("end", f"\nname : {name}\nusn : {usn}\nbranch : {branch}\n")
    
    def clear():
        TB.delete("0.0","end")

    DB = ctk.CTkButton(Display, text = "Display", command = display, width = 300, height = 40)
    DB.grid(pady = (40, 0))
    
    TB = ctk.CTkTextbox(Display,width = 600, height = 500)
    TB.grid(
        padx = 100,
        pady = (20,0)
    )

    CB = ctk.CTkButton(Display, text = "clear", command = clear, width = 300, height = 40)
    CB.grid(pady = (20, 0))

#----------------------------ADD STUDENT------------------------------
def ADD():
    AddStudent = ctk.CTkToplevel(app)
    AddStudent.title("add student")
    AddStudent.geometry("500x700")
    AddStudent.focus()
    AddStudent.lift()
    AddStudent.attributes("-topmost", True)

    def send_message():
        print("sent message")
        name = entry.get()
        usn = int(usn_entry.get())
        branch = branch_entry.get()
        
        with open("Data.json","r") as f: 
            students = json.load(f)
     
        for student in students: 
            if "usn" in students :
                num = student["usn"]
                if usn == num:
                    warning.configure(text = "this usn is already used", text_color = "red")
                    return
                                   
            else:
                num = student["usn"]
                if usn == num:
                    warning.configure(text = "this usn is already used", text_color = "red")
                    return


        student = {"usn" : usn, "name" : name, "branch" : branch}
        students.append(student)
        with open("Data.json","w") as f:
            json.dump(students , f, indent = 2)
        warning.configure(text = "student added", text_color = "green")
        

    my_label =ctk.CTkLabel(AddStudent,text="Add Student", font = ("Arial", 40))
    my_label.grid(padx = 100, pady = (100,0))

    warning =ctk.CTkLabel(AddStudent,text="", font = ("Arial", 20))
    warning.grid(padx = 0, pady = (10,0))



    my_label =ctk.CTkLabel(AddStudent,text="student's name", font = ("Arial", 20))
    my_label.grid(padx = (0,150), pady = (50,10))

    entry = ctk.CTkEntry(AddStudent, width = 300, height = 5,corner_radius = 15, bg_color = "black")
    entry.grid(padx = 100, pady = (0,50))
    


    my_label =ctk.CTkLabel(AddStudent,text="enter the student's usn", font = ("Arial", 20))
    my_label.grid(padx = (0,100), pady = (0,10))

    usn_entry = ctk.CTkEntry(AddStudent, width = 300, height = 5,corner_radius = 15, bg_color = "black")
    usn_entry.grid(padx = 100, pady = (0,50))



    my_label =ctk.CTkLabel(AddStudent,text="enter student's branch", font = ("Arial", 20))
    my_label.grid(padx = (0,100), pady = (0,10))

    branch_entry = ctk.CTkEntry(AddStudent, width = 300, height = 5,corner_radius = 15, bg_color = "black")
    branch_entry.grid(padx = 100, pady = (0,100))
  
    SendButton = ctk.CTkButton(
        AddStudent,
        text="Send",
        width=100,
        height=40,
        corner_radius=15,
        command=send_message,
        bg_color = "transparent")
    SendButton.grid( padx = 100, pady = 0 )

def SEARCH():
    SearchStudent = ctk.CTkToplevel(app)
    SearchStudent.geometry("500x700")
    SearchStudent.title("Search Student")
    SearchStudent.focus()
    SearchStudent.lift()
    SearchStudent.attributes("-topmost", True)
    def search_student():
        SearchName = iput.get()
        with open("Data.json","r") as f:
            students = json.load(f)
        
        for student in students:
            name = student["name"]
            if SearchName == name:
                usn = student["usn"]
                branch = student["branch"]
                oput.delete("0.0","end")
                oput.insert("end" , f"\nthe student with the {SearchName}, \nusn :- {usn}, \nbranch :- {branch}\n")
                warning.configure(text = "the student is found", text_color = "green")
                break
            
        else:
            oput.delete("0.0","end")
            oput.insert("end", f"there is no student with name {SearchName}\n")
            warning.configure(text = f"there no student with name {SearchName}", font =("Aerial",25), text_color = "red")
        

    Label = ctk.CTkLabel(SearchStudent,text = "search student", font = ("Aerial", 40))
    Label.grid(padx = 100,pady = (30,0))

    warning = ctk.CTkLabel(SearchStudent, text ="", font = ("Aerial", 35))
    warning.grid(padx = 0, pady = (20,0))

    iputlabel = ctk.CTkLabel(SearchStudent, text ="enter the name of the student", font = ("Aerial", 20))
    iputlabel.grid(padx = (20,200), pady = (25,0))

    iput = ctk.CTkEntry(SearchStudent,width = 300,height = 10,corner_radius = 15, bg_color = "black")
    iput.grid(padx = (20,150), pady = (10,0))

    SearchButton = ctk.CTkButton(
        SearchStudent,
        text = "search",
        width = 100,
        height = 40,
        corner_radius = 15,
        command = search_student,
        )
    SearchButton.grid(padx = (225,150), pady = (10,0))

    oputlabel = ctk.CTkLabel(SearchStudent, text = "student details",font = ("Aerial", 40))
    oputlabel.grid(padx = 100,pady = (30,0))

    oput = ctk.CTkTextbox(SearchStudent, width = 400, height = 250)
    oput.grid(padx = (50,50), pady =(10,0))

    SearchButton = ctk.CTkButton(
        SearchStudent,
        text = "search",
        width = 100,
        height = 40,
        corner_radius = 15,
        command = search_student,
        )
    SearchButton.grid(padx = (300,100), pady = (300,0))

def DELETE():
    DeleteStudent = ctk.CTkToplevel(app)
    DeleteStudent.geometry("1200x700")
    DeleteStudent.title("Delete Student")
    DeleteStudent.focus()
    DeleteStudent.lift()
    DeleteStudent.attributes("-topmost", True)
    def display():
        with open("Data.json", "r") as f:
            students = json.load(f)
        for student in students:
            usn = student["usn"]
            name = student["name"]
            branch = student["branch"]
            tb.insert("end",f"\n----------------------------------\n\n name of the student: {name},\n\n usn of the student: {usn},\n\n branch of the student: {branch}\n" "\n----------------------------------\n")

    def deleteButton():
        usn = int(iput.get())
        with open("Data.json", "r") as f:
            students = json.load(f)
        for student in students:
            if usn == student["usn"]:
                students.remove(student)
                label2.configure(text = "student removed", text_color = "red")
                break
            with open("Data.json", "r") as f:
                students = json.load(f)

            for student in students:
                usn = student["usn"]
                name = student["name"]
                branch = student["branch"]
                tb.delete("0.0","end")
                tb.insert("end", f"\nname = {name}, \nusn : {usn}, \nbranch : {branch} \n")    
        else :
            label2.configure(text = "student not found", text_color = "red")

        with open("Data.json", "w") as f:
            json.dump(students, f, indent = 2)

       

    DispFrame = ctk.CTkFrame(DeleteStudent, width = 500, height = 650)
    DispFrame.grid(row = 0, column = 0, padx = (50,50), pady = (25,25))

    DB = ctk.CTkButton(DispFrame, text = "Display", width = 100, height = 50, corner_radius = 15, command = display)
    DB.grid(padx = 200,pady = (25,25))
    tb = ctk.CTkTextbox(DispFrame, width = 400, height = 500, corner_radius = 25)
    tb.grid(padx = 15, pady = (0, 0))


    DelFrame = ctk.CTkFrame(DeleteStudent, width = 500, height = 650)
    DelFrame.grid(row = 0, column = 1, padx = (50, 50), pady = (25,25), sticky = "nsew")

    delete_label = ctk.CTkLabel(DelFrame, text = "delete student identity", font = ("Aerial", 35))
    delete_label.grid(padx = (75,100) , pady = (0,0))

    label1 = ctk.CTkLabel(DelFrame, text = "enter the usn of the student", font = ("Aerial", 20))
    label1.grid(padx = (5, 150), pady = (25, 0))

    iput = ctk.CTkEntry(DelFrame, width = 400, height = 20)
    iput.grid(padx = (5, 0), pady = (10,0))

    delbutton = ctk.CTkButton(DelFrame, text = "Delete", width = 100, height = 40, corner_radius = 15,  command = deleteButton)
    delbutton.grid(padx = (300,0), pady = (10, 0))
     
    label2 = ctk.CTkLabel(DelFrame, text = "", font = ("Aerial", 20))
    label2.grid(padx = (5,150), pady = (30,0))

def EDIT():
    EditStudent = ctk.CTkToplevel(app)
    EditStudent.geometry("1200x700")
    EditStudent.title("Edit Student")
    EditStudent.focus()
    EditStudent.attributes("-topmost", True)
    def sendB():
        check = int(usn_entry.get())
        with open("Data.json", "r") as f:
            students = json.load(f)
        for student in students:
            usn = student["usn"]
            if check == usn:
                name = student["name"]
                branch = student["branch"]
                Tb.delete("0.0", "end")
                Tb.insert("end",f"\nname of student : {name}\n\nusn of the student : {usn}\n\nbranch of student : {branch}")

    def done():
        new_name = nameentry.get()
        new_usn = int(usnentry.get())
        new_branch = branchentry.get()
        old_usn = int(usn_entry.get())
        
        with open("Data.json", "r") as f:
            students = json.load(f)
        for student in students:
            i = students.index(student)
            if old_usn == student["usn"]:
                updated = {"usn" : new_usn, "name" : new_name, "branch" : new_branch} 
                students[i] = updated
                with open("Data.json", "w") as f:
                    json.dump(students, f, indent =2)
                Tb.delete("0.0","end")
                Tb.insert("end",f"\nupdated name : {new_name},\n\nupdated usn : {new_usn},\n\nupdated branch : {new_branch}")
                break

        else:
            Tb.delete("0.0","end")
            Tb.insert("end", f"\n there is no student with {old_usn}\n")
            
        

    
    editframe1 = ctk.CTkFrame(EditStudent,width = 400, height = 650)
    editframe1.grid(row = 0, column = 1, padx = (25,75), pady = (25,25))

    Tb = ctk.CTkTextbox(editframe1, width = 400, height = 600)
    Tb.grid(padx = 50, pady = (25,25))

    
    editframe2 = ctk.CTkFrame(EditStudent,width = 500, height = 650)
    editframe2.grid(row = 0, column = 0, padx = (25,75), pady = (25,50),sticky = "nsew")
    
    label1 = ctk.CTkLabel(editframe2, text = "Edit Student", font = ("Aerial", 35))
    label1.grid(padx = 100, pady = (50, 0))

    usn_entry = ctk.CTkEntry(
        editframe2, 
        width = 300, 
        height = 25, 
        placeholder_text = "enter us of student"
        )
    usn_entry.grid(padx = (0,100), pady = (50, 0))

    sb = ctk.CTkButton(editframe2, text = "search", command = sendB)
    sb.grid(padx = (100,25), pady = (10,0))

    label3 = ctk.CTkLabel(editframe2, text = "New Details Of The Student", font = ("Aerial", 35))
    label3.grid(padx = (40,70), pady = (50, 0))

    nameentry = ctk.CTkEntry(
        editframe2, 
        width = 300,
        height = 25,
        placeholder_text = "enter new name"
    )
    nameentry.grid(padx = (0,100), pady = (50,0))

    usnentry = ctk.CTkEntry(
        editframe2,
        width = 300,
        height = 25,
        placeholder_text = "enter new usn"
    )
    usnentry.grid(padx = (0,100), pady = (50,0))

    branchentry = ctk.CTkEntry(
        editframe2, 
        width = 300,
        height = 25,
        placeholder_text = "enter new branch"
    )
    branchentry.grid(padx = (0,100), pady = (50,0))

    db = ctk.CTkButton(editframe2, text = "done", command = done)
    db.grid(padx = (95,30), pady = (10,0))

def EXIT():
    print("exited")
    app.destroy()    




#---------app define---------
app=ctk.CTk()
app.title("Student manager")
app.geometry("650x500")
ctk.set_appearance_mode("system")
app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(1, weight=1)


#---------------name for the app--------------
my_label =ctk.CTkLabel(app,text='student management system', font = ("Arial", 40, "bold"))
my_label.grid(padx = (50,0), pady = (50,0))


#----------------------------option buttons panel--------------------------------
buttons = ctk.CTkFrame(app, width = 100, height = 400, corner_radius = 25)
buttons.grid(padx =(0,90),pady = (40,20),sticky = "nse")


#-------------------------------buttons-------------------------------------------
button_1 = ctk.CTkButton(buttons, text = "display student data",command = DISPLAY)
button_1.grid(row=1,pady =40, padx = 20)

button_2 = ctk.CTkButton(buttons, text = "add student data", command = ADD)
button_2.grid(row=1, column = 1,pady =40, padx = 20 )

button_3 = ctk.CTkButton(buttons, text = "search student data", command = SEARCH)
button_3.grid(row=3, pady =40, padx = 20)

button_4 = ctk.CTkButton(buttons, text = "delete student data", command = DELETE)
button_4.grid( row=2,pady =40, padx = 20  )

button_5 = ctk.CTkButton(buttons, text = "edit student data", command = EDIT)
button_5.grid(row=2, column = 1,pady =40, padx = 20  )

button_6 = ctk.CTkButton(buttons, text = "exit", command = EXIT)
button_6.grid(row=3, column = 1,pady =40, padx = 20 )


app.mainloop()