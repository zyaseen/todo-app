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
  todo add "Prepare quarterly report" --priority high --tags "work,urgent"
  todo list
  todo list --priority high --status incomplete
  todo list --search "groceries" --sort alpha
  todo update 1 --title "Buy groceries and cook dinner"
  todo update 1 --priority medium --tags "shopping,home"
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
        add_parser.add_argument('--priority', choices=['high', 'medium', 'low'],
                               help='Priority level of the task')
        add_parser.add_argument('--tags',
                               help='Comma-separated list of tags (e.g., "work,urgent,shopping")')
        add_parser.add_argument('--due',
                               help='Due date/time in various formats (YYYY-MM-DD, YYYY-MM-DD HH:MM, relative like "tomorrow 3pm", "next friday")')
        add_parser.add_argument('--recurring',
                               help='Recurrence pattern: daily, weekly:weekday, monthly:day, yearly (e.g., --recurring weekly:friday)')

        # List command
        list_parser = subparsers.add_parser('list', help='List all tasks')
        list_parser.add_argument('--search', help='Search keyword in title or description')
        list_parser.add_argument('--status', choices=['all', 'incomplete', 'completed'],
                                default='all', help='Filter by completion status')
        list_parser.add_argument('--priority', choices=['high', 'medium', 'low', 'none'],
                                help='Filter by priority level')
        list_parser.add_argument('--tag', help='Filter by tag presence')
        list_parser.add_argument('--sort', choices=['created', 'alpha', 'priority', 'tags'],
                                help='Sort by criteria')
        list_parser.add_argument('--reverse', action='store_true',
                                help='Reverse sort order')
        list_parser.add_argument('--overdue', action='store_true',
                                help='Show only overdue tasks')
        list_parser.add_argument('--due-soon', action='store_true',
                                help='Show only tasks due within 24 hours')
        list_parser.add_argument('--due-today', action='store_true',
                                help='Show only tasks due today')
        list_parser.add_argument('--show-recurring', action='store_true',
                                help='Show recurring task templates and next instances')

        # Update command
        update_parser = subparsers.add_parser('update', help='Update an existing task')
        update_parser.add_argument('id', type=int, help='ID of the task to update')
        update_parser.add_argument('--title', help='New title for the task')
        update_parser.add_argument('--desc', '--description', dest='description',
                                  help='New description for the task')
        update_parser.add_argument('--priority', choices=['high', 'medium', 'low', 'none'],
                                  help='New priority level for the task')
        update_parser.add_argument('--tags',
                                  help='New comma-separated list of tags (replaces all)')
        update_parser.add_argument('--add-tag',
                                  help='Add a single tag to the task')
        update_parser.add_argument('--remove-tag',
                                  help='Remove a single tag from the task')
        update_parser.add_argument('--due',
                                  help='New due date/time in various formats (YYYY-MM-DD, YYYY-MM-DD HH:MM, relative like "tomorrow 3pm", "next friday")')

        # Delete command
        delete_parser = subparsers.add_parser('delete', help='Delete a task')
        delete_parser.add_argument('id', type=int, help='ID of the task to delete')

        # Complete command
        complete_parser = subparsers.add_parser('complete', help='Mark a task as complete')
        complete_parser.add_argument('id', type=int, help='ID of the task to mark complete')

        # Incomplete command
        incomplete_parser = subparsers.add_parser('incomplete', help='Mark a task as incomplete')
        incomplete_parser.add_argument('id', type=int, help='ID of the task to mark incomplete')

        # Reminders command
        reminders_parser = subparsers.add_parser('reminders', help='Show overdue and due-soon tasks')
        reminders_parser.add_argument('--notify', action='store_true',
                                     help='Show desktop notifications for overdue/due-soon tasks')

        args = parser.parse_args()

        # Execute the appropriate command
        if args.command == 'add':
            # Parse tags if provided
            tags = []
            if args.tags:
                tags = [tag.strip() for tag in args.tags.split(',')]

            # Parse due date if provided
            due_datetime = None
            if args.due:
                try:
                    from .utils import parse_date_string
                    due_datetime = parse_date_string(args.due)
                except ValueError as e:
                    self.console.print(f"[red]ERROR[/red] Invalid due date format: {str(e)}")
                    return

            # Parse recurrence if provided
            recurrence = None
            if args.recurring:
                try:
                    recurrence = self._parse_recurrence_string(args.recurring)
                except ValueError as e:
                    self.console.print(f"[red]ERROR[/red] Invalid recurrence format: {str(e)}")
                    return

            self.add_task(args.title, args.description, args.priority, tags, due_datetime, recurrence)
        elif args.command == 'list':
            self.list_tasks(
                args.search, args.status, args.priority, args.tag, args.sort, args.reverse,
                args.overdue, args.due_soon, args.due_today, args.show_recurring
            )
        elif args.command == 'update':
            # Parse due date if provided
            due_datetime = None
            if args.due:
                try:
                    from .utils import parse_date_string
                    due_datetime = parse_date_string(args.due)
                except ValueError as e:
                    self.console.print(f"[red]ERROR[/red] Invalid due date format: {str(e)}")
                    return

            self.update_task(
                args.id, args.title, args.description, args.priority,
                args.tags, args.add_tag, args.remove_tag, due_datetime
            )
        elif args.command == 'delete':
            self.delete_task(args.id)
        elif args.command == 'complete':
            self.mark_task_complete(args.id)
        elif args.command == 'incomplete':
            self.mark_task_incomplete(args.id)
        elif args.command == 'reminders':
            self.show_reminders(args.notify)

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

    def add_task(self, title: str, description: str = "", priority: Optional[str] = None,
                 tags: Optional[list] = None, due_datetime: Optional[datetime] = None,
                 recurrence: Optional[dict] = None):
        """
        Adds a new task with the given parameters.

        Args:
            title (str): The title of the task
            description (str): The optional description of the task
            priority (Optional[str]): The optional priority level
            tags (Optional[list]): The optional list of tags
            due_datetime (Optional[datetime]): The optional due date/time
            recurrence (Optional[dict]): The optional recurrence pattern
        """
        if tags is None:
            tags = []
        try:
            task = self.todo_list.add_task(title, description, priority, tags, due_datetime, recurrence)
            self.console.print(f"[green]SUCCESS[/green] Added task '{task.title}' with ID {task.id}")
        except ValueError as e:
            self.console.print(f"[red]ERROR[/red] {str(e)}")

    def list_tasks(self, search: Optional[str] = None, status: Optional[str] = None,
                   priority: Optional[str] = None, tag: Optional[str] = None,
                   sort: Optional[str] = None, reverse: bool = False,
                   overdue: bool = False, due_soon: bool = False,
                   due_today: bool = False, show_recurring: bool = False):
        """
        Lists tasks with optional filtering, searching, sorting, and due date options.

        Args:
            search (Optional[str]): Keyword to search for in title or description
            status (Optional[str]): Filter by completion status (all, incomplete, completed)
            priority (Optional[str]): Filter by priority level (high, medium, low, none)
            tag (Optional[str]): Filter by tag presence
            sort (Optional[str]): Sort by criteria (created, alpha, priority, tags)
            reverse (bool): Reverse sort order
            overdue (bool): Show only overdue tasks
            due_soon (bool): Show only tasks due within 24 hours
            due_today (bool): Show only tasks due today
            show_recurring (bool): Show recurring task templates and next instances
        """
        # Apply special filters first
        if overdue:
            tasks = self.todo_list.get_overdue_tasks()
        elif due_soon:
            tasks = self.todo_list.get_due_soon_tasks()
        elif due_today:
            tasks = self.todo_list.get_due_today_tasks()
        elif show_recurring:
            tasks = self.todo_list.get_recurring_tasks()
        else:
            # Check if there are no tasks at all before applying standard filters
            all_tasks = self.todo_list.get_all_tasks()
            if not all_tasks:
                # If there are no tasks at all, only show "No tasks found" if no filters were applied
                if not search and status == "all" and not priority and not tag:
                    self.console.print("[yellow]No tasks found[/yellow]")
                    return
                # If filters were applied but there are no tasks, it's still "no tasks match criteria"
                else:
                    self.console.print("[yellow]No tasks match your search/filter criteria[/yellow]")
                    return

            # Get tasks based on standard filters and search
            tasks = self.todo_list.combine_filters_search(
                search_keyword=search,
                status=status,
                priority=priority,
                tag=tag,
                sort_by=sort,
                reverse=reverse
            )

        if not tasks:
            self.console.print("[yellow]No tasks match your search/filter criteria[/yellow]")
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

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None,
                    priority: Optional[str] = None, tags: Optional[str] = None,
                    add_tag: Optional[str] = None, remove_tag: Optional[str] = None,
                    due_datetime: Optional[datetime] = None):
        """
        Updates the title, description, priority, tags, and/or due date of an existing task.

        Args:
            task_id (int): The ID of the task to update
            title (Optional[str]): The new title (if provided)
            description (Optional[str]): The new description (if provided)
            priority (Optional[str]): The new priority (if provided)
            tags (Optional[str]): The new comma-separated tags (if provided)
            add_tag (Optional[str]): A tag to add to the task
            remove_tag (Optional[str]): A tag to remove from the task
            due_datetime (Optional[datetime]): The new due date/time (if provided)
        """
        # Get the existing task to access current tags
        task = self.todo_list.get_task_by_id(task_id)
        if not task:
            self.console.print(f"[red]ERROR[/red] Task with ID {task_id} not found")
            return

        # Process tags
        final_tags = None
        if tags is not None:
            # Replace all tags with new list
            final_tags = [tag.strip() for tag in tags.split(',')]
        elif add_tag is not None or remove_tag is not None:
            # Modify existing tags
            final_tags = task.tags[:]  # Copy existing tags
            if add_tag:
                if add_tag not in final_tags:
                    final_tags.append(add_tag)
            if remove_tag and remove_tag in final_tags:
                final_tags.remove(remove_tag)

        # Handle priority 'none' value specially
        final_priority = priority
        if priority == 'none':
            final_priority = None

        success = self.todo_list.update_task(task_id, title, description, final_priority, final_tags, due_datetime)
        if success:
            self.console.print(f"[green]SUCCESS[/green] Updated task with ID {task_id}")
        else:
            self.console.print(f"[red]ERROR[/red] Task with ID {task_id} not found")

    def show_reminders(self, notify: bool = False):
        """
        Shows overdue and due-soon tasks.

        Args:
            notify (bool): Whether to show desktop notifications for overdue/due-soon tasks
        """
        overdue_tasks = self.todo_list.get_overdue_tasks()
        due_soon_tasks = self.todo_list.get_due_soon_tasks()

        # Combine and remove duplicates
        all_urgent_tasks = []
        seen_ids = set()
        for task in overdue_tasks + due_soon_tasks:
            if task.id not in seen_ids:
                all_urgent_tasks.append(task)
                seen_ids.add(task.id)

        if not all_urgent_tasks:
            self.console.print("[green]No urgent tasks at the moment[/green]")
            return

        table = Table(title="Urgent Tasks (Overdue & Due Soon)")
        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Due Date", style="magenta")
        table.add_column("Priority", style="yellow")
        table.add_column("Status", style="red")
        table.add_column("Title", style="green")

        for task in all_urgent_tasks:
            # Format due date with overdue indicator
            due_date_str = task.due_datetime.strftime('%Y-%m-%d %H:%M') if task.due_datetime else "No due date"
            if not task.completed and task.due_datetime and task.due_datetime < datetime.now():
                due_date_str = f"[red]{due_date_str}[/red] [bold red]OVERDUE[/bold red]"

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

            # Format status
            status = "[x]" if task.completed else "[ ]"

            table.add_row(
                str(task.id),
                due_date_str,
                priority_indicator,
                status,
                task.title
            )

        self.console.print(table)

        # Optionally show notifications
        if notify:
            try:
                from plyer import notification
                for task in all_urgent_tasks:
                    notification.notify(
                        title="Todo Reminder",
                        message=f"{task.title} (ID: {task.id}) - {'OVERDUE' if task.due_datetime and task.due_datetime < datetime.now() else 'DUE SOON'}",
                        timeout=5
                    )
            except ImportError:
                self.console.print("[yellow]Notifications not available (plyer not installed)[/yellow]")

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