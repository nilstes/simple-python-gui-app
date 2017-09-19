from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import person_db

def open_edit(root, person_data=None): # Hvis person_data ikke sendes inn settes den til "ingenting"

    # Definerer aksjon for lagring
    def save():
        if(id.get()):
            print("save " + name.get())
            person_db.update_person(id.get(), name.get(), address.get())
        else:
            print("create " + name.get())
            person_db.create_person(name.get(), address.get())           
        window.destroy()
        
    # Definerer aksjon for sletting
    def delete():
        print("delete " + name.get())
        if messagebox.askokcancel("Slett", "Er du sikker på at du vil slette personen?", parent=window):
            person_db.delete_person(id.get())
            window.destroy()

    # Definerer aksjon for å laste opp nytt bilde
    def load_image():
        formater = [('Bilder','*.png;*.gif')]
        filename = filedialog.askopenfilename(filetypes=formater, parent=window)
        photo = PhotoImage(file=filename)
        image_label.configure(image=photo)
        image_label.image = photo

    # Oppretter et nytt vindu for å editere personinfo
    window = Toplevel(root)

    # Legger dataene i egne Var-variabler som GUI'et kan bruke
    id = StringVar()
    name = StringVar()
    address = StringVar()

    if person_data:
        id.set(person_data[0])
        name.set(person_data[1])
        address.set(person_data[2])
        
    # Oppretter widgets og plasserer dem i grid'en
    name_label = Label(window, text="Navn:")    
    name_label.grid(column=0, row=0, padx=2, pady=2)
    name_entry = Entry(window, textvariable=name)   
    name_entry.grid(column=1, row=0, padx=2, pady=2)
    address_label = Label(window, text="Adresse:")  
    address_label.grid(column=0, row=1, padx=2, pady=2)
    address_entry = Entry(window, textvariable=address)   
    address_entry.grid(column=1, row=1, padx=2, pady=2)
    save_button = Button(window, text="Lagre", command=save)  
    save_button.grid(column=1, row=3, padx=2, pady=2)
    upload_button = Button(window, text="Last opp bilde", command=load_image)  
    upload_button.grid(column=0, row=2, padx=2, pady=2)

    # Legger til slette-knapp KUN hvis personen allerede eksisterer
    if person_data:
        delete_button = Button(window, text="Slett", command=delete)  
        delete_button.grid(column=0, row=3, padx=2, pady=2)

    # Legger til bilde
    image_base64 = ""
    photo = PhotoImage(data=image_base64)
    image_label = Label(window, borderwidth=2, relief="groove")
    image_label.grid(column=1, row=2)