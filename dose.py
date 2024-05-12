import tkinter as tk
from tkinter import ttk


def medoc_changed(event):
    # """ handle the month changed event """
     if selected_medoc.get()=="Augmentin":

          Animal_cb['values'] = ('Oiseau', 'Mammifère', 'Hérisson')
          Animal_label.grid(column=0, row=1, pady=20,sticky=tk.W, padx=100)
          Animal_cb.grid(row=1, column=1,sticky=tk.W, pady=20)

def Animal_changed(event):
    # """ handle the month changed event """
    print("test")
    Poids_label.grid(row=2, column=0,sticky=tk.W, pady=20, padx=100)
    ent_poids.grid(row=2, column=1,sticky=tk.W, pady=20)
    btn_calcul.grid(row=3, column=0, columnspan=2, pady=20)

def Montre_poids():

    poids = ent_poids.get()
    #celsius = (5 / 9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{poids} gr" # f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
    lbl_result.grid(row=4, column=0, columnspan=2, pady=20)
    # showinfo(
    #     title='Result',
    #     message=f'You selected {selected_medoc.get()}!'
     ##)
# root window
root = tk.Tk()
#root.geometry("240x100")
root.state('zoomed')
root.title('Login')
root.resizable(1, 1)

root['background']='#ccffee'

# configure the grid
root.columnconfigure(0, weight=1,minsize=75)
root.columnconfigure(1, weight=3, minsize=50)


# Frame 1

# frm_entry = tk.Frame(master=root)
# frm_entry.pack()

# username
username_label = ttk.Label(root, text="Choisir son médicament:",font=("Arial", 40), background="#ccffee")
username_label.grid(column=0, row=0, pady=20,sticky=tk.W, padx=100)
#username_label.grid(column=0, row=0)

# username_entry = ttk.Entry(frm_entry)
# #username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
# username_entry.grid(column=1, row=0)


# label
# label = ttk.Label(master=frm_entry, text="Choisir un medoc:")
# #label.pack(fill=tk.X, padx=5, pady=5)
# label.grid(row=0, column=0, pady=10)

selected_medoc = tk.StringVar()
medoc_cb = ttk.Combobox(master=root, textvariable=selected_medoc,width=20,font="Arial 40 bold")
medoc_cb['values'] = ('Augmentin', 'Melox', 'Dexa')
medoc_cb['state'] = 'readonly'
#medoc_cb.pack(fill=tk.X, padx=5, pady=5)
medoc_cb.grid(row=0, column=1,sticky=tk.W, pady=20)
medoc_cb.bind('<<ComboboxSelected>>', medoc_changed)
current_medoc = ""
medoc_cb.set(current_medoc)



Animal_label = ttk.Label(root, text= "Choisir un animal:" ,font=("Arial", 40), background="#ccffee")
#Animal_label.grid(column=0, row=1, pady=20,sticky=tk.W, padx=100)

selected_Animal = tk.StringVar()
Animal_cb = ttk.Combobox(master=root, textvariable=selected_Animal,width=20,font="Arial 40 bold")

Animal_cb['state'] = 'readonly'
#medoc_cb.pack(fill=tk.X, padx=5, pady=5)
#Animal_cb.grid(row=1, column=1,sticky=tk.W, pady=20)
Animal_cb.bind('<<ComboboxSelected>>', Animal_changed)
current_Animal = ""
Animal_cb.set(current_Animal)

Poids_label= ttk.Label(root, text= "Indiquer son poids:" ,font=("Arial", 40), background="#ccffee")
ent_poids = tk.Entry(master=root, width=10, font="Arial 40 bold")

btn_calcul = tk.Button(
    master=root,
    text="Calcul du volume à prélever",
    command=Montre_poids,
    width=30,
    font=("Arial", 40),
    background="#ffff33"
)

lbl_result = tk.Label(master=root, font=("Arial", 40), background="#ccffee")


root.mainloop()