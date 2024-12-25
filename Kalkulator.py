import tkinter as tk
def kalkulator():
    prv_broj = (entry1.get())
    znak = entry2.get()
    vtor_broj = (entry3.get())
    zadaca = prv_broj + " " + znak + " " + vtor_broj
    presmetka = eval(zadaca)
    label4.config(text=f"Resultat: {presmetka}")
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)



screen = tk.Tk()
screen.geometry("200x200")

label1 = tk.Label(text="prv broj: ")
label1.grid(row=0,column=0)
label2 = tk.Label(text="znak: ")
label2.grid(row=1,column=0)
label3 = tk.Label(text="vtor broj: ")
label3.grid(row=2,column=0)
entry1 = tk.Entry()
entry1.grid(row=0,column=1)
entry2 = tk.Entry()
entry2.grid(row=1,column=1)
entry3 = tk.Entry()
entry3.grid(row=2,column=1)
button1 = tk.Button(text="click",command=kalkulator)
button1.grid(row=3,column=0)
label4 = tk.Label(screen, text="Resultat: ")
label4.grid(row=4, column=0, columnspan=2)
screen.mainloop()
