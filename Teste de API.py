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

def explicar_erro(status_code):
    mensagens = {
        200: "✅ Sucesso! A requisição foi concluída e a resposta chegou certinha.",
        201: "✅ Criado com sucesso! Algo novo foi adicionado.",
        204: "✅ Sucesso, mas sem conteúdo. A requisição funcionou, mas não tem nada pra mostrar.",
        400: "🚫 Erro 400: A requisição foi mal formulada. Verifique se os dados enviados estão corretos.",
        401: "🔐 Erro 401: Não autorizado. A chave da API pode estar errada ou ausente.",
        403: "🚫 Erro 403: Acesso proibido. Você não tem permissão para acessar isso.",
        404: "❓ Erro 404: Nada encontrado. A URL está certa? Esse endpoint existe?",
        405: "📛 Erro 405: Método não permitido. Você tentou usar um tipo de requisição (GET, POST...) que esse endpoint não aceita.",
        408: "⌛ Erro 408: Tempo esgotado. O servidor demorou demais pra responder.",
        429: "⏱️ Erro 429: Você enviou muitas requisições em pouco tempo. Respira e tenta de novo depois.",
        500: "💥 Erro 500: Erro interno no servidor. A culpa não é sua.",
        502: "💢 Erro 502: Gateway ruim. O servidor recebeu uma resposta inválida.",
        503: "🚧 Erro 503: Serviço indisponível. O servidor está temporariamente fora do ar.",
        504: "📶 Erro 504: O servidor demorou demais pra responder. Timeout."
    }

    return mensagens.get(status_code, f"⚠️ Erro desconhecido (código {status_code}).")

try:
    response = requests.post(url, headers=headers, json=payload)

    if response.ok:
        print("✅ Tudo certo! Resposta recebida:")
        print(response.json())
    else:
        explicacao = explicar_erro(response.status_code)
        print(explicacao)
        print("📝 Detalhes técnicos:", response.text)

except requests.exceptions.RequestException as e:
    print("🚨 Erro de conexão com a API:", e)

except Exception as e:
    print("❌ Ocorreu um erro inesperado:", e)
