import requests
import json

from cred import GPT_API_KEY
url = "https://api.openai.com/v1/chat/completions"

payload = json.dumps({
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "user",
      "content": "Hello!"
    }
  ]
})

Authorization = "Bearer" + " " + GPT_API_KEY

headers = {
  'Content-Type': 'application/json',
  'Authorization': Authorization
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)