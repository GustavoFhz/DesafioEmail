import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Cria o cliente do Gemini usando a API Key
# A chave deve estar definida como GEMINI_API_KEY no .env
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_response(email_text, category):
    """
    Gera uma resposta automática para emails de suporte
    com base na categoria do email.
    """

    # Emails improdutivos recebem uma resposta fixa
    # Evita consumo desnecessário da API
    if category == "Improdutivo":
        return "Agradecemos sua mensagem! No momento não é necessária nenhuma ação adicional."

    # Prompt estruturado para garantir respostas profissionais

    prompt = f"""
Você é um atendente de suporte técnico profissional.

Regras:
- Responda em português do Brasil
- Seja educado, claro e objetivo
- Explique o problema relatado
- Informe possíveis soluções ou próximos passos
- Finalize cordialmente

Email do cliente:
{email_text}

Resposta do suporte:
"""

    # Chamada ao modelo de linguagem do Gemini
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    # Retorna apenas o texto da resposta gerada
    return response.text.strip()
