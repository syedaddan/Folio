import logging
from livekit.agents import (
    WorkerOptions,
    cli,
)

from utils.config import prewarm_with_vad
from utils.groq import entrypoint


logger = logging.getLogger("folio")


if __name__ == "__main__":
    cli.run_app(
        WorkerOptions(
            entrypoint_fnc=entrypoint,
            prewarm_fnc=prewarm_with_vad,
        ),
    )
