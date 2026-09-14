import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

from utils.ui import display_welcome_banner
from utils.storage import load_json, save_json
from utils.validators import is_non_empty, is_valid_phone, is_positive_number
from utils.auth import login_user, logout_user, get_current_user
from utils.decorators import require_auth, require_admin

console = Console()

def display_header():
    console.clear()
    display_welcome_banner()

def view_routes():
    display_header()
    routes = load_json("data/routes.json")
    
    table = Table(title="Available SACCO Routes", header_style="bold magenta")
    table.add_column("Route ID", style="cyan")
    table.add_column("Source")
    table.add_column("Destination")
    table.add_column("Fare (KES)", justify="right", style="green")

    if not routes:
        console.print("[yellow]No routes registered in the system yet.[/yellow]")
    else:
        for r in routes:
            table.add_row(r.get("route_id", "-"), r.get("source", "-"), r.get("destination", "-"), f"{r.get('fare', 0):.2f}")
        console.print(table)
    
    Prompt.ask("\nPress [bold]Enter[/bold] to return to menu")

@require_admin
def add_route():
    display_header()
    console.print("[bold yellow]Add New Route[/bold yellow]\n")
    
    route_id = Prompt.ask("Enter Route ID (e.g., R01)")
    source = Prompt.ask("Enter Departure Point")
    destination = Prompt.ask("Enter Destination")
    fare = Prompt.ask("Enter Fare Amount (KES)")
    
    if not (is_non_empty(route_id) and is_non_empty(source) and is_non_empty(destination)):
        console.print("[bold red]Error: All fields are required![/bold red]")
    elif not is_positive_number(fare):
        console.print("[bold red]Error: Fare must be a positive number![/bold red]")
    else:
        routes = load_json("data/routes.json")
        routes.append({"route_id": route_id, "source": source, "destination": destination, "fare": float(fare)})
        save_json("data/routes.json", routes)
        console.print("[bold green]✓ Route added successfully![/bold green]")
        
    Prompt.ask("\nPress [bold]Enter[/bold] to continue")

@require_admin
def add_matatu():
    display_header()
    console.print("[bold yellow]Register New Matatu[/bold yellow]\n")
    
    plate_number = Prompt.ask("Enter License Plate (e.g., KBC 123A)")
    route_id = Prompt.ask("Enter Assigned Route ID (e.g., R01)")
    capacity = Prompt.ask("Enter Vehicle Capacity")
    
    if not (is_non_empty(plate_number) and is_non_empty(route_id)):
        console.print("[bold red]Error: All fields are required![/bold red]")
    elif not is_positive_number(capacity):
        console.print("[bold red]Error: Capacity must be a positive number![/bold red]")
    else:
        matatus = load_json("data/matatu.json")
        matatus.append({
            "plate_number": plate_number, 
            "route_id": route_id, 
            "capacity": int(capacity)
        })
        save_json("data/matatu.json", matatus)
        console.print("[bold green]✓ Matatu registered successfully![/bold green]")
        
    Prompt.ask("\nPress [bold]Enter[/bold] to continue")

def login_flow():
    display_header()
    console.print("[bold cyan]System Login[/bold cyan]\n")
    phone = Prompt.ask("Enter registered Phone Number")
    
    if not is_valid_phone(phone):
        console.print("[bold red]Invalid phone format! Use 07XXXXXXXX or +2547XXXXXXXX[/bold red]")
    else:
        user = login_user(phone)
        if user:
            console.print(f"[bold green]Welcome back, {user['name']}![/bold green]")
        else:
            console.print("[bold red]User not found in system database.[/bold red]")
    Prompt.ask("\nPress [bold]Enter[/bold] to continue")

def main():
    while True:
        display_header()
        current_user = get_current_user()
        
        if current_user:
            console.print(f"Logged in as: [bold cyan]{current_user['name']}[/bold cyan] ([yellow]{current_user['role']}[/yellow])\n")
        else:
            console.print("[dim]Status: Guest User[/dim]\n")

        console.print("1. View SACCO Routes")
        console.print("2. Login")
        console.print("3. Add New Route (Admin Only)")
        console.print("4. Add New Matatu (Admin Only)")
        console.print("5. Logout")
        console.print("6. Exit")
        
        choice = Prompt.ask("\nSelect an option", choices=["1", "2", "3", "4", "5", "6"])

        if choice == "1":
            view_routes()
        elif choice == "2":
            login_flow()
        elif choice == "3":
            add_route()
        elif choice == "4":
            add_matatu()
        elif choice == "5":
            logout_user()
            console.print("[yellow]Logged out successfully.[/yellow]")
            Prompt.ask("\nPress [bold]Enter[/bold] to continue")
        elif choice == "6":
            console.print("[bold green]Thank you for using Matatu SACCO Manager![/bold green]")
            sys.exit(0)

if __name__ == "__main__":
    main()