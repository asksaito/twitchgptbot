import os
import openai
import settings

# openai.organization = "org-xxxx"
openai.api_key = os.getenv("OPENAI_API_KEY")

def call_chatgpt(prompt):
    # ChatGPT completions API https://platform.openai.com/docs/api-reference/completions/create
    response = openai.Completion.create(
        model = settings.CHATGPT_MODEL,
        prompt = prompt,
        max_tokens = settings.CHATGPT_MAX_TOKENS
    )

    response_text = response['choices'][0]['text']
    print(response_text)
    return response_text
