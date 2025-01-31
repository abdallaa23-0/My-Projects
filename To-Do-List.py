import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

tasks = []

def show_tasks():
    for widget in task_frame.winfo_children():
        widget.destroy()
    
    for idx, (task, completed, progress) in enumerate(tasks, 1):
        status = "✓" if completed else "✗"
        task_label = tk.Label(task_frame, text=f"{idx}. {task} [{status}]", font=("Helvetica Neue", 14), bg="white")
        task_label.grid(row=idx, column=0, sticky="w", padx=10, pady=5)
        
        progress_bar = ttk.Progressbar(task_frame, length=200, mode='determinate', style="TProgressbar")
        progress_bar['value'] = progress
        progress_bar.grid(row=idx, column=1, padx=10, pady=5)
        
        progress_button = tk.Button(task_frame, text="Update Progress", command=lambda idx=idx-1: update_progress(idx), bg="#007AFF", fg="white", font=("Helvetica Neue", 12), relief="flat", bd=0)
        progress_button.grid(row=idx, column=2, padx=10, pady=5)

def add_task():
    task = task_entry.get()
    if task:
        tasks.append((task, False, 0))
        task_entry.delete(0, tk.END)
        show_tasks()
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = int(task_entry.get()) - 1
        tasks.pop(selected_task_index)
        show_tasks()
    except (IndexError, ValueError):
        messagebox.showwarning("Warning", "You must enter a valid task number to delete.")

def toggle_task_status():
    try:
        selected_task_index = int(task_entry.get()) - 1
        task, completed, progress = tasks[selected_task_index]
        tasks[selected_task_index] = (task, not completed, progress)
        show_tasks()
    except (IndexError, ValueError):
        messagebox.showwarning("Warning", "You must enter a valid task number to toggle status.")

def update_progress(index):
    progress = tasks[index][2]
    if progress < 100:
        progress += 10
        task, completed, _ = tasks[index]
        tasks[index] = (task, completed, progress)
        show_tasks()

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("To-Do List Application")
root.geometry("600x400")
root.configure(bg="white")

style = ttk.Style()
style.theme_use('clam')
style.configure("TProgressbar", thickness=10, troughcolor='white', background='#007AFF', troughrelief='flat', bordercolor='white', lightcolor='#007AFF', darkcolor='#007AFF')

frame = tk.Frame(root, bg="white")
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=40, font=("Helvetica Neue", 14), bd=0, highlightthickness=1, highlightcolor="#007AFF")
task_entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(frame, text="Add Task", command=add_task, bg="#007AFF", fg="white", font=("Helvetica Neue", 12), relief="flat", bd=0)
add_button.pack(side=tk.LEFT)

task_frame = tk.Frame(root, bg="white")
task_frame.pack(pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="#FF3B30", fg="white", font=("Helvetica Neue", 12), relief="flat", bd=0)
delete_button.pack(pady=5)

toggle_button = tk.Button(root, text="Toggle Completed", command=toggle_task_status, bg="#34C759", fg="white", font=("Helvetica Neue", 12), relief="flat", bd=0)
toggle_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=exit_app, bg="#8E8E93", fg="white", font=("Helvetica Neue", 12), relief="flat", bd=0)
exit_button.pack(pady=5)

show_tasks()

root.mainloop()