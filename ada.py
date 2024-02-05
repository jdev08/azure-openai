# text-embedding-ada-002
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

ENDPOINT=os.getenv('ENDPOINT')
API_KEY=os.getenv('API_KEY')
DEPELOPMENT_NAME=os.getenv('DEPELOPMENT_NAME_ADA')

def api_test():
  url = f"{ENDPOINT}/openai/deployments/{DEPELOPMENT_NAME}/embeddings?api-version=2022-12-01"
  headers = {
    "Content-Type": "application/json",
    "api-key": API_KEY,
  }
  body = { 
    "input": "The quick brown fox jumps over the lazy dog.",
}  
  response = requests.post(url, headers=headers, data=json.dumps(body))
  print(response.json())        
  return response

api_test()