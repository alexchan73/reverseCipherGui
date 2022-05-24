from tkinter import *

#Creating base frame
window = Tk()
window.title('Reverse Cipher Encryptor')
window.geometry('210x210')


def encrypt():
    target_string = user_input.get()  #getting entry text
    copy_entry.insert(0,str(target_string[::-1]))

Label(window, text="Enter text you wish to encrypt").pack()

#Asking user to input string
user_input = Entry(window)
user_input.pack()

#Button to encrypt message
Button(window, text="Click to Encrypt", command=encrypt).pack()

#Label for below result
myLabel = Label(text = "Encrypted Text will show below")
myLabel.pack()

#Empty entry box that will generate the encrypted message, user is able to highlight the text.
copy_entry = Entry(window)
copy_entry.pack()

window.mainloop()