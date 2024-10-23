import tkinter as tk
from tkinter import messagebox
import os

# Load tasks from file
def load_tasks():
    if not os.path.exists('tasks.txt'):
        return []
    with open('tasks.txt', 'r') as file:
        tasks = [line.strip().split(';') for line in file.readlines()]
        return [{'task': task[0], 'completed': task[1] == 'True'} for task in tasks]

# Save tasks to file
def save_tasks(tasks):
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(f"{task['task']};{task['completed']}\n")

# Add a new task to the list
def add_task():
    task = entry_task.get().strip()
    if task:
        tasks.append({'task': task, 'completed': False})
        update_task_list()
        entry_task.delete(0, tk.END)
        save_tasks(tasks)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Update the task list in the GUI
def update_task_list():
    listbox_tasks.delete(0, tk.END)
    for i, task in enumerate(tasks):
        task_text = f"{task['task']} (✓)" if task['completed'] else task['task']
        listbox_tasks.insert(tk.END, task_text)

# Mark the selected task as complete
def complete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        tasks[selected_task_index]['completed'] = True
        update_task_list()
        save_tasks(tasks)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as complete.")

# Remove the selected task
def remove_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        del tasks[selected_task_index]
        update_task_list()
        save_tasks(tasks)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

# UI Setup
root = tk.Tk()
root.title("To-Do List")

# Frame for task entry
frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

entry_task = tk.Entry(frame_tasks, width=40)
entry_task.pack(side=tk.LEFT, padx=10)
button_add_task = tk.Button(frame_tasks, text="Add Task", command=add_task)
button_add_task.pack(side=tk.LEFT)

# Listbox to display tasks
listbox_tasks = tk.Listbox(root, width=50, height=10)
listbox_tasks.pack(pady=10)

# Frame for action buttons
frame_actions = tk.Frame(root)
frame_actions.pack(pady=10)

button_complete_task = tk.Button(frame_actions, text="Mark Complete", command=complete_task)
button_complete_task.pack(side=tk.LEFT, padx=10)

button_remove_task = tk.Button(frame_actions, text="Remove Task", command=remove_task)
button_remove_task.pack(side=tk.LEFT)

# Load tasks at startup
tasks = load_tasks()
update_task_list()

# Start the GUI loop
root.mainloop()
