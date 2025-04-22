# 📝 README - Teste da API DeepSeek

## 🔍 Visão Geral
Este script Python realiza uma integração básica com a API do DeepSeek Chat, enviando uma mensagem simples e recebendo uma resposta.

## 🛠️ Funcionamento do Código

### 📚 Bibliotecas Utilizadas
- `os`: Para acessar variáveis de ambiente
- `requests`: Para fazer requisições HTTP
- `python-dotenv`: Para carregar variáveis de um arquivo `.env`

### ⚙️ Fluxo Principal
1. **Configuração Inicial**:
   - Carrega variáveis do arquivo `.env` usando `load_dotenv()`
   - Obtém a chave da API com `os.getenv("DEEPSEEK_API_KEY")`

2. **Preparação da Requisição**:
   - Define os cabeçalhos (headers) com a autorização Bearer Token
   - Monta o payload (corpo da requisição) com:
     - Modelo: `deepseek-chat`
     - Mensagem: "Olá, DeepSeek!"

3. **Envio e Tratamento da Resposta**:
   - Faz uma requisição POST para `https://api.deepseek.com/chat/completions`
   - Trata três cenários:
     - Sucesso (status 200): exibe a resposta JSON
     - Erro da API: exibe o código e mensagem de erro
     - Erro de conexão: exibe a exceção

## 🚀 Como Usar

1. **Instale as dependências**:
   ```bash
   pip install requests python-dotenv
   ```

2. **Crie um arquivo `.env`** na raiz do projeto:
   ```env
   DEEPSEEK_API_KEY="sua_chave_aqui"
   ```

3. **Execute o script**:
   ```bash
   python nome_do_script.py
   ```

## ⚠️ Importante
- Mantenha seu arquivo `.env` seguro e fora do controle de versão
- Adicione `.env` ao seu `.gitignore`
- Nunca compartilhe sua chave de API publicamente

## 📊 Saídas Esperadas

✅ **Resposta de sucesso**:
```json
Resposta: {
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "choices": [...],
  "usage": {...}
}
```

❌ **Possíveis erros**:
- `401 Unauthorized`: Chave API inválida
- `429 Too Many Requests`: Limite de requisições excedido
- `ConnectionError`: Problemas de conexão com a API

## 📁 Estrutura Recomendada
```
projeto/
├── .env            # Arquivo com sua chave (local apenas)
├── .gitignore      # Deve conter `.env`
└── script.py       # Este código
```

## 🔄 Próximos Passos
- Adicionar tratamento mais robusto de erros
- Implementar histórico de conversação
- Adicionar suporte a parâmetros como `temperature` e `max_tokens`
