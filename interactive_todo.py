"""
Interactive command-line interface for the Todo CLI application.

This module provides an interactive menu-driven interface for managing tasks.
"""
import argparse
from typing import Optional
from src.todo.todo_list import TodoList
from src.todo.task import Task
from rich.console import Console
from rich.table import Table


class InteractiveTodoCLI:
    """
    Interactive command-line interface for the Todo CLI application.
    """
    
    def __init__(self):
        """
        Initializes the interactive CLI with a TodoList and Rich console.
        """
        self.todo_list = TodoList()
        self.console = Console()

    def display_menu(self):
        """
        Displays the main menu options.
        """
        self.console.print("\n[bold cyan]Todo CLI Application[/bold cyan]")
        self.console.print("1. Add Task")
        self.console.print("2. List Tasks")
        self.console.print("3. Update Task")
        self.console.print("4. Delete Task")
        self.console.print("5. Mark Task Complete")
        self.console.print("6. Mark Task Incomplete")
        self.console.print("7. Exit")
        self.console.print("-" * 30)

    def add_task_interactive(self):
        """
        Interactive method to add a new task.
        """
        try:
            title = input("Enter task title: ").strip()
            if not title:
                self.console.print("[red]ERROR[/red] Task title cannot be empty")
                return

            description = input("Enter task description (optional, press Enter to skip): ").strip()
            
            task = self.todo_list.add_task(title, description)
            self.console.print(f"[green]SUCCESS[/green] Added task '{task.title}' with ID {task.id}")
        except ValueError as e:
            self.console.print(f"[red]ERROR[/red] {str(e)}")

    def list_tasks_interactive(self):
        """
        Interactive method to list all tasks.
        """
        tasks = self.todo_list.get_all_tasks()
        
        if not tasks:
            self.console.print("[yellow]No tasks found[/yellow]")
            return

        table = Table(title="Todo List")
        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Status", style="red",)
        table.add_column("Title", style="green")
        table.add_column("Description", style="blue")

        for task in tasks:
            status = "[x]" if task.completed else "[ ]"
            description = task.description if task.description else "[italic]No description[/italic]"
            table.add_row(
                str(task.id),
                status,
                task.title,
                description
            )

        self.console.print(table)

    def update_task_interactive(self):
        """
        Interactive method to update an existing task.
        """
        if not self.todo_list.get_all_tasks():
            self.console.print("[yellow]No tasks available to update[/yellow]")
            return

        self.list_tasks_interactive()
        try:
            task_id = int(input("Enter the ID of the task to update: "))
        except ValueError:
            self.console.print("[red]ERROR[/red] Invalid ID. Please enter a number.")
            return

        # Get current task details
        current_task = self.todo_list.get_task_by_id(task_id)
        if not current_task:
            self.console.print(f"[red]ERROR[/red] Task with ID {task_id} not found")
            return

        # Get new title (or keep current)
        new_title = input(f"Enter new title (current: '{current_task.title}', press Enter to keep current): ").strip()
        if not new_title:
            new_title = None  # Will keep the current title

        # Get new description (or keep current)
        new_desc = input(f"Enter new description (current: '{current_task.description}', press Enter to keep current): ").strip()
        if not new_desc:
            new_desc = None  # Will keep the current description

        success = self.todo_list.update_task(task_id, new_title, new_desc)
        if success:
            self.console.print(f"[green]SUCCESS[/green] Updated task with ID {task_id}")
        else:
            self.console.print(f"[red]ERROR[/red] Failed to update task with ID {task_id}")

    def delete_task_interactive(self):
        """
        Interactive method to delete a task.
        """
        if not self.todo_list.get_all_tasks():
            self.console.print("[yellow]No tasks available to delete[/yellow]")
            return

        self.list_tasks_interactive()
        try:
            task_id = int(input("Enter the ID of the task to delete: "))
        except ValueError:
            self.console.print("[red]ERROR[/red] Invalid ID. Please enter a number.")
            return

        success = self.todo_list.delete_task(task_id)
        if success:
            self.console.print(f"[green]SUCCESS[/green] Deleted task with ID {task_id}")
        else:
            self.console.print(f"[red]ERROR[/red] Task with ID {task_id} not found")

    def mark_task_complete_interactive(self):
        """
        Interactive method to mark a task as complete.
        """
        if not self.todo_list.get_all_tasks():
            self.console.print("[yellow]No tasks available[/yellow]")
            return

        self.list_tasks_interactive()
        try:
            task_id = int(input("Enter the ID of the task to mark complete: "))
        except ValueError:
            self.console.print("[red]ERROR[/red] Invalid ID. Please enter a number.")
            return

        success = self.todo_list.mark_task_complete(task_id)
        if success:
            self.console.print(f"[green]SUCCESS[/green] Marked task with ID {task_id} as complete")
        else:
            self.console.print(f"[red]ERROR[/red] Task with ID {task_id} not found")

    def mark_task_incomplete_interactive(self):
        """
        Interactive method to mark a task as incomplete.
        """
        if not self.todo_list.get_all_tasks():
            self.console.print("[yellow]No tasks available[/yellow]")
            return

        self.list_tasks_interactive()
        try:
            task_id = int(input("Enter the ID of the task to mark incomplete: "))
        except ValueError:
            self.console.print("[red]ERROR[/red] Invalid ID. Please enter a number.")
            return

        success = self.todo_list.mark_task_incomplete(task_id)
        if success:
            self.console.print(f"[green]SUCCESS[/green] Marked task with ID {task_id} as incomplete")
        else:
            self.console.print(f"[red]ERROR[/red] Task with ID {task_id} not found")

    def run_interactive(self):
        """
        Runs the interactive CLI application.
        """
        while True:
            self.display_menu()
            choice = input("Select an option (1-7): ").strip()

            if choice == "1":
                self.add_task_interactive()
            elif choice == "2":
                self.list_tasks_interactive()
            elif choice == "3":
                self.update_task_interactive()
            elif choice == "4":
                self.delete_task_interactive()
            elif choice == "5":
                self.mark_task_complete_interactive()
            elif choice == "6":
                self.mark_task_incomplete_interactive()
            elif choice == "7":
                self.console.print("[bold green]Goodbye![/bold green]")
                break
            else:
                self.console.print("[red]ERROR[/red] Invalid option. Please select 1-7.")


def main():
    """
    Main entry point for the interactive CLI application.
    """
    cli = InteractiveTodoCLI()
    cli.run_interactive()


if __name__ == "__main__":
    main()