"""Interface for ``python -m pss_autodial``."""

import os
from argparse import ArgumentParser
from collections.abc import Sequence

from dotenv import load_dotenv

from pss_autodial.pss_autodial import run_application

from . import __version__

__all__ = ["main"]


def main(args: Sequence[str] | None = None) -> None:
    """Argument parser for the CLI."""
    parser = ArgumentParser()
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=__version__,
    )
    parser.parse_args(args)

    print(os.environ)
    print("TESTIBG")
    load_dotenv()  # reads variables from a .env file and sets them in os.environ
    print(os.environ)
    run_application()


if __name__ == "__main__":
    main()
