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