def classify_email(text):
    
    text = text.lower()

    # Lista de palavras-chave que indicam um email produtivo
    palavrachave_produtiva = [
        "problema", "erro", "status", "suporte",
        "dúvida", "ajuda", "solicitação", "anexo"
    ]

    for palavra in  palavrachave_produtiva:
        if palavra in text:
            return "Produtivo"
    return "Improdutivo"
