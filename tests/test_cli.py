import subprocess
import sys

from pssAutoDial import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "pssAutoDial", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
