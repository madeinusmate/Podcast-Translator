from google.cloud import speech
import os
import six
from google.cloud import translate_v2 as translate
from google.cloud import texttospeech
import html

os.environ[
    'GOOGLE_APPLICATION_CREDENTIALS'] = "/Users/stefano/Library/google-cloud-sdk/Podcast Translator-f4426a9e08bb.json"
source_file_names=["Business_Wars", "Motley_Fool", "Pomp"]

for file_name in source_file_names:

    #Call speech-to-text-API
    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri="gs://podcast_audio_files/" + file_name + ".wav")
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
        language_code="en-US",
        enable_automatic_punctuation=True,
        audio_channel_count = 2,
    )

    print("Initiating Podcast Translator for " + file_name + ".wav")

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Transcribing the input audio...")

    response = operation.result(timeout=90)
    transcription = ""
    for result in response.results:
        transcription=transcription + " " + format(result.alternatives[0].transcript)

    print(file_name + ".wav transctiption completed: " + transcription)


    #Call Translate API

    translate_client = translate.Client()

    if isinstance(transcription, six.binary_type):
        transcription = transcription.decode("utf-16")

    result = translate_client.translate(transcription, target_language="it")

    print("Translating the input text...")


    translation=format(result["translatedText"])

    #parsing for HTML ascii char
    translation=html.unescape(translation)

    print(file_name + ".wav translation completed: " + translation)

    # call Text-to-Speech API
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=translation)

    voice = texttospeech.VoiceSelectionParams(
            language_code="it-IT",
            name="it-IT-Wavenet-C",
            ssml_gender=texttospeech.SsmlVoiceGender.MALE,
        )

    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    print("Clearing my vocal chords...")

    with open( file_name + "_output.mp3", "wb") as out:
        out.write(response.audio_content)
        print(file_name + " Audio output saved as " + file_name + "_output.mp3")


