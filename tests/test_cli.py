import subprocess
import sys

from pss_autodial import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "pss_autodial", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
