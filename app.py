# api/index.py  
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola desde Flask y Vercel!"

# Importante para Vercel:
# expone una variable llamada 'app'
    resultado = ""

    if request.method == "POST":

        expresion = request.form.get("expresion", "")

        try:
            resultado = str(eval(expresion))
        except:
            resultado = "Error"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Calculadora Flask</title>

        <style>
            body {{
                font-family: Arial;
                max-width: 500px;
                margin: 50px auto;
                padding: 20px;
            }}

            input {{
                width: 100%;
                padding: 10px;
                font-size: 18px;
                margin-bottom: 10px;
            }}

            button {{
                width: 100%;
                padding: 10px;
                background: #0078d4;
                color: white;
                border: none;
                cursor: pointer;
            }}

            .resultado {{
                margin-top: 20px;
                padding: 15px;
                background-color: #f3f3f3;
                border-radius: 5px;
            }}
        </style>
    </head>

    <body>

        <h1>Calculadora</h1>

        <form method="POST">
            <input
                type="text"
                name="expresion"
                placeholder="Ejemplo: 5+3*2"
                required>
            <button type="submit">Calcular</button>
        </form>

        <div class="resultado">
            <h3>Resultado:</h3>
            <p>{resultado}</p>
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()