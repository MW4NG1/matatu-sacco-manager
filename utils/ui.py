from rich.console import Console
from rich.panel import Panel

console = Console()

def display_welcome_banner():
    console.print(Panel.fit(
        "[bold cyan]Matatu Sacco Manager[/bold cyan]\n[dim]Streamlined Operations & Fleet Management[/dim]",
        border_style="blue",
        padding=(1, 2)
    ))