from click.testing import CliRunner
from logging_monitor.cli import log


def test_log():
    runner = CliRunner()
    result = runner.invoke(
        log, ["--level", "ERROR", "--message", "This is a test message"]
    )
    assert result.exit_code == 0
    assert result.output == "ERROR | This is a test message\n"
