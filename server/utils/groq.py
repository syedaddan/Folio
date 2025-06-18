import os
import time
import asyncio
import logging
from dotenv import load_dotenv

from openai import AsyncOpenAI
from livekit.agents import (
    AutoSubscribe,
    JobContext,
    llm,
    metrics,
    VoicePipelineAgent
)
from livekit.plugins import openai, deepgram, elevenlabs

from utils.prompts import sys_prompt, summarize_content


logger = logging.getLogger("voice-assistant")
logger.setLevel(logging.INFO)

load_dotenv()

lock = asyncio.Lock()
client = AsyncOpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY")
)


async def summarize_context(chat_ctx: llm.ChatContext):
    # Perform summarization
    start = time.time()
    summary = await client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": summarize_content.format(conversation=chat_ctx.messages),
            }
        ],
        model="llama-3.1-8b-instant"
    )
    chat_ctx.messages = [chat_ctx.messages[0]] + [llm.ChatMessage(role="system", content=summary.choices[0].message.content)]
    logger.info(f"Time Taken: {time.time() - start}")
    logger.info(f"Generated Summary: {summary.choices[0].message.content}")
    logger.info(f"Updated Messages: {chat_ctx.messages}")


async def entrypoint(ctx: JobContext):
    initial_ctx = llm.ChatContext().append(
        role="system",
        text=sys_prompt,
    )

    logger.info(f"connecting to room {ctx.room.name}")
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    # wait for the first participant to connect
    participant = await ctx.wait_for_participant()
    logger.info(
        f"starting voice assistant for participant {participant.identity}"
    )

    elevenlabs_tts_voice = elevenlabs.Voice(
        id="IKne3meq5aSn9XLyUdCD",
        name="Charlie",
        category="Default"
    )

    agent = VoicePipelineAgent(
        vad=ctx.proc.userdata["vad"],
        stt=deepgram.STT(),
        llm=openai.LLM(api_key=os.environ.get("GROQ_API_KEY")).with_groq(model="llama-3.3-70b-versatile"),
        tts=elevenlabs.TTS(voice=elevenlabs_tts_voice),
        chat_ctx=initial_ctx
    )

    agent.start(ctx.room, participant)

    @agent.on("agent_speech_committed")
    def handle_conversation(_: llm.ChatMessage):
        # Start summarization in a separate task
        asyncio.create_task(summarize_context(agent.chat_ctx))

    usage_collector = metrics.UsageCollector()

    @agent.on("metrics_collected")
    def _on_metrics_collected(mtrcs: metrics.AgentMetrics):
        metrics.log_metrics(mtrcs)
        usage_collector.collect(mtrcs)

    async def log_usage():
        summary = usage_collector.get_summary()
        logger.info(f"Usage: ${summary}")

    ctx.add_shutdown_callback(log_usage)

    await agent.say(
        "Hi there, this is Folio. I am the portfolio that speaks for itself, created by Syed Addan, what do you want to know about me or Syed?",
        allow_interruptions=True
    )
