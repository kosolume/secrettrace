"""Command-line interface for SecretTrace."""

from pathlib import Path
from typing import Annotated

import typer

from secrettrace import __version__

app = typer.Typer(
    name="secrettrace",
    help="Find potentially exposed secrets without sending source code off-device.",
    no_args_is_help=False,
    invoke_without_command=True,
)


def version_callback(value: bool) -> None:
    """Print the installed version and exit."""
    if value:
        typer.echo(f"SecretTrace {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    ctx: typer.Context,
    version: Annotated[
        bool | None,
        typer.Option("--version", callback=version_callback, is_eager=True, help="Show version."),
    ] = None,
) -> None:
    """Run SecretTrace commands."""
    del version
    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())


@app.command()
def scan(
    path: Annotated[
        Path,
        typer.Argument(exists=True, file_okay=False, readable=True, resolve_path=True),
    ] = Path("."),
) -> None:
    """Scan a directory (detection engine planned for the next milestone)."""
    typer.echo(f"Scan target validated: {path}")
    typer.echo("Detection engine is not implemented in the foundation release.", err=True)
    raise typer.Exit(code=2)
