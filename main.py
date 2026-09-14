import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

from utils.storage import load_json, save_json
from utils.validators import is_non_empty, is_valid_phone, is_positive_number
from utils.auth import login_user, logout_user, get_current_user
from utils.decorators import require_auth, require_admin

console = Console()

def display_header():
    console.clear()
    console.print(
        Panel.fit(
            "[bold green]🚌 MATATU SACCO MANAGEMENT SYSTEM[/bold green]\n"
            "[dim]Streamlining Transport & Route Operations[/dim]",
            border_style="green"
        )
    )
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