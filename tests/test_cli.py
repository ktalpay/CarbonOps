from typer.testing import CliRunner

from carbonops import __version__
from carbonops.cli import app


runner = CliRunner()


def test_version_command_outputs_package_version():
    result = runner.invoke(app, ["version"])

    assert result.exit_code == 0
    assert result.stdout.strip() == __version__


def test_schedule_command_returns_pre_alpha_placeholder_behavior():
    result = runner.invoke(
        app,
        [
            "schedule",
            "--region",
            "gb_london",
            "--duration",
            "30m",
            "--mode",
            "delay",
        ],
    )

    assert result.exit_code == 0
    assert "region=gb_london" in result.stdout
    assert "duration=30m" in result.stdout
    assert "mode=delay" in result.stdout
    assert "placeholder" in result.stdout
