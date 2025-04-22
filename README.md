# 📝 **DeepSeek API Test**  

Este repositório contém um script Python simples para testar a integração com a **API do DeepSeek Chat**.  

🔗 **API Oficial**: [DeepSeek API Documentation](https://platform.deepseek.com/docs)  

---

## 🚀 **Como Usar**  

### **Pré-requisitos**  
- Python 3.6+  
- Biblioteca `requests` instalada  
- Uma **chave de API válida** do DeepSeek  

### **Instalação**  
1. Clone este repositório:  
   ```bash
   git clone https://github.com/seu-usuario/deepseek-api-test.git
   cd deepseek-api-test
   ```

2. Instale as dependências:  
   ```bash
   pip install requests
   ```

3. Adicione sua chave de API no arquivo `deepseek_api_test.py`:  
   ```python
   api_key = "sua_chave_de_api_aqui"  # Substitua pela sua chave
   ```

---

## 🛠 **Executando o Script**  

Execute o script Python:  
```bash
python deepseek_api_test.py
```

### **Possíveis Saídas**  
✅ **Conexão bem-sucedida**:  
```json
Resposta da API: {"id": "chatcmpl-123", "object": "chat.completion", "choices": [...]}
```

❌ **Erro de autenticação/saldo**:  
```
Erro na API. Status Code: 403  
Detalhes do erro: {"error": {"message": "Insufficient Balance", "type": "unknown_error"}}
```

❌ **Erro de conexão**:  
```
Falha na conexão com a API: ConnectionError(...)
```

---

## 🔧 **Solução de Problemas**  

| **Erro**                     | **Causa**                          | **Solução**                          |
|-------------------------------|------------------------------------|--------------------------------------|
| `Insufficient Balance`        | Saldo insuficiente na conta        | Recarregue créditos no painel da API |
| `Invalid API Key`             | Chave de API incorreta             | Verifique e atualize a chave         |
| `ConnectionError`             | Falha na rede/URL incorreta        | Verifique a URL e sua conexão        |

---

## 📌 **Notas Importantes**  
⚠️ **Nunca exponha sua chave de API publicamente** (evite commits com `api_key` no GitHub).  
💡 Caso a API esteja indisponível, verifique o [status oficial do DeepSeek](https://status.deepseek.com).  

---

## 📜 **Licença**  
MIT License. Consulte o arquivo [LICENSE](LICENSE) para mais informações.  

---

Feito com ❤️ por [Vitor Gomes](https://github.com/sVitorgomes823).  
🔗 **Contribuições são bem-vindas!** 🚀  

--- 

### 🔎 **Próximos Passos**  
- [ ] Adicionar suporte a streaming de respostas  
- [ ] Implementar histórico de conversação  
- [ ] Adicionar mais parâmetros (`temperature`, `max_tokens`)  

