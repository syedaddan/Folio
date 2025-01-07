import logging

from dotenv import load_dotenv
from livekit.agents import (
    AutoSubscribe,
    JobContext,
    llm,
)
from livekit.agents.pipeline import VoicePipelineAgent
from livekit.plugins import openai, deepgram, elevenlabs

from utils.config import tts_voice
from utils.prompts import sys_prompt


load_dotenv()
logger = logging.getLogger("folio - groq")


async def entrypoint(ctx: JobContext):
    initial_ctx = llm.ChatContext().append(
        role="system",
        text=sys_prompt,
    )

    logger.info(f"connecting to room {ctx.room.name}")
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    # Wait for the first participant to connect
    participant = await ctx.wait_for_participant()
    logger.info(f"starting voice assistant for participant {participant.identity}")

    agent = VoicePipelineAgent(
        vad=ctx.proc.userdata["vad"],
        stt=deepgram.STT(
            model="nova-2-conversationalai",
            detect_language=True
        ),
        llm=openai.LLM.with_groq(
            model="llama-3.1-8b-instant"
        ),
        tts=elevenlabs.TTS(
            voice=tts_voice,
            model="eleven_turbo_v2_5"
        ),
        chat_ctx=initial_ctx
    )

    agent.start(ctx.room, participant)

    # The agent should be polite and greet the user when it joins :)
    await agent.say("Hey, how can I help you today?", allow_interruptions=True)