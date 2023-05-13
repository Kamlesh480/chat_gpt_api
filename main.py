import openai
import requests
import json

from cred import GPT_API_KEY

openai.api_key = GPT_API_KEY

Authorization = "Bearer" + " " + GPT_API_KEY


def get_gpt3_5_response(messages: list):
    """
    Returns the response from GPT-3.5 model based on the provided messages.

    Args:
        messages: A list of messages.

    Returns:
        A string containing the response from GPT-3.5 model.
    """

    engine = "davinci"
    prompt = json.dumps(messages)
    headers = {
        "Content-Type": "application/json",
        "Authorization": Authorization
    }
    payload = {
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 100,
        "stop": "\n"
    }
    response = requests.post(f"https://api.openai.com/v1/engines/{engine}/completions", headers=headers, json=payload)
    return response.json()



messages = [
    {
        "name": "user",
        "content": "Hi, can you recommend a good Italian restaurant in the area?",
        "role": "sender"
    }
]

# call the function to get a response from the GPT-3 model
response = get_gpt3_5_response(messages)

# print the response
print(response)