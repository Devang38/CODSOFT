import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.task_entry = tk.Entry(root)
        self.task_entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.tasks_listbox = tk.Listbox(root)
        self.tasks_listbox.pack()

        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def complete_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            self.tasks_listbox.delete(selected_index)

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()