import requests

# Este é um exemplo de código para testar a API do DeepSeek.

# Chave de API e URL da API do DeepSeek
api_key = "sk-ff13ee550c3f4c39b10e1e40bc7b83f7"
url = "https://api.deepseek.com/chat/completions"

# Validação da chave de API
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Verifica se a chave de API é válida
payload = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "user", "content": "Olá, DeepSeek! Como você está?"}
    ],

    # Caso queira adicionar mais parâmetros, como temperatura ou max_tokens, adicione aqui

}

# Envia a requisição para a API e captura a resposta
try:
    response = requests.post(url, headers=headers, json=payload)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        print("Resposta da API:", response.json())
    else:
        print(f"Erro na API. Status Code: {response.status_code}")
        print("Detalhes do erro:", response.text)  # Mostra a resposta completa em caso de erro

# mostra a resposta completa em caso de erro
except requests.exceptions.RequestException as e:
    print("Falha na conexão com a API:", e)
except Exception as e:
    print("Erro inesperado:", e)


# A APi encontra-se sem saldo, por isso não é possível realizar nenhum teste.
# Necessário adicionar saldo para realizar os testes.
