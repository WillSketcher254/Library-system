import tkinter
import customtkinter
from customtkinter import *
from tkinter import messagebox
import customtkinter as ctk

borrowed = []
#The BOOKS

existing_bks = []
books = 0
with open('books.txt','r')as file:
    text = file.read()
    for line in text.splitlines():
        books += 1
        existing_bks.append(line)

#The members
existing_mbrs = []
mbrs = 0
with open('names.txt','r')as file:
    text = file.read()
    for line in text.splitlines():
        mbrs += 1
        existing_mbrs.append(line)

## MAIN CLASS
class Book:

    def __init__(self, title, author, book_no, student):
        self.title = title
        self.author = author
        self.book_no = book_no
        self.student = student

    def borrow(self):
        new_book = (f'Student Name: {self.student}, Book Title: {self.title}, Book Author: {self.author}, book_no: {self.book_no}')

        borrowed.append(new_book)

    def display_borrowed():
        print(borrowed)



class Library:
    def __init__(self):
        self.existing_mbrs = []

    def borrowAct(self, book, on_book_select):
        bookInfo = book.split(',')
        user_name = on_book_select.entry1.get()
        user_ID = on_book_select.entry2.get()

        new_student = f'{user_name}, {user_ID}'
        
        if new_student in self.existing_mbrs:
            newValue = ''
        else:
            self.existing_mbrs.append(new_student)
            newValue = '** A New Member Added **'

        if user_ID != '' and user_name == '':
            messagebox.showinfo('Input Failure', "Please enter The Student's name")
        elif user_name != '' and user_ID == '':
            messagebox.showinfo('Input Failure', "Please enter The Student's ID")
        else:
            on_book_select.entry1.delete(0, ctk.END)
            on_book_select.entry2.delete(0, ctk.END)

            messagebox.showinfo('Borrow', f"{newValue}\nStudent {user_name} (ID: {user_ID}) has borrowed \nBook {book}")

            student = user_name
            title = bookInfo[0]
            author = bookInfo[1]
            book_no = bookInfo[2]

            book_obj = Book(title, author, book_no, student)
            book_obj.borrow()

library = Library()

def on_book_select(book_name):

    selected = book_name.split(',')
    properties = f'Book Title: {selected[0]}\n Book Author: {selected[1]}\n Book Number: {selected[2]}'
    if hasattr(on_book_select, 'selectedLabel'):
        on_book_select.selectedLabel.destroy()
        on_book_select.stuLabel.destroy()
        on_book_select.entry1.destroy()
        on_book_select.entry2.destroy()
        on_book_select.borrowBtn.destroy()

    on_book_select.selectedLabel = customtkinter.CTkLabel(bottom_Frame,text=f'Selected Book: \n {properties}',font=my_font,text_color='#283164',justify='left')
    on_book_select.selectedLabel.place(relx=0.05,rely=0.1)
    on_book_select.stuLabel = customtkinter.CTkLabel(bottom_Frame,text=f'Borrower Name',font=my_font,text_color='#2190c8',justify='left')
    on_book_select.stuLabel.place(relx=0.05,rely=0.4)
    on_book_select.entry1 = customtkinter.CTkEntry(bottom_Frame, placeholder_text='Name of student...',font=my_font,width=250)
    on_book_select.entry1.place(relx=0.05,rely=0.45)
    on_book_select.entry2 = customtkinter.CTkEntry(bottom_Frame, placeholder_text='Student ID ...',font=my_font,width=250)
    on_book_select.entry2.place(relx=0.05,rely=0.55)
    on_book_select.borrowBtn = customtkinter.CTkButton(bottom_Frame, text='Borrowed', fg_color='#2190c8', hover_color='#c021c8',font=my_font,width=250,command=lambda:library.borrowAct(book_name,on_book_select))
    on_book_select.borrowBtn.place(relx=0.05,rely=0.65)

