import os
import time
import GoogleCloud
import speech_recognition as sr
import requests
import pyttsx3
import wave
from playsound import playsound
from MohirAi import MohirAi
from Embedding import get_closest


def select_language():
    playsound('Salomlash.wav')
    playsound('Privetstvie.mp3')
    playsound('Greeting.mp3')

    ch = int(input("choice:"))

    if ch == 1:
        uzbek_bot()

    elif ch == 2:
        russian_bot()

    elif ch == 3:
        english_bot()

    else:
        select_language()


def uzbek_bot():
    openaiurl = "https://api.openai.com/v1"

    headers = {"Authorization": f"Bearer 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"}

    playsound('Bo\'shlash.wav')

    mohir = MohirAi(api_key="aade9eb8-f6ea-4b7f-b31d-373c91871e3b:46a1a02f-9b59-4554-a2e2-2e7e0b8eeb7b")

    while True:
        print("[-] Record audio using microphone")

        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Say something!")
            audio = r.listen(source)

        audio_file_path = "savol.wav"

        print(f"Generating WAV file, saving at location: {audio_file_path}")
        with open(audio_file_path, "wb") as f:
            f.write(audio.get_wav_data())

        print("[-] Call to MohirAI API's to get the STT response")

        speech_to_text = mohir.stt(audio_file_path)

        print("Response from MohirAI API's", speech_to_text)

        if speech_to_text == '.':
            continue

        url = f"{openaiurl}/chat/completions"

        print(get_closest(speech_to_text,lang='uzb'))

        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": f'''
                    Представь, что ты работник колл-цетра курсов по програмированию. Давай клиентам краткие инструкции о том, 
                    как решить их проблемы. Твоя цель-помогать клиентам в решении их проблем касаемо их вопросов с сервисом банка.
                    Кстати говоря работаешь ты в Mohirdev, который находится в Узбекистане. Поискав свою базу данных, я обнаружил,
                    что похожий вопрос уже встречался в истории, однако я не уверен, что они точно подходят для данного случая. 
                    Пожалуйста, по предоставленным 5 ответам определи, релевантны-ли они. В случае если релеванты, то
                    перефразируй их, добавь немного текста если его мало и используй эти 5 ответов в качестве базы данных для своих ответов. 
                    В случае, если ответы не подходят под вопрос, ответь что-то нейтральное. Если не знаешь, что ответить, попроси их позвонить по номеру: +998781136272
                    Не обращайся в ответе ко мне, обращайся напрямую к клиенту. Не упоминай, в ответе то, что тебе были предоставлены ответы.
                    Ответь на узбекском языке! Это очень важно!!!
                    Ниже прикрепляю сам вопрос клиента: 
                    {speech_to_text}
                    
                    Ниже прикрепляю самые релевантные ответы:
                    {get_closest(speech_to_text)}
                    '''
                }
            ]
        }

        response = requests.post(url, json=data, headers=headers)

        print("Status Code", response.status_code)
        chatgpt_response = response.json()["choices"][0]["message"]["content"]
        print("Response from LLM ", chatgpt_response)


        print("[-] Try to convert TTS from the response")
        mohir.tts(text=chatgpt_response, model="dilfuza", mood="happy", filename="javob")


def russian_bot():
    playsound('Nachalo.mp3')

    openaiurl = "https://api.openai.com/v1"

    headers = {"Authorization": f"Bearer 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"}

    # implement a counter
    while True:
        print("[-] Record audio using microphone")

        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Say something!")
            audio = r.listen(source)

        audio_file_path = "vopros.mp3"

        print(f"Generating WAV file, saving at location: {audio_file_path}")
        with open(audio_file_path, "wb") as f:
            f.write(audio.get_wav_data())

        print("[-] Call to STT API's to get the STT response")

        url = f"{openaiurl}/audio/transcriptions"

        data = {
            "model": "whisper-1",
            "file": audio_file_path,
        }
        files = {
            "file": open(audio_file_path, "rb")
        }

        response = requests.post(url, files=files, data=data, headers=headers)
        print(response.json())
        print("Status Code", response.status_code)
        speech_to_text = response.json()["text"]
        print("Response from STT API's", speech_to_text)

        if speech_to_text == '.':
            continue


        print("[-] Querying LLM model with the STT response data")
        url = f"{openaiurl}/chat/completions"

        print(get_closest(speech_to_text))

        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": f'''
                    Представь, что ты работник колл-цетра курсов по програмированию. Давай клиентам краткие инструкции о том, 
                    как решить их проблемы. При необходимости, можешь попросить данные клиента, для открытия заявки.
                    Твоя цель-помогать клиентам в решении их проблем касаемо их вопросов с сервисом банка.
                    Кстати говоря работаешь ты в Mohirdev, который находится в Узбекистане. Поискав свою базу данных, я обнаружил,
                    что похожий вопрос уже встречался в истории, однако я не уверен, что они точно подходят для данного случая. 
                    Пожалуйста, по предоставленным 5 ответам определи, релевантны-ли они. В случае если релеванты, то
                    перефразируй их, добавь немного текста если его мало. 
                    В случае, если ответы не подходят под вопрос, ответь что-то нейтральное. Если не знаешь, что ответить, попроси их позвонить по номеру: +998781136272
                    Не обращайся в ответе ко мне, обращайся напрямую к клиенту. Не упоминай, в ответе то, что тебе были предоставлены ответы.
                    
                    Ниже прикрепляю сам вопрос клиента: 
                    {speech_to_text}
                    
                    Ниже прикрепляю самые релевантные ответы:
                    {get_closest(speech_to_text)}
                    '''
                }
            ]
        }

        response = requests.post(url, json=data, headers=headers)

        print("Status Code", response.status_code)
        chatgpt_response = response.json()["choices"][0]["message"]["content"]
        print("Response from LLM ", chatgpt_response)

        ###################################################################
        ###      4. Try to convert TTS from the response                ###
        ###################################################################

        print("[-] Try to convert TTS from the response")

        GoogleCloud.speak_russian(chatgpt_response, 'otvet')


def english_bot():
    playsound('Start.mp3')

    openaiurl = "https://api.openai.com/v1"

    headers = {"Authorization": f"Bearer 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"}

    # implement a counter
    while True:

        ###################################################################
        ###           1. Record using microphone                        ###
        ###################################################################

        print("[-] Record audio using microphone")

        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Say something!")
            audio = r.listen(source)

        audio_file_path = "question.mp3"

        # write audio to a WAV file
        print(f"Generating WAV file, saving at location: {audio_file_path}")
        with open(audio_file_path, "wb") as f:
            f.write(audio.get_wav_data())

        ###################################################################
        ###      2. Call to STT API's and getting result            ###
        ###################################################################

        print("[-] Call to STT API's to get the STT response")

        url = f"{openaiurl}/audio/transcriptions"

        data = {
            "model": "whisper-1",
            "file": audio_file_path,
        }
        files = {
            "file": open(audio_file_path, "rb")
        }

        response = requests.post(url, files=files, data=data, headers=headers)
        print(response.json())
        print("Status Code", response.status_code)
        speech_to_text = response.json()["text"]
        print("Response from STT API's", speech_to_text)

        if speech_to_text == '.':
            continue


        print("[-] Querying LLM with the STT response data")
        url = f"{openaiurl}/chat/completions"

        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content":
                        f'''
                    Переведи следующий текст на русский язык:
                    {speech_to_text}
                    '''
                }
            ]

        }
        response = requests.post(url, json=data, headers=headers)

        chatgpt_response = response.json()["choices"][0]["message"]["content"]

        print(speech_to_text)

        print(get_closest(speech_to_text))

        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": f'''
                    Представь, что ты работник колл-цетра курсов по програмированию. Давай клиентам краткие инструкции о том, 
                    как решить их проблемы. При необходимости, можешь попросить данные клиента, для открытия заявки.
                    Твоя цель-помогать клиентам в решении их проблем касаемо их вопросов с сервисом банка.
                    Кстати говоря работаешь ты в Mohirdev, который находится в Узбекистане. Поискав свою базу данных, я обнаружил,
                    что похожий вопрос уже встречался в истории, однако я не уверен, что они точно подходят для данного случая. 
                    Пожалуйста, по предоставленным 5 ответам определи, релевантны-ли они. В случае если релеванты, то
                    перефразируй их, добавь немного текста если его мало. 
                    В случае, если ответы не подходят под вопрос, ответь что-то нейтральное. Если не знаешь, что ответить, попроси их позвонить по номеру: +9 9 8 7 8 1 1 3 6 2 7 2
                    Не обращайся в ответе ко мне, обращайся напрямую к клиенту. Не упоминай, в ответе то, что тебе были предоставлены ответы.
                    Ответь на английском языке! Это очень важно!!!
                    Ниже прикрепляю сам вопрос клиента: 
                    {speech_to_text}

                    Ниже прикрепляю самые релевантные ответы:
                    {get_closest(speech_to_text)}
                    '''
                }
            ]
        }

        response = requests.post(url, json=data, headers=headers)

        print("Status Code", response.status_code)
        chatgpt_response = response.json()["choices"][0]["message"]["content"]
        print("Response from LLM"
              "l ", chatgpt_response)

        ###################################################################
        ###      4. Try to convert TTS from the response                ###
        ###################################################################

        print("[-] Try to convert TTS from the response")

        GoogleCloud.speak_english(chatgpt_response, 'answer')


if __name__ == '__main__':
    select_language()
