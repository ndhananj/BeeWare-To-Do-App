"""
A simple to-do list application
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class ToDoListApp(toga.App):
    def startup(self):
        # Main window
        self.main_window = toga.MainWindow(title=self.formal_name)

        # Widgets
        self.todo_input = toga.TextInput(placeholder="Enter task", style=Pack(flex=1))
        add_button = toga.Button("Add", on_press=self.add_task, style=Pack(padding=5))
        delete_button = toga.Button("Delete", on_press=self.delete_task, style=Pack(padding=5))
        self.todo_list = toga.DetailedList(data=[], style=Pack(flex=1),on_select=self.on_select_item)

        # Layout boxes like HTML
        input_box = toga.Box(style=Pack(direction=ROW, padding=5, gap=5))
        input_box.add(self.todo_input)
        input_box.add(add_button)
        input_box.add(delete_button)

        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10, gap=10))
        main_box.add(input_box)
        main_box.add(self.todo_list)

        # Set content and show
        self.main_window.content = main_box
        self.main_window.show()

    def add_task(self, widget):
        task = self.todo_input.value.strip()
        if task:
            self.todo_list.data.append(task)
            self.todo_input.value = ""

    def delete_task(self, widget):
        selected = self.todo_list.value
        if selected:
            self.todo_list.data.remove(selected)

    def on_select_item(self, widget, row):
        # Handle selection if needed
        pass

def main():
    return ToDoListApp()
