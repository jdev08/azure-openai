import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

ENDPOINT=os.getenv('ENDPOINT')
API_KEY=os.getenv('API_KEY')
DEPELOPMENT_NAME=os.getenv('DEPELOPMENT_NAME_GPT')

def api_test():
  url = f"{ENDPOINT}/openai/deployments/{DEPELOPMENT_NAME}/chat/completions?api-version=2023-12-01-preview"
  headers = {
    "Content-Type": "application/json",
    "api-key": API_KEY,
  }
  body = { 
    "messages": [ 
        { "role": "system", "content": "You are a helpful assistant." }, 
        { "role": "user", "content": [  
            { 
                "type": "text", 
                "text": "make some sentences for me." 
            },
        ] } 
    ], 
    "max_tokens": 2000 
}  
  response = requests.post(url, headers=headers, data=json.dumps(body))
  print(response.json())        
  return response

api_test()