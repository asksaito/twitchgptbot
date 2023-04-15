import os
import openai

# openai.organization = "org-xxxx"
openai.api_key = os.getenv("OPENAI_API_KEY")

def call_chatgpt(prompt):
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = prompt,
        max_tokens = 50,
        stop = '.'
    )

    response_text = response['choices'][0]['text']
    print(response_text)
    return response_text
