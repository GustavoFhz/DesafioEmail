from flask import Flask, render_template, request
from classifier import classify_email
from ai_response import generate_response
from pypdf import PdfReader

app = Flask(__name__)

# Extensões de arquivos permitidas
ALLOWED_EXTENSIONS = {"txt", "pdf"}

def allowed_file(filename):
    # Verifica se o arquivo possui extensão válida
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def read_txt(file):
    # Lê conteúdo de arquivo .txt
    return file.read().decode("utf-8")

def read_pdf(file):
    # Extrai texto de arquivo .pdf
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


@app.route("/", methods=["GET", "POST"])
def index():
    category = None
    response = None
    email_text = ""

    if request.method == "POST":

        # Texto digitado pelo usuário
        email_text = request.form.get("email_text", "").strip()

        # Arquivo enviado pelo formulário
        file = request.files.get("email_file")

        # Se houver arquivo válido, ele tem prioridade
        if file and file.filename != "" and allowed_file(file.filename):
            ext = file.filename.rsplit(".", 1)[1].lower()

            if ext == "txt":
                email_text = read_txt(file)
            elif ext == "pdf":
                email_text = read_pdf(file)

        # Classifica e gera resposta apenas se houver texto
        if email_text:
            category = classify_email(email_text)
            response = generate_response(email_text, category)

    return render_template(
        "index.html",
        category=category,
        response=response,
        email_text=email_text
    )


if __name__ == "__main__":
    app.run(debug=True)
