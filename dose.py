import tkinter as tk
from tkinter import ttk


def medoc_changed(event):
     if selected_medoc.get()=="Augmentin":

          animal_dropdown['values'] = ('Oiseau', 'Mammifère', 'Hérisson')
          animal_label.grid(column=0, row=1, pady=20,sticky=tk.W, padx=100)
          animal_dropdown.grid(row=1, column=1,sticky=tk.W, pady=20)

def Animal_changed(event):

    poids_label.grid(row=2, column=0,sticky=tk.W, pady=20, padx=100)
    poids_entry.grid(row=2, column=1,sticky=tk.W, pady=20)
    calcul_btn.grid(row=3, column=0, columnspan=2, pady=20)

def calcul_dose():

    poids = poids_entry.get()
    resultat_label["text"] = f"{poids} gr" 
    resultat_label.grid(row=4, column=0, columnspan=2, pady=20)


window = tk.Tk()
window.state('zoomed')
window.title('Login')
window.resizable(1, 1)
window['background']='#ccffee'
window.columnconfigure(0, weight=1,minsize=75)
window.columnconfigure(1, weight=3, minsize=50)


# Ligne 1

medoc_label = ttk.Label(window, text="Choisir son médicament:",font=("Arial", 40), background="#ccffee")
medoc_label.grid(column=0, row=0, pady=20,sticky=tk.W, padx=100)

selected_medoc = tk.StringVar()
medoc_dropdown = ttk.Combobox(master=window, textvariable=selected_medoc,width=20,font="Arial 40 bold")
medoc_dropdown['values'] = ('Augmentin', 'Melox', 'Dexa')
medoc_dropdown['state'] = 'readonly'
medoc_dropdown.grid(row=0, column=1,sticky=tk.W, pady=20)
medoc_dropdown.bind('<<ComboboxSelected>>', medoc_changed)
current_medoc = ""
medoc_dropdown.set(current_medoc)

# Ligne 2
animal_label = ttk.Label(window, text= "Choisir un animal:" ,font=("Arial", 40), background="#ccffee")

selected_Animal = tk.StringVar()
animal_dropdown = ttk.Combobox(master=window, textvariable=selected_Animal,width=20,font="Arial 40 bold")

animal_dropdown['state'] = 'readonly'
animal_dropdown.bind('<<ComboboxSelected>>', Animal_changed)
current_Animal = ""
animal_dropdown.set(current_Animal)

poids_label= ttk.Label(window, text= "Indiquer son poids:" ,font=("Arial", 40), background="#ccffee")
poids_entry = tk.Entry(master=window, width=10, font="Arial 40 bold")

calcul_btn = tk.Button(
    master=window,
    text="Calcul du volume à prélever",
    command=calcul_dose,
    width=30,
    font=("Arial", 40),
    background="#ffff33"
)

resultat_label = tk.Label(master=window, font=("Arial", 40), background="#ccffee")


window.mainloop()