from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

def open_edit(root):

    # Definerer aksjon for lagring
    def save():
        print("save: ")
        window.destroy()

    # Definerer aksjon for sletting
    def delete():
        print("delete: ")
        if messagebox.askokcancel("Slett", "Er du sikker på at du vil slette personen?", parent=window):
            print("Yes!")
            window.destroy()

    # Definerer aksjon for å laste opp nytt bilde
    def load_image():
        formater = [('Bilder','*.png;*.gif')]
        filename = filedialog.askopenfilename(filetypes=formater, parent=window)
        photo = PhotoImage(file=filename)
        image_label.configure(image=photo)
        image_label.image = photo

    window = Toplevel(root)

    name = StringVar()
    name_entry = Entry(window, textvariable=name)   
    name_label = Label(window, text="Navn:")
    
    adress = StringVar()
    address_entry = Entry(window, textvariable=adress)   
    address_label = Label(window, text="Adresse:")
    
    save_button = Button(window, text="Lagre", command=save)  
    delete_button = Button(window, text="Slett", command=delete)  
    upload_button = Button(window, text="Last opp bilde", command=load_image)  

    name_label.grid(column=0, row=0, padx=2, pady=2)
    name_entry.grid(column=1, row=0, padx=2, pady=2)
    address_label.grid(column=0, row=1, padx=2, pady=2)
    address_entry.grid(column=1, row=1, padx=2, pady=2)
    save_button.grid(column=1, row=3, padx=2, pady=2)
    delete_button.grid(column=0, row=3, padx=2, pady=2)
    upload_button.grid(column=0, row=2, padx=2, pady=2)
                       
    image_base64 = ""
    photo = PhotoImage(data=image_base64)
    image_label = Label(window, borderwidth=2, relief="groove")
    image_label.grid(column=1, row=2)