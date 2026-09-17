"""CLI foundation tests."""

from typer.testing import CliRunner

from secrettrace.cli import app

runner = CliRunner()


def test_version_option_reports_package_version() -> None:
    result = runner.invoke(app, ["--version"])

    assert result.exit_code == 0
    assert result.stdout.strip() == "SecretTrace 0.1.0"


def test_root_command_displays_help_when_no_command_is_given() -> None:
    result = runner.invoke(app)

    assert result.exit_code == 0
    assert "Find potentially exposed secrets" in result.stdout


def test_scan_validates_target_but_reports_unimplemented(tmp_path: object) -> None:
    result = runner.invoke(app, ["scan", str(tmp_path)])

    assert result.exit_code == 2
    assert "Scan target validated" in result.stdout
    assert "Detection engine is not implemented" in result.stderr
