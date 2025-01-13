from livekit.plugins import elevenlabs
from livekit.plugins import silero
from livekit.agents import JobProcess


def prewarm_with_vad(proc: JobProcess):
    proc.userdata["vad"] = silero.VAD.load(
        min_silence_duration=0.3,
        activation_threshold=0.7
    )


tts_voice = elevenlabs.Voice(
    id="iP95p4xoKVk53GoZ742B",
    name="Chris",
    category="Conversational",
    settings=elevenlabs.VoiceSettings(
        stability=0.8,
        similarity_boost=0.7,
        style=0.8,
        use_speaker_boost=True
    )
)