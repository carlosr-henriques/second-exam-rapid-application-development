from tkinter import *
import backend as bck

tupla_selecionada = None

def get_selecionado(event):
    global tupla_selecionada
    index = lista.curselection()[0]
    tupla_selecionada = lista.get(index)
    entrada_nome.insert(END, tupla_selecionada[1])
    entrada_matricula.insert(END, tupla_selecionada[2])
    entrada_email.insert(END, tupla_selecionada[3])
    entrada_endereco.insert(END, tupla_selecionada[4])
    entrada_campus.insert(END, tupla_selecionada[5])
    entrada_periodo.insert(END, tupla_selecionada[6])
    entrada_av1.insert(END, tupla_selecionada[7])
    entrada_av2.insert(END, tupla_selecionada[8])
    entrada_av3.insert(END, tupla_selecionada[9])
    entrada_avd.insert(END, tupla_selecionada[10])
    entrada_avds.insert(END, tupla_selecionada[11])

def incluir():
    bck.insert(txtNome.get(), nmrMatricula.get(), txtEmail.get(), txtEndereco.get(), txtCampus.get(), txtPeriodo.get(), nmrAv1.get(), nmrAv2.get(), nmrAv3.get(), nmrAvd.get(), nmrAvds.get())
    lista.delete(0, END)
    lista.insert(txtNome.get(), nmrMatricula.get(), txtEmail.get(), txtEndereco.get(), txtCampus.get(), txtPeriodo.get(), nmrAv1.get(), nmrAv2.get(), nmrAv3.get(), nmrAvd.get(), nmrAvds.get())
    entrada_nome.delete(0, END)
    entrada_matricula.delete(0, END)
    entrada_email.delete(0, END)
    entrada_endereco.delete(0, END)
    entrada_campus.delete(0, END)
    entrada_periodo.delete(0, END)
    entrada_av1.delete(0, END)
    entrada_av2.delete(0, END)
    entrada_av3.delete(0, END)
    entrada_avd.delete(0, END)
    entrada_avds.delete(0, END)
    exibir()

    
def exibir():
    lista.delete(0, END)
    for linha in bck.view(nmrMatricula.get()):
        lista.insert(0, linha)
        
        
root = Tk()
root.title("Painel de acesso")
width = 800
height = 500
sc_width = root.winfo_screenwidth()
sc_height = root.winfo_screenheight()
x = (sc_width/2) - (width/2)
y = (sc_height/2) - (height/2)
root.geometry("%dx%d+%d+%d"%(width, height, x, y))
root.configure(background="#D72323")
root.resizable(0, 0)
frame = Frame(root)

#logo = PhotoImage(file="logo.png")

#leftframe = Frame(root, width=200, height=500, background="#EEEEEE", relief="raise")
#leftframe.pack(side=LEFT)

#rightframe = Frame(root, width=650, height=500, background="#D72323", relief="raise")
#rightframe.pack(side=RIGHT)

#label = Label(frame, text="Bem-vindo")
#label.pack()

#logo_label = Label(leftframe, image=logo, background="#EEEEEE")
#logo_label.place(x=0, y=100)

label_nome = Label(root, text="Nome", bg='#D72323', fg="#EEEEEE")
label_nome.grid(row=0, column=0)
label_matricula = Label(root, text="Matrícula", bg='#D72323', fg="#EEEEEE")
label_matricula.grid(row=1, column=0)
label_email = Label(root, text="Email", bg='#D72323', fg="#EEEEEE")
label_email.grid(row=2, column=0)
label_endereco = Label(root, text="Endereço", bg='#D72323', fg="#EEEEEE")
label_endereco.grid(row=3, column=0)
label_campus = Label(root, text="Campus", bg='#D72323', fg="#EEEEEE")
label_campus.grid(row=0, column=2)
label_periodo = Label(root, text="PerÍodo", bg='#D72323', fg="#EEEEEE")
label_periodo.grid(row=1, column=2)
label_av1 = Label(root, text="AV1", bg='#D72323', fg="#EEEEEE")
label_av1.grid(row=2, column=2)
label_av2 = Label(root, text="AV2", bg='#D72323', fg="#EEEEEE")
label_av2.grid(row=3, column=2)
label_av3 = Label(root, text="AV3", bg='#D72323', fg="#EEEEEE")
label_av3.grid(row=0, column=4)
label_avd = Label(root, text="AVD", bg='#D72323', fg="#EEEEEE")
label_avd.grid(row=1, column=4)
label_avds = Label(root, text="AVDS", bg='#D72323', fg="#EEEEEE")
label_avds.grid(row=2, column=4)

txtNome         = StringVar()
nmrMatricula    = IntVar()
txtEmail        = StringVar()
txtEndereco     = StringVar()
txtCampus       = StringVar()
txtPeriodo      = StringVar()
nmrAv1          = DoubleVar()
nmrAv2          = DoubleVar()
nmrAv3          = DoubleVar()
nmrAvd          = DoubleVar()
nmrAvds         = DoubleVar()

entrada_nome = Entry(root,  textvariable=txtNome)
entrada_nome.grid(row=0, column=1)
entrada_matricula = Entry(root,  textvariable=nmrMatricula)
entrada_matricula.grid(row=1, column=1)
entrada_email = Entry(root,  textvariable=txtEmail)
entrada_email.grid(row=2, column=1)
entrada_endereco = Entry(root,  textvariable=txtEndereco)
entrada_endereco.grid(row=3, column=1)
entrada_campus = Entry(root,  textvariable=txtCampus)
entrada_campus.grid(row=0, column=3)
entrada_periodo = Entry(root,  textvariable=txtPeriodo)
entrada_periodo.grid(row=1, column=3)
entrada_av1 = Entry(root,  textvariable=nmrAv1)
entrada_av1.grid(row=2, column=3)
entrada_av2 = Entry(root,  textvariable=nmrAv2)
entrada_av2.grid(row=3, column=3)
entrada_av3 = Entry(root,  textvariable=nmrAv3)
entrada_av3.grid(row=0, column=5)
entrada_avd = Entry(root,  textvariable=nmrAvd)
entrada_avd.grid(row=1, column=5)
entrada_avds = Entry(root,  textvariable=nmrAvds)
entrada_avds.grid(row=2, column=5)

lista = Listbox(root, height=8, width=60)
lista.grid(row=6, column=0, rowspan=6, columnspan=2)

sb = Scrollbar(root)
sb.grid(row=6, column=2, rowspan=6)

lista.configure(yscrollcommand=sb.set)
sb.configure(command=lista.yview)

lista.bind("<<ListboxSelect>>", get_selecionado)


b1 = Button(root, text="Cadastrar", width=22, bg="#F0ECE3", command=incluir)
b1.grid(row=6, column=5)
b2 = Button(root, text="Exibir", width=22, bg="#C7B198", command=exibir)
b2.grid(row=7, column=5)
b3 = Button(root, text="Fechar", width=22, bg="#596E79", command=root.destroy)
b3.grid(row=8, column=5)


root.mainloop()