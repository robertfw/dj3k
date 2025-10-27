#!/usr/bin/env python

import logging
import os
import sys

import dotenv
from django.core import management

logger = logging.getLogger(__name__)


def _start_debugpy() -> None:
    logger.info("Starting debugpy")
    import debugpy  # noqa: PLC0415, T100

    debugpy.listen(("0.0.0.0", 9876))  # noqa: S104, T100
    logger.info("debugpy listening on port 9876")

    if os.environ.get("ENABLE_DEBUGPY_WAIT_FOR_CLIENT"):
        logger.info("Waiting for debugpy client to connect...")
        debugpy.wait_for_client()  # noqa: T100
        logger.info("debugpy client connected")


def main() -> None:
    dotenv.load_dotenv()
    management.execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
