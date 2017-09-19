from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import base64
import person_db

# Åpner eget vindu for å editere person
def open_edit(root, search, person_data=None): # Hvis person_data ikke sendes inn settes den til "ingenting"

    # Definerer aksjon for lagring
    def save():
        if(id.get()):
            print("save " + name.get())  # Kun logg
            person_db.update_person(id.get(), name.get(), address.get(), age.get(), image_base64.get())
        else:
            print("create " + name.get())  # Kun logg
            person_db.create_person(name.get(), address.get(), age.get(), image_base64.get())           
        window.destroy()  # Lukk dette vinduet
        search()  # Oppdater data i hovedvinduet på nytt siden vi har oppdatert innhold
        
    # Definerer aksjon for sletting
    def delete():
        print("delete " + name.get())  # Kun logg
        if messagebox.askokcancel("Slett", "Er du sikker på at du vil slette personen?", parent=window):
            person_db.delete_person(id.get())
            window.destroy()  # Lukk dette vinduet
            search()  # Oppdater data i hovedvinduet på nytt siden vi har oppdatert innhold

    # Definerer aksjon for å laste opp nytt bilde
    def load_image():
        formater = [('Bilder','*.png;*.gif')]  # Kun png og gif. JPG krever PIL-bibliotek i tillegg
        filename = filedialog.askopenfilename(filetypes=formater, parent=window)
        with open(filename, "rb") as file:
            bytes = file.read()
            b64 = base64.b64encode(bytes)
            photo = PhotoImage(data=b64)
            image_label.configure(image=photo)
            image_label.image = photo
            image_base64.set(b64.decode('utf-8'))

    # Oppretter et nytt vindu for å editere personinfo
    window = Toplevel(root)

    # Logger inndata
    print("open_edit: data=" + str(person_data))

    # Vi lager Var-variabler for å holde orden på endringer brukeren gjør i GUI'et
    id = StringVar()
    name = StringVar()
    address = StringVar()
    age = IntVar()
    image_base64 = StringVar()
    
    # Hvis vi dobbeltklikket på listen fyller vi ut data'ene vi allerede har
    if person_data: 
        id.set(person_data[0])
        name.set(person_data[1])
        address.set(person_data[2])
        age.set(person_data[3])
        # Hent mulig bilde fra databasen
        b64 = person_db.get_image_base64(id.get()) 
        if b64:
            image_base64.set(b64) 
        
    # Oppretter widgets og plasserer dem i grid'en
    name_label = Label(window, text="Navn:")    
    name_label.grid(column=0, row=0, padx=2, pady=2)
    name_entry = Entry(window, textvariable=name)   
    name_entry.grid(column=1, row=0, padx=2, pady=2)
    address_label = Label(window, text="Adresse:")  
    address_label.grid(column=0, row=1, padx=2, pady=2)
    address_entry = Entry(window, textvariable=address)   
    address_entry.grid(column=1, row=1, padx=2, pady=2)
    age_label = Label(window, text="Alder:")  
    age_label.grid(column=0, row=2, padx=2, pady=2)
    age_entry = Entry(window, textvariable=age)   
    age_entry.grid(column=1, row=2, padx=2, pady=2)
    save_button = Button(window, text="Lagre", command=save)  
    save_button.grid(column=1, row=4, padx=2, pady=2)
    upload_button = Button(window, text="Last opp bilde", command=load_image)  
    upload_button.grid(column=0, row=3, padx=2, pady=2)

    # Legger til slette-knapp KUN hvis personen allerede eksisterer
    if person_data:
        delete_button = Button(window, text="Slett", command=delete)  
        delete_button.grid(column=0, row=4, padx=2, pady=2)

    # Legger til bilde, og bildedata hvis det eksisterer
    image_label = Label(window, borderwidth=2, relief="groove")
    image_label.grid(column=1, row=3)
    if image_base64.get(): # Hvis det finnes et bilde
        photo = PhotoImage(data=image_base64.get().encode('utf-8'))
        image_label.configure(image=photo)
        image_label.image = photo
