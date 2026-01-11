"""
Command-line interface for the Todo CLI application.

This module defines the CLI argument parser and command handlers
for all required subcommands.
"""
import argparse
from typing import Optional
from .todo_list import TodoList
from .task import Task
from rich.console import Console
from rich.table import Table


class TodoCLI:
    """
    Command-line interface for the Todo CLI application.
    """
    
    def __init__(self):
        """
        Initializes the CLI with a TodoList and Rich console.
        """
        self.todo_list = TodoList()
        self.console = Console()

    def run(self):
        """
        Runs the CLI application by parsing arguments and executing the appropriate command.
        """
        parser = argparse.ArgumentParser(
            prog='todo',
            description='A command-line todo application',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""Examples:
  todo add "Buy groceries" 
  todo add "Complete project" --desc "Finish the specification document"
  todo list
  todo update 1 --title "Buy groceries and cook dinner"
  todo update 1 --desc "Milk, eggs, and bread"
  todo delete 1
  todo complete 1
  todo incomplete 1"""
        )
        
        subparsers = parser.add_subparsers(dest='command', help='Available commands', required=True)

        # Add command
        add_parser = subparsers.add_parser('add', help='Add a new task')
        add_parser.add_argument('title', help='Title of the task')
        add_parser.add_argument('--desc', '--description', dest='description', default="", 
                               help='Description of the task')

        # List command
        list_parser = subparsers.add_parser('list', help='List all tasks')

        # Update command
        update_parser = subparsers.add_parser('update', help='Update an existing task')
        update_parser.add_argument('id', type=int, help='ID of the task to update')
        update_parser.add_argument('--title', help='New title for the task')
        update_parser.add_argument('--desc', '--description', dest='description', 
                                  help='New description for the task')

        # Delete command
        delete_parser = subparsers.add_parser('delete', help='Delete a task')
        delete_parser.add_argument('id', type=int, help='ID of the task to delete')

        # Complete command
        complete_parser = subparsers.add_parser('complete', help='Mark a task as complete')
        complete_parser.add_argument('id', type=int, help='ID of the task to mark complete')

        # Incomplete command
        incomplete_parser = subparsers.add_parser('incomplete', help='Mark a task as incomplete')
        incomplete_parser.add_argument('id', type=int, help='ID of the task to mark incomplete')

        args = parser.parse_args()

        # Execute the appropriate command
        if args.command == 'add':
            self.add_task(args.title, args.description)
        elif args.command == 'list':
            self.list_tasks()
        elif args.command == 'update':
            self.update_task(args.id, args.title, args.description)
        elif args.command == 'delete':
            self.delete_task(args.id)
        elif args.command == 'complete':
            self.mark_task_complete(args.id)
        elif args.command == 'incomplete':
            self.mark_task_incomplete(args.id)

    def add_task(self, title: str, description: str = ""):
        """
        Adds a new task with the given title and description.
        
        Args:
            title (str): The title of the task
            description (str): The optional description of the task
        """
        try:
            task = self.todo_list.add_task(title, description)
            self.console.print(f"[green]SUCCESS[/green] Added task '{task.title}' with ID {task.id}")
        except ValueError as e:
            self.console.print(f"[red]ERROR[/red] {str(e)}")

    def list_tasks(self):
        """
        Lists all tasks with their ID, title, description, and status indicator.
        """
        tasks = self.todo_list.get_all_tasks()
        
        if not tasks:
            self.console.print("[yellow]No tasks found[/yellow]")
            return

        table = Table(title="Todo List")
        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Status", style="magenta")
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

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None):
        """
        Updates the title and/or description of an existing task.
        
        Args:
            task_id (int): The ID of the task to update
            title (Optional[str]): The new title (if provided)
            description (Optional[str]): The new description (if provided)
        """
        success = self.todo_list.update_task(task_id, title, description)
        if success:
            self.console.print(f"[green]SUCCESS[/green] Updated task with ID {task_id}")
        else:
            self.console.print(f"[red]ERROR[/red] Task with ID {task_id} not found")

    def delete_task(self, task_id: int):
        """
        Deletes the task with the given ID.
        
        Args:
            task_id (int): The ID of the task to delete
        """
        success = self.todo_list.delete_task(task_id)
        if success:
            self.console.print(f"[green]SUCCESS[/green] Deleted task with ID {task_id}")
        else:
            self.console.print(f"[red]ERROR[/red] Task with ID {task_id} not found")

    def mark_task_complete(self, task_id: int):
        """
        Marks the task with the given ID as complete.
        
        Args:
            task_id (int): The ID of the task to mark complete
        """
        success = self.todo_list.mark_task_complete(task_id)
        if success:
            self.console.print(f"[green]SUCCESS[/green] Marked task with ID {task_id} as complete")
        else:
            self.console.print(f"[red]ERROR[/red] Task with ID {task_id} not found")

    def mark_task_incomplete(self, task_id: int):
        """
        Marks the task with the given ID as incomplete.
        
        Args:
            task_id (int): The ID of the task to mark incomplete
        """
        success = self.todo_list.mark_task_incomplete(task_id)
        if success:
            self.console.print(f"[green]SUCCESS[/green] Marked task with ID {task_id} as incomplete")
        else:
            self.console.print(f"[red]ERROR[/red] Task with ID {task_id} not found")


def main():
    """
    Main entry point for the CLI application.
    """
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()