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

    def _parse_recurrence_string(self, recurrence_str: str):
        """
        Parses a recurrence string into a recurrence dictionary.

        Args:
            recurrence_str (str): String in format like 'daily', 'weekly:friday', 'monthly:15', 'yearly'

        Returns:
            dict: Recurrence pattern dictionary
        """
        parts = recurrence_str.split(':')
        recurrence_type = parts[0].lower()

        if recurrence_type not in ['daily', 'weekly', 'monthly', 'yearly']:
            raise ValueError(f"Invalid recurrence type: {recurrence_type}. Must be one of: daily, weekly, monthly, yearly")

        recurrence_dict = {'type': recurrence_type}

        if recurrence_type == 'weekly':
            if len(parts) < 2:
                raise ValueError("Weekly recurrence must specify a weekday (e.g., 'weekly:friday')")
            weekday = parts[1].lower()
            valid_weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
            if weekday not in valid_weekdays:
                raise ValueError(f"Invalid weekday: {weekday}. Must be one of: {', '.join(valid_weekdays)}")
            recurrence_dict['weekday'] = weekday
        elif recurrence_type == 'monthly':
            if len(parts) < 2:
                raise ValueError("Monthly recurrence must specify a day (e.g., 'monthly:15')")
            try:
                day = int(parts[1])
                if day < 1 or day > 31:
                    raise ValueError(f"Invalid day for monthly recurrence: {day}. Must be between 1 and 31")
            except ValueError as e:
                if "invalid literal" in str(e):
                    raise ValueError(f"Invalid day for monthly recurrence: {parts[1]}. Must be a number between 1 and 31")
                else:
                    raise e

        return recurrence_dict

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
        self.console.print("7. Search Tasks")
        self.console.print("8. Filter Tasks")
        self.console.print("9. Exit")
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

            # Get priority
            priority_input = input("Enter priority (high/medium/low or press Enter for none): ").strip().lower()
            priority = None
            if priority_input in ["high", "medium", "low"]:
                priority = priority_input
            elif priority_input and priority_input != "none":
                self.console.print(f"[red]ERROR[/red] Invalid priority value: {priority_input}. Must be high, medium, or low.")
                return

            # Get tags
            tags_input = input("Enter tags (comma-separated, e.g., work,urgent or press Enter for none): ").strip()
            tags = []
            if tags_input:
                tags = [tag.strip() for tag in tags_input.split(",")]

            # Get due date
            due_date_input = input("Enter due date (YYYY-MM-DD, relative like 'tomorrow', 'next friday', or press Enter for none): ").strip()
            due_datetime = None
            if due_date_input:
                try:
                    from src.todo.utils import parse_date_string
                    due_datetime = parse_date_string(due_date_input)
                except ValueError as e:
                    self.console.print(f"[red]ERROR[/red] Invalid due date format: {str(e)}")
                    return

            # Get recurrence
            recurrence_input = input("Enter recurrence (daily, weekly:weekday, monthly:day, yearly, or press Enter for none): ").strip().lower()
            recurrence = None
            if recurrence_input:
                try:
                    recurrence = self._parse_recurrence_string(recurrence_input)
                except ValueError as e:
                    self.console.print(f"[red]ERROR[/red] Invalid recurrence format: {str(e)}")
                    return

            task = self.todo_list.add_task(title, description, priority, tags, due_datetime, recurrence)
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
        table.add_column("Due Date", style="magenta")
        table.add_column("Priority", style="yellow")
        table.add_column("Tags", style="blue")
        table.add_column("Status", style="red")
        table.add_column("Title", style="green")
        table.add_column("Description", style="dim")

        for task in tasks:
            # Format due date
            due_date_str = ""
            if task.due_datetime:
                # Check if overdue
                from datetime import datetime
                if not task.completed and task.due_datetime < datetime.now():
                    due_date_str = f"[red]{task.due_datetime.strftime('%Y-%m-%d %H:%M')}[/red] [bold red]OVERDUE[/bold red]"
                else:
                    due_date_str = task.due_datetime.strftime('%Y-%m-%d %H:%M')

            # Format priority indicator
            priority_indicator = ""
            if task.priority == "high":
                priority_indicator = "[H]"
            elif task.priority == "medium":
                priority_indicator = "[M]"
            elif task.priority == "low":
                priority_indicator = "[L]"
            elif task.priority is None:
                priority_indicator = "[N]"

            # Format tags
            tags_str = " ".join([f"#{tag}" for tag in task.tags]) if task.tags else ""

            # Format status
            status = "[x]" if task.completed else "[ ]"

            description = task.description if task.description else "[italic]No description[/italic]"

            table.add_row(
                str(task.id),
                due_date_str,
                priority_indicator,
                tags_str,
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

        # Get new priority (or keep current)
        new_priority_input = input(f"Enter new priority (current: '{current_task.priority}', high/medium/low/none, press Enter to keep current): ").strip().lower()
        new_priority = current_task.priority  # Default to current priority
        if new_priority_input == "none":
            new_priority = None
        elif new_priority_input in ["high", "medium", "low"]:
            new_priority = new_priority_input
        elif new_priority_input:  # If user entered something but it's not valid
            self.console.print(f"[red]ERROR[/red] Invalid priority value: {new_priority_input}. Must be high, medium, low, or none.")
            return

        # Get new tags (or keep current)
        new_tags_input = input(f"Enter new tags (current: '{', '.join(current_task.tags) if current_task.tags else 'none'}, comma-separated, press Enter to keep current): ").strip()
        new_tags = current_task.tags[:]  # Default to current tags
        if new_tags_input:  # If user entered new tags
            new_tags = [tag.strip() for tag in new_tags_input.split(",")]

        # Get new due date (or keep current)
        current_due_date = current_task.due_datetime.strftime('%Y-%m-%d %H:%M') if current_task.due_datetime else 'none'
        new_due_date_input = input(f"Enter new due date (current: '{current_due_date}', format: YYYY-MM-DD or relative like 'tomorrow', press Enter to keep current): ").strip()
        new_due_datetime = current_task.due_datetime  # Default to current due date
        if new_due_date_input:  # If user entered a new due date
            if new_due_date_input.lower() == 'none' or new_due_date_input.lower() == '':
                new_due_datetime = None
            else:
                try:
                    from src.todo.utils import parse_date_string
                    new_due_datetime = parse_date_string(new_due_date_input)
                except ValueError as e:
                    self.console.print(f"[red]ERROR[/red] Invalid due date format: {str(e)}")
                    return

        success = self.todo_list.update_task(task_id, new_title, new_desc, new_priority, new_tags, new_due_datetime)
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

    def search_tasks_interactive(self):
        """
        Interactive method to search tasks by keyword.
        """
        if not self.todo_list.get_all_tasks():
            self.console.print("[yellow]No tasks available to search[/yellow]")
            return

        keyword = input("Enter search keyword (to search in title or description): ").strip()
        if not keyword:
            self.console.print("[yellow]No keyword provided, showing all tasks[/yellow]")
            self.list_tasks_interactive()
            return

        tasks = self.todo_list.search_tasks(keyword)
        
        if not tasks:
            self.console.print("[yellow]No tasks match your search criteria[/yellow]")
            return

        table = Table(title=f"Search Results for '{keyword}'")
        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Priority", style="magenta")
        table.add_column("Tags", style="blue")
        table.add_column("Status", style="red")
        table.add_column("Title", style="green")
        table.add_column("Description", style="dim")

        for task in tasks:
            # Format priority indicator
            priority_indicator = ""
            if task.priority == "high":
                priority_indicator = "[H]"
            elif task.priority == "medium":
                priority_indicator = "[M]"
            elif task.priority == "low":
                priority_indicator = "[L]"
            elif task.priority is None:
                priority_indicator = "[N]"
            
            # Format tags
            tags_str = " ".join([f"#{tag}" for tag in task.tags]) if task.tags else ""
            
            # Format status
            status = "[x]" if task.completed else "[ ]"
            
            description = task.description if task.description else "[italic]No description[/italic]"
            
            table.add_row(
                str(task.id),
                priority_indicator,
                tags_str,
                status,
                task.title,
                description
            )

        self.console.print(table)

    def filter_tasks_interactive(self):
        """
        Interactive method to filter tasks by various criteria.
        """
        if not self.todo_list.get_all_tasks():
            self.console.print("[yellow]No tasks available to filter[/yellow]")
            return

        # Get filter criteria from user
        print("Leave empty to skip a filter:")
        status = input("Filter by status (incomplete/completed/all): ").strip().lower()
        if status and status not in ["incomplete", "completed", "all"]:
            self.console.print(f"[red]ERROR[/red] Invalid status: {status}. Must be incomplete, completed, or all.")
            return

        priority = input("Filter by priority (high/medium/low/none): ").strip().lower()
        if priority and priority not in ["high", "medium", "low", "none"]:
            self.console.print(f"[red]ERROR[/red] Invalid priority: {priority}. Must be high, medium, low, or none.")
            return
        if priority == "none":
            priority = None

        tag = input("Filter by tag: ").strip()

        # Get due date filters
        due_filter = input("Filter by due date status (overdue/due-soon/due-today/all, press Enter for all): ").strip().lower()
        if due_filter and due_filter not in ["overdue", "due-soon", "due-today", "all"]:
            self.console.print(f"[red]ERROR[/red] Invalid due date filter: {due_filter}. Must be overdue, due-soon, due-today, or all.")
            return

        # Get recurring filter
        recurring_filter = input("Show only recurring tasks? (y/n, press Enter for all): ").strip().lower()
        show_recurring = recurring_filter in ['y', 'yes']

        # Get sort criteria
        sort_by = input("Sort by (created/alpha/priority/tags, press Enter for no sorting): ").strip().lower()
        if sort_by and sort_by not in ["created", "alpha", "priority", "tags"]:
            self.console.print(f"[red]ERROR[/red] Invalid sort option: {sort_by}. Must be created, alpha, priority, or tags.")
            return

        reverse = False
        if sort_by:
            reverse_input = input("Reverse sort order? (y/n, default is n): ").strip().lower()
            reverse = reverse_input in ['y', 'yes']

        # Apply filters based on user selections
        if due_filter == "overdue":
            tasks = self.todo_list.get_overdue_tasks()
        elif due_filter == "due-soon":
            tasks = self.todo_list.get_due_soon_tasks()
        elif due_filter == "due-today":
            tasks = self.todo_list.get_due_today_tasks()
        elif show_recurring:
            tasks = self.todo_list.get_recurring_tasks()
        else:
            # Apply standard filters
            tasks = self.todo_list.combine_filters_search(
                status=status if status != "all" else None,
                priority=priority,
                tag=tag if tag else None,
                sort_by=sort_by if sort_by else None,
                reverse=reverse
            )

        if not tasks:
            self.console.print("[yellow]No tasks match your search/filter criteria[/yellow]")
            return

        table = Table(title="Filtered Tasks")
        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Due Date", style="magenta")
        table.add_column("Priority", style="yellow")
        table.add_column("Tags", style="blue")
        table.add_column("Status", style="red")
        table.add_column("Title", style="green")
        table.add_column("Description", style="dim")

        for task in tasks:
            # Format due date
            due_date_str = ""
            if task.due_datetime:
                # Check if overdue
                from datetime import datetime
                if not task.completed and task.due_datetime < datetime.now():
                    due_date_str = f"[red]{task.due_datetime.strftime('%Y-%m-%d %H:%M')}[/red] [bold red]OVERDUE[/bold red]"
                else:
                    due_date_str = task.due_datetime.strftime('%Y-%m-%d %H:%M')

            # Format priority indicator
            priority_indicator = ""
            if task.priority == "high":
                priority_indicator = "[H]"
            elif task.priority == "medium":
                priority_indicator = "[M]"
            elif task.priority == "low":
                priority_indicator = "[L]"
            elif task.priority is None:
                priority_indicator = "[N]"

            # Format tags
            tags_str = " ".join([f"#{tag}" for tag in task.tags]) if task.tags else ""

            # Format status
            status = "[x]" if task.completed else "[ ]"

            description = task.description if task.description else "[italic]No description[/italic]"

            table.add_row(
                str(task.id),
                due_date_str,
                priority_indicator,
                tags_str,
                status,
                task.title,
                description
            )

        self.console.print(table)

    def run_interactive(self):
        """
        Runs the interactive CLI application.
        """
        while True:
            self.display_menu()
            choice = input("Select an option (1-9): ").strip()

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
                self.search_tasks_interactive()
            elif choice == "8":
                self.filter_tasks_interactive()
            elif choice == "9":
                self.console.print("[bold green]Goodbye![/bold green]")
                break
            else:
                self.console.print("[red]ERROR[/red] Invalid option. Please select 1-9.")


def main():
    """
    Main entry point for the interactive CLI application.
    """
    cli = InteractiveTodoCLI()
    cli.run_interactive()


if __name__ == "__main__":
    main()