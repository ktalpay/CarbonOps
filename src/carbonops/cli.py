import typer
from datetime import datetime

app = typer.Typer(help="Carbon‑aware DevOps CLI – schedule builds by carbon windows.")

@app.command()
def version():
    \"\\"Show version\\"\\"
    from . import __version__
    typer.echo(__version__)

@app.command()
def schedule(region: str = typer.Option(..., help="Region identifier, e.g., gb_london"),
             duration: str = typer.Option("30m", help="Job duration (e.g., 30m, 2h)"),
             mode: str = typer.Option("delay", help="Policy: delay|relocate|run-now")):
    \"\\"Simulate a scheduling decision (placeholder).\\"\\"
    now = datetime.utcnow().isoformat(timespec="minutes")
    typer.echo(f"[{now}] region={region} duration={duration} mode={mode}")
    typer.echo("Decision: delay 15m (placeholder, add real adapters in v0.0.2)")

def main():
    app()

if __name__ == "__main__":
    main()
