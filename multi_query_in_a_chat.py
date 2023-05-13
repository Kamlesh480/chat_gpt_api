import openai
import requests
import json

from cred import GPT_API_KEY

openai.api_key = GPT_API_KEY

Authorization = "Bearer" + " " + GPT_API_KEY



def get_gpt3_5_response(messages, conversation_id=None):
    """
    Returns the response from GPT-3.5 model based on the provided messages.

    Args:
    messages: A list of messages.
    conversation_id: A string representing the conversation ID for a previous conversation.

    Returns:
    A string containing the response from GPT-3.5 model.
    """
    model = "davinci"
    headers = {
        "Content-Type": "application/json",
        "Authorization": Authorization
    }
    prompt = json.dumps(messages)
    payload = {
        "model": model,
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 100,
        "stop": "\n"
    }
    if conversation_id:
        payload["conversation_id"] = conversation_id

    response = requests.post("https://api.openai.com/v1/completions", headers=headers, json=payload)


    response_json = response.json()
    print(response_json)

    return response_json["choices"][0]["text"].strip(), response_json.get("conversation_id") #coming null


messages = [    {"text": "Hello", "user": "customer", "conversation_id": "abc123"},    {"text": "Hi, how can I help you today?", "user": "bot", "conversation_id": "abc123"},    {"text": "I have a question about my account", "user": "customer", "conversation_id": "abc123"},    {"text": "Sure, what's your question?", "user": "bot", "conversation_id": "abc123"},    {"text": "Can I change my email address?", "user": "customer", "conversation_id": "abc123"}]

# call the function to get a response from the GPT-3 model
response = get_gpt3_5_response(messages)
print("---------")
print(response)
