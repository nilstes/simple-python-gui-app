from tkinter import *
import person_edit
import person_db
import person_statistics

# Oppretter liste for søkeresultatet
result = []

# Definerer aksjon for personsøket
def search():
    result_listbox.delete(0, END)
    result.clear()
    db_result = person_db.search(name.get(), address.get())
    for element in db_result:
        result.append(element)
        result_listbox.insert(END, element[1])
       
# Definerer aksjon for menyvalget "Opprett Ny Person"
def new_person():
    person_edit.open_edit(root, search)

# Definerer aksjon for menyvalget "Vis aldersdistribusjon"
def view_address_statistics():
    counts, adresses = person_db.get_adress_counts()
    person_statistics.show_bar_chart(counts, adresses, "Adresse", "Antall")

# Definerer aksjon for menyvalget "Vis aldersdistribusjon"
def view_age_statistics():
    ages = person_db.get_ages()
    person_statistics.show_histogram(ages, 0, 120, 24, "Alder", "Antall")

# Definerer aksjon for dobbeltklikk på en person i lista
def edit_person(event):
    person_edit.open_edit(root, search, result[result_listbox.curselection()[0]])

# Opprett hovedvindu
root = Tk()

# Oppretter en ledetekster
name_label = Label(root, text="Navn:")
address_label = Label(root, text="Adresse:")

# Oppretter tekstfelter brukeren kan søke fra
name = StringVar()  # Definerer en tekstvariabel for tekstfeltet 
name_entry = Entry(root, textvariable=name)
address = StringVar()  # Definerer en tekstvariabel for tekstfeltet 
address_entry = Entry(root, textvariable=address)

# Oppretter en knapp med teksten "Søk", som kaller funksjonen search() ved trykk
search_button = Button(root, text="Søk", command=search)  

# Oppretter listeboks med scrollbar for søkeresultat
scrollbar = Scrollbar(root, orient=VERTICAL)
result_listbox = Listbox(root, yscrollcommand=scrollbar.set)
scrollbar.config(command=result_listbox.yview)
result_listbox.bind('<Double-Button-1>', edit_person)

# Plasserer widget'ene i vinduet i et rutenett (grid)
name_label.grid(column=0, row=0, padx=2, pady=2)
name_entry.grid(column=1, row=0, padx=2, pady=2)
address_label.grid(column=2, row=0, padx=2, pady=2)
address_entry.grid(column=3, row=0, padx=2, pady=2)
search_button.grid(column=4, row=0, columnspan=2, padx=2, pady=2)
result_listbox.grid(column=0, row=1, columnspan=5, rowspan=10, sticky=EW)
scrollbar.grid(column=5, row=1, rowspan=10, sticky=NS)

# Lag meny
menubar = Menu(root)
personMenu = Menu(menubar, tearoff=0)
personMenu.add_command(label="Registrer ny", command=new_person)
statisticsMenu = Menu(menubar, tearoff=0)
statisticsMenu.add_command(label="Se adressedistribusjon", command=view_address_statistics)
statisticsMenu.add_command(label="Se aldersdistribusjon", command=view_age_statistics)
menubar.add_cascade(label="Person", menu=personMenu)
menubar.add_cascade(label="Statistikk", menu=statisticsMenu)
root.config(menu=menubar)

# Søk på data for å fylle listen
search()

# Starter GUI'et
root.mainloop()
