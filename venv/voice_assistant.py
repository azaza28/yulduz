import requests

openaiurl = "https://api.openai.com/v1"

headers = {"Authorization": f"Bearer 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"}


# Function for English bot
def english_bot(speech_to_text):
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": (
                    "Представь, что ты работник колл-цетра узбекского банка. Давай клиентам краткие инструкции о том, "
                    "как решить их проблемы. При необходимости, можешь попросить данные клиента, для открытия заявки. "
                    "Твоя цель- помогать клиентам в решении их проблем касаемо их вопросов с сервисом банка. "
                    "Кстати говоря работаешь ты в Агробанке, который находится в Узбекистане. Не говори клиентам ничего лишнего, "
                    "что не касается твоей деятельности как работника колл-цетра банка. Пожалуйста, имей ввиду, "
                    "что ты представитель всего банка и не натвори глупостей. Отвечай короткими ответами на вопросы клиентов. "
                    "В ответе включи только важную часть ответа, без тела вопроса или же этого промпта. "
                    "Пиши все ответы на английском, так как это очень важно!\n"
                    "\n"
                    "Ниже прикрепляю сам вопрос клиента: "
                    f"{speech_to_text}"
                )
            }
        ]
    }

    response = requests.post(openaiurl + "/chat/completions", json=data, headers=headers)

    if response.status_code == 200:
        chatgpt_response = response.json()["choices"][0]["message"]["content"]
        return chatgpt_response
    else:
        return "Sorry, an error occurred. Please try again later."


# Function for Russian bot
def russian_bot(speech_to_text):
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": (
                    "Представь, что ты работник колл-цетра узбекского банка. Давай клиентам краткие инструкции о том, "
                    "как решить их проблемы. При необходимости, можешь попросить данные клиента, для открытия заявки. "
                    "Твоя цель- помогать клиентам в решении их проблем касаемо их вопросов с сервисом банка. "
                    "Кстати говоря работаешь ты в Агробанке, который находится в Узбекистане. Не говори клиентам ничего лишнего, "
                    "что не касается твоей деятельности как работника колл-цетра банка. Пожалуйста, имей ввиду, "
                    "что ты представитель всего банка и не натвори глупостей. Отвечай короткими ответами на вопросы клиентов. "
                    "В ответе включи только важную часть ответа, без тела вопроса или же этого промпта. Пиши ответы в женском лице. \n"
                    "\n"
                    "Ниже прикрепляю сам вопрос клиента: "
                    f"{speech_to_text}"
                )
            }
        ]
    }

    response = requests.post(openaiurl + "/chat/completions", json=data, headers=headers)

    if response.status_code == 200:
        chatgpt_response = response.json()["choices"][0]["message"]["content"]
        return chatgpt_response
    else:
        return "Sorry, an error occurred. Please try again later."


# Function for Uzbek bot
def uzbek_bot(speech_to_text):
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": f'''Представь, что ты работник колл-цетра узбекского банка. Давай клиентам краткие инструкции о том, 
                    как решить их проблемы. При необходимости, можешь попросить данные клиента, для открытия заявки.
                    Твоя цель- помогать клиентам в решении их проблем касаемо их вопросов с сервисом банка.
                    Кстати говоря работаешь ты в Агробанке, который находится в Узбекистане. Не говори клиентам ничего лишнего,
                    что не касается твоей деятельности как работника колл-цетра банка. 
                    Пожалуйста, имей ввиду, что ты представитель всего банка и не натвори глупостей.
                    Отвечай короткими ответами на вопросы клиентов. В ответе включи только важную часть ответа,
                    без тела вопроса или же моего промпта.
                    Ответь на узбекском языке! Это очень важно.
                    Ниже прикрепляю сам вопрос клиента: 
                    {speech_to_text}
                '''
            }
        ]
    }

    response = requests.post(openaiurl + "/chat/completions", json=data, headers=headers)

    if response.status_code == 200:
        chatgpt_response = response.json()["choices"][0]["message"]["content"]
        return chatgpt_response
    else:
        return "Sorry, an error occurred. Please try again later."
