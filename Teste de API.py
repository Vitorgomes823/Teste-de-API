# Este Script tem como objetivo testar a API do DeepSeek

import os
import requests
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

# Lê a chave do ambiente
api_key = os.getenv("DEEPSEEK_API_KEY")
url = "https://api.deepseek.com/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

payload = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "user", "content": "Olá, DeepSeek!"}
    ]
}

try:
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Resposta:", response.json())
    else:
        print(f"Erro {response.status_code}:", response.text)
except Exception as e:
    print("Erro:", e)
