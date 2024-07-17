from tkinter import *
from random import randint
root = Tk()
root.title('Codemy.com - Strong Password Generator')
root.iconbitmap('codemy.ico')
root.geometry("500x300")


# Generate Random Strong Password
def new_rand():
    #clear our enter box 
    password_enter.delete(0,END)
    #get pw lenght and convert to int
    pw_lenght=int(my_enter.get())
    #create var for our password
    my_password=''
    #loop throght password lenght
    for x in range(pw_lenght):
        my_password += chr(randint(33,126))
    #output password to screen 
    password_enter.insert(0, my_password)
    
#Copy to clipboard
def cliper():
   # Clear the clipboard
	root.clipboard_clear()
	# Copy to clipboard
	root.clipboard_append(password_enter.get())


#Label Frame
lf = LabelFrame(root, text="How Many Characters?")
lf.pack(pady=20)


#create Enter box to Designate Number of Characters
my_enter = Entry(lf, font=("Helvetica",24))
my_enter.pack(padx=20,pady=20)


#create Enter box for our Returned Password
password_enter =Entry(root, text='', font=("Helvetica", 24), bd=0, bg="systembuttonface")
password_enter.pack(padx=20)


#create a fram for our Button
my_frame = Frame(root)
my_frame.pack(padx=20)


#create our Button
my_button = Button(my_frame, text="Generator strong password" , command=new_rand)
my_button.grid(row=0,column=0,padx=10)
clip_button =Button(my_frame , text="Copy to clipboard" , command=cliper)
clip_button.grid(row=0, column=1 , padx=10)
root.mainloop()


