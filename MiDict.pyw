from tkinter import *
import os
import json


root = Tk()
root.title('Mi Diccionario')
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.iconphoto(False,PhotoImage(file = "icon.png"))

path = os.getcwd()
directory = os.listdir(path)

with open("data_file.json","r") as read_file:
    mydict = json.load(read_file)

def clean_entry():
    my_text.delete(0.0,"end") 

def search():
    my_text.delete(0.0,"end")
    nombre = my_entry.get()
    if nombre in mydict:
        my_text.insert(0.0,mydict[nombre].get("text"))
    else:
        my_text.insert(0.0,"No se encontro esa entrada")

def create():
    nombre = my_entry.get()
    if nombre in mydict:
        clean_entry()
        my_text.insert(0.0,"Esa entrada ya existe")
    else:
        texto = my_text.get(0.0,"end")
        entrada = dict(text = texto)
        mydict[nombre] = entrada
        with open("data_file.json","w") as write_file:
            json.dump(mydict,write_file,indent = 4)
        clean_entry()
        my_text.insert(0.0,"Entrada agregada")

def modify():
    nombre = my_entry.get()
    if nombre in mydict:
        texto = my_text.get(0.0,"end")
        entrada = dict(text = texto)
        mydict[nombre] = entrada
        with open("data_file.json","w") as write_file:
            json.dump(mydict,write_file,indent = 4)
        clean_entry()
        my_text.insert(0.0,"Entrada modificada")
    else:
        my_text.insert(0.0,"No se encontro esa entrada")

def clear():
    clean_entry()

def FP():

    def select():
        myJsonfile = fileslist.get(ANCHOR)
        # Para debug
        title.config(text=myJsonfile)
        if (myJsonfile != ""): 
            FirstPhase.destroy()
            SecondPhase.pack()

    def create_file():
        my_file = "New_file.json"
        with open(os.path.join(path, my_file), 'w') as fp:
            pass
        directory = os.listdir(path)
        fileslist.delete(0,'end')
        for files in directory:
            if files.endswith(".json"):
                fileslist.insert(END,files)

    FirstPhase = Frame(root)
    FirstPhase.pack()

    selector = Frame(FirstPhase)
    title = Label(FirstPhase,text="Seleccione que archivo va a usar, o cree uno nuevo (Despues puede cambiarle el nombre).")
    title.pack(pady=20)
    my_scrollbar = Scrollbar(selector,orient=VERTICAL)
    fileslist = Listbox(selector,width=50,yscrollcommand=my_scrollbar.set)
    my_scrollbar.config(command=fileslist.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    selector.pack()
    fileslist.pack(pady=15)
    for files in directory:
        if files.endswith(".json"):
            fileslist.insert(END,files)

    selectorbutton = Button(FirstPhase,text="Seleccionar",command=select)
    selectorbutton.pack(pady=20)
    createbutton = Button(FirstPhase,text="Crear archivo nuevo",command=create_file)
    createbutton.pack(pady=20)


FP()

SecondPhase = Frame(root)

my_label_frame = LabelFrame(SecondPhase, text="Buscador")
my_label_frame.pack(pady=20)

# Create entry box
my_entry = Entry(my_label_frame, font=("Helvetica", 18), width=47)
my_entry.pack(pady=20, padx=20)

# create text box frame
my_frame = Frame(SecondPhase)
my_frame.pack(pady=5)

# Create Vertical Scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create Text Box
my_text = Text(my_frame, yscrollcommand=text_scroll.set, wrap = WORD,font=("Helvetica", 11))
my_text.pack()

# Configure Scrollbars
text_scroll.config(command=my_text.yview)

# Button Frame
button_frame = Frame(SecondPhase)
button_frame.pack(pady=10)

# Buttons
search_button = Button(button_frame, text="Buscar", font=("Helvetica", 24), fg="#3a3a3a", command=search)
search_button.grid(row=0, column=0, padx=20)

create_button = Button(button_frame, text="Crear", font=("Helvetica", 24), fg="#3a3a3a", command=create)
create_button.grid(row=0, column=1, padx=20)

clear_button = Button(button_frame, text="Modificar", font=("Helvetica", 24), fg="#3a3a3a", command=modify)
clear_button.grid(row=0, column=2, padx=20)

clear_button = Button(button_frame, text="Limpiar", font=("Helvetica", 24), fg="#3a3a3a", command=clear)
clear_button.grid(row=0, column=3, padx=20)

root.mainloop()