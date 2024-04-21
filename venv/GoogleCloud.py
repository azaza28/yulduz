import os
from google.cloud import texttospeech_v1
from playsound import playsound

# Set Google Cloud credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'KEY.json'

# Create a TextToSpeechClient
client = texttospeech_v1.TextToSpeechClient()


def speak_turkish(text, filename):
    """
    Generate speech from Turkish text using Google Cloud Text-to-Speech API and save it to an MP3 file.

    Parameters:
        text (str): The text to be converted to speech.
        filename (str): The name of the file to save the generated audio.
    """
    text = '<speak>' + text + '</speak>'
    synthesis_input = texttospeech_v1.SynthesisInput(ssml=text)

    voice = texttospeech_v1.VoiceSelectionParams(
        name='tr-TR-Wavenet-A',
        language_code='tr-TR'
    )

    audio_config = texttospeech_v1.AudioConfig(
        audio_encoding=texttospeech_v1.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    filename = filename + '.mp3'

    with open(filename, 'wb') as output:
        output.write(response.audio_content)

    playsound(filename)


def speak_english(text, filename):
    """
    Generate speech from English text using Google Cloud Text-to-Speech API and save it to an MP3 file.

    Parameters:
        text (str): The text to be converted to speech.
        filename (str): The name of the file to save the generated audio.
    """
    synthesis_input = texttospeech_v1.SynthesisInput(text=text)

    voice = texttospeech_v1.VoiceSelectionParams(
        name='en-US-Journey-F',
        language_code='en-US'
    )

    audio_config = texttospeech_v1.AudioConfig(
        audio_encoding=texttospeech_v1.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    filename = filename + '.mp3'

    with open(filename, 'wb') as output:
        output.write(response.audio_content)

    playsound(filename)


def speak_russian(text, filename):
    """
    Generate speech from Russian text using Google Cloud Text-to-Speech API and save it to an MP3 file.

    Parameters:
        text (str): The text to be converted to speech.
        filename (str): The name of the file to save the generated audio.
    """
    text = '<speak>' + text + '</speak>'
    synthesis_input = texttospeech_v1.SynthesisInput(ssml=text)

    voice = texttospeech_v1.VoiceSelectionParams(
        name='ru-RU-Wavenet-C',
        language_code='ru-RU'
    )

    audio_config = texttospeech_v1.AudioConfig(
        audio_encoding=texttospeech_v1.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    filename = filename + '.mp3'

    with open(filename, 'wb') as output:
        output.write(response.audio_content)

    playsound(filename)
