import tkinter
from tkinter import *
from tkinter import messagebox
import json

def load_tasks():
        task_list.delete ( 0, tkinter.END )
        try:
            with open("tasks.json", "r") as f:
                data = json.load(f)
                for task in data:
                    text=""
                    if task["color"]== "green":
                        text="TAREA REALIZADA - "+ task["text"]
                    else:
                        text= task["text"]
                    task_list.insert(tkinter.END, text)
                    task_list.itemconfig(tkinter.END, fg=task["color"])
        except FileNotFoundError:
            pass

def save_tasks():
        data = []
        for i in range(task_list.size()):
            text = task_list.get(i)
            text = text.replace("TAREA REALIZADA - ","")
            color = task_list.itemcget(i, "fg")
            data.append({"text": text, "color": color})
        with open("tasks.json", "w") as f:
            json.dump(data, f)

def enter_data():
        new_task = new_task_txt.get()
        
        if new_task :
            task_list.insert(tkinter.END, new_task)
            task_list.itemconfig(tkinter.END, fg="black")
            new_task_txt.delete(0, tkinter.END)
            save_tasks()
        else:
            messagebox.showwarning(title="Error", message="Necesitas escribir una tarea en el campo de Nueva Tarea")

def mark_done():
        task_index = task_list.curselection()
        if task_index:
            task_list.itemconfig(task_index, fg="green")
            save_tasks()
            load_tasks()

def delete_task():
        task_index = task_list.curselection()
        if task_index:
            task_list.delete(task_index)
            save_tasks()
    

window = tkinter.Tk()
window.title("Lista de Tareas")



frame1 = tkinter.Frame(window)
frame1.pack(side="top")

new_task_label = tkinter.Label(frame1, text="Tarea Nueva")
new_task_label.pack()

new_task_txt = tkinter.Entry(frame1, width=60)
new_task_txt.pack(padx=25, side="left")

button = tkinter.Button(frame1, text="Salvar tarea", command= enter_data)
button.pack(padx=25, pady=5)

task_list_label = tkinter.Label(window, text="Tareas", font=("TkDefaultFont", 16))
task_list_label.pack(pady=10)

frame2 = tkinter.Frame(window)
frame2.pack(side="bottom")

task_list = tkinter.Listbox(window, selectbackground="light grey", height=15, font=("TkDefaultFont", 12), selectforeground="black")
task_list.pack(padx=25,pady=10, expand=True, fill=BOTH)

button = tkinter.Button(frame2, text="Tarea Realizada", command= mark_done)
button.pack(side="left", padx=20, pady=5)

button = tkinter.Button(frame2, text="Borrar Tarea", command= delete_task)
button.pack(side="right", padx=20, pady=5)


load_tasks()
window.mainloop()