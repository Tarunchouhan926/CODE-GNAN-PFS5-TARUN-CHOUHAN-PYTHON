import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
def otp(email):
    otp = random.randint(1111,9999)
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    mailusername = "Tarunchouhan1947@gmail.com"
    mailpassword = "xqmd vmwz ibqy ijii"
    from_email = "Tarunchouhan1947@gmail.com"
    to_email = email
    subject = f'OTP for Login'
    body = f"Hello \nWelcome to College Management System\nHere is your otp : {otp}"
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
    server.login(mailusername, mailpassword)  # Login to the email account
    # Send the email
    server.send_message(msg)
    # Disconnect from the server
    server.quit()
    return otp
def student_sendmessage(roll,name,age,email,branch,college):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    mailusername = "Tarunchouhan1947@gmail.com"
    mailpassword = "xqmd vmwz ibqy ijii"
    from_email = 'Tarunchouhan1947@gmail.com'
    to_email = email
    subject = f'Student Login'
    body = f"Hello \nWelcome to {college}\nHere is Your Details\nRoll: {roll}\nName: {name}\nAge: {age}\nBranch: {branch}"
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
    server.login(mailusername, mailpassword)  # Login to the email account
    # Send the email
    server.send_message(msg)
    # Disconnect from the server
    server.quit()
def teacher_sendmessage(name,age,email,subject,college):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    mailusername = "Tarunchouhan1947@gmail.com"
    mailpassword = "xqmd vmwz ibqy ijii"
    from_email = 'Tarunchouhan1947@gmail.com'
    to_email = email
    subject = f'Teacher Login'
    body = f"Hello \nWelcome to {college}\nHere is Your Details\n\nName: {name}\nAge: {age}\nSubject: {subject}"
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Upgrade the connection to a secur1e encrypted SSL/TLS connection
    server.login(mailusername, mailpassword)  # Login to the email account
    # Send the email
    server.send_message(msg)
    # Disconnect from the server
    server.quit()
class person:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email
class student(person):
    def __init__(self,name,age,email,roll,branch):
        super().__init__(name,age,email)
        self.roll = roll
        self.branch = branch
class teacher(person):
    def __init__(self,name,age,email,subject):
        super().__init__(name,age,email)
        self.subject = subject
class college:
    def __init__(self,name):
        self.name = name
        self.students = []
        self.teachers = []
    def add_student(self,student):
        self.students.append(student)
    def add_teacher(self,teacher):
        self.teachers.append(teacher)
    def display_students(self):
        if len(self.students) == 0:
            print("No students to this college")
        else:
            for i in self.students:
                print("Roll number:",i.roll)
                print("Name:",i.name)
                print("Branch:",i.branch)
                print()
    def display_teachers(self):
        if len(self.teachers) == 0:
            print("No teachers to this college")
        else:
            for i in self.teachers:
                print("Name:",i.name)
                print("Subject:",i.subject)
                print()
        
colleges = []
while True:
    print("Choose Option: ")
    print("1. To create College")
    print("2. To create Student")
    print("3. To Create Teacher")
    print("4. To print Students")
    print("5. To print Teachers")
    x = int(input())
    if x == 1:
        clg_name = input("Enter  College Name: ")
        x = False
        for i in colleges:
            if i.name == clg_name:
                x = True
                break
        if x == True:
            print("College Already Exits!")
        else:
            clg = college(clg_name)
            colleges.append(clg)
            print("College Created")
            print()
    elif x == 2:
        clg_name = input("Which College Student Belongs to ? \n")
        x = False
        for i in colleges:
            if i.name == clg_name:
                x = True
                y = i
                break
        if x == False:
            print("College Does not Exist!")
        else:
            roll = int(input("Enter Roll Number: "))
            name = input("enter Name of the student: ")
            age = int(input("Enter age of student: "))
            email = input("Enter email: ")
            branch = input("Enter Branch: ")
            x = otp(email)
            z = int(input("Enter your otp: "))
            if x == z:
                s1 = student(name,age,email,roll,branch)
                y.add_student(s1)
                student_sendmessage(roll,name,age,email,branch,clg_name)
                print("Student Added Sucessfully.\nCheck Your mail")
                print()
            else:
                print("Wrong otp entered. Try Again !")
    elif x == 3:
        clg_name = input("Which College Teacher Belongs to ? \n")
        x = False
        for i in colleges:
            if i.name == clg_name:
                x = True
                y = i
                break
        if x == False:
            print("College Does not Exist!")
        else:
            name = input("enter Name of the student: ")
            age = int(input("Enter age of student: "))
            email = input("Enter email: ")
            subject = input("Enter Subject: ")
            x = otp(email)
            m = int(input("Enter your otp"))
            if x == m:
                t1 = teacher(name,age,email,subject)
                y.add_teachers(t1)
                teacher_sendmessage(name,age,email,subject,clg_name)
                print("Teacher Added Sucessfully.\nCheck Your Mail")
                print()
            else:
                print("Wrong otp entered. Try again !")
    elif x == 4:
        clg_name = input("Which College students details do you want ?")
        x = False
        for i in colleges:
            if i.name == clg_name:
                x = True
                y = i
                break
        if x == False:
            print("College Does not Exist!")
        else:
            y.display_students()
    elif x == 5:
        clg_name = input("Which College teachers details do you want ?")
        x = False
        for i in colleges:
            if i.name == clg_name:
                x = True
                y = i
                break
        if x == False:
            print("College Does not Exist!")
        else:
            y.display_teachers()
