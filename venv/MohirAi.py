import requests
from playsound import playsound


class MohirAi:
    """
    A class representing interactions with the Mohir AI API for text-to-speech (TTS) and speech-to-text (STT) functionalities.
    """

    def __init__(self, api_key):
        """
        Initialize the MohirAi object with the provided API key.

        Parameters:
            api_key (str): The API key for accessing the Mohir AI API.
        """
        self.api_key = api_key
        self.base_url = "https://mohir.ai/api/v1"

    def tts(self, text, model, mood, filename):
        """
        Generate speech from text using the Mohir AI Text-to-Speech (TTS) API and save it to a WAV file.

        Parameters:
            text (str): The text to be converted to speech.
            model (str): The model to use for speech synthesis. Available models: "davron", "dilfuza".
            mood (str): The mood of the generated speech. Possible values: "happy", "neutral", "sad".
            filename (str): The name of the file to save the generated audio.

        Returns:
            bool: True if the audio file was successfully generated and saved, False otherwise.
        """
        url = f"{self.base_url}/tts"

        headers = {
            "Authorization": self.api_key,
            "Content-Type": "application/json"
        }

        data = {
            "text": text,
            "model": model,
            "mood": mood
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            print("Request successful.")

            response_data = response.json()
            audio_url = response_data["result"]["url"]

            audio_response = requests.get(audio_url)

            if audio_response.status_code == 200:
                print("Audio file downloaded successfully.")

                with open(filename + ".wav", "wb") as audio_file:
                    audio_file.write(audio_response.content)

                print("Audio file saved successfully.")
                playsound(filename + '.wav')  # Play the audio file
                return True
            else:
                print("Error downloading audio file:", audio_response.status_code)
                return False
        else:
            print("Error:", response.status_code, response.text)
            return False

    def stt(self, audio_file_path):
        """
        Convert speech to text using the Mohir AI Speech to Text (STT) API.

        Parameters:
            audio_file_path (str): Path to the audio file to be converted to text.

        Returns:
            str: Transcribed text.
        """
        url = f"{self.base_url}/stt"

        headers = {
            "Authorization": self.api_key
        }

        form_data = {
            "file": open(audio_file_path, "rb"),
        }

        response = requests.post(url, headers=headers, files=form_data)

        if response.status_code == 200:
            print("Request successful.")
            return response.json()['result']['text']
        else:
            print("Error:", response.status_code, response.text)
            return None

