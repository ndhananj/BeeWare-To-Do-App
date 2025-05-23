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
        add_button = toga.Button("Add", on_press=self.add_task, style=Pack(margin=5))
        delete_button = toga.Button("Delete", on_press=self.delete_task, style=Pack(margin=5))
        self.todo_list = toga.DetailedList(data=[], style=Pack(flex=1), on_select=self.on_select_item)

        # Layout boxes like HTML
        input_box = toga.Box(style=Pack(direction=ROW, margin=5, gap=5))
        input_box.add(self.todo_input)
        input_box.add(add_button)
        input_box.add(delete_button)

        main_box = toga.Box(style=Pack(direction=COLUMN, margin=10, gap=10))
        main_box.add(input_box)
        main_box.add(self.todo_list)

        # Set content and show
        self.main_window.content = main_box
        self.main_window.show()

    def add_task(self, widget):
        task = self.todo_input.value.strip()
        if task:
            # Create a proper dictionary for DetailedList
            task_item = {
                'title': task,
                'subtitle': '',  # Optional: Add a description or leave empty
                'icon': None     # Optional: You can provide an icon or leave as None
            }
            self.todo_list.data.append(task_item)
            self.todo_input.value = ""

    def delete_task(self, widget):
        selected = self.todo_list.selection
        if selected:
            self.todo_list.data.remove(selected)

    def on_select_item(self, widget):
        # Get the selected item directly from the widget
        selected = self.todo_list.selection
        print(f"Selected: {selected}")

def main():
    return ToDoListApp()
