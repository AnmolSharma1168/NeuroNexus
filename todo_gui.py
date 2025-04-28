import tkinter as tk
from tkinter import messagebox
import json

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task():
    task = entry.get()
    if task:
        tasks.append({"title": task, "completed": False})
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks(tasks)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")


def complete_task():
    try:
        selected_index = listbox.curselection()[0]
        tasks[selected_index]["completed"] = True
        listbox.itemconfig(selected_index, {'fg': 'green'})
        save_tasks(tasks)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as complete.")


def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
        tasks.pop(selected_index)
        save_tasks(tasks)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")

entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady = 20)

add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

complete_button = tk.Button(root, text="Mark as Complete", width=20, command=complete_task)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_button.pack(pady=5)

listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 12))
listbox.pack(pady=20)

tasks = load_tasks()
for task in tasks:
    listbox.insert(tk.END, task['title'])
    if task['completed']:
        idx = tasks.index(task)
        listbox.itemconfig(idx, {'fg': 'green'})

root.mainloop()
