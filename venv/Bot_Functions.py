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


def uzbek_stt(audio_file_path):
    openaiurl = "https://api.openai.com/v1"

    headers = {"Authorization": f"Bearer API KEY"}

    mohir = MohirAi(api_key="API KEY")

    speech_to_text = mohir.stt(audio_file_path)

    print("Response from MohirAI API's", speech_to_text)

    if speech_to_text == '.':
        return None

    url = f"{openaiurl}/chat/completions"

    print(get_closest(speech_to_text, lang='uzb'))

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

    return chatgpt_response


def russian_stt(audio_file_path):
    openaiurl = "https://api.openai.com/v1"

    headers = {"Authorization": f"Bearer API KEY"}

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
    speech_to_text = response.json()["text"]
    print("Response from STT API's", speech_to_text)

    if speech_to_text == '.':
        return None

    print("[-] Querying LLM  with the STT response data")
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

    return chatgpt_response


def english_stt(audio_file_path):
    openaiurl = "https://api.openai.com/v1"

    headers = {"Authorization": f"Bearer API KEY"}

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
    speech_to_text = response.json()["text"]
    print("Response from STT API's", speech_to_text)

    if speech_to_text == '.':
        return None

    print("[-] Querying LLM  with the STT response data")
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

    return chatgpt_response


def uzbek(speech_to_text):
    openaiurl = "https://api.openai.com/v1"

    headers = {"Authorization": f"Bearer API KEY"}

    mohir = MohirAi(api_key="API KEY")

    if speech_to_text == '.':
        return None

    url = f"{openaiurl}/chat/completions"

    print(get_closest(speech_to_text, lang='uzb'))

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

    return chatgpt_response


def russian(speech_to_text):
    openaiurl = "https://api.openai.com/v1"

    headers = {"Authorization": f"Bearer API KEY"}

    if speech_to_text == '.':
        return None

    print("[-] Querying LLM  with the STT response data")
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

    return chatgpt_response


def english(speech_to_text):
    openaiurl = "https://api.openai.com/v1"

    headers = {"Authorization": f"Bearer API KEY"}

    if speech_to_text == '.':
        return None

    print("[-] Querying LLM  with the STT response data")
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

    return chatgpt_response