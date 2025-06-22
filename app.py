import os
import uuid
from pathlib import Path
import gradio as gr
import assemblyai as aai
from translate import Translator
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv

load_dotenv()
ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
DEFAULT_ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
DEFAULT_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID")


def voice_to_voice(audio_file, user_api_key, user_voice_id):
    transcript = transcribe_audio(audio_file)
    if transcript.status == aai.TranscriptStatus.error:
        raise gr.Error(transcript.error)
    else:
        transcript = transcript.text

    list_translations = translate_text(transcript)
    generated_audio_paths = []

    for translation in list_translations:
        translated_audio_file_name = text_to_speech(translation, user_api_key, user_voice_id)
        generated_audio_paths.append(Path(translated_audio_file_name))

    return (*generated_audio_paths, *list_translations)


def transcribe_audio(audio_file):
    aai.settings.api_key = ASSEMBLYAI_API_KEY
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_file)
    return transcript


def translate_text(text: str):
    languages = ["ru", "tr", "ar", "de", "es", "ja"]
    translations = []
    for lang in languages:
        translator = Translator(from_lang="en", to_lang=lang)
        translated = translator.translate(text)
        translations.append(translated)
    return translations


def text_to_speech(text: str, api_key: str = None, voice_id: str = None) -> str:
    api_key = api_key or DEFAULT_ELEVENLABS_API_KEY
    voice_id = voice_id or DEFAULT_VOICE_ID

    client = ElevenLabs(api_key=api_key)

    response = client.text_to_speech.convert(
        voice_id=voice_id,
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_multilingual_v2",
        voice_settings=VoiceSettings(
            stability=0.5,
            similarity_boost=0.8,
            style=0.5,
            use_speaker_boost=True,
        ),
    )

    file_path = f"{uuid.uuid4()}.mp3"
    with open(file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{file_path} saved.")
    return file_path


with gr.Blocks() as demo:
    gr.Markdown("## 🎙️ Voice-to-Voice Translation App")
    gr.Markdown("## Record your voice in English and hear translations in multiple languages with optional voice cloning via ElevenLabs.")

    with gr.Row():
        with gr.Column():
            audio_input = gr.Audio(
                sources=["microphone"],
                type="filepath",
                show_download_button=True,
                waveform_options=gr.WaveformOptions(
                    waveform_color="#01C6FF",
                    waveform_progress_color="#0066B4",
                    skip_length=2,
                    show_controls=False,
                ),
            )

            user_api_key = gr.Textbox(label="🔑 Your ElevenLabs API Key (optional)", type="password", placeholder="Paste here to use your voice clone")
            user_voice_id = gr.Textbox(label="🗣️ Your Cloned Voice ID from ElevenLabs (optional)", placeholder="Your ElevenLabs voice ID")

            with gr.Row():
                submit = gr.Button("Submit", variant="primary")
                btn = gr.ClearButton(audio_input, "Clear")

    with gr.Row():
        with gr.Group():
            ru_output = gr.Audio(label="Russian")
            ru_text = gr.Markdown()
        with gr.Group():
            tr_output = gr.Audio(label="Turkish")
            tr_text = gr.Markdown()
        with gr.Group():
            ar_output = gr.Audio(label="Arabic")
            ar_text = gr.Markdown()

    with gr.Row():
        with gr.Group():
            de_output = gr.Audio(label="German")
            de_text = gr.Markdown()
        with gr.Group():
            es_output = gr.Audio(label="Spanish")
            es_text = gr.Markdown()
        with gr.Group():
            jp_output = gr.Audio(label="Japanese")
            jp_text = gr.Markdown()

    outputs = [
        ru_output, tr_output, ar_output,
        de_output, es_output, jp_output,
        ru_text, tr_text, ar_text,
        de_text, es_text, jp_text,
    ]

    submit.click(
        fn=voice_to_voice,
        inputs=[audio_input, user_api_key, user_voice_id],
        outputs=outputs,
        show_progress=True
    )

if __name__ == "__main__":
    demo.launch()



