import tkinter as tk
from tkinter import messagebox

class Task:
    def _init_(self, task, priority):
        self.task = task
        self.priority = priority

    def _lt_(self, other):
        return self.priority < other.priority

class Heap:
    def _init_(self):
        self.tasks = []

    def push(self, task):
        self.tasks.append(task)
        self._heapify_up()

    def pop(self):
        if not self.tasks:
            return None
        if len(self.tasks) == 1:
            return self.tasks.pop()
        top_task = self.tasks[0]
        self.tasks[0] = self.tasks.pop()
        self._heapify_down()
        return top_task

    def _heapify_up(self):
        current_index = len(self.tasks) - 1
        while current_index > 0:
            parent_index = (current_index - 1) // 2
            if self.tasks[current_index] < self.tasks[parent_index]:
                self.tasks[current_index], self.tasks[parent_index] = (
                    self.tasks[parent_index],
                    self.tasks[current_index],
                )
                current_index = parent_index
            else:
                break

    def _heapify_down(self):
        current_index = 0
        while True:
            left_child_index = 2 * current_index + 1
            right_child_index = 2 * current_index + 2
            smallest_child_index = current_index

            if (
                left_child_index < len(self.tasks)
                and self.tasks[left_child_index] < self.tasks[smallest_child_index]
            ):
                smallest_child_index = left_child_index

            if (
                right_child_index < len(self.tasks)
                and self.tasks[right_child_index] < self.tasks[smallest_child_index]
            ):
                smallest_child_index = right_child_index

            if smallest_child_index != current_index:
                self.tasks[current_index], self.tasks[smallest_child_index] = (
                    self.tasks[smallest_child_index],
                    self.tasks[current_index],
                )
                current_index = smallest_child_index
            else:
                break

class Scheduler:
    def _init_(self):
        self.tasks_heap = Heap()

    def add_task(self, task, priority):
        self.tasks_heap.push(Task(task, priority))

    def complete_task(self):
        top_task = self.tasks_heap.pop()
        if top_task:
            messagebox.showinfo('Task Completed', top_task.task)
        else:
            messagebox.showinfo('No Tasks', 'No tasks to complete.')

    def display_tasks(self):
        tasks_info = "\n".join(
            [f"Priority: {task.priority}, Task: {task.task}" for task in self.tasks_heap.tasks]
        )
        if not tasks_info:
            messagebox.showinfo('No Tasks', 'No tasks available.')
        else:
            messagebox.showinfo('Tasks', f'Tasks:\n{tasks_info}')

def add_task_window():
    add_task_win = tk.Toplevel(root)
    add_task_win.title('Add Task')
    add_task_win.geometry('300x150')
    add_task_win.configure(bg='#F0F0F0')  # Light gray background

    tk.Label(add_task_win, text='Task:', font=('Arial', 12), bg='#F0F0F0').pack()
    task_entry = tk.Entry(add_task_win, font=('Arial', 12))
    task_entry.pack()

    tk.Label(add_task_win, text='Priority:', font=('Arial', 12), bg='#F0F0F0').pack()
    priority_entry = tk.Entry(add_task_win, font=('Arial', 12))
    priority_entry.pack()

    def submit():
        scheduler.add_task(task_entry.get(), int(priority_entry.get()))
        add_task_win.destroy()

    submit_button = tk.Button(add_task_win, text='Submit', command=submit, font=('Arial', 12), bg='#4CAF50', fg='#FFFFFF')  # Green button
    submit_button.pack()

def complete_task_window():
    scheduler.complete_task()

def display_tasks_window():
    scheduler.display_tasks()

root = tk.Tk()
root.title('Heap-based Task Scheduler')
root.geometry('400x300')
root.configure(bg='#E0E0E0')  # Light gray background

scheduler = Scheduler()

add_task_button = tk.Button(root, text='Add Task', command=add_task_window, font=('Arial', 12), bg='#2196F3', fg='#FFFFFF')  # Blue button
add_task_button.pack(pady=10)

complete_task_button = tk.Button(root, text='Complete Task', command=complete_task_window, font=('Arial', 12), bg='#FF9800', fg='#FFFFFF')  # Orange button
complete_task_button.pack(pady=10)

display_tasks_button = tk.Button(root, text='Display Tasks', command=display_tasks_window, font=('Arial', 12), bg='#795548', fg='#FFFFFF')  # Brown button
display_tasks_button.pack(pady=10)

root.mainloop()