def show(event):
    if event == 'borrow':
        mbrsLabel.place(rely=10,relx=0.6)
        scrollbar3.place(rely=15,relx=0.6) 

        bookLabel.place(relx=0.5,rely=0.05)
        scrollbar.place(relx=0.5,rely=0.15) 
        scrollbar2.place(relx=10,rely=0.15) 
        trackLabel.place(relx=10)
    elif event == 'track':
        check()
        mbrsLabel.place(rely=10,relx=0.6) 
        scrollbar3.place(rely=15,relx=0.6)

        bookLabel.place(relx=0.5,rely=10.05)
        scrollbar.place(relx=0.5,rely=10.15) 
        scrollbar2.place(rely=0.1,relx=0.05) 
        trackLabel.place(relx=0.1)
        if hasattr(on_book_select, 'selectedLabel'):
            on_book_select.selectedLabel.destroy()
            on_book_select.stuLabel.destroy()
            on_book_select.entry1.destroy()
            on_book_select.entry2.destroy()
            on_book_select.borrowBtn.destroy()
    elif event == 'member':
        members()
        mbrsLabel.place(rely=0.05,relx=0.6) 
        scrollbar3.place(rely=0.15,relx=0.6)

        bookLabel.place(relx=0.5,rely=10.05)
        scrollbar.place(relx=0.5,rely=10.15) 
        scrollbar2.place(rely=0.1,relx=10.15) 
        trackLabel.place(relx=10)
        if hasattr(on_book_select, 'selectedLabel'):
            on_book_select.selectedLabel.destroy()
            on_book_select.stuLabel.destroy()
            on_book_select.entry1.destroy()
            on_book_select.entry2.destroy()
            on_book_select.borrowBtn.destroy()

        
        

my_font=('Comic Sans MS', 20)

app = customtkinter.CTk()
app.geometry('700x500')
app.title('Library System')

#My frames
top_Frame = customtkinter.CTkFrame(master=app, fg_color='dark gray')
top_Frame.pack(side='top', fill = 'x',expand=False)
bottom_Frame = customtkinter.CTkFrame(master=app, fg_color='light gray')
bottom_Frame.pack(side='top', fill = 'both',expand=True)

#Top
labeling = customtkinter.CTkLabel(master=top_Frame,text='Library Management System', font=('Comic Sans MS', 28), text_color='blue')
labeling.place(rely=0.2,relx=0.35)
members = customtkinter.CTkButton(master=top_Frame, fg_color='blue',hover_color='purple',text='Members', font=my_font, command=lambda:show('member'))
members.place(rely=0.75,relx=0.1)
borrowBk = customtkinter.CTkButton(master=top_Frame, fg_color='blue',hover_color='purple',text='Borrow', font=my_font, command=lambda:show('borrow'))
borrowBk.place(rely=0.75,relx=0.35)

tracked = customtkinter.CTkButton(master=top_Frame, fg_color='blue',hover_color='purple',text='Tracked & borrowed', font=my_font, command=lambda:show('track'))
tracked.place(rely=0.75,relx=0.6)

#Borrow Section
bookLabel = customtkinter.CTkLabel(bottom_Frame,text=f'Books Available: {books}',font=my_font,text_color='black')
scrollbar = customtkinter.CTkScrollableFrame(bottom_Frame,width=600,height=400)
scrollbar2 = customtkinter.CTkScrollableFrame(bottom_Frame,width=1200,height=500)
scrollbar3 = customtkinter.CTkScrollableFrame(bottom_Frame,width=400,height=400)


for book in existing_bks:
    label =customtkinter.CTkLabel(scrollbar,text=book,font=my_font,text_color='white')
    label.pack(pady=5)
    label.bind("<Button-1>", lambda event, book_name=book: on_book_select(book_name))


#Tracking  Books Borrowed
trackLabel=customtkinter.CTkLabel(bottom_Frame,text=f'Borrowed Books ',font=my_font,text_color='black')    
def check():
    
    if hasattr(check, 'labels'):  
        for label in check.labels: 
            label.destroy()
    
    check.labels = []

    for book in borrowed:
        label = customtkinter.CTkLabel(scrollbar2, text=book, font=my_font, text_color='white',justify='left')
        label.pack(pady=5)
        check.labels.append(label)

# SHowing All Members Present
mbrsLabel = customtkinter.CTkLabel(bottom_Frame,text=f'Registered Members:',font=my_font,text_color='black') 

def members():
    if hasattr(members,'label'):
        for label in members.label:
            label.destroy()

    members.label = []
    for member in existing_mbrs:
        label = customtkinter.CTkLabel(scrollbar3, text=member, font=my_font, text_color='white',justify='left')
        label.pack(pady=5)
        members.label.append(label)

app.mainloop()
