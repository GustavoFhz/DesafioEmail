# 📧 Auto Email Support com Gemini API

Projeto em Python que **classifica emails de suporte** e **gera respostas automáticas profissionais** utilizando a **API do Google Gemini**.

O objetivo é **automatizar atendimentos**, reduzindo esforço manual e evitando consumo desnecessário de API para mensagens improdutivas.

---

## 🚀 Funcionalidades

* Classificação de emails (Produtivo / Improdutivo)
* Resposta automática apenas para emails produtivos
* Integração com **Google Gemini API**
* Uso de variáveis de ambiente com `.env`
* Respostas em **português do Brasil**, educadas e objetivas

---

## 🧠 Como funciona

1. O email do cliente é analisado
2. Se for **Improdutivo**, retorna uma resposta fixa
3. Se for **Produtivo**, o texto é enviado para o Gemini
4. O modelo gera uma resposta profissional baseada em regras definidas no prompt

---

## 📁 Estrutura básica do projeto

```
project/
│── app.py
│── ai_response.py
│── classifier.py
│── .env.example
│── .gitignore
│── requirements.txt
│── README.md
```

---

## 🔧 Pré-requisitos

* Python 3.9+
* Conta Google com acesso à **Gemini API**
* `pip` instalado

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

Crie e ative um ambiente virtual (opcional, recomendado):

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuração do `.env`

Crie um arquivo `.env` na raiz do projeto com base no exemplo:

```env
GEMINI_API_KEY=sua_api_key_aqui
```

⚠️ **Nunca versionar o `.env`** — ele está corretamente ignorado no `.gitignore`.

---

## ▶️ Exemplo de uso

```python
from ai_response import generate_response

email = "Estou com erro ao acessar minha conta"
category = "Produtivo"

response = generate_response(email, category)
print(response)
```

---

## 🧪 Lógica principal (resumo)

* Emails improdutivos recebem resposta padrão
* Emails produtivos geram prompt estruturado
* Chamada ao modelo `gemini-3-flash-preview`
* Retorno apenas do texto gerado

---

## 🛡️ Boas práticas adotadas

* Uso de `.env` para segurança
* `.env.example` para facilitar setup
* Evita consumo de API desnecessário
* Prompt bem definido para respostas consistentes

---

## 📌 Tecnologias utilizadas

* Python
* Google Gemini API
* python-dotenv

---

## 📄 Licença

Este projeto é livre para uso educacional e experimental.

---

## ✨ Autor

Desenvolvido por **Gustavo Silva**
Estudante de Engenharia de Software e desenvolvedor backend



